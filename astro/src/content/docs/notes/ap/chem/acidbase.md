---
title: "Unit 8: Acid-Base Equilibrium"
description: "AP Chemistry notes on acids, bases, pH, buffers, titrations, equilibrium calculations, and acid-base reaction reasoning."
sidebar:
  order: 8
---

## Definitions of acids and bases

### Arrhenius Theory

An **Arrhenius acid** increases the concentration of $$\text{H}^+$$ (really $$\text{H}_3\text{O}^+$$ in water) in aqueous solution; an **Arrhenius base** increases $$[\text{OH}^-]$$. The model is useful for water-based chemistry but does not describe ammonia as a base in water without extra bookkeeping, and it does not address nonaqueous systems.

<div class="theorem-box">

**Example.** Ammonia contains no hydroxide ion in its formula. Can it nevertheless increase aqueous hydroxide concentration? Explain the limitation of identifying bases only by an OH group in their formulas.

Ammonia accepts a proton from water: $$\mathrm{NH_3+H_2O\rightleftharpoons NH_4^++OH^-}$$. It therefore increases hydroxide concentration without dissociating into preexisting hydroxide ions. Inspecting the formula alone misses the reaction with solvent. The Brønsted-Lowry definition describes this proton-transfer behavior directly.

</div>

### Brønsted–Lowry Theory

A **Brønsted–Lowry acid** is a proton donor; a **Brønsted–Lowry base** is a proton acceptor. When an acid $$\text{HA}$$ donates a proton to water,

$$
\text{HA}(aq) + \text{H}_2\text{O}(l) \rightleftharpoons \text{H}_3\text{O}^+(aq) + \text{A}^-(aq),
$$

the species $$\text{A}^-$$ is the **conjugate base** of $$\text{HA}$$, and $$\text{H}_3\text{O}^+$$ is the **conjugate acid** of $$\text{H}_2\text{O}$$. Every Brønsted acid has a conjugate base, and every base has a conjugate acid, differing by one $$\text{H}^+$$ in the formula and one charge unit. For AP purposes, we will generally use this theory.

A key consequence is an **inverse strength relationship**: the stronger an acid, the weaker its conjugate base, and vice versa. A strong acid like $$\text{HCl}$$ ionizes almost completely precisely *because* its conjugate base $$\text{Cl}^-$$ has essentially no tendency to grab a proton back. A weak acid like $$\text{HF}$$ ionizes only slightly because its conjugate base $$\text{F}^-$$ is a reasonably good proton acceptor that pulls the equilibrium back toward the molecular form. This is the qualitative idea behind $$K_a\times K_b=K_w$$ (derived below).

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing,angles,quotes}
\begin{tikzpicture}[>=Stealth, font=\small]
\node (ha) at (-3,0.7) {$\mathrm{HA}$};
\node (w) at (-1,0.7) {$+\mathrm{H_2O}$};
\node at (0,0.7) {$\rightleftharpoons$};
\node (h3o) at (1.4,0.7) {$\mathrm{H_3O^+}$};
\node (a) at (3.2,0.7) {$+\mathrm{A^-}$};
\draw[<->, blue, thick] (ha) to[bend right=35] node[below] {conjugate pair} (a);
\draw[<->, red, thick] (w) to[bend left=35] node[above] {conjugate pair} (h3o);
\draw[->, thick] (-2.6,-0.6) -- (1.3,-0.6) node[midway, below] {proton transfer};
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** In $$\mathrm{HCO_3^-+H_2O\rightleftharpoons CO_3^{2-}+H_3O^+}$$, identify the acid and conjugate base. Can bicarbonate act as a base in a different reaction?

Bicarbonate donates a proton here, so it is the acid and carbonate is its conjugate base. With an acid, bicarbonate can instead accept a proton to form $$\mathrm{H_2CO_3}$$, making it a base in that reaction. Its negative charge does not fix its role: the actual direction of proton transfer determines the classification.

</div>

### Lewis Theory

A **Lewis acid** accepts an electron pair; a **Lewis base** donates an electron pair. This picture includes reactions without proton transfer (e.g. $$\text{BF}_3$$ with $$\text{NH}_3$$) and matches how metal ions bind ligands in [Unit 7](/notes/ap/chem/equilibrium/) complex-ion formation. This is usually not covered on the AP exam.

<div class="theorem-box">

**Example.** In $$\mathrm{BF_3+NH_3\rightarrow F_3B-NH_3}$$, identify the Lewis acid and base. Explain why this reaction shows that Lewis acid-base chemistry is broader than proton transfer.

Ammonia donates nitrogen's lone pair to form the B-N bond, so it is the Lewis base. Boron trifluoride accepts the pair and is the Lewis acid. No proton changes partners in this reaction. Electron-pair donation and acceptance can form an acid-base adduct even when neither reactant supplies an acidic proton.

</div>

---

## Nomenclature (summary)

**Binary acids** (hydrogen + one other nonmetal): the anion name ending *-ide* becomes *hydro-…-ic acid* (e.g. $$\text{HCl}$$, hydrochloric acid). **Oxyacids** use the oxyanion stem: *-ate* → *-ic acid* ($$\text{NO}_3^-$$ → nitric acid), *-ite* → *-ous acid* ($$\text{NO}_2^-$$ → nitrous acid); prefixes such as *hypo-* and *per-* carry over.

Ionic hydroxides are named as cation + hydroxide. Molecular bases include ammonia ($$\text{NH}_3$$), amines (e.g. $$\text{CH}_3\text{NH}_2$$), and related nitrogen compounds that accept protons in water.

<div class="theorem-box">

**Example.** Compare the names and chlorine oxidation numbers in $$\mathrm{HClO}$$ and $$\mathrm{HClO_3}$$. Explain why the naming difference is not a statement about how many protons each donates.

These are hypochlorous acid and chloric acid. With H at $$+1$$ and O at $$-2$$, chlorine is $$+1$$ and $$+5$$ respectively. Both formulas contain one ionizable proton; the oxyanion-derived names distinguish oxygen content, not proton count.

</div>

---

## Strength of acids and structural trends

Strong acids and strong bases are treated as complete ionization or dissociation in dilute aqueous solution for stoichiometry and pH estimates. Weak species reach equilibrium between the unionized form and ions.

The unifying principle behind every acid-strength trend is **conjugate-base stability**: anything that makes the conjugate base more stable (better able to hold the negative charge after the proton leaves) makes the acid stronger, because it pulls the ionization equilibrium toward products.

For binary acids $$\text{HX}$$, bond polarity and bond strength both matter: across a period, polarity toward $$\text{X}$$ can strengthen the acid; down a group, longer/weaker $$\text{H–X}$$ often dominates and acidity increases ($$\text{HF}$$ is a weak acid in water; $$\text{HCl}$$, $$\text{HBr}$$, $$\text{HI}$$ are strong). The down-a-group trend wins because the larger halogen forms a longer, weaker bond to hydrogen that breaks more easily, and the resulting larger anion spreads its charge over more volume.

For **oxoacids** with the same central atom, more electronegative atoms attached to that center or a higher oxidation state (more terminal oxygens) generally strengthens the acid: those extra electronegative oxygens pull electron density away from the O–H bond and spread out the negative charge of the conjugate base. This is why acid strength rises in the series $$\text{HClO}<\text{HClO}_2<\text{HClO}_3<\text{HClO}_4$$. For **carboxylic acids**, electron-withdrawing groups (such as the chlorines in chloroacetic acids) stabilize the conjugate base and increase $$K_a$$, while the resonance delocalization of the carboxylate anion is what makes carboxylic acids more acidic than alcohols in the first place.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing,angles,quotes}
\begin{tikzpicture}[>=Stealth, font=\small]
\draw[step=0.55, gray!35] (0,0) grid (3.3,2.75);
\draw[->, blue, very thick] (0.3,-0.35) -- (3.0,-0.35) node[midway, below] {acidity increases};
\draw[->, blue, very thick] (3.65,0.3) -- (3.65,2.45) node[midway, right] {down group};
\node at (1.65,3.1) {binary hydrides};
\node[draw, rounded corners] at (7,2.1) {$\mathrm{HClO}$};
\node[draw, rounded corners] at (7,1.2) {$\mathrm{HClO_2}$};
\node[draw, rounded corners] at (7,0.3) {$\mathrm{HClO_3}$};
\draw[->, thick] (8.2,2.1) -- (8.2,0.3) node[midway, right, align=center] {more O atoms\\stabilize base\\stronger acid};
\end{tikzpicture}
```

Acid-base reactions favor formation of the **weaker acid** and **weaker base**. A quick way to predict direction is to compare acid strengths: the side with the larger $$K_a$$ acid tends to react toward the side with the smaller $$K_a$$ acid. In $$\text{p}K_a$$ language, reactions tend to go from lower $$\text{p}K_a$$ acid to higher $$\text{p}K_a$$ acid.

<div class="theorem-box">

**Example.** Two equal-concentration acids are $$\mathrm{CH_3COOH}$$ and $$\mathrm{ClCH_2COOH}$$. Predict which has lower pH using the conjugate bases.

Chlorine withdraws electron density and stabilizes negative charge on the chloroacetate conjugate base. That favors acid ionization, so chloroacetic acid has larger Ka and lower pH at equal concentration. The comparison concerns stability after proton loss, not simply the number of H atoms.

</div>

---

## Strong acids and strong bases

Common strong acids (memorize for AP): $$\text{HCl}$$, $$\text{HBr}$$, $$\text{HI}$$ (hydrohalic acids), $$\text{HNO}_3$$, $$\text{HClO}_4$$, $$\text{HClO}_3$$, and $$\text{H}_2\text{SO}_4$$ (oxoacids)for the first proton only (the second proton is weak in the dilute-solution sense: $$\text{HSO}_4^-$$ is a weak acid). A notable exception to hydrohalic trend is that $$\text{HF}$$ is weak.

Strong bases are the group 1 hydroxides ($$\text{LiOH}$$, $$\text{NaOH}$$, $$\text{KOH}$$, …) and the heavier group 2 hydroxides commonly used in lab ($$\text{Ca(OH)}_2$$, $$\text{Sr(OH)}_2$$, $$\text{Ba(OH)}_2$$). $$\text{Mg(OH)}_2$$ is only slightly soluble but what dissolves is essentially fully dissociated.

For a strong acid at moderate concentration, $$[\text{H}_3\text{O}^+] \approx$$ the analytical concentration of the acid (if one proton per formula unit). For a strong diprotic acid such as $$\text{H}_2\text{SO}_4$$, treat the first step as complete and the second with $$K_{a2}$$ if the problem requires it.

<div class="theorem-box">

**Example.** A student calls $$0.0010\ M$$ HCl weaker than $$0.10\ M$$ acetic acid because the HCl is more dilute. Explain the distinction.

Strength describes the extent of ionization; concentration describes amount per volume. HCl is still the strong acid because it ionizes essentially completely. A concentrated weak acid can nevertheless produce more hydronium than a very dilute strong acid, so pH alone cannot label acid strength without concentration information.

</div>

---

## Weak acids: $$K_a$$ and ICE tables

For a weak monoprotic acid $$\text{HA}$$,

$$
K_a = \frac{[\text{H}_3\text{O}^+][\text{A}^-]}{[\text{HA}]},
$$

with the usual equilibrium concentrations. The same logic as [Unit 7](/notes/ap/chem/equilibrium/) **ICE** tables applies: define $$x$$ as the amount of $$\text{HA}$$ that ionizes per liter, then solve $$K_a = x^2/(C - x)$$ (or the quadratic if $$x$$ is not negligible). When $$C \gg K_a$$ and $$x \ll C$$, the approximation $$K_a \approx x^2/C$$ is common; check with a percent-ionization or “5%” rule if your course uses it.

$$
\text{p}K_a = -\log K_a
$$

Smaller $$\text{p}K_a$$ means a stronger acid (larger $$K_a$$).

<div class="theorem-box">

**Example.** A hypothetical acid has $$K_a=1.0\times10^{-3}$$ and initial concentration $$0.010\ M$$. Test whether neglecting x is reasonable.

The shortcut gives $$x=\sqrt{K_aC}=0.00316\ M$$, or $$31.6\%$$ ionization, so it fails the 5% check. Solve $$x^2/(0.010-x)=0.0010$$ instead: $$x=0.00270\ M$$. Keeping the depleted denominator matters when a substantial fraction reacts.

</div>

---

## Weak bases: $$K_b$$

For a weak base $$\text{B}$$ (e.g. $$\text{NH}_3$$),

$$
\text{B}(aq) + \text{H}_2\text{O}(l) \rightleftharpoons \text{BH}^+(aq) + \text{OH}^-(aq),
$$

$$
K_b = \frac{[\text{BH}^+][\text{OH}^-]}{[\text{B}]}, \qquad \text{p}K_b = -\log K_b.
$$

ICE setup parallels weak acids, but you solve for $$[\text{OH}^-]$$ and then find pH from $$K_w$$ and pOH.

<div class="theorem-box">

**Example.** A $$0.10\ M$$ weak base has $$K_b=1.0\times10^{-5}$$ at $$25^\circ\mathrm{C}$$. A student gets pH 3.00 from $$-\log\sqrt{K_bC}$$. Correct the result.

The square root estimates hydroxide, $$[OH^-]=1.0\times10^{-3}\ M$$. Its negative logarithm is pOH, not pH. Thus $$\mathrm{pH}=14.00-3.00=11.00$$. The estimate ionizes only $$1\%$$ of the base, consistent with neglecting depletion.

</div>

---

## Conjugate $$K_a$$ and $$K_b$$; $$K_w$$

For a conjugate pair $$\text{HA}/\text{A}^-$$ in water at a given temperature,

$$
K_a \times K_b = K_w,
$$

where $$K_b$$ refers to $$\text{A}^-$$ acting as a base toward water. Similarly $$\text{p}K_a + \text{p}K_b = \text{p}K_w$$ (at $$25\,^\circ\text{C}$$, $$\text{p}K_w = 14.00$$ when $$K_w = 1.0 \times 10^{-14}$$).

**Autoionization** of water:

$$
2\,\text{H}_2\text{O}(l) \rightleftharpoons \text{H}_3\text{O}^+(aq) + \text{OH}^-(aq), \qquad K_w = [\text{H}_3\text{O}^+][\text{OH}^-].
$$

At $$25\,^\circ\text{C}$$, $$K_w = 1.0 \times 10^{-14}$$; $$K_w$$ depends on temperature, so $$\text{pH} + \text{pOH} = 14$$ is not universal outside standard conditions unless $$K_w$$ is updated.

<div class="theorem-box">

**Example.** At a certain temperature, $$K_w=4.0\times10^{-14}$$. Find neutral pH and explain why a measured pH of 6.85 is not acidic at this temperature.

Neutrality requires equal hydronium and hydroxide: both are $$\sqrt{K_w}=2.0\times10^{-7}\ M$$. Neutral pH is $$6.70$$. At pH 6.85 hydronium is lower than its neutral value, so the solution is basic. The familiar boundary of 7.00 assumes $$25^\circ\mathrm{C}$$.

</div>

---

## pH and pOH

$$
\text{pH} = -\log[\text{H}_3\text{O}^+], \qquad \text{pOH} = -\log[\text{OH}^-], \qquad \text{pH} + \text{pOH} = \text{p}K_w.
$$

Neutral water at $$25\,^\circ\text{C}$$ has $$\text{pH} = 7.00$$ because $$[\text{H}_3\text{O}^+] = [\text{OH}^-]$$. $$\text{pH} < 7$$ is acidic and $$\text{pH} > 7$$ is basic at that temperature; at other temperatures, neutral pH shifts slightly because $$K_w$$ changes.

Because pH is logarithmic, a change of $$1.00$$ pH unit means a tenfold change in $$[\text{H}_3\text{O}^+]$$. A solution with pH $$3$$ has $$100$$ times the hydronium concentration of a solution with pH $$5$$.

Use inverse logarithms to move back from pH or pOH to concentration:

$$
[\text{H}_3\text{O}^+] = 10^{-\text{pH}}, \qquad [\text{OH}^-] = 10^{-\text{pOH}}.
$$

:::strategy

1. **Strong acid or strong base only**: use stoichiometric dissociation first, then pH/pOH.
2. **Weak acid or weak base only**: write $$K_a$$ or $$K_b$$ and use an ICE table.
3. **Mixture with strong acid/base reaction**: do limiting-reactant stoichiometry first; then decide what remains.
4. **Weak acid + conjugate base** or **weak base + conjugate acid**: use buffer logic.
5. **At a titration equivalence point**: identify the salt left behind and analyze its hydrolysis.

:::

<div class="theorem-box">

**Example.** Equal volumes of strong acid solutions at pH 2.00 and 4.00 are mixed. Find the final pH and explain why averaging pH values fails.

Average concentrations, not logarithms: $$[H_3O^+]=(0.0100+0.000100)/2=0.00505\ M$$. Therefore pH is $$2.30$$, not 3.00. The more concentrated acid supplies nearly all the hydronium.

</div>

---

## Percent ionization

**Percent ionization** (or **percent dissociation** for a weak acid) is

$$
\%\ \text{ionization} = \frac{[\text{H}_3\text{O}^+]_{\text{eq}}}{[\text{HA}]_{\text{initial}}} \times 100\%,
$$

using the initial analytical concentration of $$\text{HA}$$ in the denominator. For a weak base, an analogous expression uses $$[\text{OH}^-]_{\text{eq}}/[\text{B}]_{\text{initial}}$$. Adding common-ion $$\text{A}^-$$ or $$\text{BH}^+$$ suppresses ionization (**Le Châtelier’s principle**), lowering percent ionization.

<div class="theorem-box">

**Example.** A weak acid is diluted by a factor of four while the small-x approximation remains valid. Predict the changes in hydronium concentration and percent ionization.

Since $$[H_3O^+]\approx\sqrt{K_aC}$$, hydronium halves. But percent ionization is proportional to $$\sqrt{K_a/C}$$ and doubles. A greater fraction of fewer acid molecules ionizes; higher percent ionization does not mean a higher hydronium concentration.

</div>

---

## Polyprotic acids

A **polyprotic acid** donates more than one proton. Successive $$K_a$$ values usually satisfy $$K_{a1} > K_{a2} > K_{a3}$$ because removing a positive proton from an increasingly negative anion is harder. Many calculations use only $$K_{a1}$$ if later steps are negligible contributors to $$[\text{H}_3\text{O}^+]$$; near the second equivalence point in a titration, the second dissociation matters.

<div class="theorem-box">

**Example.** A diprotic acid has $$K_{a1}=10^{-3}$$ and $$K_{a2}=10^{-8}$$. Explain why treating a $$0.10\ M$$ solution as providing $$0.20\ M$$ hydronium fails.

Neither ionization is complete. The first step establishes hydronium, which further suppresses the much weaker second ionization. Two protons per formula unit specify neutralization capacity with sufficient base, not the free hydronium concentration before titration.

</div>

---

## Oxides and acid–base character

Nonmetal oxides tend to be **acidic anhydrides** (react with water to give acids). Metal oxides, especially ionic ones, tend to be **basic anhydrides** (give hydroxide or raise pH in water). **Amphoteric** oxides/hydroxides (e.g. $$\text{Al}_2\text{O}_3$$, $$\text{Al(OH)}_3$$) react with both strong acid and strong base.

<div class="theorem-box">

**Example.** Equal moles of $$\mathrm{Na_2O}$$ and $$\mathrm{CO_2}$$ are separately introduced into water. Predict opposite acid-base effects and support them with reactions.

Sodium oxide gives $$\mathrm{Na_2O+H_2O\rightarrow2Na^++2OH^-}$$, raising pH. Dissolved carbon dioxide participates in $$\mathrm{CO_2+2H_2O\rightleftharpoons H_3O^++HCO_3^-}$$, lowering pH. Oxygen in a formula does not by itself establish acid or base behavior.

</div>

---

## Amphoteric species

An **amphoteric** substance can act as acid or base. Water is the usual example: it donates a proton to $$\text{NH}_3$$ and accepts one from $$\text{HCl}$$. Polyprotic anions such as $$\text{HCO}_3^-$$ and $$\text{HSO}_4^-$$ can donate or accept a proton depending on what they meet.

<div class="theorem-box">

**Example.** Show how bicarbonate can consume either added H+ or added OH-, and identify its role in each reaction.

With acid, $$\mathrm{HCO_3^-+H^+\rightarrow H_2CO_3}$$, followed by possible carbon dioxide loss; bicarbonate accepts a proton. With base, $$\mathrm{HCO_3^-+OH^-\rightarrow CO_3^{2-}+H_2O}$$; bicarbonate donates a proton. It is amphiprotic because it can do both.

</div>

---

## Acid–base properties of salts

Salts dissociate into ions that may **hydrolyze** (react with water). A salt of strong acid + strong base (e.g. $$\text{NaCl}$$) gives neutral pH (neglecting tiny temperature effects). Weak acid + strong base (e.g. $$\text{CH}_3\text{COONa}$$) gives a basic solution because $$\text{A}^-$$ is a base. Strong acid + weak base (e.g. $$\text{NH}_4\text{Cl}$$) gives an acidic solution because $$\text{NH}_4^+$$ is an acid. Weak + weak salts require comparing $$K_a$$ of the cation acid and $$K_b$$ of the anion base.

Useful salt classification:

| Salt source | pH prediction | Reason |
| --- | --- | --- |
| Strong acid + strong base | Neutral | Neither ion hydrolyzes significantly |
| Weak acid + strong base | Basic | Conjugate base reacts with water to make $$\text{OH}^-$$ |
| Strong acid + weak base | Acidic | Conjugate acid reacts with water to make $$\text{H}_3\text{O}^+$$ |
| Weak acid + weak base | Compare $$K_a$$ and $$K_b$$ | Larger constant dominates |

For an anion from a weak acid,

$$
\text{A}^-(aq) + \text{H}_2\text{O}(l) \rightleftharpoons \text{HA}(aq) + \text{OH}^-(aq).
$$

For a cation from a weak base,

$$
\text{BH}^+(aq) + \text{H}_2\text{O}(l) \rightleftharpoons \text{B}(aq) + \text{H}_3\text{O}^+(aq).
$$

<div class="theorem-box">

**Example.** A salt contains a cation with $$K_a=10^{-9}$$ and an anion with $$K_b=10^{-5}$$. Predict whether its dilute solution is acidic or basic and explain why 'salts are neutral' fails.

Both ions react with water, but the anion's base reaction is much more favorable. The solution is basic. Electrical neutrality still holds: zero net bulk charge does not require equal hydronium and hydroxide concentrations.

</div>

---

## Buffers

A **buffer** resists pH change when modest amounts of strong acid or strong base are added. It contains a weak acid and its conjugate base in comparable amounts (or a weak base + conjugate acid).

The reason it works is that a buffer keeps a reservoir of **both** a proton donor and a proton acceptor on hand. When a small amount of strong **acid** is added, the conjugate base $$\text{A}^-$$ neutralizes it (soaking up the added $$\text{H}_3\text{O}^+$$ to form $$\text{HA}$$); when a small amount of strong **base** is added, the weak acid $$\text{HA}$$ neutralizes it (donating a proton to form $$\text{A}^-$$). Because the strong acid or base is converted into a weak conjugate rather than left free, the pH barely moves—only the *ratio* $$[\text{A}^-]/[\text{HA}]$$ shifts slightly. The **Henderson–Hasselbalch equation** (same assumptions as the small-change approximation from equilibrium) is

$$
\text{pH} = \text{p}K_a + \log\left(\frac{[\text{A}^-]}{[\text{HA}]}\right),
$$

with concentrations evaluated after any same-volume mixing (or use moles in the ratio if volume is common to both). The equation is most reliable when both species are present and neither concentration is extremely small.

**Buffer capacity** increases with total concentration of buffer components. When $$[\text{HA}] = [\text{A}^-]$$, $$\text{pH} = \text{p}K_a$$ and the system can absorb equal challenge from added acid or base in a symmetric sense (maximum buffering range is often quoted near $$\text{p}K_a \pm 1$$).

### Buffer stoichiometry before equilibrium

When a strong acid or strong base is added to a buffer, do the neutralization reaction **before** using Henderson-Hasselbalch.

Added strong acid consumes conjugate base:

$$
\text{A}^- + \text{H}_3\text{O}^+ \longrightarrow \text{HA} + \text{H}_2\text{O}.
$$

Added strong base consumes weak acid:

$$
\text{HA} + \text{OH}^- \longrightarrow \text{A}^- + \text{H}_2\text{O}.
$$

After the stoichiometry step, use the new moles of $$\text{HA}$$ and $$\text{A}^-$$ in the Henderson-Hasselbalch ratio. If either buffer component is used up, the solution is no longer a buffer and the excess strong acid/base controls pH. Note that all pH-pKa pairs can be substituted for pOH-pKb pairs.

<div class="theorem-box">

**Example.** Two equal-volume buffers have the same acid/base ratio, but one contains ten times as many moles of each component. Compare initial pH and response to an equal small acid addition.

Henderson-Hasselbalch predicts the same initial pH because the ratios match. The acid addition converts the same number of conjugate-base moles to acid in each buffer, causing a smaller fractional ratio change in the more concentrated buffer. Equal pH does not imply equal capacity.

</div>

---

## Titrations

In a **titration**, a solution of known concentration (**titrant**) is added from a buret to the **analyte** until reaction is complete. For acid–base work, the **equivalence point** is the stoichiometric point: moles of $$\text{H}^+$$ supplied equal moles of $$\text{OH}^-$$ accepted (account for diprotic acids and stoichiometry).

Titration curve shape:

- Strong acid / strong base: equivalence near $$\text{pH} = 7$$ at $$25\,^\circ\text{C}$$, steep vertical jump.
- Weak acid / strong base: equivalence $$\text{pH} > 7$$ (conjugate base hydrolysis).
- Weak base / strong acid: equivalence $$\text{pH} < 7$$ (conjugate acid).

At the **half-equivalence point** of a weak acid titrated with strong base, $$[\text{HA}] \approx [\text{A}^-]$$ and $$\text{pH} \approx \text{p}K_a$$ (buffer maximum in that sense). Polyprotic acids show multiple equivalence steps and multiple near-plateau regions corresponding to each $$\text{p}K_a$$.

### Titration calculation stages

For a weak acid $$\text{HA}$$ titrated with strong base:

| Region | What controls pH? | Usual method |
| --- | --- | --- |
| Before base is added | Weak acid equilibrium | $$K_a$$ ICE table |
| Before equivalence | Buffer mixture of $$\text{HA}$$ and $$\text{A}^-$$ | Stoichiometry, then Henderson-Hasselbalch |
| Half-equivalence | $$[\text{HA}] = [\text{A}^-]$$ | $$\text{pH} = \text{p}K_a$$ |
| Equivalence | Conjugate base $$\text{A}^-$$ | $$K_b = K_w/K_a$$ ICE table |
| After equivalence | Excess strong base | Stoichiometry for leftover $$\text{OH}^-$$ |

For a weak base titrated with strong acid, swap the acid/base roles: the buffer contains $$\text{B}$$ and $$\text{BH}^+$$, the half-equivalence point gives $$\text{pOH} = \text{p}K_b$$ or $$\text{pH} = \text{p}K_a$$ for $$\text{BH}^+$$, and the equivalence point is acidic.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[axis lines=left, width=9cm, height=5.5cm, xmin=0, xmax=50, ymin=0, ymax=14, xlabel={volume base added}, ylabel={pH}, xtick=\empty, ytick={0,7,14}, grid=both, grid style={gray!15}]
\addplot[blue, very thick, samples=200, domain=0:50] {3 + 8/(1+exp(-0.45*(x-25))) + 0.025*x};
\addplot[dashed] coordinates {(25,0) (25,14)};
\addplot[dashed] coordinates {(0,7) (50,7)};
\node[anchor=south west] at (axis cs:25,8.6) {equivalence point};
\node[anchor=south] at (axis cs:12.5,5.0) {buffer region};
\node[anchor=north] at (axis cs:12.5,4.7) {$pH=pK_a$};
\end{axis}
\end{tikzpicture}
```

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[axis lines=left, width=9cm, height=5.5cm, xmin=0, xmax=50, ymin=0, ymax=14, xlabel={volume base added}, ylabel={pH}, xtick=\empty, ytick={0,7,14}, grid=both, grid style={gray!15}]
\addplot[blue, very thick, samples=200, domain=0:50] {3 + 8/(1+exp(-0.45*(x-25))) + 0.025*x};
\addplot[dashed] coordinates {(25,0) (25,14)};
\addplot[dashed] coordinates {(0,7) (50,7)};
\node[anchor=south west] at (axis cs:25,8.6) {equivalence point};
\node[anchor=south] at (axis cs:12.5,5.0) {buffer region};
\node[anchor=north] at (axis cs:12.5,4.7) {$pH=pK_a$};
\end{axis}
\end{tikzpicture}
```


If an acid can dissociate more than once, it's titration curve follows a polyprotic titration curve:

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[axis lines=left, width=9cm, height=5.5cm, xmin=0, xmax=70, ymin=0, ymax=14, xlabel={volume base added}, ylabel={pH}, xtick=\empty, ytick={0,7,14}, grid=both, grid style={gray!15}]
\addplot[blue, very thick, samples=240, domain=0:70] {2 + 4/(1+exp(-0.35*(x-20))) + 5/(1+exp(-0.35*(x-48))) + 0.015*x};
\addplot[dashed] coordinates {(20,0) (20,14)};
\addplot[dashed] coordinates {(48,0) (48,14)};
\node[anchor=south] at (axis cs:20,9.5) {1st eq.};
\node[anchor=south] at (axis cs:48,11.5) {2nd eq.};
\end{axis}
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** Titrate $$25.0\ \mathrm{mL}$$ of $$0.100\ M$$ weak monoprotic acid with $$0.100\ M$$ NaOH. Why must the pH method change between $$12.5$$, $$25.0$$, and $$30.0\ \mathrm{mL}$$ of added base?

At $$12.5\ \mathrm{mL}$$, equal amounts of acid and conjugate base form a buffer, so $$\mathrm{pH}=\mathrm{p}K_a$$. At $$25.0\ \mathrm{mL}$$, stoichiometric neutralization leaves conjugate base; use its hydrolysis equilibrium. At $$30.0\ \mathrm{mL}$$, excess hydroxide dominates: $$[\mathrm{OH^-}]=(0.00300-0.00250)/0.0550=0.00909\ M$$, giving pH about $$11.96$$ at $$25^\circ\mathrm{C}$$. An equilibrium expression is chosen only after identifying what remains from neutralization.

</div>

### pH Indicators

**Acid–base indicators** are weak acids or bases whose conjugate forms have different colors. The **endpoint** is where the color change is observed; it should lie near the **equivalence point** of a titration.


| Indicator | Approximate transition range | Acid color | Base color |
| --- | ---: | --- | --- |
| Methyl orange | $$3.1-4.4$$ | red | yellow |
| Bromothymol blue | $$6.0-7.6$$ | yellow | blue |
| Phenolphthalein | $$8.2-10.0$$ | colorless | pink |
| Universal indicator | broad range | red/orange | green/blue/purple |


Choose an indicator whose transition range lies within the steep vertical region of the titration curve. A strong acid-strong base titration has a steep jump around pH $$7$$, so many indicators can work. A weak acid-strong base titration has an equivalence point above $$7$$, so phenolphthalein is often better than methyl orange. A weak base-strong acid titration has an equivalence point below $$7$$, so an acidic-range indicator is usually better.

<div class="theorem-box">

**Example.** A weak-acid/strong-base titration has a steep pH jump from about 7 to 10 near equivalence. Indicator X changes color from pH 3 to 4; indicator Y changes from 8 to 9. Which is suitable, and what concentration error would an early endpoint cause?

Y changes within the steep region, so a small added volume carries it through its transition near equivalence. X changes too early, while acid remains unneutralized. Using that too-small base volume as the equivalence volume underestimates the initial acid amount and concentration. The best choice matches the curve's steep interval, not a rule that every indicator must change at pH 7.

</div>

---

## Common ion effect

The **common ion effect** is the suppression of ionization of a weak electrolyte when a solution already contains one of its ions (from a salt). It is the same Le Châtelier’s principle logic as in [Unit 7](/notes/ap/chem/equilibrium/): added $$\text{A}^-$$ shifts $$\text{HA}$$ ionization left, lowering $$[\text{H}_3\text{O}^+]$$.

---

:::checklist

1. Identify strong vs weak; write the correct net ionic chemistry.
2. Use $$K_w$$, $$K_a$$, and $$K_b$$ at a consistent temperature; link conjugates with $$K_a K_b = K_w$$.
3. Use **ICE** tables for weak acids/bases; watch dilution and the **common ion effect**.
4. Buffers: **Henderson–Hasselbalch equation** or full equilibrium when assumptions fail.
5. Titrations: stoichiometry first, then equilibrium at the **equivalence point** or **half-equivalence point** for $$\text{p}K_a$$.

:::

<div class="theorem-box">

**Example.** Adding sodium acetate to acetic acid raises pH. Does the acid's Ka decrease? Explain using its equilibrium expression.

Ka stays fixed at a fixed temperature. Added acetate raises the numerator of $$Q_a=[H_3O^+][A^-]/[HA]$$ before adjustment, so some hydronium and acetate combine to form HA. The resulting lower hydronium concentration restores the same Ka, rather than creating a new constant.

</div>

---

## Reference: common strong acids and bases

| Strong acids (typical list) | Strong bases (typical list) |
|----------------------------|-----------------------------|
| $$\text{HCl}$$, $$\text{HBr}$$, $$\text{HI}$$ | $$\text{LiOH}$$, $$\text{NaOH}$$, $$\text{KOH}$$, … |
| $$\text{HNO}_3$$, $$\text{HClO}_4$$, $$\text{HClO}_3$$ | $$\text{Ca(OH)}_2$$, $$\text{Sr(OH)}_2$$, $$\text{Ba(OH)}_2$$ |
| $$\text{H}_2\text{SO}_4$$ (first $$\text{H}^+$$ only) | |

$$\text{HF}$$ is weak; $$\text{HSO}_4^-$$ is a weak acid.

<div class="theorem-box">

**Example.** A student uses the strong-acid list to assign $$[H_3O^+]=2C$$ for every sulfuric acid solution. Explain the needed qualification.

The first ionization is treated as complete, but the second is governed by the bisulfate equilibrium. Its contribution depends on concentration and the hydronium already present. Two equivalents of strong base are needed per mole for complete neutralization, but that stoichiometric fact does not mean both ionizations are initially complete.

</div>

---

:::equations

| Idea | Equation | Conditions |
| --- | --- | --- |
| Water and pH | $$K_w=[H_3O^+][OH^-]$$; $$\mathrm{pH}=-\log[H_3O^+]$$; $$\mathrm{pH}+\mathrm{pOH}=\mathrm{p}K_w$$ | $$\mathrm{p}K_w=14.00$$ at 25 degrees C in the dilute-solution model. |
| Weak acid/base | $$K_a=[H_3O^+][A^-]/[HA]$$; $$K_b=[BH^+][OH^-]/[B]$$ | Water omitted as solvent; conjugate pairs satisfy $$K_aK_b=K_w$$. |
| Weak acid only | $$K_a=x^2/(C-x)$$; $$x\approx\sqrt{K_aC}$$ | No added conjugate base; approximation needs small depletion and negligible water contribution. |
| Percent ionization | $$\%ionization=x/C\times100\%$$ | x is the amount ionized per unit volume, not necessarily every hydronium source. |
| Buffer | $$\mathrm{pH}=\mathrm{p}K_a+\log([A^-]/[HA])$$ | Neutralization first; both components remain appreciable. |
| Strong-acid addition | $$n_{A^-,f}=n_{A^-,0}-n_{H^+}$$; $$n_{HA,f}=n_{HA,0}+n_{H^+}$$ | Valid before A- is exhausted; divide by common volume or use the mole ratio in the buffer equation. |
| Monoprotic equivalence | $$M_aV_a=M_bV_{eq}$$ | One acidic proton and one hydroxide per base formula unit. |
| Half-equivalence | $$\mathrm{pH}\approx\mathrm{p}K_a$$ | Weak monoprotic acid titrated by strong base in the buffer regime. |
| Equivalence hydrolysis | $$[OH^-]\approx\sqrt{K_bC_{salt}}$$ | Weak-acid/strong-base titration; use total mixed volume and check small change. |
| After equivalence | $$[OH^-]\approx n_{OH^-,excess}/V_{total}$$ | Excess strong base dominates over salt hydrolysis and water autoionization. |

:::

## Practice

### MCQ

::::problem
1. A buffer contains $$0.0100\ \mathrm{mol}$$ HA and $$0.0150\ \mathrm{mol}$$ its conjugate base. Add $$0.0200\ \mathrm{mol}$$ HCl and make the final volume $$0.500\ \mathrm{L}$$. With $$K_a=10^{-5}$$, what is the approximate pH?

   (A) $$2.00$$<br>
   (B) $$4.82$$<br>
   (C) $$5.18$$<br>
   (D) $$12.00$$

:::solution
Strong acid consumes all 0.0150 mol conjugate base and leaves 0.00500 mol excess hydronium. Its concentration is 0.0100 M, giving pH 2.00. The common hydronium suppresses the weak acid's additional ionization. Henderson-Hasselbalch is inapplicable after a buffer component is exhausted.

$$
\boxed{\text{A}}.
$$
:::
::::

::::problem
2. A weak monoprotic acid reaches equivalence after $$40.0\ \mathrm{mL}$$ of strong base. At $$30.0\ \mathrm{mL}$$ added, its pH is 5.00. What is its approximate Ka?

   (A) $$1.0\times10^{-5}$$<br>
   (B) $$3.3\times10^{-6}$$<br>
   (C) $$3.0\times10^{-5}$$<br>
   (D) $$1.0\times10^{-10}$$

:::solution
At three-quarter equivalence, conjugate base to remaining acid is $$30/(40-30)=3$$. Thus $$5.00=\mathrm{p}K_a+\log3$$, giving $$\mathrm{p}K_a=4.523$$ and $$K_a=3.0\times10^{-5}$$. The observed pH equals pKa only at half-equivalence.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
3. A weak acid has $$K_a=1.0\times10^{-3}$$ and formal concentration $$0.0100\ M$$. Neglecting water autoionization, which pH and approximation judgment are correct?

   (A) 2.50; small-x is valid<br>
   (B) 2.57; small-x is invalid<br>
   (C) 3.00; small-x is valid<br>
   (D) 1.00; small-x is invalid

:::solution
The shortcut gives $$x=0.00316\ M$$, more than 5% of 0.0100 M. Solving $$x^2/(0.0100-x)=0.0010$$ instead gives $$x=0.00270\ M$$ and pH 2.57. Calling an acid weak does not guarantee small fractional ionization.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
4. At $$25^\circ\mathrm{C}$$, mix $$20.0\ \mathrm{mL}$$ of $$0.100\ M$$ strong monoprotic acid with $$15.0\ \mathrm{mL}$$ of $$0.100\ M$$ barium hydroxide. Assuming complete dissociation and additive volumes, what is pH?

   (A) $$1.54$$<br>
   (B) $$7.00$$<br>
   (C) $$12.15$$<br>
   (D) $$12.46$$

:::solution
Acid supplies 0.00200 mol hydronium; barium hydroxide supplies $$2(0.0150)(0.100)=0.00300\ \mathrm{mol}$$ hydroxide. Excess hydroxide is $$0.00100/0.0350=0.0286\ M$$. Its pOH is 1.54, giving pH 12.46. The base produces two hydroxide ions per formula unit.

$$
\boxed{\text{D}}.
$$
:::
::::

::::problem
5. Two $$1.00\ \mathrm{L}$$ buffers initially have equal acid/base ratios and the same pH. X contains 0.0100 mol each of HA and A-, and Y contains 0.100 mol each. Add 0.00500 mol HCl to each with negligible volume change. Which pH changes follow?

   (A) X: $$-0.477$$; Y: $$-0.0435$$<br>
   (B) Both: $$-0.477$$<br>
   (C) X: $$+0.477$$; Y: $$+0.0435$$<br>
   (D) X: $$-0.0435$$; Y: $$-0.477$$

:::solution
For X the new base/acid ratio is $$0.00500/0.0150=1/3$$, giving a -0.477 pH change. For Y it is $$0.0950/0.105=0.9048$$, giving -0.0435. Equal initial pH does not imply equal capacity; the same addition consumes very different fractions of the available base.

$$
\boxed{\text{A}}.
$$
:::
::::

::::problem
6. At equivalence, a weak-acid/strong-base titration contains $$0.0400\ M$$ conjugate base. The acid has $$K_a=4.0\times10^{-5}$$ at $$25^\circ\mathrm{C}$$. What is the approximate pH?

   (A) $$5.50$$<br>
   (B) $$7.00$$<br>
   (C) $$8.50$$<br>
   (D) $$9.50$$

:::solution
The base constant is $$K_b=10^{-14}/(4.0\times10^{-5})=2.5\times10^{-10}$$. Hydrolysis gives $$[\mathrm{OH^-}]\approx\sqrt{K_bC}=3.16\times10^{-6}\ M$$. Thus pOH is 5.50 and pH is 8.50. The small change is less than 0.01% of the salt concentration, so the approximation is justified.

$$
\boxed{\text{C}}.
$$
:::
::::

### FRQ

::::frq{id=chem-acidbase-challenge-1}
7. A 25.00 mL sample of monoprotic weak acid HA requires 30.00 mL of 0.1000 M NaOH to reach equivalence. At 10.00 mL added, the pH is 4.20. All measurements are at $$25^\circ\mathrm{C}$$; use $$K_w=1.00\times10^{-14}$$ and additive volumes.

   $$(A)$$ Determine the original acid concentration and infer Ka from the partial-titration measurement.

   $$(B)$$ Estimate the initial pH and check the small-change approximation.

   $$(C)$$ Calculate the approximate pH at equivalence, accounting for dilution.

   $$(D)$$ Calculate the pH after 32.00 mL of NaOH has been added and explain why the controlling calculation changes.

:::solution
$$(A)$$ Initial acid is $$0.03000(0.1000)=0.003000\ \mathrm{mol}$$, giving $$0.003000/0.02500=0.1200\ M$$. At 10.00 mL, neutralization leaves 0.002000 mol HA and forms 0.001000 mol A-. Thus $$4.20=\mathrm{p}K_a+\log(0.001000/0.002000)$$, giving $$\mathrm{p}K_a=4.501$$ and $$K_a=3.15\times10^{-5}$$. The pH measurement is not at half-equivalence.

$$(B)$$ Before adding base, $$[H_3O^+]\approx\sqrt{K_aC}=\sqrt{(3.15\times10^{-5})(0.1200)}=1.94\times10^{-3}\ M$$. The pH is approximately 2.71. The fractional change is $$0.00194/0.1200=1.62\%$$, below the usual 5% guideline. This justifies the estimate at the stated precision, unlike simply assuming every weak acid ionizes negligibly.

$$(C)$$ The salt concentration is $$0.003000/(0.02500+0.03000)=0.05455\ M$$. Its base constant is $$K_b=K_w/K_a=3.17\times10^{-10}$$. Hydrolysis gives $$[OH^-]\approx\sqrt{K_bC}=4.16\times10^{-6}\ M$$, so pOH is 5.38 and pH is 8.62. The acid has been converted to conjugate base; the Henderson-Hasselbalch acid/base ratio is not the correct equivalence-point model.

$$(D)$$ Base exceeds the initial acid by $$0.003200-0.003000=0.0002000\ \mathrm{mol}$$. In 0.05700 L, $$[OH^-]=0.003509\ M$$, giving pOH 2.455 and pH 11.545. Excess strong hydroxide dominates and suppresses the conjugate base's hydrolysis. Stoichiometry must identify this excess before choosing an equilibrium equation.
:::
::::

::::frq{id=chem-acidbase-challenge-2}
8. Prepare a 1.00 L buffer containing 0.0800 mol HA and 0.120 mol NaA. The acid has $$K_a=2.00\times10^{-5}$$ at $$25^\circ\mathrm{C}$$. Neglect volume changes when small amounts of solid or concentrated reagent are added, and use the usual buffer approximation where valid.

   $$(A)$$ Calculate the initial pH and the pH after adding 0.0500 mol HCl. Show the neutralization step first.

   $$(B)$$ For a fresh original buffer, calculate the maximum HCl addition that keeps pH at or above 4.50.

   $$(C)$$ Dilute a fresh original buffer to 10.00 L, then add 0.0500 mol HCl. Compare its approximate final pH with part A and explain how capacity per liter differs.

   $$(D)$$ For another fresh original buffer, add 0.130 mol HCl. Estimate the final pH and explain why the buffer equation must no longer be used.

:::solution
$$(A)$$ Initially $$\mathrm{pH}=4.699+\log(0.120/0.0800)=4.875$$. Added acid reacts by $$\mathrm{A^-+H^+\rightarrow HA}$$, leaving 0.0700 mol A- and 0.130 mol HA. The new pH is $$4.699+\log(0.0700/0.130)=4.430$$. Using the original ratio after addition would miss the chemical consumption of the buffer base.

$$(B)$$ Let x be moles HCl added. The boundary condition is $$10^{4.50-4.699}=(0.120-x)/(0.0800+x)=0.6325$$. Solving gives $$x=(0.120-0.6325(0.0800))/(1+0.6325)=0.0425\ \mathrm{mol}$$. This is below the 0.120 mol needed to exhaust the base; a specified pH tolerance can be exceeded well before a component disappears.

$$(C)$$ Dilution leaves component mole amounts unchanged, and the same acid addition again leaves 0.0700 mol A- and 0.130 mol HA. Their concentration ratio is unchanged by the common larger volume, so the approximate final pH is again 4.430. The buffer contains one-tenth as many buffer moles per liter, however, so its capacity per liter is lower. Equal total added moles to the whole sample is different from equal added moles per liter.

$$(D)$$ All 0.120 mol A- is protonated, leaving 0.0100 mol excess strong acid in 1.00 L. Thus hydronium is approximately 0.0100 M and pH is about 2.00; weak-acid ionization is suppressed by this hydronium. The Henderson-Hasselbalch approximation assumes appreciable amounts of both HA and A-. Substituting a negative remaining base amount would be chemically meaningless.
:::
::::
