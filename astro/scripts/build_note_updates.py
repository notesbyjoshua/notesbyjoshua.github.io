import json
import re
import subprocess
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
NOTES = "astro/src/content/docs/notes/"
EXTENSIONS = (".md", ".mdx")


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True)


def body(source):
    return re.sub(r"\A---\r?\n.*?\r?\n---(?:\r?\n|$)", "", source, count=1, flags=re.S)


def tokens(source):
    source = re.sub(r"<!--[\s\S]*?-->", "", source)
    source = re.sub(r"\$\$.*?\$\$", " ", source, flags=re.S)
    source = re.sub(r"<[^>]+>", " ", source)
    return re.findall(r"\w+", source.lower())


def equations(source):
    values = re.findall(r"\$\$(.*?)\$\$", source, re.S)
    normalized = []
    for value in values:
        value = re.sub(r"\\(?:lvert|rvert|vert)\b", "|", value)
        value = re.sub(r"\\(?:left|right|displaystyle)\b|\\[,;! ]|\s+", "", value)
        value = value.replace(r"\dfrac", r"\frac").replace(r"\tfrac", r"\frac")
        normalized.append(value)
    return set(normalized)


def illustrations(source):
    images = re.findall(r"!\[[^\]]*\]\(([^)]+)\)|<img\b[^>]*\bsrc=[\"']([^\"']+)", source)
    tikz = re.findall(r"```(?:tikz|latex)\b(.*?)```", source, re.S)
    return Counter([a or b for a, b in images] + [re.sub(r"\s+", "", code) for code in tikz])


def classify(before, after, message=""):
    old, new = body(before), body(after)
    if old == new:
        return None
    mode = re.search(r"^Note-Update:\s*(skip|significant)\s*$", message, re.M | re.I)
    if mode and mode[1].lower() == "skip":
        return None
    a, b = tokens(old), tokens(new)
    changes = [op for op in SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if op[0] != "equal"]
    removed = sum(i2 - i1 for _, i1, i2, _, _ in changes)
    added = sum(j2 - j1 for _, _, _, j1, j2 in changes)
    reasons = []
    if equations(old) != equations(new):
        reasons.append("Equations updated")
    if illustrations(old) != illustrations(new):
        reasons.append("Diagrams updated")
    old_headings = re.findall(r"^#{2,6}\s+.+", old, re.M)
    new_headings = re.findall(r"^#{2,6}\s+.+", new, re.M)
    if len(old_headings) != len(new_headings) and added + removed >= 15:
        reasons.append("Sections updated")
    for pattern, label in [
        (r"^:::(?:problem|frq)\b|^\*\*Example\b", "Examples or practice updated"),
        (r"^:::solution\b|^#{2,6}\s+Solution\b", "Solutions updated"),
    ]:
        if len(re.findall(pattern, old, re.M)) != len(re.findall(pattern, new, re.M)):
            reasons.append(label)
    if added + removed >= 100 or abs(added - removed) >= 40:
        reasons.append("Explanations expanded" if added - removed >= 40 else "Note content revised")
    if not reasons and not (mode and mode[1].lower() == "significant"):
        return None
    summary = re.search(r"^Note-Summary:\s*(.+)$", message, re.M)
    return summary[1].strip()[:240] if summary else "; ".join(reasons) or "Note content revised"


def build_history(root, since):
    git(root, "merge-base", "--is-ancestor", since, "HEAD")
    commits = git(root, "rev-list", "--first-parent", "--reverse", f"{since}..HEAD").splitlines()
    pages = {}
    for commit in commits:
        parent = git(root, "rev-parse", f"{commit}^1").strip()
        date, message = git(root, "show", "-s", "--format=%cI%n%B", commit).split("\n", 1)
        records = iter(git(root, "diff", "--name-status", "-z", "--find-renames", parent, commit, "--", NOTES).split("\0"))
        for status in records:
            if not status:
                continue
            previous = path = next(records)
            if status.startswith(("R", "C")):
                path = next(records)
            if status.startswith("R") and previous in pages:
                pages[path] = pages.pop(previous)
            if status == "D":
                pages.pop(path, None)
                continue
            if not path.endswith(EXTENSIONS):
                continue
            before = "" if status == "A" else git(root, "show", f"{parent}:{previous}")
            after = git(root, "show", f"{commit}:{path}")
            summary = classify(before, after, message)
            if summary:
                pages.setdefault(path, []).insert(0, {"id": commit, "date": date, "summary": summary})
                pages[path] = pages[path][:10]
    return {"baseline": since, "pages": pages}


if __name__ == "__main__":
    config = json.loads((ROOT / "astro/scripts/note-updates.json").read_text())
    history = build_history(ROOT, config["since"])
    output = ROOT / "astro/src/data/note-updates.json"
    serialized = json.dumps(history, indent=2, ensure_ascii=False) + "\n"
    if not output.exists() or output.read_text() != serialized:
        output.write_text(serialized)
    print(f"Note updates: {sum(map(len, history['pages'].values()))} significant changes on {len(history['pages'])} pages")
