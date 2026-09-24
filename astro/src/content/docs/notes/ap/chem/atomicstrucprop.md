---
title: "Unit 1: Atomic Structure and Properties"
description: "AP Chemistry notes on atomic structure, periodic trends, electron configurations, Coulombic attraction, and photoelectron spectra."
sidebar:
  order: 1
---

## The basics of chemistry

### Significant figures

**Significant figures** are the digits in a measurement that carry meaning—every digit we are entitled to report given how well we know the quantity. They matter whenever you round a calculated result so it does not pretend to be more precise than the data that produced it. On the AP exam they appear mainly in lab-style questions; in research they are non-negotiable.

- Nonzero digits are always significant.
- **Leading zeros** (as in $$0.0045$$) are not significant; they only locate the decimal point. **Captive zeros** between nonzero digits are significant (e.g. $$1.05$$ has three significant figures).
- **Trailing zeros** require care: if a decimal point is shown, trailing zeros are significant ($$12.0$$ has three); if there is no decimal, trailing zeros do not ocunt towards significant figures.
- **Exact numbers** (such as a counted dozen eggs or a defined conversion within a system) have effectively unlimited significant figures and do not limit your result.
- For addition and subtraction, round the result to the same number of *decimal places* as the term with the fewest. For multiplication and division, round to the same number of *significant figures* as the factor with the fewest.

<div class="theorem-box">

**Example.** A balance reads $$2.50\ \text{g}$$ for an empty container and $$2.56\ \text{g}$$ after adding a sample. A student reports a sample mass of $$0.0600\ \text{g}$$ because both readings have three significant figures. What is wrong?

Subtraction is limited by decimal place, not by matching significant-figure counts. The difference is $$0.06\ \text{g}$$, known only to the hundredths place. The added zeros in $$0.0600$$ claim precision the balance did not provide. Subtracting nearby measurements can leave far fewer significant figures than either measurement alone.

</div>

### Matter and its classification

**Matter** is anything that has mass and occupies volume. Chemists classify it first by composition.

- **Elements** are made of one kind of atom
- **Compounds** contain two or more elements combined in definite proportion.
- A **pure substance** has fixed composition, meaning only one type of substance makes it up.
- A **mixture** combines substances without fixed proportion. A **homogeneous mixture** (solution) are uniform on a macroscopic scale, meaning you cannot tell the difference between molecules jsut by looking at it, while a **heterogeneous mixture** does not have this property.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing,angles,quotes}
\begin{tikzpicture}[>=Stealth, font=\small]
\node[draw, rounded corners, fill=blue!7, minimum width=2.7cm, minimum height=0.8cm] (matter) at (0,3) {Matter};
\node[draw, rounded corners, fill=green!7] (pure) at (-3,1.6) {Pure substance};
\node[draw, rounded corners, fill=orange!8] (mix) at (3,1.6) {Mixture};
\node[draw, rounded corners] (el) at (-4.2,0.2) {Element};
\node[draw, rounded corners] (co) at (-1.8,0.2) {Compound};
\node[draw, rounded corners] (hom) at (1.8,0.2) {Homogeneous};
\node[draw, rounded corners] (het) at (4.2,0.2) {Heterogeneous};
\draw[->, thick] (matter) -- (pure); \draw[->, thick] (matter) -- (mix);
\draw[->, thick] (pure) -- (el); \draw[->, thick] (pure) -- (co);
\draw[->, thick] (mix) -- (hom); \draw[->, thick] (mix) -- (het);
\node[align=center] at (-4.2,-0.8) {one type\\of atom};
\node[align=center] at (-1.8,-0.8) {fixed ratio\\of elements};
\node[align=center] at (1.8,-0.8) {uniform\\throughout};
\node[align=center] at (4.2,-0.8) {nonuniform\\parts};
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** Two clear liquids each appear uniform. One leaves crystals after evaporation; the other evaporates completely. Does this prove the second is a pure substance?

No. The first contains a nonvolatile component, consistent with a solution. The second could be a pure liquid or a mixture of volatile liquids such as ethanol and water. A single visible phase establishes apparent homogeneity, not chemical purity. Additional evidence, such as composition measurements or a distillation profile, is needed.

</div>

### Reading the periodic table

The **periodic table** arranges elements by increasing **atomic number** $$Z$$. Horizontal rows are **periods**; vertical columns are **groups** (or families). Groups may be labeled $$1$$–$$18$$ or with Roman numerals and letters in older notation. Several families have traditional names that appear frequency:

- **Alkali metals** (group 1, excluding hydrogen)
- **Alkaline earth metals** (group 2)
- **Transition metals** (groups 3–12)
- **Pnictogens** (group 15)
- **Chalcogens** (group 16)
- **Halogens** (group 17)
- **Noble gases** (group 18)

Below the main block, the **lanthanides** and **actinides** are the **inner transition metals** (often called **rare-earth metals** in informal usage for the lanthanides).

For any entry, the atomic number $$Z$$ is the number of **protons** in the nucleus and defines the element. The **mass number** $$A$$ counts protons plus **neutrons** in a given **isotope**:

$$
A = Z + N
$$

where $$N$$ is the neutron count. Isotopes of the same element share $$Z$$ but differ in $$A$$ (and therefore in $$N$$).

<div class="theorem-box">

**Example.** A periodic table lists chlorine's atomic number as 17 and average atomic mass near 35.45. A student assigns every chlorine atom 18.45 neutrons. Explain both mistakes and identify the neutron count in chlorine-37.

Individual nuclei contain whole numbers of neutrons. The tabulated mass averages the masses of naturally occurring isotopes; it is not one atom's mass number. Chlorine-37 has $$37-17=20$$ neutrons. Isotopes share their proton count and periodic-table position even though their neutron counts differ.

</div>

---

## Ions

An **ion** is an atom or group of atoms with a net electric charge from gain or loss of electrons. A **cation** is positive (fewer electrons than protons); an **anion** is negative (more electrons than protons). A good way to remember this is that cats are always positive so CATions are positively charged! **Metals** tend to form cations and **nonmetals** tend to form anions. In addition, many **transition metals** exhibit variable charge in compounds because several oxidation states are comparably stable (mentioned later in more detail) due to the availability of their $$d$$ orbital (mentioned later as well).

### Polyatomic ions

**Polyatomic ions** are charged covalent units that behave as a single piece in **ionic compounds** due to their lower eneergy state compared to their individual atomic states: for example, nitrate ($$\text{NO}_3^-$$), sulfate ($$\text{SO}_4^{2-}$$), and ammonium ($$\text{NH}_4^+$$) are all good exmamples of polyatomic ions. These are the polyatomic ions you need to memorize for AP Chem:


| Polyatomic ion | Formula | Charge |
| --- | --- | ---: |
| Ammonium | $$\mathrm{NH_4^+}$$ | $$+1$$ |
| Acetate | $$\mathrm{C_2H_3O_2^-}$$ | $$-1$$ |
| Hydroxide | $$\mathrm{OH^-}$$ | $$-1$$ |
| Nitrate / nitrite | $$\mathrm{NO_3^-}$$ / $$\mathrm{NO_2^-}$$ | $$-1$$ |
| Chlorate / chlorite / hypochlorite | $$\mathrm{ClO_3^-}$$ / $$\mathrm{ClO_2^-}$$ / $$\mathrm{ClO^-}$$ | $$-1$$ |
| Perchlorate | $$\mathrm{ClO_4^-}$$ | $$-1$$ |
| Carbonate / bicarbonate | $$\mathrm{CO_3^{2-}}$$ / $$\mathrm{HCO_3^-}$$ | $$-2$$ / $$-1$$ |
| Sulfate / sulfite | $$\mathrm{SO_4^{2-}}$$ / $$\mathrm{SO_3^{2-}}$$ | $$-2$$ |
| Phosphate / hydrogen phosphate | $$\mathrm{PO_4^{3-}}$$ / $$\mathrm{HPO_4^{2-}}$$ | $$-3$$ / $$-2$$ |
| Chromate / dichromate | $$\mathrm{CrO_4^{2-}}$$ / $$\mathrm{Cr_2O_7^{2-}}$$ | $$-2$$ |
| Permanganate | $$\mathrm{MnO_4^-}$$ | $$-1$$ |

<div class="theorem-box">

**Example.** How many moles of each ion form when $$0.200\ \mathrm{mol}$$ of $$\mathrm{Al_2(SO_4)_3}$$ dissolves completely? Explain why the solution is neutral even though it contains different numbers of cations and anions.

Each formula unit supplies two aluminum ions and three sulfate ions, giving $$0.400\ \mathrm{mol}$$ $$\mathrm{Al^{3+}}$$ and $$0.600\ \mathrm{mol}$$ $$\mathrm{SO_4^{2-}}$$. Their charge amounts are proportional to $$0.400(3)=1.20$$ and $$0.600(-2)=-1.20$$, which cancel. Electrical neutrality requires equal total positive and negative charge, not equal ion counts. Sulfate remains a polyatomic ion rather than separating into sulfur and oxygen atoms.

</div>

---

## Avogadro’s number, the mole, and molar mass

- The **mole** is the chemist’s unit of counting: one mole contains **Avogadro’s number** (sometimes denoted as $$N_A$$) of specified entities (atoms, molecules, ions, formula units, etc.):

$$
1 \text{ mol} = 6.022 \times 10^{23} \text{ entities}
$$

If you are ever confused by moles and molar conversions, just replace "moles" with "dozens" and think about it that way.

The **molar mass** of an element is the mass of one mole of its atoms, numerically equal (in $$\text{g/mol}$$) to the **average atomic mass** listed on the periodic table. For a **compound**, add the molar masses of all atoms in the formula to obtain the compound’s molar mass.

Lastly, the **mass percent** of an element in a compound compares the mass of that element in one mole of compound to the molar mass of the whole:

$$
\% \text{ element} = \frac{\text{mass of element in } 1 \text{ mol of compound}}{\text{molar mass of compound}} \times 100\%
$$

### Empirical and molecular formulas

The **molecular formula** gives the *actual numbers* of atoms of each element in one molecule of a molecular compound (or one formula unit of an ionic solid, where “molecule” is not literal). The **empirical formula** gives the *smallest whole-number ratio* of atoms in that substance. Ionic compounds are usually reported by their empirical formula anyway (e.g. $$\text{NaCl}$$, $$\text{CaF}_2$$) because the crystal is an extended lattice, not discrete $$\text{NaCl}$$ molecules.

For a molecular substance, the molecular formula is a *whole-number multiple* of the empirical formula:

$$
\text{molecular formula} = (\text{empirical formula})_n, \qquad n = 1,\,2,\,3,\,\ldots
$$

The **empirical formula mass** is the molar mass of the empirical formula as written. If you know the molar mass of the compound (from experiment, such as mass spectrometry, or from the problem), then

$$
n = \frac{M_{\text{compound}}}{M_{\text{empirical}}},
$$

and you round $$n$$ to the nearest integer when the data allows it (subject to measurement uncertainty).

<div class="theorem-box">

**Example.** Two compounds have empirical formula $$\mathrm{CH_2O}$$. Their molar masses are $$60.0$$ and $$180.0\ \mathrm{g\,mol^{-1}}$$. Can they have the same molecular formula or be identified uniquely from these data?

The empirical-formula mass is about $$30.0\ \mathrm{g\,mol^{-1}}$$, so the multipliers are $$2$$ and $$6$$. Their molecular formulas are $$\mathrm{C_2H_4O_2}$$ and $$\mathrm{C_6H_{12}O_6}$$. They cannot have the same molecular formula, but neither formula uniquely identifies a compound: different atom connectivities can give the same molecular formula.

</div>

### From mass percent to the empirical formula

When a problem gives **mass percentages** (or masses of elements in a sample), treat the sample as a sample of *$$100\ \text{g}$$* so each element’s mass in grams equals its *percent* numerically.

:::strategy

1. Convert each element’s mass to moles using its molar mass.

2. Divide *every* mole amount by the *smallest* mole amount among the elements.

3. If ratios are not whole numbers within reasonable rounding, multiply all subscripts by a small integer ($$2$$, $$3$$, $$\ldots$$) to clear fractions (e.g. $$1 : 1 : 1.33$$ $$\rightarrow$$ multiply by $$3$$). If you see a ratio that is very hard to convert to integers, you likely did something wrong.

:::

That yields the empirical formula. **Combustion analysis** problems follow the same logic: measured masses of $$\text{CO}_2$$ and $$\text{H}_2\text{O}$$ produced fix the carbon and hydrogen in the original sample; any oxygen is often obtained by difference from the original sample mass if the compound contains only C, H, and O.

<div class="theorem-box">

**Example.** A compound is $$43.6\%$$ phosphorus and $$56.4\%$$ oxygen by mass. A student rounds its mole ratio $$1:2.50$$ to $$1:3$$. Find the correct empirical formula using atomic masses $$31.0$$ and $$16.0$$.

A $$100\ \mathrm{g}$$ sample contains $$43.6/31.0=1.41\ \mathrm{mol}$$ P and $$56.4/16.0=3.53\ \mathrm{mol}$$ O, giving approximately $$1:2.50$$. Multiplying both entries by two gives $$2:5$$ and $$\mathrm{P_2O_5}$$. A ratio near a simple fraction should be scaled, not rounded to an unrelated integer. This establishes only the empirical formula; molar mass is needed to determine the molecular formula.

</div>

---

## Mass spectrometry

**Mass spectrometry** separates ions by *mass-to-charge ratio* $$\frac{m}{z}$$. A typical spectrum plots *relative abundance* (or detector *intensity*) on the vertical axis against $$\frac{m}{z}$$ on the horizontal axis. For an element, the pattern of peaks reveals isotope masses and their approximate natural abundances; for molecules, *fragmentation* patterns can support structure assignment in advanced work. An example of a mass spectrometer chart is shown below:

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[axis lines=left, width=10cm, height=5.5cm, ymin=0, ymax=110, xmin=18, xmax=32, xlabel={mass-to-charge ratio}, ylabel={relative abundance}, ytick={0,50,100}, xtick={20,22,24,26,28,30}, grid=both, grid style={gray!15}]
\addplot[ybar, bar width=5pt, fill=blue!35, draw=blue!70!black] coordinates {(20,18) (21,6) (22,42) (24,100) (25,12) (26,35) (28,75) (30,20)};
\end{axis}
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** An element has two isotopes of masses $$10.0$$ and $$11.0\ \mathrm{u}$$ and average mass $$10.8\ \mathrm{u}$$. A student assigns the taller peak to the lighter isotope. Determine whether that assignment fits the data.

Let $$f$$ be the lighter isotope's fraction. Then $$10.0f+11.0(1-f)=10.8$$ gives $$f=0.20$$. The heavier isotope is $$80\%$$ abundant and should have the taller peak if detector response and charge are comparable. An unweighted midpoint of $$10.5$$ would assume equal abundances without evidence.

</div>

---

## Measurements of error and efficiency

In laboratory work, **theoretical yield** is the amount of product predicted from stoichiometry assuming complete conversion. **Actual yield** is what you isolate. **Percent yield** measures how much of the theoretical amount you obtained:

$$
\% \text{ yield} = \frac{\text{actual yield}}{\text{theoretical yield}} \times 100\%
$$

**Percent error** compares a measured value to an accepted or theoretical value:

$$
\% \text{ error} = \left| \frac{\text{actual} - \text{theoretical}}{\text{theoretical}} \right| \times 100\%
$$

**Efficiency** in an energy context is the fraction of input energy that appears as useful output:

$$
\text{efficiency} = \frac{\text{useful energy output}}{\text{energy input}} \times 100\%
$$

Do not confuse percent yield (a mass or mole recovery for a reaction) with thermodynamic efficiency (an energy ratio). Use percent error when judging how far a measurement sits from a reference value.

<div class="theorem-box">

**Example.** A dry product should weigh $$1.80\ \mathrm{g}$$, but a student records $$1.95\ \mathrm{g}$$. Determine the apparent yield and whether it proves that more product formed than stoichiometry permits.

The apparent yield is $$(1.95/1.80)100\%=108\%$$. This contradicts the assumed pure, dry product model, not conservation of mass. Retained solvent or contamination adds measured mass without adding the intended product; drying to constant mass helps distinguish these possibilities.

</div>

---

## Molarity

**Molarity** ($$M$$) expresses concentration as moles of solute per liter of solution:

$$
M = \frac{\text{moles of solute}}{\text{liters of solution}} = \frac{\text{mol}}{L}
$$

since volume changes with temperature, molarity is *temperature-dependent*. It depends on the amount of solute per volume of solution, not on the total mass of the solution by itself.

<div class="theorem-box">

**Example.** A student dissolves $$0.100\ \mathrm{mol}$$ of solute in $$1.00\ \mathrm{L}$$ of water and labels it $$0.100\ M$$. Explain what must be measured before that label is justified.

Molarity uses solution volume, not solvent volume. Dissolving the solute may change the volume, so the final solution volume must be measured. To prepare the intended concentration, dissolve in less than $$1.00\ \mathrm{L}$$ of water and dilute to a final volume of $$1.00\ \mathrm{L}$$.

</div>

---

## Oxidation numbers

An **oxidation number** (oxidation state) is a formal bookkeeping charge assigned to an atom in a compound or ion, as if electrons in every bond belonged entirely to the more electronegative partner. It tracks how electron density shifts relative to the element in its standard state.

Useful conventions include:

- Any element in its elemental form (e.g. $$\text{O}_2$$, $$\text{Na}$$) has oxidation number $$0$$.
- A monatomic ion matches its charge (e.g. $$\text{Na}^+$$ is $$+1$$).
- Oxygen is usually $$-2$$ except in peroxides such as $$\text{H}_2\text{O}_2$$ ($$-1$$ for O) and in compounds with fluorine.
- Hydrogen is usually $$+1$$ except in metal hydrides (e.g. $$\text{NaH}$$), where it is $$-1$$.
- Fluorine is $$-1$$ in all compounds. Other halogens are $$-1$$ unless bonded to a more electronegative element (such as oxygen).

The rule of thumb is that you always assign the most electronegative atom first in terms of oxidation states.

<div class="theorem-box">

**Example.** Oxygen appears in $$\mathrm{H_2O_2}$$ and $$\mathrm{OF_2}$$. Determine its oxidation number in each and explain why the usual $$-2$$ shortcut fails.

In the peroxide, $$2(+1)+2x=0$$ gives $$x=-1$$. In $$\mathrm{OF_2}$$, fluorine takes $$-1$$, so $$x+2(-1)=0$$ gives $$x=+2$$. The sum must equal the species charge; assigning oxygen $$-2$$ blindly would violate that constraint.

</div>

---

## Quantum mechanics in chemistry

### Electron configuration and quantum numbers

Each electron in an atom is described by four **quantum numbers** that arise from the *wave-mechanical* model.

The **principal quantum number** $$n$$ is a positive integer ($$n = 1, 2, 3, \ldots$$). It sets the shell and is the main contributor to orbital energy for hydrogen-like atoms.

The **azimuthal** (or **angular momentum**) quantum number $$l$$ runs from $$0$$ to $$n - 1$$ and labels subshell shape:

- $$l = 0$$ → s orbital
- $$l = 1$$ → p orbital
- $$l = 2$$ → d orbital
- $$l = 3$$ → f orbital

The **magnetic quantum number** $$m_l$$ takes integer values from $$-l$$ to $$+l$$ and distinguishes *orientations* of a subshell in space (e.g. $$p_x$$ and $$p_y$$)

The **spin quantum number** $$m_s$$ is $$+\frac{1}{2}$$ or $$-\frac{1}{2}$$ for the two **spin** states of a single electron.

The **Pauli exclusion principle** states that no two electrons in the same atom may share the same set of four quantum numbers, so at most two electrons occupy any one atomic orbital, and they must have *opposite spin*.

The **Aufbau principle** directs you to fill orbitals in order of increasing energy. The familiar $$n s$$, $$(n-1) d$$, $$(n-2) f$$ crossing is why the periodic table has its shape. Exceptions (e.g. chromium $$\text{Cr}$$, copper $$\text{Cu}$$, and several heavier transition metals) reflect especially stable $$d^5$$ or $$d^{10}$$ arrangements; those same stability patterns contribute to variable metal oxidation states in compounds.

**Hund’s rule** favors placing electrons singly in degenerate orbitals of a subshell before pairing, with *parallel spins* where possible, to reduce *electron–electron repulsion*.

**Heisenberg’s uncertainty principle** limits how sharply *position* and *momentum* can be known simultaneously for a quantum particle: a conceptual foundation for why we speak in terms of orbitals (probability distributions) rather than classical orbits. It states that:

$$
\Delta x \Delta p \ge \frac{h}{4\pi}
$$

This means that the uncertainty in position and momentum are always above some constant, implying that both cannot be known at a time. This is why we have electron clouds instead of set orbits.

**Abbreviated configurations** use the previous noble gas core in brackets, e.g.

$$
\text{Cs}:\; [\text{Xe}]\, 6s^1
$$

Two species are **isoelectronic** if they have the same electron configuration (e.g. $$\text{Br}^-$$ and $$\text{Se}^{2-}$$). Among isoelectronic ions, **ionic radius** decreases as **nuclear charge** increases because the same electron count is pulled closer by more protons (e.g. $$\text{Na}^+$$ is smaller than $$\text{F}^-$$).

<div class="theorem-box">

**Example.** A student writes $$[\mathrm{Ar}]3d^44s^2$$ for chromium and removes a $$3d$$ electron first to form its cation. Correct both choices.

Ground-state chromium is $$[\mathrm{Ar}]3d^54s^1$$. Subshell energies are close enough that the simple filling order does not predict this ground state correctly. Ionization removes the $$4s$$ electron first, giving $$\mathrm{Cr}^+:[\mathrm{Ar}]3d^5$$. The order used to introduce orbital filling is not a rule that the last written subshell always loses electrons first.

</div>

### Energy, light, and quantization

For electromagnetic radiation (for AP Chemistry this is just light), **wavelength** $$\lambda$$ (distance between waves) and **frequency** $$\nu$$ (or $$f$$ (how many waves appear in a second) are related by

$$
c = \nu \lambda,
$$

where $$c \approx 3.00 \times 10^8 \text{ m/s}$$ is the *speed of light* in vacuum. Frequency is measured in hertz ($$\text{Hz}$$, or $$\text{s}^{-1}$$), and wavelength is usually given in $$nm$$, which requires conversions to $$m$$ to work.

Physicist Max Planck related photon energy to frequency through **Planck's constant**:

$$
E = h\nu = \frac{hc}{\lambda},
$$

with Planck’s constant $$h \approx 6.626 \times 10^{-34} \text{ J}\cdot\text{s}$$. Essentially, Max Planck discovered that energy came in packets called **quanta**. which explains **atomic spectra** and **line colors** in **flame tests** and discharge tubes: each transition corresponds to a specific $$\Delta E$$ and therefore a characteristic photon energy. The release of light is caused by an electron moving to a lower energy state, which the absorbance of light is  caused by an electron moving to a higher energy state.

Physicist Louis de Broglie associated a wavelength with any particle of momentum $$p$$:

$$
\lambda = \frac{h}{p} = \frac{h}{mv}
$$

for nonrelativistic speeds, demonstrating that any object has an intristic wavelength. However, at only quantum levels is this wavelength significant.

<div class="theorem-box">

**Example.** An atom has levels at $$0$$, $$3.0\times10^{-19}$$, and $$5.0\times10^{-19}\ \mathrm{J}$$. Can a ground-state atom absorb a $$2.0\times10^{-19}\ \mathrm{J}$$ photon? Could an excited atom emit one?

Not from the ground state in this three-level model: neither available gap is $$2.0\times10^{-19}\ \mathrm{J}$$. An atom in the highest level can emit that energy by dropping to the middle level. The photon must match the difference between the actual initial and final levels, not merely an energy difference somewhere in the diagram.

</div>

### Photoelectric effect and photoelectron spectroscopy

In the **photoelectric effect**, photons eject electrons from a metal surface only when the photon energy exceeds a threshold set by the material’s **work function** $$\Phi$$. Increasing frequency increases the maximum kinetic energy of emitted electrons according to

$$
K_{\max} = h\nu - \Phi,
$$

but for all purposes, memorizing this equation is not necessary for the AP Chemistry exam. It's just important to know that increasing *intensity* at fixed frequency increases the number of ejected electrons, not their maximum *kinetic energy*.

**Photoelectron spectroscopy** (**PES**) measures how much energy must be supplied to remove electrons from subshells in atoms or molecules. Peaks appear at **binding energies** characteristic of each orbital type; relative peak areas (after accounting for ionization cross sections) reflect electron counts in those subshells. An example problem is shown below, feel free to try it out!

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[axis lines=left, width=10cm, height=5.5cm, xmin=0, xmax=10, ymin=0, ymax=6, xlabel={binding energy}, ylabel={relative electrons}, xtick=\empty, ytick=\empty, x dir=reverse, grid=both, grid style={gray!15}]
\addplot[ycomb, very thick, blue, mark=*] coordinates {(9,2) (6.2,2) (2.8,6) (1.1,1)};
\node[anchor=north east] at (axis cs:10,0) {core};
\node[anchor=north west] at (axis cs:0,0) {valence};
\end{axis}
\end{tikzpicture}
```

Read the binding-energy axis before interpreting a PES peak shift. Lower binding energy means easier electron removal; whether that is left or right depends on the axis direction. Nuclear charge, shielding, and the occupied subshell all affect binding energy.

<div class="theorem-box">

**Example.** A metal ejects electrons under light of frequency $$\nu$$. The intensity is doubled at the same frequency. Predict the changes in maximum electron kinetic energy and electron emission rate, assuming ordinary single-photon photoemission.

Each photon still has energy $$h\nu$$, so $$K_{\max}=h\nu-\Phi$$ is unchanged. Higher intensity supplies more photons per second and can eject more electrons per second. It does not combine two photons into one more energetic photon in this model.

</div>

---

## Electromagnetic spectrum

The **electromagnetic spectrum** orders all electromagnetic radiation by **photon energy** (equivalently frequency or wavelength). **Visible light** spans roughly

$$
380\text{ nm} \text{ to } 760\text{ nm},
$$

a narrow window between **ultraviolet** and **infrared**. Moving toward shorter wavelength corresponds to higher photon energy (**gamma rays** and **X-rays** at the extreme) and longer wavelength to lower energy (**microwave**, **radio**).

// put em.jpg here (the thing in assets)

<div class="theorem-box">

**Example.** Two monochromatic beams deliver the same energy per second, one at $$400\ \mathrm{nm}$$ and one at $$800\ \mathrm{nm}$$. Compare their photon arrival rates.

The $$400\ \mathrm{nm}$$ photons each carry twice the energy because $$E=hc/\lambda$$. At equal power, the $$800\ \mathrm{nm}$$ beam therefore delivers twice as many photons per second. Equal beam power does not imply equal photon energy or equal photon count.

</div>

---

## Orbitals, nodes, shielding, and penetration

An **atomic orbital** is a three-dimensional region where the probability of finding an electron exceeds some threshold. The total number of **nodes** for an orbital is $$n - 1$$, with $$l$$ **angular nodes** (planar/conical surfaces), and the rest being **spherical nodes** (spherical surfaces).

A **node** is a surface where the orbital wavefunction is zero, so its probability density is zero there. In the hydrogen-like orbital model, nodes come in two types:

- **Radial nodes** are spherical surfaces centered on the nucleus. They separate inner and outer regions of the orbital and number $$n-l-1$$.
- **Angular nodes** occur in particular directions and number $$l$$. For a real $$p_z$$ orbital the angular node is the xy plane; d orbitals can have planar or conical nodal surfaces.

Thus a $$2s$$ orbital has one radial node and no angular nodes, while a $$2p$$ orbital has no radial nodes and one angular node. Both have one total node but different shapes. The positive and negative regions in orbital drawings indicate wavefunction sign, not positive and negative electric charge. The electron does not follow a classical path that has to cross a nodal surface. See [OpenStax's orbital discussion](https://openstax.org/books/chemistry/pages/6-3-development-of-quantum-theory).

**Diagram placeholder:** Compare a cross-section of a $$2s$$ orbital with its spherical radial node and a $$2p_z$$ orbital with its xy nodal plane. Label wavefunction signs separately from probability density.

For a given $$n$$ in many-electron atoms, subshell energies usually follow

$$
E_{ns} < E_{np} < E_{nd} < E_{nf},
$$

because s orbitals *penetrate* closer to the nucleus and experience less **shielding** from inner electrons than p, d, or f orbitals at comparable $$n$$.

**Shielding** (screening) means inner and same-shell electrons reduce the **full nuclear charge** $$Z$$ felt by an electron of interest. More effective shielding lowers **effective nuclear charge** and stabilizes outer electrons less. Penetration explains why an $$ns$$ electron can be more tightly bound than an $$(n-1)d$$ electron despite the larger $$n$$ in the label, leading to the *aufbau* order you use when writing configurations.

### Effective nuclear charge

**Effective nuclear charge** $$Z_{\text{eff}}$$ is the net positive charge experienced by an electron in a many-electron atom after shielding. A simple textbook form is

$$
Z_{\text{eff}} = Z - S,
$$

where $$S$$ is a **shielding constant** summarizing electron–electron repulsion. **Slater’s rules** and more advanced models give numerical estimates; qualitatively, $$S$$ grows as you add *inner shells*, so going *down a group* increases shielding even though $$Z$$ increases. On the AP exam, this equation will not be tested in full but it is good to know that shielding decreases effective nuclear charge.

Penetration order among subshell types at comparable $$n$$ is often summarized as

$$
s > p > d > f,
$$

meaning s electrons “see” more of the nucleus and are stabilized relative to p, d, and f in the same shell.

<div class="theorem-box">

**Example.** Sodium and magnesium both lose a $$3s$$ electron in their first ionization. Why does magnesium generally require more energy even though its additional electron also adds repulsion?

Magnesium has one more proton, while both atoms have the same neon-like core. The extra valence electron does not fully shield the extra nuclear charge, so magnesium's $$3s$$ electrons experience stronger net attraction and a more contracted distribution. Repulsion matters, but it does not cancel the nuclear-charge increase. Counting electrons without considering their shielding effectiveness misses the trend.

</div>

---

## Periodic trends

**Ionization energy** is the energy required to remove an electron from a gaseous atom or ion (first, second, … ionization energies for successive removals). **Electron affinity** is the energy change when an electron is added; *more exothermic* addition corresponds to a *more favorable* affinity in the usual sign convention.

**Atomic radius** gauges the size of the **electron cloud** (often defined by metallic or covalent radii in different contexts). **Metallic character** is the tendency to lose electrons and behave as a metal (cations); **nonmetallic character** is the tendency to gain or share electrons with nonmetals (anions).

Broad patterns: **atomic radius** increases *down a group* (new shells, more shielding) and decreases *across a period* (rising $$Z_{\text{eff}}$$). **Ionization energy** and **electron affinity** (for representative elements) generally show opposite *horizontal* trends to radius. **Metallic character** decreases across a period and increases down a group. Exceptions, such as the **ionization energy** dip at boron or the **electron affinity** anomaly for nitrogen, appear when subshell structure or pairing changes the cost of removing or adding an electron.

// put periodictriends.png here (the thing in assets)

<div class="theorem-box">

**Example.** Magnesium has a higher first ionization energy than aluminum even though aluminum is farther right. Explain this exception using their valence configurations.

Magnesium loses a $$3s$$ electron from $$[\mathrm{Ne}]3s^2$$; aluminum loses a $$3p$$ electron from $$[\mathrm{Ne}]3s^23p^1$$. The aluminum $$3p$$ electron is higher in energy and less penetrating than a $$3s$$ electron. That subshell change outweighs the increase in nuclear charge for this comparison.

</div>

---

## Electrostatics and Coulomb’s law

**Electrostatics** describes forces and *potential energies* between charges at rest. The **Coulomb force** between two point charges is

$$
F = k \frac{Q_1 Q_2}{r^2},
$$

where $$r$$ is their separation, $$Q_1$$ and $$Q_2$$ carry signs, and $$k \approx 8.99 \times 10^9 \,\text{N}\cdot\text{m}^2/\text{C}^2$$. Like charges repel; opposite charges attract.

The **electric potential energy** of the pair is

$$
U = k \frac{Q_1 Q_2}{r}.
$$

These expressions reappear when you interpret **lattice energy**, **bond** formation, and **ionic** attraction in [Unit 2](/notes/ap/chem/compounds/).

<div class="theorem-box">

**Example.** Two opposite point charges are moved from separation $$r$$ to $$2r$$. Compare the attraction magnitude and potential energy, taking zero potential energy at infinite separation.

The force magnitude becomes one-fourth as large, while $$U=kQ_1Q_2/r$$ becomes half its original negative value. Thus potential energy increases toward zero even though its magnitude decreases. Separating the charges requires positive work against the attraction.

</div>

---


## Practice

### MCQ

::::problem
1. A neutral atom has successive ionization energies $$580, 1800, 2700, 11600\ \mathrm{kJ/mol}$$. Which inference best fits a main-group atom?

   (A) One valence electron<br>
   (B) Two valence electrons<br>
   (C) Three valence electrons<br>
   (D) Four valence electrons

:::solution
The large jump occurs after three electrons have been removed. Removing the fourth disrupts a core shell. The jump's location, rather than the largest listed energy alone, identifies three valence electrons.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
2. Two ions each contain 10 electrons. Ion X has 12 protons and ion Y has 9. Which comparison is justified?

   (A) X is larger because it is more positive<br>
   (B) X is smaller because its nuclear attraction is stronger<br>
   (C) Y is smaller because it has fewer protons<br>
   (D) Their radii are equal because their electron counts match

:::solution
X is magnesium(II) and Y is fluoride. With the same occupied shells and electron count, X's larger nuclear charge contracts its electron cloud more strongly. Equal electron configurations do not guarantee equal radii.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
3. Equal-energy pulses at $$300\ \mathrm{nm}$$ and $$600\ \mathrm{nm}$$ strike a detector. What is the ratio of photon counts $$N_{600}/N_{300}$$?

   (A) $$1/4$$<br>
   (B) $$1/2$$<br>
   (C) $$1$$<br>
   (D) $$2$$

:::solution
Photon energy is inversely proportional to wavelength. The 600 nm photons each have half the energy, so twice as many are required to carry the same total pulse energy: $$N=E_{pulse}\lambda/(hc)$$.

$$
\boxed{\text{D}}.
$$
:::
::::

::::problem
4. An element contains isotopes of masses $$24.0$$ and $$26.0\ \mathrm{u}$$. Its measured average is $$24.4\ \mathrm{u}$$. Which is the heavier isotope's abundance?

   (A) $$20\%$$<br>
   (B) $$40\%$$<br>
   (C) $$60\%$$<br>
   (D) $$80\%$$

:::solution
Let f be the heavier fraction. Then $$24.0(1-f)+26.0f=24.4$$, so $$2.0f=0.4$$ and $$f=0.20$$. Assigning 80% to the heavier isotope would give 25.6 u instead.

$$
\boxed{\text{A}}.
$$
:::
::::

::::problem
5. A compound is $$40.0\%$$ C, $$6.7\%$$ H, and $$53.3\%$$ O by mass, with molar mass about $$180\ \mathrm{g/mol}$$. Which molecular formula fits? Use atomic masses 12, 1, and 16.

   (A) $$\mathrm{CH_2O}$$<br>
   (B) $$\mathrm{C_3H_6O_3}$$<br>
   (C) $$\mathrm{C_6H_{12}O_6}$$<br>
   (D) $$\mathrm{C_6H_6O_6}$$

:::solution
A 100 g sample gives about 3.33 mol C, 6.7 mol H, and 3.33 mol O: ratio 1:2:1. The empirical mass is 30 g/mol, so the molecular formula is six times CH2O. Mass percent determines the ratio; molar mass determines the multiplier.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
6. PES peaks for a neutral atom correspond to electron counts $$2,2,6,2,3$$ from most tightly bound to least tightly bound subshells. Which removal produces its first cation?

   (A) Removal from 1s because it is closest to the nucleus<br>
   (B) Removal from 3p because it has the lowest binding energy<br>
   (C) Removal from 2p because it contains the most electrons<br>
   (D) Removal from 3s because s orbitals always ionize first

:::solution
The counts give $$1s^22s^22p^63s^23p^3$$. The first electron removed is from the least tightly bound occupied subshell, 3p. Peak area tells electron count, whereas binding energy tells removal cost.

$$
\boxed{\text{B}}.
$$
:::
::::

### FRQ

::::frq{id=chem-atomicstrucprop-1}
7. A sample of chlorine contains $$75.78\%$$ $$^{35}\text{Cl}$$ atoms and $$24.22\%$$ $$^{37}\text{Cl}$$ atoms.

   $$(A)$$ Calculate the average atomic mass of chlorine.

   $$(B)$$ Explain why the average atomic mass is closer to $$35$$ than to $$37$$.

   $$(C)$$ A PES spectrum for chlorine shows peaks from core electrons and valence electrons. Explain why core-electron peaks appear at higher binding energy than valence-electron peaks.

   $$(D)$$ **Original extension.** A different chlorine sample has an average mass of approximately $$35.60\ \text{amu}$$. Using isotope masses of $$35$$ and $$37\ \text{amu}$$, determine its percent chlorine-37 and explain whether its electron configuration differs from that of the first sample.

:::solution
$$(A)$$ Use a weighted average:

$$
(0.7578)(35)+(0.2422)(37)=35.4844.
$$

The percentages must be written as decimals because each isotope contributes only its fractional abundance to the average.

The average atomic mass is

$$
\boxed{35.48\ \text{amu}}.
$$

$$(B)$$ The average is closer to $$35$$ because the $$^{35}\text{Cl}$$ isotope is much more abundant than $$^{37}\text{Cl}$$. In a weighted average, the more abundant isotope pulls the average closer to its mass. Since about three-fourths of the atoms are $$^{35}\text{Cl}$$, the average should sit much nearer $$35$$ than $$37$$, which matches the calculated value.

$$(C)$$ Core electrons are closer to the nucleus and experience a larger effective nuclear attraction than valence electrons. They are also less shielded by other electrons. Because the attraction between the nucleus and a core electron is stronger, more energy is required to remove a core electron from the atom. Therefore, core-electron peaks appear at higher binding energy on a PES spectrum than valence-electron peaks.

$$(D)$$ Let $$f$$ be the fraction of chlorine-37. Then $$35(1-f)+37f=35.60$$, so $$f=0.300$$, or $$30.0\%$$. The samples have different neutron distributions, not different atomic numbers. Neutral atoms of both isotopes therefore have the same ground-state electron configuration; a change in average mass does not imply a change in valence electrons.
:::
::::

::::frq{id=chem-atomicstrucprop-2}
8. Sterling silver contains silver and copper. In a released AP Chemistry question, students compared atomic radii using Coulomb's law. (Adapted from College Board, [2024 AP Chemistry FRQ 3](https://apcentral.collegeboard.org/media/pdf/ap24-frq-chemistry.pdf).)

   $$(A)$$ Identify which atom has the larger atomic radius: $$\text{Ag}$$ or $$\text{Cu}$$.

   $$(B)$$ Use shell structure and Coulomb's law to justify your answer.

   $$(C)$$ Explain why comparing only nuclear charge is not enough to predict the radius in this case.

   $$(D)$$ **Original extension.** Compare the radii of $$\text{Cu}^+$$ and $$\text{Cu}^{2+}$$. State their ground-state electron configurations and explain why nuclear charge alone cannot explain their difference.

:::solution
$$(A)$$ $$\text{Ag}$$ has the larger atomic radius.

$$(B)$$ Silver's valence electrons occupy a higher principal energy level than copper's valence electrons. Copper is in period 4, while silver is in period 5, so the outer electrons in silver are farther from the nucleus. By Coulomb's law, attraction decreases as distance increases:

$$
F\propto \frac{q_1q_2}{r^2}.
$$

Silver also has more inner electrons, which increases shielding. The greater distance and shielding make the attraction between the nucleus and valence electrons weaker, so the atomic radius is larger.

$$(C)$$ Silver has more protons than copper, which by itself would increase attraction. But the valence electrons in silver are also farther from the nucleus and more shielded. Radius depends on the balance of nuclear charge, shielding, and distance, not nuclear charge alone. On the AP exam, a complete explanation should explicitly compare both the attractive force from the nucleus and the distance/shielding effect.

$$(D)$$ The configurations are $$[\text{Ar}]3d^{10}$$ and $$[\text{Ar}]3d^9$$, respectively; the $$4s$$ electrons are removed before $$3d$$ electrons. Both ions have $$29$$ protons, so nuclear charge is unchanged. Removing another electron reduces electron-electron repulsion and allows the remaining electron cloud to contract. Thus $$\text{Cu}^{2+}$$ is smaller. These ions are not isoelectronic, so an isoelectronic-series argument would not apply.
:::
::::
