import subprocess
import tempfile
import unittest
from pathlib import Path

from build_note_updates import NOTES, build_history, classify


class ClassificationTests(unittest.TestCase):
    def test_small_edits_stay_quiet(self):
        cases = [
            ("This is teh definition.", "This is the definition."),
            ("The result is very useful.", "The result is useful."),
            ("## Motion\nA moving object.", "## Motion\n\nA **moving** object."),
            ("---\nprogress: 40\n---\nSame notes", "---\nprogress: 80\n---\nSame notes"),
            ("$$\\left| x \\right|$$", "$$\\lvert x\\rvert$$"),
            ("$$x + y$$", "$$ x+y $$"),
            ("Let $$x$$ be positive. Then $$x$$ increases.", "Let $$x$$ be positive. It increases."),
            ("$$\\left| x \\right|$$\n" * 100, "$$\\lvert x\\rvert$$\n" * 100),
        ]
        for before, after in cases:
            with self.subTest(after=after):
                self.assertIsNone(classify(before, after))

    def test_equation_correction_is_significant(self):
        self.assertEqual(classify("$$F=ma$$", "$$F=-ma$$"), "Equations updated")

    def test_diagram_changes_but_not_alt_text(self):
        self.assertIsNotNone(classify('![Graph](/a.png)', '![Graph](/b.png)'))
        self.assertIsNone(classify('![Grahp](/a.png)', '![Graph](/a.png)'))

    def test_new_examples_practice_and_solutions(self):
        for addition in ["**Example.** A short worked example.", ":::problem\nFind x.\n:::", ":::solution\nx=2\n:::"]:
            with self.subTest(addition=addition):
                self.assertIsNotNone(classify("An explanation.", "An explanation.\n" + addition))

    def test_expansion_and_removal(self):
        before = "An explanation."
        after = before + "\n## New section\n" + " ".join(f"word{i}" for i in range(45))
        self.assertIsNotNone(classify(before, after))
        self.assertIsNotNone(classify(after, before))

    def test_short_new_section(self):
        before = "An explanation."
        after = before + "\n## Assumptions\n" + " ".join(f"word{i}" for i in range(16))
        self.assertEqual(classify(before, after), "Sections updated")

    def test_commit_overrides(self):
        self.assertIsNone(classify("$$a=b$$", "$$a=c$$", "Cleanup\n\nNote-Update: skip"))
        message = "Correction\n\nNote-Update: significant\nNote-Summary: Corrected the direction of the force."
        self.assertEqual(classify("Force acts left.", "Force acts right.", message), "Corrected the direction of the force.")
        self.assertIsNone(classify("Same notes", "Same notes", message))


class HistoryTests(unittest.TestCase):
    def test_multiple_commits_rename_merge_and_deletion(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)

            def git(*args):
                return subprocess.check_output(["git", "-C", directory, *args], text=True, stderr=subprocess.PIPE).strip()

            def commit(message):
                git("add", ".")
                git("commit", "-m", message)
                return git("rev-parse", "HEAD")

            git("init", "-b", "main")
            git("config", "user.email", "test@example.com")
            git("config", "user.name", "Test")
            note = root / NOTES / "motion.md"
            note.parent.mkdir(parents=True)
            note.write_text("---\ntitle: Motion\n---\nAn object moves.\n$$F=ma$$\n")
            baseline = commit("Baseline")
            note.write_text(note.read_text().replace("moves", "is moving"))
            commit("Small wording edit")
            self.assertEqual(build_history(root, baseline)["pages"], {})
            note.write_text(note.read_text().replace("F=ma", "F=-ma"))
            significant = commit("idk")
            note.write_text(note.read_text().replace("is moving", "moves forward"))
            commit("Another small edit")
            history = build_history(root, baseline)
            self.assertEqual(history["pages"][NOTES + "motion.md"][0]["id"], significant)
            renamed = note.with_name("forces.md")
            note.rename(renamed)
            commit("Rename only")
            self.assertEqual(len(build_history(root, baseline)["pages"][NOTES + "forces.md"]), 1)
            git("checkout", "-b", "branch")
            renamed.write_text(renamed.read_text() + "\n:::problem\nFind the force.\n:::\n")
            commit("Add practice on a branch")
            git("checkout", "main")
            git("merge", "--no-ff", "branch", "-m", "Merge practice")
            self.assertEqual(len(build_history(root, baseline)["pages"][NOTES + "forces.md"]), 2)
            renamed.unlink()
            commit("Delete note")
            self.assertEqual(build_history(root, baseline)["pages"], {})


if __name__ == "__main__":
    unittest.main()
