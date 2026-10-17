---
title: "Unit 1: Atomic Structure and Properties"
description: "AP Chemistry notes on atomic structure, periodic trends, electron configurations, Coulombic attraction, and photoelectron spectra."
sidebar:
  order: 1
---

## The Basics of Chemistry

### Significant figures

**Significant figures** are the digits justified by a measurement’s precision. Use them when rounding a calculated result so it does not imply greater precision than the original data support. Sig-figs (or sig-digs) follow a strict set of rules:

- Nonzero digits are always significant.
- **Leading zeros** (as in $$0.0045$$) are not significant; they only locate the decimal point. **Captive zeros** between nonzero digits are significant (e.g. $$1.05$$ has three significant figures).
- **Trailing zeros** require care: if a decimal point is shown, trailing zeros are significant ($$12.0$$ has three); if there is no decimal, trailing zeros do not ocunt towards significant figures.
- **Exact numbers** (such as a counted dozen eggs or a defined conversion within a system) have effectively unlimited significant figures and do not limit your result.
- For addition and subtraction, round the result to the same number of *decimal places* as the term with the fewest. For multiplication and division, round to the same number of *significant figures* as the factor with the fewest.

<div class="theorem-box">

**Example.** A balance reads $$2.50\ \text{g}$$ for an empty container and $$2.56\ \text{g}$$ after adding a sample. A student reports a sample mass of $$0.0600\ \text{g}$$ because both readings have three significant figures. What is wrong?

Subtraction is limited by decimal place, not by matching significant-figure counts. The difference is $$0.06\ \text{g}$$, known only to the hundredths place. The added zeros in $$0.0600$$ claim precision the balance did not provide. Subtracting nearby measurements can leave far fewer significant figures than either measurement alone.

</div>

<div class="theorem-box">

**Example.** A sample's mass is found by subtracting $$1.247\times10^2\ \mathrm{g}$$ from $$1.263\times10^2\ \mathrm{g}$$. Its volume is $$2.50\times10^{-1}\ \mathrm{mL}$$. Calculate its density in scientific notation with the correct significant figures.

First align the powers of ten. The masses are $$124.7$$ and $$126.3\ \mathrm{g}$$, both measured to the tenths place, so the difference is $$1.6\ \mathrm{g}$$. This difference has only two significant figures, even though each original mass has four.

$$
\rho=\frac{1.6}{2.50\times10^{-1}}=6.4\times10^0\ \mathrm{g/mL}.
$$

The subtraction determines the precision of the numerator; the final division is therefore limited to two significant figures.

</div>

### Matter and its classification

**Matter** is anything that has mass and occupies volume, and is the fundamental building block of chemistry. Chemists classify it first by composition.

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

**Metals** occupy the left and center of the table, including the two detached rows. **Nonmetals** cluster in the upper right; hydrogen is a nonmetal even though it appears above group 1. **Metalloids**, commonly B, Si, Ge, As, Sb, and Te, lie along the staircase between these regions and have properties intermediate between typical metals and nonmetals. The boundary is a useful guide, not a sharp rule for every property or classification.

---

## Ions

An **ion** is an atom or group of atoms with a net electric charge from gain or loss of electrons. A **cation** is positive (fewer electrons than protons); an **anion** is negative (more electrons than protons). A good way to remember this is that cats are always positive so CATions are positively charged!

**Metals** tend to form cations and **nonmetals** tend to form anions. In addition, many **transition metals** exhibit variable charge in compounds because several oxidation states are comparably stable (mentioned later in more detail) due to the availability of their $$d$$ orbital (mentioned later).

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

---

## Avogadro’s number, the mole, and molar mass

The **mole** is the chemist’s unit of counting: one mole contains **Avogadro’s number** (sometimes denoted as $$N_A$$) of specified entities (atoms, molecules, ions, formula units, etc.):

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

<div class="theorem-box">

**Example.** A molecular compound is $$54.5\%$$ carbon, $$9.1\%$$ hydrogen, and $$36.4\%$$ oxygen by mass. Its molar mass is $$88.0\ \mathrm{g/mol}$$. Using atomic masses $$12.0$$, $$1.00$$, and $$16.0$$, determine its molecular formula.

For a $$100\ \mathrm{g}$$ sample, the mole amounts are $$54.5/12.0=4.54$$ for carbon, $$9.1/1.00=9.1$$ for hydrogen, and $$36.4/16.0=2.275$$ for oxygen. Dividing each by the smallest gives approximately $$2:4:1$$, so the empirical formula is $$\mathrm{C_2H_4O}$$.

Its empirical-formula mass is $$2(12.0)+4(1.00)+16.0=44.0\ \mathrm{g/mol}$$. The multiplier is $$88.0/44.0=2$$, giving molecular formula $$\mathrm{C_4H_8O_2}$$. Multiply every subscript, not just the carbon subscript.

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

**Example.** An element has two isotopes of masses $$10.0$$ and $$11.0\ \mathrm{amu}$$ and average mass $$10.8\ \mathrm{amu}$$. A student assigns the taller peak to the lighter isotope. Determine whether that assignment fits the data.

Let $$f$$ be the lighter isotope's fraction. Then $$10.0f+11.0(1-f)=10.8$$ gives $$f=0.20$$. The heavier isotope is $$80\%$$ abundant and should have the taller peak if detector response and charge are comparable. An unweighted midpoint of $$10.5$$ would assume equal abundances without evidence.

</div>

<div class="theorem-box">

**Example.** A hypothetical element has only two isotopes, with masses $$62.0$$ and $$64.0\ \mathrm{amu}$$. Its singly charged ions give the relative intensities below. Assuming equal detector response per ion, calculate each isotope's percent abundance and the average atomic mass.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[axis lines=left, width=9cm, height=5cm, xmin=61, xmax=65, ymin=0, ymax=110, xtick={62,64}, ytick={0,25,50,75,100}, xlabel={mass-to-charge ratio}, ylabel={relative intensity}]
\addplot[ycomb, very thick, blue] coordinates {(62,100) (64,25)};
\node[anchor=south] at (axis cs:62,100) {100};
\node[anchor=south] at (axis cs:64,25) {25};
\end{axis}
\end{tikzpicture}
```

The intensities sum to $$125$$, not $$100$$. Thus the lighter isotope's fraction is $$100/125=0.800$$ and the heavier isotope's fraction is $$25/125=0.200$$: their abundances are $$80.0\%$$ and $$20.0\%$$.

$$
\overline m=(0.800)(62.0)+(0.200)(64.0)=62.4\ \mathrm{amu}.
$$

A base peak labeled 100 is a relative intensity, not necessarily a 100% abundance.

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

**Example.** Dissolve $$5.85\ \mathrm{g}$$ NaCl, with molar mass $$58.5\ \mathrm{g/mol}$$, to make $$250.0\ \mathrm{mL}$$ of solution. Transfer $$20.0\ \mathrm{mL}$$ of this solution to a second flask and dilute to $$100.0\ \mathrm{mL}$$. Find both concentrations.

The stock contains $$5.85/58.5=0.100\ \mathrm{mol}$$, so its concentration is $$0.100/0.2500=0.400\ M$$. The transferred portion contains $$0.400(0.0200)=0.00800\ \mathrm{mol}$$. Dilution changes the volume but not this solute amount, giving $$0.00800/0.1000=0.0800\ M$$. Use the final solution volumes in both calculations, not the amount of water added.

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

The rule of thumb is that you always assign the most electronegative atom first in terms of oxidation states. Note that hydrogen must have $$+1$$ or $$-1$$ since you can only fill/empty its first subshell.

<div class="theorem-box">

**Example.** Find chromium's oxidation number in $$\mathrm{K_2Cr_2O_7}$$, and explain why the sum for the dichromate ion differs from the sum for the whole compound.

Potassium is $$+1$$ and oxygen is $$-2$$. For the neutral compound, $$2(+1)+2x+7(-2)=0$$, so $$2x=12$$ and each chromium is $$+6$$. For $$\mathrm{Cr_2O_7^{2-}}$$ alone, $$2x+7(-2)=-2$$ gives the same result. Oxidation numbers sum to the charge of the species being analyzed, not always to zero.

</div>

<div class="theorem-box">

**Example.** Oxygen appears in $$\mathrm{H_2O_2}$$ and $$\mathrm{OF_2}$$. Determine its oxidation number in each and explain why the usual $$-2$$ shortcut fails.

In the peroxide, $$2(+1)+2x=0$$ gives $$x=-1$$. In $$\mathrm{OF_2}$$, fluorine takes $$-1$$, so $$x+2(-1)=0$$ gives $$x=+2$$. The sum must equal the species charge; assigning oxygen $$-2$$ blindly would violate that constraint.

</div>

---

## Quantum mechanics in chemistry

### Electron configuration and quantum numbers

Each electron in an atom is described by four **quantum numbers** that arise from the wave-mechanical model (basically everything is a wave and a particle at the same time).

The **principal quantum number** $$n$$ is a positive integer ($$n = 1, 2, 3, \ldots$$). It sets the shell and is the main contributor to orbital energy for hydrogen-like atoms.

The **azimuthal** (or **angular momentum**) quantum number $$l$$ runs from $$0$$ to $$n - 1$$ and labels subshell shape:

- $$l = 0$$ → s orbital
- $$l = 1$$ → p orbital
- $$l = 2$$ → d orbital
- $$l = 3$$ → f orbital

The **magnetic quantum number** $$m_l$$ takes integer values from $$-l$$ to $$+l$$ and distinguishes *orientations* of a subshell in space (e.g. $$p_x$$ and $$p_y$$)

The **spin quantum number** $$m_s$$ is $$+\frac{1}{2}$$ or $$-\frac{1}{2}$$ for the two **spin** states of a single electron.

When assigning these numbers to electrons, you follow a set list of rules:

- The **Pauli exclusion principle** states that no two electrons in the same atom may share the same set of four quantum numbers, so at most two electrons occupy any one atomic orbital, and they must have *opposite spin*.

- The **Aufbau principle** directs you to fill orbitals in order of increasing energy. The familiar $$n s$$, $$(n-1) d$$, $$(n-2) f$$ crossing is why the periodic table has its shape. Exceptions (e.g. chromium $$\text{Cr}$$, copper $$\text{Cu}$$, and several heavier transition metals) reflect especially stable $$d^5$$ or $$d^{10}$$ arrangements; those same stability patterns contribute to variable metal oxidation states in compounds.

- **Hund’s rule** favors placing electrons singly in degenerate orbitals of a subshell before pairing, with *parallel spins* where possible, to reduce *electron–electron repulsion*.

- **Heisenberg’s uncertainty principle** limits how precisely position and momentum can be known simultaneously for a quantum particle: a conceptual foundation for why we speak in terms of orbitals (probability distributions) rather than classical orbits. It states that: $$\Delta x \Delta p \ge \frac{h}{4\pi} = \frac{\bar h}{2}$$. This means that the uncertainty in position and momentum are always above some constant, implying that both cannot be known at a time. This is why we have electron clouds instead of set orbits. $$h$$ is Planck's constant and $$\bar h$$ is the reduced Planck's constant

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

<img class="note-img" src="/assets/APs/AP%20Chem/atomicstrucprop/em.jpg" alt="Electromagnetic spectrum from radio waves to gamma rays, with decreasing wavelength and increasing photon energy" loading="lazy" decoding="async" />

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

Taking into account shielding, the nuclear charge should be modified. **Effective nuclear charge** $$Z_{\text{eff}}$$ is the net positive charge experienced by an electron in a many-electron atom after shielding:
$$
Z_{\text{eff}} = Z - S,
$$

where $$S$$ is a **shielding constant** summarizing electron–electron repulsion.

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

<img class="note-img" src="/assets/APs/AP%20Chem/atomicstrucprop/periodictrends.png" alt="Periodic table showing general directions of increasing atomic radius, ionization energy, and metallic character" loading="lazy" decoding="async" />

The arrows summarize broad trends, not exception-free rules. In the image, increasing electron affinity means a generally greater tendency to accept an electron; if electron-gain energy is reported with an exothermic negative sign, more favorable attachment corresponds to a more negative value.

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

:::equations

| Idea | Equation | Conditions |
| --- | --- | --- |
| Particle counts | $$A=Z+N$$; ion charge in elementary-charge units $$=N_p-N_e$$ | Isotopes share Z, not necessarily A. |
| Moles and particles | $$n=m/M_{molar}$$; $$N=nN_A$$ | Specify the counted entities. |
| Average isotope mass | $$\overline m=\sum_i f_im_i$$; $$\sum_i f_i=1$$ | Normalize isotope intensities before weighting. |
| Molecular-formula multiplier | $$k=M_{compound}/M_{empirical}$$ | k must be consistent with a positive integer within measurement precision. |
| Molarity and dilution | $$M=n/V$$; $$M_1V_1=M_2V_2$$ | V is final solution volume in liters; dilution conserves solute when no reaction occurs. |
| Yield and error | $$\%yield=(actual/theoretical)100\%$$; $$\%error=\lvert measured-accepted\rvert\,100\%/\lvert accepted\rvert$$ | Yield is not the same as percent error; accepted value must be nonzero. |
| Energy efficiency | $$\eta=E_{useful}/E_{input}$$ | Multiply by 100% to report a percentage. |
| Light | $$c=\lambda\nu$$; $$E_{photon}=h\nu=hc/\lambda$$; $$N_{photons}=E_{pulse}/E_{photon}$$ | Use consistent wavelength units. |
| Photoemission | $$K_{max}=h\nu-\Phi$$; $$\lambda_0=hc/\Phi$$ | Emission requires photon energy at least the work function in the single-photon model. |
| Orbital nodes | $$N_{radial}=n-l-1$$; $$N_{angular}=l$$; $$N_{total}=n-1$$ | Hydrogen-like orbital model. |
| Effective nuclear charge | $$Z_{eff}\approx Z-S$$ | S is shielding; this is an approximate model. |
| Coulomb interaction | $$F=k\lvert Q_1Q_2\rvert/r^2$$; $$U=kQ_1Q_2/r$$ | F is force magnitude; U is signed and zero at infinite separation. |
| Uncertainty | $$\Delta x\Delta p\ge h/(4\pi)$$ | Position and momentum uncertainties refer to the same direction. |

:::

## Practice

### MCQ

::::problem
1. A period-3 element X has successive ionization energies of approximately $$740,1450,7730,10500\ \mathrm{kJ/mol}$$. For its usual monatomic ion, which electron count and radius comparison with $$\mathrm{Na^+}$$ are consistent with these data?

   (A) 10 electrons; smaller than sodium ion<br>
   (B) 10 electrons; larger than sodium ion<br>
   (C) 12 electrons; smaller than sodium ion<br>
   (D) 8 electrons; larger than sodium ion

:::solution
The large jump after the second removal identifies two valence electrons, so X is magnesium and its usual ion is magnesium(II). It has 10 electrons, just like sodium ion, but 12 protons rather than 11. With the same occupied shells, the stronger nuclear attraction makes the magnesium ion smaller.

$$
\boxed{\text{A}}.
$$
:::
::::

::::problem
2. A hypothetical element has isotopes of masses $$50.0$$ and $$52.0\ \mathrm{amu}$$ and an average atomic mass of $$50.6\ \mathrm{amu}$$. If atoms pair randomly to form diatomic molecules, what fraction contains one atom of each isotope?

   (A) $$0.21$$<br>
   (B) $$0.30$$<br>
   (C) $$0.42$$<br>
   (D) $$0.49$$

:::solution
The heavy-isotope fraction satisfies $$50(1-f)+52f=50.6$$, giving $$f=0.30$$. Mixed molecules arise in two ways, light-heavy and heavy-light, so their fraction is $$2(0.70)(0.30)=0.42$$. Using just one product misses half the mixed pairs.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
3. A surface has threshold wavelength $$600\ \mathrm{nm}$$. Equal-energy pulses of $$300\ \mathrm{nm}$$ and $$400\ \mathrm{nm}$$ light strike it. In the single-photon model, what are $$N_{400}/N_{300}$$ and $$K_{max,300}/K_{max,400}$$?

   (A) $$3/4$$ and $$4/3$$<br>
   (B) $$4/3$$ and $$2$$<br>
   (C) $$4/3$$ and $$4/3$$<br>
   (D) $$3/4$$ and $$2$$

:::solution
Equal pulse energy gives photon count proportional to wavelength, hence $$N_{400}/N_{300}=4/3$$. The threshold work function is $$hc/(600\ \mathrm{nm})$$. Subtracting this from each photon energy gives a kinetic-energy ratio $$(1/300-1/600)/(1/400-1/600)=2$$. Photon-energy ratios alone do not give the electron kinetic-energy ratio.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
4. A compound contains $$40.0\%$$ C, $$6.7\%$$ H, and the remainder O. Its molar mass is $$90.0\ \mathrm{g/mol}$$. Use atomic masses 12.0, 1.00, and 16.0. Which molecular formula is consistent with both measurements?

   (A) $$\mathrm{CH_2O}$$<br>
   (B) $$\mathrm{C_3H_3O_3}$$<br>
   (C) $$\mathrm{C_2H_4O_2}$$<br>
   (D) $$\mathrm{C_3H_6O_3}$$

:::solution
Oxygen is 53.3% by mass. A 100 g sample gives approximately 3.33 mol C, 6.7 mol H, and 3.33 mol O, a 1:2:1 ratio. The empirical mass is 30.0 g/mol, so the molecular formula is three times the empirical formula. Neither the mass percentages nor the molar mass can be ignored.

$$
\boxed{\text{D}}.
$$
:::
::::

::::problem
5. Dissolve $$2.50\ \mathrm{g}$$ of $$\mathrm{CuSO_4\cdot5H_2O}$$, molar mass $$250.\ \mathrm{g/mol}$$, to make $$100.0\ \mathrm{mL}$$ solution. Dilute a $$15.0\ \mathrm{mL}$$ portion to $$60.0\ \mathrm{mL}$$. What is the final copper(II) concentration?

   (A) $$0.0100\ M$$<br>
   (B) $$0.0250\ M$$<br>
   (C) $$0.0625\ M$$<br>
   (D) $$0.100\ M$$

:::solution
The hydrate supplies $$2.50/250.=0.0100\ \mathrm{mol}$$ copper ions, giving a 0.100 M stock. The transferred portion contains $$0.100(0.0150)=0.00150\ \mathrm{mol}$$ copper ions. Dividing by 0.0600 L gives 0.0250 M. Waters of hydration contribute to the solid's molar mass but do not multiply the copper amount.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
6. Neutral X and Y have valence configurations $$3s^2$$ and $$3s^23p^1$$, respectively. Which paired prediction is correct?

   (A) Y has both the higher first ionization energy and larger usual cation<br>
   (B) X has the smaller neutral atom and smaller usual cation<br>
   (C) X has the higher first ionization energy, but Y has the smaller usual cation<br>
   (D) Y has the higher first ionization energy, but X has the smaller usual cation

:::solution
X is Mg and Y is Al. The first electron removed from Al occupies the higher-energy, less penetrating 3p subshell, so its first ionization energy is lower than Mg's. The usual ions, magnesium(II) and aluminum(III), both have 10 electrons; aluminum's greater nuclear charge makes its ion smaller. Different comparisons require different electron configurations.

$$
\boxed{\text{C}}.
$$
:::
::::

### FRQ

::::frq{id=chem-atomicstrucprop-challenge-1}
7. A hypothetical element X forms singly charged ions with mass-spectrum peaks at $$m/z=78.0$$ and $$80.0$$, with relative intensities 100 and 25. Assume equal detector response. A molecular compound of X and fluorine contains 57.9% X by mass and has molar mass $$135.4\ \mathrm{g/mol}$$. Use $$M_F=19.0\ \mathrm{g/mol}$$ and $$N_A=6.022\times10^{23}\ \mathrm{mol^{-1}}$$.

   $$(A)$$ Determine the isotope abundances and X's average atomic mass.

   $$(B)$$ Determine the empirical and molecular formulas of the compound from the composition data.

   $$(C)$$ Find the number of molecules containing the heavier X isotope in a 0.6770 g sample. Determine the masses of its two isotope-specific molecular ions, treating fluorine as mass 19.0.

   $$(D)$$ Predict the relative molecular-ion peak intensities and explain how doubly charged ions would change their positions.

:::solution
$$(A)$$ Normalize by the total intensity, 125. The abundances are $$100/125=80.0\%$$ and $$25/125=20.0\%$$. The average is $$0.800(78.0)+0.200(80.0)=78.4\ \mathrm{amu}$$. A peak normalized to 100 is not a statement that every atom has that mass.

$$(B)$$ For 100 g, $$57.9/78.4=0.7385\ \mathrm{mol}$$ X and $$42.1/19.0=2.216\ \mathrm{mol}$$ F give approximately a 1:3 ratio. The empirical formula is $$\mathrm{XF_3}$$, with mass $$78.4+3(19.0)=135.4\ \mathrm{g/mol}$$. This matches the measured molar mass, so the multiplier is one and the molecular formula is also $$\mathrm{XF_3}$$. The isotope-weighted average, rather than either individual isotope mass, is used for the bulk sample.

$$(C)$$ Total compound amount is $$0.6770/135.4=0.005000\ \mathrm{mol}$$. One X atom occurs in each molecule, so 20.0% of molecules contain the heavier isotope: $$N=0.200(0.005000)(6.022\times10^{23})=6.02\times10^{20}$$ molecules. Individual molecular ions have masses $$78.0+57.0=135.0$$ and $$80.0+57.0=137.0\ \mathrm{amu}$$, not the average formula mass.

$$(D)$$ With one X atom per molecule, the isotope fractions remain 80.0% and 20.0%, so equal-response peak intensities retain a 4:1 ratio. Singly charged peaks occur at 135.0 and 137.0; doubly charged versions would occur at $$m/z=67.5$$ and $$68.5$$. Charge changes peak position without changing isotope mass. Comparing intensities across charge states would require knowing their relative formation and detector responses.
:::
::::

::::frq{id=chem-atomicstrucprop-challenge-2}
8. A period-3 element Y has subshell electron counts $$2,2,6,2,1$$ in order of decreasing binding energy. A metal surface has work function $$\Phi=3.00\times10^{-19}\ \mathrm{J}$$. Use $$h=6.63\times10^{-34}\ \mathrm{J\,s}$$ and $$c=3.00\times10^8\ \mathrm{m/s}$$.

   $$(A)$$ Identify Y and its usual cation's electron configuration. Predict whether that cation or magnesium(II) is smaller, and justify.

   $$(B)$$ Explain why Y can have a lower first ionization energy than magnesium despite its larger nuclear charge, then predict where Y's largest early successive-ionization jump occurs.

   $$(C)$$ Calculate the maximum electron kinetic energy when the surface is illuminated at $$400.\ \mathrm{nm}$$ and determine the longest wavelength that can eject electrons.

   $$(D)$$ Equal-energy pulses of 400 nm and 800 nm light strike the surface. Compare photon counts and decide which pulse ejects electrons in the single-photon model.

:::solution
$$(A)$$ The counts give $$1s^22s^22p^63s^23p^1$$, totaling 13 electrons: aluminum. Removing the three valence electrons gives $$\mathrm{Al^{3+}}:[\mathrm{Ne}]$$. Both aluminum(III) and magnesium(II) have 10 electrons, but aluminum has 13 protons instead of 12. Its greater nuclear attraction contracts the same occupied electron shells more strongly, so aluminum(III) is smaller.

$$(B)$$ Aluminum's first removed electron is in 3p, which is higher in energy and less penetrating than magnesium's 3s electron. That subshell difference makes removal easier despite the larger proton count. After aluminum loses three valence electrons, removing a fourth electron disrupts the neon-like core. The large jump is therefore between the third and fourth ionization energies, not between the first and second.

$$(C)$$ Photon energy is $$hc/\lambda=(6.63\times10^{-34})(3.00\times10^8)/(4.00\times10^{-7})=4.97\times10^{-19}\ \mathrm{J}$$. Subtracting the work function gives $$K_{max}=1.97\times10^{-19}\ \mathrm{J}$$. At threshold, $$hc/\lambda_0=\Phi$$, so $$\lambda_0=6.63\times10^{-7}\ \mathrm{m}=663\ \mathrm{nm}$$. Longer wavelengths carry too little energy per photon.

$$(D)$$ At fixed pulse energy, photon count is proportional to wavelength, so the 800 nm pulse contains twice as many photons. Its photon energy is only $$2.49\times10^{-19}\ \mathrm{J}$$, below the work function. It ejects no electrons in the stated model, while 400 nm photons can eject electrons. Greater photon count cannot compensate for insufficient energy per individual photon.
:::
::::
