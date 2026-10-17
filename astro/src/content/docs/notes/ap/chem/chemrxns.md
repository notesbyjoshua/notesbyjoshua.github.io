---
title: "Unit 4: Chemical Reactions"
description: "AP Chemistry notes on chemical reactions, stoichiometry, net ionic equations, redox, precipitation, and reaction evidence."
sidebar:
  order: 4
---

## Physical versus chemical change

- A **chemical change** produces new substances with new chemical identities. Observable clues include a lasting color change, gas evolution (from something other than simple boiling), formation of a precipitate, a large temperature change from the reaction itself, light emission, or a new odor. Those clues are suggestive, not proof; the decisive idea is reorganization at the molecular level (bond breaking and forming).
- A **physical change** alters state, size, shape, or mixing without creating a new chemical species: melting, boiling, dissolving sugar in water (the sucrose molecules remain intact), or crushing a sample. Dissolving an ionic compound in water is still often grouped with “physical” solution formation in introductory courses, even though the ions separate from the crystal—a distinction worth keeping straight when you discuss conductivity and equilibrium later.

<div class="theorem-box">

**Example.** Bubbles appear both when water boils and when acid is added to a carbonate. Explain why the bubbles alone cannot distinguish physical and chemical change.

Boiling produces water vapor, so molecular identity is retained. Acid-carbonate reaction produces carbon dioxide, a different substance. Gas formation is an observation; identifying the gas or showing the change in composition establishes which process occurred.

</div>

---

## Representing and balancing reactions

A **chemical equation** lists **reactants** (left) and **products** (right), usually separated by a single arrow $$(\longrightarrow)$$ for a reaction treated as one-way in stoichiometry, or $$(\rightleftharpoons)$$ when equilibrium matters ([Unit 7](/notes/ap/chem/equilibrium/)). **State symbols** clarify what you are counting:

$$(s)$$ solid, $$(l)$$ liquid, $$(g)$$ gas, $$(aq)$$ dissolved in water (aqueous).

If an element is a component of the reaction **ALONE**, they are written in their standard/naturally-occuring form (e.g. $$\text{O}_2(g)$$, $$\text{Na}(s)$$, $$\text{Br}_2(l)$$). Otherwise, they can take on any form. Coefficients are the smallest **integers** (or a set of integers) consistent with conservation of atoms: they give **mole ratios** for limiting-reactant work, titrations, and gas-law stoichiometry. Make sure that on each side of a reaction, you start and end with the same number of atoms/moles.

### Balancing by inspection (non-redox and simple cases)

1. **Balance** elements that appear in only one reactant and one product first (often metals or central atoms).
2. Treat **unchanged polyatomic ions** (such as $$\text{NO}_3^-$$ or $$\text{SO}_4^{2-}$$) as a unit if they appear intact on both sides (Make sure to include them in brackets, otherwise they do not count as polyatomic ions).
3. Balance **hydrogen** and **oxygen** last when they appear in several compounds (common in combustion and acid–base).
4. If you temporarily need a **fractional** coefficient to balance an element (e.g. $$\frac{1}{2}\text{O}_2$$), **multiply the entire equation** by the denominator so all coefficients are integers.

The balanced equation conserves **mass** (atom counts). For **ionic** reactions in solution, you may also write:

- **Molecular equation** — Molecular formulas are formulas as written in the bottle/usually stated in the problem (e.g. $$\text{AgNO}_3(aq) + \text{NaCl}(aq)$$)

- **Total ionic equation** — You treat strong electrolytes as **separated ions**, while solids, liquids, weak electrolytes, and gases usually **undissociated** (Check solubility rules below for electrolytes; strong electrolytes are soluble in water)

- **Net ionic equation** — Write the total ionic equation but cancel **spectator ions** that do not change (Basically anything that can cancel on both sides) and only species that actually react

**Redox** reactions in acidic or basic solution often needs the *half-reaction method* (below) because oxidation numbers change and **electron** and **charge** balance are not handled by atom counting alone.

<div class="theorem-box">

**Example.** A student balances hydrogen combustion by changing $$\mathrm{H_2O}$$ to $$\mathrm{H_2O_2}$$. Explain the error and give the balanced equation for making water.

Changing a subscript changes the product's identity to hydrogen peroxide. Coefficients change amounts without changing identities: $$2\mathrm{H_2}+\mathrm{O_2}\rightarrow2\mathrm{H_2O}$$. Both sides now contain four H atoms and two O atoms.

</div>

---

## Stoichiometry, limiting reactants, and yield

Once an equation is balanced, the coefficients are **mole ratios**: a conversion factor between any two species in the reaction. Every quantitative reaction problem is some version of the same three-step path:

1. Convert what you are **given** into **moles** (using molar mass for a mass, $$M\times V$$ for a solution, or the ideal gas law $$PV=nRT$$ for a gas).
2. Use the **mole ratio** from the balanced equation to cross over to the species you **want**.
3. Convert moles of the wanted species back into the requested unit (grams, liters of solution, liters of gas, particles).

$$
\text{given quantity} \longrightarrow \text{mol given} \xrightarrow{\text{mole ratio}} \text{mol wanted} \longrightarrow \text{wanted quantity}.
$$

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing,angles,quotes}
\begin{tikzpicture}[>=Stealth, font=\small]
\node[draw, rounded corners, fill=blue!8] (mol) at (0,0) {moles};
\node[draw, rounded corners] (mass1) at (-4,1.6) {mass};
\node[draw, rounded corners] (sol1) at (-4,0) {solution volume};
\node[draw, rounded corners] (gas1) at (-4,-1.6) {gas volume};
\node[draw, rounded corners] (ratio) at (0,-2.4) {balanced-equation mole ratio};
\node[draw, rounded corners] (mass2) at (4,1.6) {target mass};
\node[draw, rounded corners] (sol2) at (4,0) {target solution};
\node[draw, rounded corners] (gas2) at (4,-1.6) {target gas};
\foreach \a in {mass1,sol1,gas1}{\draw[->, thick] (\a) -- (mol);}
\draw[->, thick] (mol) -- (ratio);
\foreach \a in {mass2,sol2,gas2}{\draw[->, thick] (ratio) -- (\a);}
\end{tikzpicture}
```

### Limiting and excess reactants

When amounts of two or more reactants are given, one usually runs out first and caps how much product forms—the **limiting reactant**. The others are **excess reactants** and have leftover material when the reaction stops. To find the limiting reactant, convert each reactant to moles and divide by its coefficient; the **smallest** of these ratios marks the limiting reactant. Equivalently, pick either reactant, compute how much of the other it *would* require, and compare to how much is actually present.

At the particle level, the limiting reactant runs out first. Some particles of the excess reactant remain because there are no longer enough particles of the other reactant to react in the required ratio.

<div class="theorem-box">

**Example.** For $$\mathrm{N_2+3H_2\rightarrow2NH_3}$$, mix $$2.00\ \mathrm{mol}$$ nitrogen with $$3.00\ \mathrm{mol}$$ hydrogen. A student calls nitrogen limiting because fewer moles were supplied. Find the error and the remaining reactant amount.

Compare amounts divided by coefficients: $$2.00/1=2.00$$ for nitrogen and $$3.00/3=1.00$$ for hydrogen. Hydrogen allows less reaction and is limiting. It consumes $$1.00\ \mathrm{mol}$$ nitrogen, leaving $$1.00\ \mathrm{mol}$$ nitrogen and producing $$2.00\ \mathrm{mol}$$ ammonia. Raw mole counts cannot be compared without the reaction ratio.

</div>

### Percent yield

The **theoretical yield** is the maximum product predicted from the limiting reactant by stoichiometry. The **actual yield** is what is recovered in the lab, which is almost always smaller because of side reactions, incomplete reactions, transfer losses, or impure reactants. The two are compared with

$$
\text{percent yield} = \frac{\text{actual yield}}{\text{theoretical yield}} \times 100\%.
$$

A yield above $$100\%$$ usually signals a measurement problem, such as a product that is still wet with solvent or contaminated with leftover reactant.

<div class="theorem-box">

**Example.** A reaction has a theoretical yield of $$1.20\ \mathrm{g}$$, but the collected solid weighs $$1.32\ \mathrm{g}$$. Is the reaction more than completely successful? Give a plausible explanation and its effect on the calculated yield.

The apparent yield is $$1.32/1.20\times100\%=110\%$$. This does not mean more pure product formed than stoichiometry allows. Retained water or another contaminant could contribute to the measured mass, making the numerator too large. Drying to constant mass can test for retained solvent; an incorrect theoretical-yield calculation is another possibility to check.

</div>

### Gravimetric and volumetric analysis

Two common quantitative experiments rest entirely on this stoichiometry:

- **Gravimetric analysis** isolates a product (often a filtered, dried **precipitate**) and weighs it; the mass of the pure solid is converted through the mole ratio back to the amount of the unknown ion in the original sample.
- **Titration** (volumetric analysis) delivers a measured volume of a solution of known concentration (the **titrant**) until it exactly reacts with the analyte at the **equivalence point**. From $$n=MV$$ and the mole ratio you solve for the unknown concentration or amount. Acid–base titrations are explored fully in [Unit 8](/notes/ap/chem/acidbase/); redox titrations follow the same bookkeeping using the balanced electron-transfer equation.

<div class="theorem-box">

**Example.** A $$0.500\ \mathrm{g}$$ impure chloride sample produces $$0.574\ \mathrm{g}$$ dry AgCl after adding excess silver nitrate. Find the chloride mass percent using molar masses $$143.3$$ for AgCl and $$35.45\ \mathrm{g/mol}$$ for Cl. Explain the effect of incomplete precipitation.

The precipitate represents $$0.574/143.3=0.00401\ \mathrm{mol}$$ chloride because AgCl contains one chloride per formula unit. Chloride mass is $$0.00401(35.45)=0.142\ \mathrm{g}$$, giving $$28.4\%$$ chloride by mass. Incomplete precipitation leaves some chloride unmeasured and biases the result low. The whole precipitate mass cannot be counted as original chloride because much of it is added silver.

</div>

---

## Double-displacement (metathesis) and precipitation

In a **double-displacement** reaction, cations and anions exchange partners, often in solution:

$$
\text{AB}(aq) + \text{CD}(aq) \longrightarrow \text{AD} (aq) + \text{CB} (s)
$$

If one combination is insoluble (in the example above it is $$CB$$), it forms a **precipitate**, a solid that may appear as cloudiness, flecks, or a settled solid at the bottom of the vessel. Different precipitates will have different colors, which may be useful in determining the contents of the reaction. If all ionic products remain soluble (aqueous), no net reaction occurs.

Learn the **solubility rules** to predict precipitates. These AP-level shortcuts have exceptions; exact solubility is handled later with $$K_{sp}$$.

| Usually soluble | Important exceptions |
| --- | --- |
| Group 1 cations and $$\text{NH}_4^+$$ salts | No common exceptions |
| $$\text{NO}_3^-$$, $$\text{C}_2\text{H}_3\text{O}_2^-$$ / $$\text{CH}_3\text{COO}^-$$, $$\text{ClO}_3^-$$, $$\text{ClO}_4^-$$ | No common exceptions |
| $$\text{Cl}^-$$, $$\text{Br}^-$$, $$\text{I}^-$$ | Insoluble with $$\text{Ag}^+$$, $$\text{Pb}^{2+}$$, and $$\text{Hg}_2^{2+}$$ |
| $$\text{SO}_4^{2-}$$ | Insoluble or only slightly soluble with $$\text{Ba}^{2+}$$, $$\text{Sr}^{2+}$$, $$\text{Pb}^{2+}$$, $$\text{Ca}^{2+}$$, and $$\text{Hg}_2^{2+}$$ |

| Usually insoluble | Important exceptions |
| --- | --- |
| $$\text{CO}_3^{2-}$$, $$\text{PO}_4^{3-}$$, $$\text{CrO}_4^{2-}$$, $$\text{S}^{2-}$$ | Soluble with Group 1 cations and $$\text{NH}_4^+$$ |
| $$\text{OH}^-$$ | Soluble with Group 1 cations and $$\text{NH}_4^+$$; $$\text{Ba}^{2+}$$, $$\text{Sr}^{2+}$$, and $$\text{Ca}^{2+}$$ hydroxides are more soluble than most other metal hydroxides |

For a precipitation prediction, swap ion partners, apply the table, and write a net ionic equation only for the solid that forms. Example:

$$
\text{Ag}^+(aq) + \text{Cl}^-(aq) \longrightarrow \text{AgCl}(s)
$$

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing,angles,quotes}
\begin{tikzpicture}[>=Stealth, font=\small]
\draw[rounded corners] (-4,-1.7) rectangle (-0.4,1.7); \node at (-2.2,1.95) {before mixing};
\draw[rounded corners] (0.4,-1.7) rectangle (4,1.7); \node at (2.2,1.95) {after mixing};
\foreach \x/\y in {-3.3/0.9,-2.7/-0.5,-1.7/0.5,-1.2/-1.0}{\fill[blue] (\x,\y) circle (2pt);}
\foreach \x/\y in {-3.0/-1.0,-2.1/1.0,-1.4/-0.2,-0.8/0.9}{\fill[red] (\x,\y) circle (2pt);}
\foreach \x/\y in {1.0/1.0,1.5/0.2,3.4/0.7,3.0/-1.0}{\fill[gray] (\x,\y) circle (2pt);}
\foreach \x/\y in {1.7/-1.1,2.0/-1.1,2.3/-1.1,1.85/-0.85,2.15/-0.85}{\fill[blue] (\x,\y) circle (2.2pt); \fill[red] ({\x+0.12},{\y+0.12}) circle (2.2pt);}
\node[align=center] at (2.2,-1.45) {solid precipitate\\plus spectator ions};
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** Mix $$20.0\ \mathrm{mL}$$ of $$0.100\ M$$ silver nitrate with $$30.0\ \mathrm{mL}$$ of $$0.100\ M$$ sodium chloride. Assuming essentially complete precipitation, identify the excess reacting ion and its concentration.

There are $$2.00\ \mathrm{mmol}$$ silver ions and $$3.00\ \mathrm{mmol}$$ chloride. The one-to-one reaction leaves $$1.00\ \mathrm{mmol}$$ chloride in $$50.0\ \mathrm{mL}$$, or $$0.0200\ M$$. Sodium and nitrate remain spectators; they must still appear in a particle diagram of the final solution.

</div>

---

## Acid–base (neutralization) reactions

**Neutralization** between a strong acid and strong base yields water and an ionic salt:

$$
\text{acid} + \text{base} \longrightarrow \text{salt} + \text{H}_2\text{O}.
$$

Such proton-transfer reactions are often rapid because water is a very stable product. This is a special form of a double-displacement reaction

Reactions of metal carbonates (and bicarbonates) with acid produce carbon dioxide as well, because carbonic acid is unstable and decomposes:

$$
\text{H}_2\text{CO}_3 \longrightarrow \text{H}_2\text{O} + \text{CO}_2.
$$

Metal oxides (basic anhydrides) react with acids like other bases as well, just giving up the oxygen to water instead of hydrogen.

<div class="theorem-box">

**Example.** Equal volumes of $$0.100\ M$$ HCl and $$0.100\ M$$ barium hydroxide are mixed. Does equal molarity imply neutralization to equivalence?

Each mole of barium hydroxide supplies two moles of hydroxide. If each volume is $$V$$ liters, acid supplies $$0.100V$$ moles H+ while base supplies $$0.200V$$ moles OH-. The remaining $$0.100V$$ moles hydroxide occupy $$2V$$ liters, giving $$0.0500\ M$$ hydroxide. The mixture is basic.

</div>

---

## Combination, decomposition, and combustion

**Synthesis** (combination) builds one product from simpler reactants, which can be elements or compounds:

$$
\text{A} + \text{B} \longrightarrow \text{AB}.
$$

**Decomposition** is the reverse picture: one compound breaks into two or more substances, often with heat or electricity. The products can be elements or compounds:

$$
\text{AB} \longrightarrow \text{A} + \text{B}.
$$

**Combustion** of a hydrocarbon in excess oxygen produces carbon dioxide and water (and other products if the fuel contains other elements such as sulfur). Incomplete combustion can yield $$\text{CO}$$ or soot (carbon):

$$
\text{Hydrocarbon} + O_2 \longrightarrow CO_2 (g) + H_2O (g / l).
$$

As usual, you should balance coefficients to make a balanced equation.

<div class="theorem-box">

**Example.** Heating calcium carbonate produces calcium oxide and carbon dioxide. Classify the reaction and decide whether a decomposition reaction must produce elements.

The reaction is $$\mathrm{CaCO_3\rightarrow CaO+CO_2}$$. One reactant gives multiple products, so this is decomposition, even though both products are compounds. Calcium stays $$+2$$, carbon $$+4$$, and oxygen $$-2$$, so this decomposition is not redox.

</div>

---

## Single-displacement reactions

In **single-displacement**, an element in its standard state replaces ions of another element in solution (or in a melt). For metals (and hydrogen in acid), activity order decides whether reaction occurs: a metal higher in the **activity series** reduces the cation of a metal below it. Hydrogen’s position marks which metals react with dilute acid to liberate $$\text{H}_2$$.


| More active metals | Tend to be oxidized more easily |
| --- | --- |
| $$\mathrm{Li, K, Ba, Ca, Na}$$ | strongest reducing metals |
| $$\mathrm{Mg, Al, Zn, Fe, Ni, Sn, Pb}$$ | can replace ions below them in solution |
| $$\mathrm{H_2}$$ | reference: metals above can react with acids to form $$\mathrm{H_2}$$ |
| $$\mathrm{Cu, Ag, Pt, Au}$$ | least active; often remain unoxidized |


For halogens, a more reactive halogen displaces the halide ion of a less reactive halogen from solution. Reactivity decreases down the group ($$\text{F}_2 > \text{Cl}_2 > \text{Br}_2 > \text{I}_2$$).

<div class="theorem-box">

**Example.** Metal X displaces copper from copper(II) solution but does not displace magnesium from magnesium(II) solution under comparable conditions. Place X in a relative activity series.

X is more readily oxidized than copper but less readily oxidized than magnesium. The supported order is $$\mathrm{Mg>X>Cu}$$. These tests bracket X; they do not uniquely identify it or establish its position relative to every other metal.

</div>

---

## Oxidation–reduction (redox)

**Redox** reactions transfer electrons between species. **Oxidation** is loss of electrons (increase in **oxidation number**); **reduction** is gain of electrons (decrease in oxidation number). A very helpful mnemonic is **OIL RIG**: **O**xidation **I**s **L**osing, **R**eduction **I**s **G**aining.

The **reducing agent** is the one being oxidized, and the **oxidizing agent** is the one being reduced. Assigning oxidation states to every atom in a formula is the standard bookkeeping method (refer to [Unit 1](/notes/ap/chem/atomicstrucprop/)). Many combustion, single-displacement, and electrochemical processes are redox; they are often slower in the lab than simple precipitation or strong acid–strong base neutralization because covalent bonds must break and form in the elemental or molecular reactants.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning}
\begin{tikzpicture}[>=Stealth, font=\small]
\node (zn) at (-3,0) {$\mathrm{Zn}$};
\node (zn2) at (-1,0) {$\mathrm{Zn^{2+}}+2e^-$};
\node (cu) at (1,0) {$\mathrm{Cu^{2+}}+2e^-$};
\node (cu0) at (3,0) {$\mathrm{Cu}$};
\draw[->, thick, blue] (zn) -- (zn2) node[midway, above] {oxidation};
\draw[->, thick, red] (cu) -- (cu0) node[midway, above] {reduction};
\draw[->, very thick] (-1.0,-0.7) -- (1.0,-0.7) node[midway, below] {electrons transferred};
\end{tikzpicture}
```

### Assigning oxidation numbers (quick rules)

The whole framework depends on assigning oxidation numbers consistently. The standard priority list:

- A **free element** is $$0$$ (e.g. $$\text{O}_2$$, $$\text{Na}$$, $$\text{P}_4$$).
- A **monatomic ion** equals its charge ($$\text{Na}^+$$ is $$+1$$, $$\text{S}^{2-}$$ is $$-2$$).
- **Fluorine** is always $$-1$$ in compounds; **oxygen** is usually $$-2$$ (but $$-1$$ in peroxides such as $$\text{H}_2\text{O}_2$$ and positive when bonded to F); **hydrogen** is $$+1$$ with nonmetals but $$-1$$ in metal hydrides such as $$\text{NaH}$$.
- The sum of oxidation numbers equals the overall **charge** of the species (zero for a neutral formula, the ion charge for a polyatomic ion).

<div class="theorem-box">

**Example.** Assign oxygen's oxidation number in $$\mathrm{H_2O_2}$$ and $$\mathrm{OF_2}$$. Why does assuming oxygen is always $$-2$$ fail?

In peroxide, hydrogen is $$+1$$, so $$2(+1)+2x=0$$ gives oxygen $$-1$$. In $$\mathrm{OF_2}$$, fluorine is $$-1$$, so $$x+2(-1)=0$$ gives oxygen $$+2$$. The sum must match the total charge, but the most reliable assignment rules must be applied first. Oxygen's usual $$-2$$ value has specific exceptions.

</div>

### Recognizing and classifying redox

If *any* element changes oxidation number from reactants to products, the reaction is redox. Combustion, single-displacement, and many synthesis/decomposition reactions are redox; most precipitation and acid–base reactions are not. A special case is **disproportionation**, where a *single* element is **both oxidized and reduced** in the same reaction—one portion goes up in oxidation number while another goes down (for example, $$\text{Cl}_2$$ reacting with cold base to give $$\text{Cl}^-$$ and $$\text{ClO}^-$$). The reverse, where two different oxidation states of an element combine into one intermediate state, is **comproportionation**.

Strong **oxidizing agents** (easily reduced) include $$\text{F}_2$$, $$\text{O}_2$$, $$\text{Cl}_2$$, $$\text{MnO}_4^-$$, $$\text{Cr}_2\text{O}_7^{2-}$$, and concentrated $$\text{HNO}_3$$. Strong **reducing agents** (easily oxidized) include reactive metals such as $$\text{Na}$$, $$\text{K}$$, and $$\text{Mg}$$, as well as $$\text{H}_2$$. These tendencies are quantified later as **standard reduction potentials** in [Unit 9](/notes/ap/chem/thermoelectro/).

<div class="theorem-box">

**Example.** Compare $$\mathrm{HCl+NaOH\rightarrow NaCl+H_2O}$$ with $$\mathrm{2H_2+O_2\rightarrow2H_2O}$$. Both form water; why is only the second redox?

In neutralization, H remains $$+1$$, O remains $$-2$$, Na remains $$+1$$, and Cl remains $$-1$$. No oxidation numbers change. In the second reaction, hydrogen changes from $$0$$ to $$+1$$ and oxygen from $$0$$ to $$-2$$, indicating oxidation and reduction. Product identity alone does not classify the electron-transfer behavior.

</div>

### Half-reactions (oxidation and reduction)

A **half-reaction** shows only the oxidation or only the reduction part of an electron transfer. Electrons $$(e^-)$$ appear as a **product** in the **oxidation** half-reaction (electrons are lost) and as a **reactant** in the **reduction** half-reaction (electrons are gained). After each half-reaction is balanced for **atoms** and **charge**, you **multiply** one or both by integers so the number of electrons lost equals the number gained, then add the half-reactions and cancel duplicated species (including $$e^-$$, $$\text{H}_2\text{O}$$, $$\text{H}^+$$, or $$\text{OH}^-$$).

**Acidic solutions** (common AP setup):

:::checklist

1. Split the net ionic transformation into **oxidation** and **reduction** halves.

2. Balance all atoms **except** O and H.

3. Balance **O** with $$\text{H}_2\text{O}$$.

4. Balance **H** with $$\text{H}^+$$.

5. Balance **charge** with $$e^-$$ on the correct side.

6. Equalize electrons; add the halves; simplify.

:::

**Basic solution:** either balance as in acid and then add $$\text{OH}^-$$ to **both sides** in pairs that neutralize $$\text{H}^+$$ as water, or balance using $$\text{H}_2\text{O}$$ and $$\text{OH}^-$$ from the start. The final combined equation should contain **no free $$\text{H}^+$$** if the medium is strongly basic.

Half-reactions describe oxidation at the anode and reduction at the cathode in **galvanic and electrolytic cells**. Tables of **standard reduction potentials** list half-reactions written as **reduction** by convention. You will learn more in [Unit 9](/notes/ap/chem/thermoelectro/).

<div class="theorem-box">

**Example.** In $$2\mathrm{H_2O_2}\rightarrow2\mathrm{H_2O}+\mathrm{O_2}$$, identify the oxidized and reduced element and explain how one reactant fills both roles.

Oxygen begins at $$-1$$ in peroxide. Oxygen going to water becomes $$-2$$ and is reduced; oxygen going to oxygen gas becomes $$0$$ and is oxidized. Peroxide is therefore both oxidizing and reducing agent in this disproportionation reaction. Hydrogen remains $$+1$$.

</div>

---

## Solubility and “like dissolves like”

**Solubility** is the maximum amount of solute that dissolves in a given amount of solvent at a specified temperature. Polar and ionic solutes tend to dissolve in polar solvents (usually water); nonpolar solutes tend to dissolve in nonpolar solvents. At the particle level, ion–dipole interactions or hydrogen bonding stabilize ions or polar molecules in water; nonpolar solutes rely mainly on weaker dispersion forces to mix with nonpolar solvents.

By convention, the solvent is the component present in greater amount and the solute is the dissolved component (by convention in dilute lab work, the minor component).

<div class="theorem-box">

**Example.** Ethanol dissolves in water but hexane barely does. Explain why saying 'both contain carbon, so they should behave alike' misses the relevant interactions.

Ethanol's O-H group can form hydrogen bonds with water, compensating for some water-water interactions disrupted during mixing. Hexane cannot provide comparable polar interactions. The carbon skeleton is only part of the molecule; the functional group changes how it interacts with the solvent.

</div>

---

## Factors affecting solubility

**Common-ion effect**: for a sparingly soluble salt in equilibrium with its solid, adding another source of the same cation or anion shifts equilibrium toward solid, lowering molar solubility. (The full equilibrium lecture is in [Unit 7](/notes/ap/chem/equilibrium/).)

Temperature: the effect on solid solubility depends on the sign of enthalpy of solution: many ionic solids become more soluble as $$T$$ rises, but exceptions exist. Gases in liquids almost always become less soluble as $$T$$ rises (molecular kinetic picture: escape from solution is easier when molecules move faster). Pressure has little effect on solid or liquid solutes but strongly affects gas solubility (Henry's Law).

<div class="theorem-box">

**Example.** A sealed carbonated drink is warmed and then opened. Separate the temperature effect from the pressure effect on dissolved carbon dioxide.

Warming generally lowers carbon dioxide solubility at a fixed gas pressure. Opening then lowers its partial pressure above the liquid, lowering the equilibrium dissolved concentration further. Gas escapes as the liquid approaches the new equilibrium; these are two distinct changes, not evidence that pressure and temperature are interchangeable.

</div>

---

## Concentration measures (revisited)

**Molarity** $$M$$ is moles of solute per liter of solution ($$\text{mol/L}$$); it changes slightly with temperature because volume changes.

**Molality** $$m$$ is moles of solute per kilogram of solvent (not kilogram of solution):

$$
m = \frac{\text{moles of solute}}{\text{kilograms of solvent}}.
$$

It is temperature-independent in the sense that it uses mass of solvent, not volume of solution.

Mass percent is

$$
\text{mass \%} = \frac{\text{mass of solute}}{\text{mass of solution}} \times 100\%.
$$

**Parts per million** and **parts per billion** report a mass ratio (or, for dilute aqueous work, often $$\text{mg}$$ solute per $$\text{kg}$$ solution, which is approximately $$\text{mg/L}$$ for water):

$$
\text{ppm} = \frac{\text{mass of solute}}{\text{mass of sample}} \times 10^6, \qquad
\text{ppb} = \frac{\text{mass of solute}}{\text{mass of sample}} \times 10^9.
$$

Do not equate $$\text{ppm}$$ to “$$mass \% \times 10^6$$”; use the fraction definition above (for example, $$1\%$$ corresponds to $$10^4$$ ppm).

**Normality** $$N$$ (still seen in some labs) is equivalents of reacting species per liter of solution: for acid–base, one equivalent of acid is one mole of $$\text{H}^+$$ donated per mole of formula (so $$\text{H}_2\text{SO}_4$$ can be $$2N$$ when both protons count in that context). On the AP exam, molarity and stoichiometry from the balanced equation are usually enough.

<div class="theorem-box">

**Example.** A solution contains $$10.0\ \mathrm{g}$$ solute in $$90.0\ \mathrm{g}$$ water. It expands when warmed without evaporation. Determine its mass percent and which of molarity and molality changes.

Mass percent is $$10.0/(10.0+90.0)\times100\%=10.0\%$$, not $$11.1\%$$. Masses and mole amounts stay fixed, so molality stays fixed. Solution volume increases, so molarity decreases. The denominator determines which concentration measure responds to thermal expansion.

</div>

---

## Colloids

A **colloid** contains dispersed particles larger than single molecules but small enough to stay suspended (roughly $$1$$–$$1000\ \text{nm}$$ is a common textbook range). Colloids are thermodynamically unstable with respect to bulk phase separation but can be kinetically persistent; charged surfaces and electrostatic repulsion often slow aggregation.

- The **Tyndall effect** is the scattering of visible light by those particles, a practical way to distinguish many colloids from true solutions. For example, milk is a colloid because it scatters light, one reason why it appears white
- **Coagulation** (heating, adding electrolyte, or mixing) can collapse the dispersion so particles aggregate and settle, just like how milk clumps can settle when milk isn't properly refrigerated

<div class="theorem-box">

**Example.** Two apparently uniform samples transmit a flashlight beam, but only one shows a visible light path from the side. Explain what this supports and what it cannot prove.

A visible path indicates scattering by dispersed particles and supports a colloidal dispersion rather than a molecular solution. It does not establish the particles' chemical identity or prove long-term stability. A macroscopically uniform appearance alone cannot distinguish a colloid from a true solution.

</div>

---

:::equations

| Idea | Equation | Conditions |
| --- | --- | --- |
| Amount conversions | $$n=m/M_{molar}$$; $$n=MV$$; $$n=PV/(RT)$$ | Solution V in liters; gas formula assumes ideal behavior. |
| Reaction extent | $$\xi_{max}=\min_i(n_{i,0}/\nu_i)$$ | Take the minimum over consumed reactants in a complete-reaction model. |
| Stoichiometric change | $$n_{reactant,f}=n_0-\nu\xi$$; $$n_{product,f}=n_0+\nu\xi$$ | Use the balanced coefficients, not subscripts. |
| Percent yield | $$\%yield=m_{actual}/m_{theoretical}\times100\%$$ | Compare the same pure product and physical state. |
| Composition | $$\%mass=m_{component}/m_{sample}\times100\%$$ | For combustion analysis, sample oxygen may require mass difference. |
| Back titration | $$n_{reagent,consumed}=n_{reagent,added}-n_{reagent,left}$$ | Convert the titration amount with its own balanced mole ratio first. |
| Redox electron balance | $$n_{e^-,lost}=n_{e^-,gained}$$ | Balance both atoms and charge; oxidation numbers sum to species charge. |
| Hydrate ratio | $$x=n_{water}/n_{anhydrous\ salt}$$ | Assumes only water is lost and the residue is fully anhydrous. |
| Solution composition | $$m_{molality}=n_{solute}/m_{solvent,kg}$$; $$x_i=n_i/\sum_jn_j$$ | Molality uses solvent mass; mole fraction uses total moles. |
| Henry's law | $$c=k_HP_{gas}$$ | Fixed temperature and the stated convention for $$k_H$$. |

:::

## Practice

### MCQ

::::problem
1. A $$1.00\ \mathrm{g}$$ mixture of $$\mathrm{CaCO_3}$$ and inert material reacts with $$30.0\ \mathrm{mL}$$ of $$1.00\ M$$ HCl. The leftover acid needs $$10.0\ \mathrm{mL}$$ of $$1.00\ M$$ NaOH for neutralization. Using $$M(\mathrm{CaCO_3})=100.\ \mathrm{g/mol}$$, what is the carbonate mass percent?

   (A) $$50.0\%$$<br>
   (B) $$100.\%$$<br>
   (C) $$75.0\%$$<br>
   (D) $$200.\%$$

:::solution
Initially there are 0.0300 mol acid and 0.0100 mol remains, so carbonate consumed 0.0200 mol HCl. Each mole of carbonate consumes two moles of acid, giving 0.0100 mol carbonate or 1.00 g. The sample is 100% carbonate within the data's precision; calling it a mixture does not guarantee a nonzero impurity fraction.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
2. Mix $$40.0\ \mathrm{mL}$$ of $$0.150\ M$$ calcium chloride with $$60.0\ \mathrm{mL}$$ of $$0.150\ M$$ sodium carbonate. Assuming complete precipitation and additive volumes, which pair of remaining ion concentrations is correct?

   (A) $$[\mathrm{Ca^{2+}}]=0.0600\ M$$ and $$[\mathrm{Na^+}]=0.0900\ M$$<br>
   (B) $$[\mathrm{CO_3^{2-}}]=0.0900\ M$$ and $$[\mathrm{Cl^-}]=0.0600\ M$$<br>
   (C) $$[\mathrm{CO_3^{2-}}]=0.0300\ M$$ and $$[\mathrm{Cl^-}]=0.120\ M$$<br>
   (D) $$[\mathrm{CO_3^{2-}}]=0.0300\ M$$ and $$[\mathrm{Cl^-}]=0.0600\ M$$

:::solution
Calcium contributes 0.00600 mol and carbonate 0.00900 mol. The 1:1 precipitate leaves 0.00300 mol carbonate in 0.100 L. Chloride is a spectator, with $$2(0.00600)=0.0120\ \mathrm{mol}$$ in the same volume, giving 0.120 M. Spectators are diluted, not consumed by this reaction.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
3. In acid, dichromate becomes chromium(III) and iron(II) becomes iron(III). A $$25.0\ \mathrm{mL}$$ iron(II) sample requires $$12.5\ \mathrm{mL}$$ of $$0.0200\ M$$ dichromate. What is the iron(II) concentration?

   (A) $$0.0100\ M$$<br>
   (B) $$0.0200\ M$$<br>
   (C) $$0.0300\ M$$<br>
   (D) $$0.0600\ M$$

:::solution
Each chromium changes from +6 to +3, accepting three electrons; two chromium atoms accept six. Each iron(II) supplies one electron, so the sample contains $$6(0.0125)(0.0200)=0.00150\ \mathrm{mol}$$ iron(II). Dividing by 0.0250 L gives 0.0600 M. The redox electron balance determines the titration ratio.

$$
\boxed{\text{D}}.
$$
:::
::::

::::problem
4. A $$2.46\ \mathrm{g}$$ sample of $$\mathrm{MgSO_4\cdot xH_2O}$$ leaves $$1.20\ \mathrm{g}$$ anhydrous salt on heating. Use molar masses 120. and 18.0. What x is obtained, and how would incomplete drying bias x?

   (A) $$7$$; too low<br>
   (B) $$7$$; too high<br>
   (C) $$5$$; too low<br>
   (D) $$5$$; too high

:::solution
Water loss is 1.26 g, or 0.0700 mol, and anhydrous salt is 0.0100 mol, so x is 7. Incomplete drying makes the apparent water loss too small and the apparent anhydrous mass too large; both effects lower the inferred ratio.

$$
\boxed{\text{A}}.
$$
:::
::::

::::problem
5. Complete combustion of $$0.900\ \mathrm{g}$$ of a compound containing only C, H, and O gives $$1.32\ \mathrm{g}$$ carbon dioxide and $$0.540\ \mathrm{g}$$ water. Use molar masses 44.0 and 18.0, and atomic masses 12.0, 1.00, and 16.0. What is its empirical formula?

   (A) $$\mathrm{C_2H_6O}$$<br>
   (B) $$\mathrm{CH_2O}$$<br>
   (C) $$\mathrm{CH_4O}$$<br>
   (D) $$\mathrm{C_2H_4O}$$

:::solution
Products show 0.0300 mol C and 0.0600 mol H atoms, accounting for 0.360+0.0600=0.420 g. The original sample therefore contains 0.480 g O, or 0.0300 mol. The ratio is 1:2:1. Oxygen from the combustion gas prevents using product oxygen directly as the sample's oxygen amount.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
6. A precipitation should produce $$2.00\ \mathrm{g}$$ of pure dry product. During filtration, 10.0% of that product is lost. The recovered solid retains water equal to 10.0% of its dry mass. What apparent percent yield is recorded?

   (A) $$90.0\%$$<br>
   (B) $$100.\%$$<br>
   (C) $$99.0\%$$<br>
   (D) $$110.\%$$

:::solution
Recovery leaves $$2.00(0.900)=1.80\ \mathrm{g}$$ dry product. Retained water adds $$0.100(1.80)=0.180\ \mathrm{g}$$, giving 1.98 g and 99.0% apparent yield. Equal stated percentages do not cancel because they use different reference masses.

$$
\boxed{\text{C}}.
$$
:::
::::

### FRQ

::::frq{id=chem-chemrxns-challenge-1}
7. A 1.500 g sample contains only $$\mathrm{Na_2CO_3}$$ and $$\mathrm{NaHCO_3}$$. It reacts with 40.00 mL of 1.000 M HCl. After carbon dioxide is fully expelled, the excess acid requires 15.00 mL of 1.000 M NaOH. Use molar masses 106.0 and $$84.00\ \mathrm{g/mol}$$.

   $$(A)$$ Write balanced net ionic reactions of carbonate and bicarbonate with acid, and find the moles of acid consumed by the sample.

   $$(B)$$ Determine the mass percent of each component by solving simultaneous equations.

   $$(C)$$ Calculate the total moles of carbon dioxide produced. Explain why acid consumed cannot simply be equated to gas produced.

   $$(D)$$ If some dissolved carbon dioxide remains and also consumes NaOH during the back titration, predict the error in the inferred carbonate mass fraction.

:::solution
$$(A)$$ The reactions are $$\mathrm{CO_3^{2-}+2H^+\rightarrow CO_2+H_2O}$$ and $$\mathrm{HCO_3^-+H^+\rightarrow CO_2+H_2O}$$. Initial acid is 0.04000 mol and leftover acid is 0.01500 mol from the 1:1 NaOH neutralization. Therefore the sample consumes 0.02500 mol H+. One carbonate consumes twice as much acid as one bicarbonate.

$$(B)$$ Let x and y be moles of sodium carbonate and sodium bicarbonate. Acid consumption gives $$2x+y=0.02500$$ and sample mass gives $$106.0x+84.00y=1.500$$. Substituting $$y=0.02500-2x$$ yields $$x=0.009677\ \mathrm{mol}$$ and $$y=0.005645\ \mathrm{mol}$$. Their masses are 1.026 g and 0.4742 g, or 68.39% carbonate and 31.61% bicarbonate.

$$(C)$$ Each reactant anion yields one carbon dioxide, so $$n_{CO_2}=x+y=0.01532\ \mathrm{mol}$$. Acid consumed is 0.02500 mol because the two anions need different numbers of protons. Equating all consumed acid with gas would treat carbonate as if it were bicarbonate and overpredict the gas amount.

$$(D)$$ Extra NaOH consumption would be incorrectly assigned to leftover HCl. Subtracting this overestimated leftover acid from the initial acid makes the inferred acid consumption by the sample too small. At fixed sample mass, carbonate consumes more acid per gram than bicarbonate, so the calculation then assigns too little carbonate. Expelling carbon dioxide separates the intended acid measurement from this interference.
:::
::::

::::frq{id=chem-chemrxns-challenge-2}
8. A 0.8000 g ore sample contains iron and inert material. All iron is dissolved and converted to iron(II), then titrated in acid with 0.02000 M permanganate. The sample uses 18.00 mL, while an identical reagent blank uses 1.00 mL. Permanganate is reduced to manganese(II). Use $$M_{Fe}=55.85\ \mathrm{g/mol}$$.

   $$(A)$$ Balance the net ionic redox equation by showing the electron transfers.

   $$(B)$$ Apply the blank correction and calculate the ore's iron mass percent.

   $$(C)$$ Suppose 10.0% of the sample iron(II) is oxidized by air before titration. Predict the reported percent if every other step and the blank correction remain unchanged.

   $$(D)$$ The final solution contains potassium, manganese(II), iron(III), and excess acid. Explain why potassium is absent from the net ionic equation and why a precipitate is not required for the reaction to count as chemical change.

:::solution
$$(A)$$ Oxidation is $$\mathrm{Fe^{2+}\rightarrow Fe^{3+}+e^-}$$. Reduction is $$\mathrm{MnO_4^-+8H^++5e^-\rightarrow Mn^{2+}+4H_2O}$$. Multiplying the iron half-reaction by five and adding gives $$\mathrm{MnO_4^-+8H^++5Fe^{2+}\rightarrow Mn^{2+}+4H_2O+5Fe^{3+}}$$. Both atoms and charge balance; total charge is +17 on either side.

$$(B)$$ The analyte accounts for $$18.00-1.00=17.00\ \mathrm{mL}$$ permanganate. Its amount is $$0.01700(0.02000)=0.0003400\ \mathrm{mol}$$, corresponding to $$5(0.0003400)=0.001700\ \mathrm{mol}$$ Fe. The iron mass is $$0.001700(55.85)=0.09495\ \mathrm{g}$$, giving $$0.09495/0.8000\times100\%=11.87\%$$. The blank removes oxidant consumed by reagents rather than sample iron.

$$(C)$$ Only 90.0% of the original iron can now supply electrons to permanganate. The inferred iron amount and mass percent scale by 0.900, giving $$0.900(11.87\%)=10.68\%$$. The iron has not vanished, but the chosen assay no longer measures the already-oxidized fraction. A reagent blank cannot compensate for oxidation specific to the sample.

$$(D)$$ Potassium accompanies the permanganate reagent but retains its charge and remains dissolved; it is a spectator ion. Iron and manganese change oxidation states through electron transfer even if all products remain aqueous. A new solid is only one possible observation of reaction, not a requirement. The balanced ionic equation records the species undergoing the chemical transformation.
:::
::::
