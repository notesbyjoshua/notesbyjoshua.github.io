---
title: "Unit 2: Compound Structure and Properties"
description: "AP Chemistry notes on compounds, bonding, molecular structure, Lewis diagrams, polarity, hybridization, and intermolecular forces."
sidebar:
  order: 2
---

## Types of chemical bonding

Electrons are the currency of chemical bonding. Whether electrons are fully transferred, shared, or pooled determines the type of bond and, in broad terms, how strong and how directional that interaction is.

### Ionic bonding

An **ionic bond** arises between a metal and a nonmetal when electrons are transferred so that both partners approach stable electron counts. The metal loses electrons to become a **cation** and the nonmetal gains electrons to become an **anion**. The resulting ions attract one another by **Coulomb’s law** (see [Unit 1](/notes/ap/chem/compounds/)). For two point charges $$Q_1$$ and $$Q_2$$ separated by distance $$r$$, the electrostatic potential energy has the familiar form as seen in Unit 1 (with $$k$$ a constant):

$$
U = k \frac{Q_1 Q_2}{r}
$$

Oppositely charged ions ($$Q_1 Q_2 < 0$$) lower their energy as $$r$$ decreases, which is why a **crystal lattice** of alternating cations and anions is stable. **Lattice energy** trends (larger charges, smaller ions) follow from this same inverse dependence on $$r$$ and linear dependence on the product of charges.

A standard example is sodium chloride: chlorine accepts an electron to form $$\text{Cl}^-$$, and sodium becomes $$\text{Na}^+$$. The compound is held together by attraction between those ions, not by shared pairs in the sense of a covalent bond. There is no universal ranking in which ionic bonds are always strongest; compare the specified substances and the energy required for the same kind of process.

<div class="theorem-box">

**Example.** Compare idealized ion-pair attractions for $$\mathrm{Na^+Cl^-}$$ and $$\mathrm{Mg^{2+}O^{2-}}$$ at the same separation. Would doubling the separation of the magnesium-oxide pair make their potential energies equal?

The charge products are $$-e^2$$ and $$-4e^2$$, so the magnesium-oxide pair has four times the magnitude of attractive potential energy at equal separation. Doubling its separation leaves twice the sodium-chloride magnitude because $$U\propto Q_1Q_2/r$$. Equal magnitudes would require four times the separation. This compares pair energies, not complete crystal lattice energies.

</div>

### Covalent bonding

A **covalent bond** forms between atoms that are both relatively electronegative, typically two **nonmetals**, when they share one or more pairs of valence electrons. Neither atom fully owns the electrons; instead, both nuclei are attracted to the same shared density. **Bond polarity** appears when the two atoms differ in **electronegativity**: the shared pair is pulled toward the more electronegative atom, giving partial charges ($$\delta^+$$ and $$\delta^-$$) even though the bond is still covalent. Usually, the cutoff for a bond being polar is a absolute difference of electronegativity above 0.5, and for an ionic bond it is usually 2.0.

Compared with ionic lattices, individual covalent bonds are often discussed in terms of **bond energy** (the energy required to break one mole of that bond in the gas phase, for a defined process). **Triple bonds** are generally stronger and shorter than **double bonds**, which are stronger and shorter than **single bonds** between the same elements.

<div class="theorem-box">

**Example.** Both $$\mathrm{CO_2}$$ and $$\mathrm{H_2O}$$ contain polar covalent bonds. Why is only one molecule polar overall?

Bond polarity concerns unequal electron sharing along one bond; molecular polarity concerns the vector sum of all bond dipoles. The equal C-O dipoles cancel in linear $$\mathrm{CO_2}$$. The O-H dipoles do not cancel in bent water, leaving a net dipole. Knowing the electronegativity difference without the geometry is insufficient.

</div>

### Metallic bonding

In a metal, valence electrons are not localized between two nuclei. Instead, they occupy a *sea of delocalized electrons* that extends through the crystal, while the metal cations sit in orderly positions. That delocalization explains **electrical conductivity** and **malleability**: applying stress shifts ion layers without necessarily breaking localized bonds, because the electron sea can still bind the structure.

<div class="theorem-box">

**Example.** A solid does not conduct electricity, but its melt does. Another conducts in both states. Identify the likely bonding models and explain why melting matters.

The first is consistent with an ionic solid: ions are fixed in the lattice but mobile in the melt. The second is consistent with a metal, whose delocalized electrons carry charge in either state. Conductivity depends on mobile charge carriers, so the mere presence of charged particles is insufficient.

</div>

---

## Nomenclature

Systematic names tell a chemist which elements are present, in what ratio, and (for ions) what the charges are. The rules differ for **ionic compounds** and **molecular (covalent) compounds**.

### Molecular compounds

If a substance contains only covalent bonds between nonmetals, it is a **molecular compound**. For a **binary molecular compound** (exactly two different elements), use numerical prefixes (mono-, di-, tri-, …) to indicate how many atoms of each element are present. The less electronegative element is usually named first; the second element takes an *-ide* ending. For example, $$\text{N}_2\text{O}$$ is **dinitrogen monoxide**, the prefixes *di-* and *mono-* describe a two-to-one ratio of nitrogen to oxygen.

If the second species is a **polyatomic ion**, name it as such rather than forcing an *-ide* ending on a single atom. Acids containing hydrogen often have special names; those conventions are developed in [Unit 8](/notes/ap/chem/acidbase/).

<div class="theorem-box">

**Example.** A student reduces $$\mathrm{N_2O_4}$$ to $$\mathrm{NO_2}$$ before naming it. Explain why this changes the answer rather than simplifying the same molecular formula.

Molecular formulas preserve the actual atom counts in one molecule. $$\mathrm{N_2O_4}$$ is dinitrogen tetroxide, whereas $$\mathrm{NO_2}$$ is nitrogen dioxide. They share an empirical ratio but describe different molecules. Reducing a molecular formula discards the information that numerical prefixes are meant to communicate.

</div>

### Ionic compounds

An **ionic compound** is named beginning with the **cation**. For metals that can take more than one charge in compounds (many transition metals) include the charge as a Roman numeral in parentheses after the metal name: $$\text{Fe}^{3+}$$ in a compound is iron(III). Then name the **anion**: monatomic anions use the *-ide* ending ($$\text{F}^-$$ is **fluoride**). Ammonium, $$\text{NH}_4^+$$, behaves like a **polyatomic cation** in naming even though it contains no metal. Hydrogen ion, $$\text{H}^+$$, does not behave like a typical metal cation in nomenclature. Prefixes are not used to show stoichiometry in simple ionic names because the charges determine the ratio.

<div class="theorem-box">

**Example.** Determine the formula of iron(III) sulfide and explain why $$\mathrm{Fe_3S_2}$$ is not consistent with the name.

Iron(III) is $$\mathrm{Fe^{3+}}$$ and sulfide is $$\mathrm{S^{2-}}$$. The smallest neutral combination contains two iron ions and three sulfide ions, giving $$\mathrm{Fe_2S_3}$$. The proposed $$\mathrm{Fe_3S_2}$$ would have net charge $$3(+3)+2(-2)=+5$$ with those ions. The Roman numeral gives a charge, not a subscript to copy directly.

</div>

### Organic molecules

Organic chemistry is the study of compounds built around carbon frameworks. Many of the same ideas (**Lewis structures**, **hybridization**, **geometry**) carry over, but carbon compounds also use a parallel naming system (IUPAC names, functional groups, and common names). Those details are not necessary for AP Chemistry, and usually organic molecules will be given to you, or will show up on the list of polyatomic ions.

<div class="theorem-box">

**Example.** Ethanol and dimethyl ether both have formula $$\mathrm{C_2H_6O}$$. Draw their atom connectivity and explain why a molecular formula is insufficient to choose an organic name.

Their connectivities are $$\mathrm{CH_3-CH_2-OH}$$ and $$\mathrm{CH_3-O-CH_3}$$. In the first, oxygen is bonded to carbon and hydrogen; in the second, it joins two carbons. These are constitutional isomers with different functional groups and different names. A molecular formula fixes the atom counts, but the bonds between those atoms must also be specified.

</div>

---

## Drawing two-dimensional structures

**Lewis structures** are schematic: they show valence electrons and bonds in two dimensions even though real molecules are three-dimensional. They are still very useful for drawing bonds, assigning **formal charge**, and spotting **resonance**.

### The octet rule

The **octet rule** says that in many compounds, atoms are most stable when they are surrounded by eight valence electrons (four pairs), matching the noble gas configuration of the noble gas in the same period. Hydrogen and helium are exceptions in the strict sense: hydrogen/helium aim for two electrons (a **duet**), not eight.

**Beryllium and boron** in period 2 can form electron-deficient compounds such as $$\text{BeCl}_2$$ and $$\text{BF}_3$$, with fewer than eight electrons around the central atom. Aluminum, in period 3, can also form electron-deficient compounds. There is no general rule that an atom must end with twice its original valence-electron count.

Heavier main-group elements (the square from *phosphorus* through *astatine* in the $$p$$ block, in the usual textbook treatment) can exhibit **expanded octets**, using $$d$$ orbitals in the hybridization picture to accommodate more than eight valence electrons when they are the central atom in certain compounds.

When drawing, always ask whether the central atom is allowed to expand or must remain octet-complete for the story you are telling.

<div class="theorem-box">

**Example.** Why can $$\mathrm{BF_3}$$ accept an electron pair from $$\mathrm{NH_3}$$ without breaking a B-F bond? Describe the electron counts before and after bonding.

Boron has three bonds and only six surrounding electrons in $$\mathrm{BF_3}$$. Nitrogen's lone pair supplies the new B-N bond, bringing boron to eight surrounding electrons while nitrogen still has an octet. A valid electron-deficient Lewis structure can therefore explain reactivity; forcing an initial octet onto boron would hide the available acceptor site.

</div>

### Formal charge

**Formal charge** is a bookkeeping tool for a single Lewis structure. It assigns each valence electron in the structure either to an atom or to a bond. For an atom,

$$
\text{FC} = (\text{valence } e^- \text{ for the free atom}) - (\text{nonbonding } e^-) - \frac{1}{2}(\text{bonding } e^-)
$$

Structures that minimize formal charge (and place negative formal charge on more electronegative atoms when a choice exists) are generally preferred as major contributors in a resonance hybrid.

<div class="theorem-box">

**Example.** In $$\mathrm{NH_4^+}$$, all N-H bonds are covalent. Why does nitrogen nevertheless have formal charge $$+1$$? Does this mean one identifiable electron was removed from nitrogen after bonding?

Nitrogen is assigned half of the eight bonding electrons and no lone-pair electrons, so its formal charge is $$5-4=+1$$. Formal charge is an equal-sharing bookkeeping convention, not a record of how the species formed or a measurement of the atom's actual partial charge. Ammonium can form when ammonia's lone pair binds a proton; no electron has to be removed in that process.

</div>

### Resonance

**Resonance** occurs when two or more Lewis structures differ only in the placement of $$\pi$$ bonds and lone pairs, not in the arrangement of nuclei. The classic example is **nitrate**, $$\text{NO}_3^-$$: the double bond can be drawn to any of the three oxygen atoms with equal validity. The real ion is a **resonance hybrid**: a single averaged distribution in which N–O bonds are equivalent by symmetry, with *fractional bond order* between single and double.

For resonance to be meaningful, the alternative structures must involve the *same connectivity*; swapping which atoms are bonded (for example, interchanging roles of carbon and nitrogen) is not resonance.

<div class="theorem-box">

**Example.** A student draws two ozone contributors and claims that one O-O bond repeatedly switches from single to double. What observation would contradict a literal switching model?

The two O-O bonds are equivalent in the isolated ozone molecule, with lengths intermediate between typical single and double bonds. The contributors describe one delocalized electron distribution, not distinct structures that the molecule alternates between. Moving electrons on paper changes the representation; it does not imply a time-dependent rearrangement of the real bonds.

</div>

### Constructing Lewis structures

A practical algorithm:

:::strategy

1. Count total **valence electrons** (adjust for charge on **ions**).
2. Choose a **central atom**—usually the least electronegative element that is not hydrogen. For only two atoms, there is no unique “center”; place them adjacent.
3. Connect atoms with **single bonds** first, then distribute remaining electrons as lone pairs to satisfy the **octet rule** (or duet for H) on outer atoms.
4. If the central atom lacks an octet, form **multiple bonds** from outer atoms that can accept higher bond order (often O, N, or C), respecting the octet / expansion rules above.
5. If several arrangements remain, favor the one with **formal charges** closest to zero.
6. Indicate **resonance** with double-headed arrows between structures.
7. Put **brackets** around the compound if it has a charge.

:::

<div class="theorem-box">

**Example.** For $$\mathrm{CO_2}$$, compare O-C-O with two single bonds against O=C=O. Both use 16 valence electrons if lone pairs are included. Decide which is the better structure.

In the single-bond drawing, carbon has only four electrons around it and formal charge $$+2$$, while each oxygen is $$-1$$. Converting one lone pair on each oxygen into a bond gives octets on every atom and zero formal charges. Counting total electrons is necessary, but checking local octets and charges is also necessary.

</div>

---

## VSEPR theory

**Valence-shell electron-pair repulsion (VSEPR)** theory explains **electron-domain geometry** and **molecular shape** by assuming that both bonding pairs and lone pairs around a central atom repel one another. The arrangement that maximizes separation *minimizes repulsion* (thus minimizes the amount of energy needed to hold the molecules) and thus corresponds to observed geometry. A double bond or triple bond counts as one electron domain toward the steric number, just like a single bond or a lone pair.

Typical pairings of steric number and lone pairs give names such as **linear**, **trigonal planar**, **tetrahedral**, **trigonal bipyramidal**, and **octahedral** for the electron-domain geometry; lone pairs then influence the **molecular geometry** (for example, **bent** instead of **trigonal planar** when one lone pair sits on a central atom with three domains).


| Electron domains | Electron geometry | Common molecular shape | Example |
| ---: | --- | --- | --- |
| 2 | linear | linear | $$\mathrm{CO_2}$$ |
| 3 | trigonal planar | trigonal planar / bent | $$\mathrm{BF_3}$$ / $$\mathrm{SO_2}$$ |
| 4 | tetrahedral | tetrahedral / trigonal pyramidal / bent | $$\mathrm{CH_4}$$ / $$\mathrm{NH_3}$$ / $$\mathrm{H_2O}$$ |
| 5 | trigonal bipyramidal | seesaw / T-shaped / linear | $$\mathrm{SF_4}$$ |
| 6 | octahedral | square pyramidal / square planar | $$\mathrm{BrF_5}$$ / $$\mathrm{XeF_4}$$ |

<div class="theorem-box">

**Example.** Both $$\mathrm{CO_2}$$ and $$\mathrm{SO_2}$$ have two atoms attached to a central atom. Explain why one is linear and the other bent.

Carbon in $$\mathrm{CO_2}$$ has two electron domains and no lone pair; its bonds point in opposite directions. Sulfur in $$\mathrm{SO_2}$$ has two bonding domains and one lone-pair domain. Three domains give a trigonal planar electron arrangement, but only the atoms define the bent molecular shape.

</div>

---

## Hybridization

Atomic orbitals on a bonded atom can mix to form **hybrid orbitals** that are consistent with VESPR. For carbon in many organic molecules, four **sigma** frameworks point toward the corners of a tetrahedron, described by $$\text{sp}^3$$ **hybridization**. $$\text{sp}^2$$ hybrids lie in a plane at $$120^\circ$$ (trigonal planar arrangement); $$\text{sp}$$ hybrids are linear at $$180^\circ$$. In addition, $$\text{sp}^3 d$$ hybridization occurs in trigonal bipyramidal configurations, while $$\text{sp}^3 d^2$$ hybridization occurs in an octahedral configuration.


| Steric number | Hybridization | Ideal geometry | Approx. angle |
| ---: | --- | --- | ---: |
| 2 | $$sp$$ | linear | $$180^\circ$$ |
| 3 | $$sp^2$$ | trigonal planar | $$120^\circ$$ |
| 4 | $$sp^3$$ | tetrahedral | $$109.5^\circ$$ |
| 5 | $$sp^3d$$ | trigonal bipyramidal | $$90^\circ,120^\circ$$ |
| 6 | $$sp^3d^2$$ | octahedral | $$90^\circ$$ |

<div class="theorem-box">

**Example.** In $$\mathrm{CH_3CHO}$$, must both carbon atoms have the same hybridization because they are in the same molecule? Determine each in the localized bonding model.

The methyl carbon has four sigma-bond directions, giving $$sp^3$$. The carbonyl carbon has three sigma-bond directions, giving $$sp^2$$; its remaining unhybridized p orbital contributes to the C=O pi bond. Hybridization is assigned locally, not once for the entire molecule.

</div>

---

## Sigma bonds, pi bonds, and bond order

A **sigma bond** ($$\sigma$$) has electron density concentrated along the *internuclear axis*; it arises from head-on overlap of hybrid or atomic orbitals. A **pi bond** ($$\pi$$) forms from *side-by-side* overlap of unhybridized $$p$$ orbitals above and below the sigma framework. A single bond is one $$\sigma$$; a double bond is one $$\sigma$$ plus one $$\pi$$; a triple bond is one $$\sigma$$ plus two $$\pi$$.

**Bond order** is half the difference between bonding and antibonding electrons in **molecular orbital** theory, but in Lewis terms it is simply the average number of bonding electron pairs between two atoms across resonance structures. **Bond length** decreases and **bond strength** increases as bond order increases between the same two elements.

<div class="theorem-box">

**Example.** Count sigma and pi bonds in $$\mathrm{HC\equiv C-CH=CH_2}$$ and explain why counting bond lines alone can mislead.

There are four C-H sigma bonds and three C-C sigma bonds, for seven sigma bonds. The triple bond supplies two pi bonds and the double bond supplies one, for three pi bonds. Every connected pair of atoms has one sigma bond; the additional lines in multiple bonds represent pi bonding.

</div>

---

## Potential energy and bond formation

When two atoms approach, the **potential energy** of the system typically drops as attractive interactions dominate, passes through a minimum at an **equilibrium bond length**, and then rises steeply as **nuclear repulsion** dominates at short distance.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[axis lines=left, width=9cm, height=5.5cm, xmin=0.6, xmax=5.5, ymin=-3, ymax=3, xlabel={internuclear distance}, ylabel={potential energy}, xtick=\empty, ytick=\empty]
\addplot[blue, very thick, samples=200, domain=0.75:5.5] {2/(x^8)-4/(x^4)};
\addplot[dashed] coordinates {(1.19,-3) (1.19,0)};
\node[anchor=north] at (axis cs:1.19,-2.7) {bond length};
\node[anchor=west] at (axis cs:2.0,-1.0) {stable bond};
\node[anchor=west] at (axis cs:0.8,2.1) {repulsion};
\end{axis}
\end{tikzpicture}
```

**Bond energy** is related to the depth of that well. Comparing curves for the same bond order (single vs double vs triple) illustrates why higher **bond order** correlates with shorter, stronger bonds.

These same curves also motivate [reaction coordinates](/notes/ap/chem/kinetics/) later: along a reaction path, the system moves on a **potential energy surface** connecting reactants, transition states, and products.

<div class="theorem-box">

**Example.** Bond X has a deeper potential-energy minimum than bond Y, but its minimum occurs at a larger separation. Which bond is stronger, and which is shorter?

X requires more energy to dissociate from its minimum to separated atoms, so it is stronger. Y has the smaller equilibrium separation, so it is shorter. Well depth measures dissociation energy and the horizontal position measures bond length; neither can be inferred solely from the other for different atom pairs.

</div>

---

## The Born–Haber cycle

:::variables
- $$U_{lattice}$$ = Lattice Energy
- $$\Delta U$$ = Change in Potential Energy
- $$\Delta H$$ = Change in Enthalpy
- $$\Delta H_{\text{ea}}$$ = Enthalpy of Electron Gain
- $$IE$$ = Ionization Energy
- $$D_{A-B}$$ = Bond Enthalpy between A and B
:::

The **Born–Haber cycle** is a **Hess’s law** (See more in [Unit 6](/notes/ap/chem/thermochemistry/)) construction for an **ionic solid**. It expresses the standard enthalpy of formation $$\Delta H_f^\circ$$ of the compound from its **elements in standard states** as a sum of steps that convert those elements into **gas-phase ions** and then let those ions **crystallize**. Any one unknown step (most often **lattice energy**) can be found if the others are known.

Take a 1:1 alkali halide $$\text{MX}$$, formed from $$\text{M}(s)$$ and $$\tfrac{1}{2}\text{X}_2(g)$$. Imagine the path:

1. **Atomize the metal** (sublimation): $$\text{M}(s) \rightarrow \text{M}(g)$$ with $$\Delta H = \Delta H_{\text{sub}}$$ (usually endothermic).

2. **Ionize the metal**: $$\text{M}(g) \rightarrow \text{M}^+(g) + e^-$$ with $$\Delta H = \text{IE}$$ (endothermic; use the correct successive ionization energies if more than one electron is lost).

3. **Atomize the halogen**: $$\tfrac{1}{2}\text{X}_2(g) \rightarrow \text{X}(g)$$ with $$\Delta H = \tfrac{1}{2}D_{\text{X–X}}$$ (endothermic; half the $$\text{X–X}$$ bond enthalpy).

4. **Attach an electron to the halogen**: $$\text{X}(g) + e^- \rightarrow \text{X}^-(g)$$ with $$\Delta H = \Delta H_{\text{ea}}$$. For halogens this step is exothermic, so $$\Delta H_{\text{ea}}$$ is negative when reported as an enthalpy change. (If a table lists **electron affinity** with a different sign convention, convert it to $$\Delta H$$ for this step before you add.)

5. **Form the crystal from gas ions**: $$\text{M}^+(g) + \text{X}^-(g) \rightarrow \text{MX}(s)$$. This step is strongly exothermic. Textbooks often define **lattice energy** $$U_{\text{lattice}}$$ as a positive number equal to the endothermic enthalpy of the **reverse** process: one mole of solid separated into isolated gaseous ions:

$$
\text{MX}(s) \rightarrow \text{M}^+(g) + \text{X}^-(g) \qquad \Delta H = +U_{\text{lattice}}
$$

Then step 5 (lattice formation from ions) has $$\Delta H = -U_{\text{lattice}}$$.

Because the overall enthalpy change from $$\text{M}(s) + \tfrac{1}{2}\text{X}_2(g)$$ to $$\text{MX}(s)$$ is $$\Delta H_f^\circ$$,

$$
\Delta H_f^\circ(\text{MX},\,s) = \Delta H_{\text{sub}} + \text{IE} + \frac{1}{2}D_{\text{X–X}} + \Delta H_{\text{ea}} - U_{\text{lattice}}.
$$

Rearranging isolates the lattice term:

$$
U_{\text{lattice}} = \Delta H_{\text{sub}} + \text{IE} + \frac{1}{2}D_{\text{X–X}} + \Delta H_{\text{ea}} - \Delta H_f^\circ.
$$

For salts with other stoichiometries (e.g. $$\text{MgCl}_2$$, $$\text{Na}_2\text{O}$$), use the correct multiple of atomization, all required ionization steps, the appropriate nonmetal atomization (e.g. $$\tfrac{1}{2}\text{O}_2$$), and electron-gain steps that match the anion charge (second-electron addition to oxygen is very endothermic; the huge lattice energy of oxides is what makes the overall formation from elements favorable). The cycle is still closed: the sum of steps along one route equals the sum along any other route between the same two **thermodynamic states**.

Qualitatively, larger ion charges and smaller ions (shorter internuclear distances in the lattice) increase $$U_{\text{lattice}}$$, consistent with Coulomb attraction in the lattice and with the trends introduced earlier in this unit. The diagram below shows the energy changes in the cycle.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing,angles,quotes}
\begin{tikzpicture}[>=Stealth, font=\small]
\draw[->] (0,0) -- (0,5.2) node[above] {enthalpy};
\draw[thick] (1,0.6) -- (4,0.6) node[right] {ionic solid};
\draw[thick] (1,4.5) -- (4,4.5) node[right] {separated gaseous ions};
\draw[thick] (1,2.0) -- (4,2.0) node[right] {atoms};
\draw[thick] (1,3.2) -- (4,3.2) node[right] {ions forming};
\draw[->, blue, thick] (0.8,0.6) -- (0.8,2.0) node[midway,left] {sublimation / bond};
\draw[->, blue, thick] (0.8,2.0) -- (0.8,3.2) node[midway,left] {ionization};
\draw[->, blue, thick] (0.8,3.2) -- (0.8,4.5) node[midway,left] {electron affinity};
\draw[->, red, thick] (4.5,4.5) -- (4.5,0.6) node[midway,right] {lattice energy};
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** For a hypothetical MX salt, sublimation, ionization, half the bond dissociation, and electron gain contribute $$100$$, $$500$$, $$120$$, and $$-350\ \mathrm{kJ/mol}$$. If formation is $$-400\ \mathrm{kJ/mol}$$, find the lattice separation energy and explain its sign.

The cycle is $$-400=100+500+120-350-U$$, so $$U=770\ \mathrm{kJ/mol}$$. This is positive for separating the crystal into gas ions. The lattice-formation step is instead $$-770\ \mathrm{kJ/mol}$$; using the positive separation value as a formation term would reverse the physical process.

</div>

---


## Practice

### MCQ

::::problem
1. Which pair has the same electron-domain geometry but different molecular geometries?

   (A) $$\mathrm{CO_2}$$ and $$\mathrm{BF_3}$$<br>
   (B) $$\mathrm{CH_4}$$ and $$\mathrm{NH_3}$$<br>
   (C) $$\mathrm{BF_3}$$ and $$\mathrm{NH_3}$$<br>
   (D) $$\mathrm{CO_2}$$ and $$\mathrm{H_2O}$$

:::solution
Both methane and ammonia have four electron domains, giving tetrahedral electron-domain geometry. Ammonia has one lone pair, so its molecular geometry is trigonal pyramidal; methane's is tetrahedral.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
2. In a simple ionic model, salt X contains $$+1,-1$$ ions at separation r, while salt Y contains $$+2,-2$$ ions at separation $$2r$$. Compare pair-attraction energy magnitudes.

   (A) Y is half of X<br>
   (B) They are equal<br>
   (C) Y is twice X<br>
   (D) Y is four times X

:::solution
Coulomb potential-energy magnitude scales as the charge product divided by separation: $$\lvert U_Y\rvert/\lvert U_X\rvert=4/2=2$$. Using an inverse-square distance would confuse potential energy with force.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
3. An octet-obeying Lewis structure of $$\mathrm{NO_2^-}$$ contains one N=O bond and one N-O bond. Which formal-charge assignment is correct?

   (A) N is 0, double-bond O is 0, single-bond O is -1<br>
   (B) N is +1 and each O is -1<br>
   (C) N is -1 and both O are 0<br>
   (D) Every atom has zero formal charge

:::solution
Nitrogen has one lone pair and three shared pairs, so $$FC_N=5-2-3=0$$. The single-bond oxygen has three lone pairs, giving $$6-6-1=-1$$; the double-bond oxygen is neutral. Charges sum to the ion's -1 charge.

$$
\boxed{\text{A}}.
$$
:::
::::

::::problem
4. Which observation supports resonance in carbonate rather than one fixed C=O bond?

   (A) Carbonate has a net charge<br>
   (B) Oxygen is more electronegative than carbon<br>
   (C) Carbon has no lone pair<br>
   (D) All three C-O bond lengths are equal and intermediate between typical single and double bonds

:::solution
Equivalent intermediate bond lengths support delocalized bonding. A fixed single double bond would distinguish one shorter bond from two longer bonds. Charge and electronegativity alone do not establish resonance.

$$
\boxed{\text{D}}.
$$
:::
::::

::::problem
5. In ethene, $$\mathrm{H_2C=CH_2}$$, rotation around the C-C axis is restricted primarily because rotation would disrupt which interaction?

   (A) Overlap of the carbon 1s orbitals<br>
   (B) Side-by-side overlap of the unhybridized p orbitals<br>
   (C) Every C-H sigma bond<br>
   (D) The attraction between separate ethene molecules

:::solution
Each carbon is approximately sp2, leaving a p orbital for the pi bond. Twisting the groups out of alignment weakens that side-by-side overlap. The restriction is intramolecular and cannot be explained by attractions between separate molecules.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
6. For a hypothetical salt, gas-ion formation from the elements costs $$+450\ \mathrm{kJ/mol}$$ overall and crystal formation from those ions releases $$800\ \mathrm{kJ/mol}$$. What is the standard formation enthalpy of the solid?

   (A) $$+1250\ \mathrm{kJ/mol}$$<br>
   (B) $$+350\ \mathrm{kJ/mol}$$<br>
   (C) $$-350\ \mathrm{kJ/mol}$$<br>
   (D) $$-800\ \mathrm{kJ/mol}$$

:::solution
Hess's law gives $$450-800=-350\ \mathrm{kJ/mol}$$. The lattice step alone is not the full formation enthalpy because creating the gas ions first requires energy.

$$
\boxed{\text{C}}.
$$
:::
::::

### FRQ

::::frq{id=chem-compounds-1}
7. Consider the molecules $$\text{CH}_2\text{O}$$ and $$\text{CH}_3\text{OH}$$.

   $$(A)$$ Draw a reasonable Lewis structure for each molecule.

   $$(B)$$ Identify the hybridization of the carbon atom in each molecule.

   $$(C)$$ Explain which molecule can form stronger intermolecular attractions with water.

   $$(D)$$ **Original extension.** Count the sigma and pi bonds in each molecule. Explain why rotation around the carbon-oxygen bond is more restricted in formaldehyde than in methanol.

:::solution
$$(A)$$ In $$\text{CH}_2\text{O}$$, carbon is bonded to two H atoms and double-bonded to O. In $$\text{CH}_3\text{OH}$$, carbon is bonded to three H atoms and single-bonded to O, while O is bonded to H and has two lone pairs.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing,angles,quotes}
\begin{tikzpicture}[>=Stealth, font=\small]
\node at (-2.8,0) {$\mathrm{H_2C=O}$};
\draw (-3.55,-0.25) -- (-3.15,-0.25); \draw (-3.55,0.25) -- (-3.15,0.25);
\node at (-3.9,0) {H}; \node at (-2.1,0) {O};
\node at (2.0,0.45) {$\mathrm{CH_3OH}$};
\draw (1.45,0.2) -- (2.45,0.2); \node at (1.2,0.2) {C}; \node at (2.7,0.2) {O-H};
\node[align=center] at (0,-1.0) {Lewis structures show bonding pairs and lone pairs};
\end{tikzpicture}
```

$$(B)$$ The carbon in $$\text{CH}_2\text{O}$$ has three electron domains, so it is

$$
\boxed{sp^2}.
$$

The carbon in $$\text{CH}_3\text{OH}$$ has four electron domains, so it is

$$
\boxed{sp^3}.
$$

$$(C)$$ $$\text{CH}_3\text{OH}$$ forms stronger attractions with water because it can both donate and accept hydrogen bonds through its $$\text{O-H}$$ group. The O atom has lone pairs that can accept hydrogen bonds, and the H attached to O can be donated into a hydrogen bond with water. $$\text{CH}_2\text{O}$$ can accept hydrogen bonds at oxygen, but it cannot donate hydrogen bonds because its H atoms are bonded to carbon, not to a highly electronegative atom. This gives methanol stronger overall interactions with water.

$$(D)$$ Formaldehyde has three sigma bonds (two C-H and one C-O) and one pi bond. Methanol has five sigma bonds (three C-H, one C-O, and one O-H) and no pi bonds. Rotating about the C=O axis would destroy the parallel p-orbital overlap that forms the pi bond. Rotation about methanol's C-O single bond does not require breaking a pi bond, although different conformations can have different energies.
:::
::::

::::frq{id=chem-compounds-2}
8. The 2026 AP Chemistry exam asked students about chromate resonance and VSEPR geometry. (Adapted from College Board, [2026 AP Chemistry FRQ 2](https://apcentral.collegeboard.org/media/pdf/ap26-frq-chemistry.pdf).)

   $$(A)$$ Predict the molecular geometry around chromium in $$\text{CrO}_4^{2-}$$.

   $$(B)$$ Explain why multiple resonance structures can be drawn for $$\text{CrO}_4^{2-}$$.

   $$(C)$$ Explain why the four Cr-O bonds are expected to be equivalent in the resonance hybrid.

   $$(D)$$ **Original extension.** Compare formal charges in a chromate structure with four single Cr-O bonds and one with two double and two single Cr-O bonds. Explain why choosing one resonance contributor does not establish two permanently different types of Cr-O bond.

:::solution
$$(A)$$ The chromium has four bonding regions around it, so the electron-domain geometry and molecular geometry are both

$$
\boxed{\text{tetrahedral}}.
$$

$$(B)$$ The double-bond character can be placed between chromium and different oxygen atoms while keeping the same atom connectivity and total number of valence electrons. These drawings differ only in electron placement, not in which atoms are bonded to which, so they are resonance structures rather than different compounds.

$$(C)$$ The resonance hybrid averages the valid resonance structures. Since no single resonance structure fully describes the ion, the Cr-O bonds have the same average bond order and are equivalent. A good particle-level explanation is that the extra electron density is delocalized over the Cr-O bonding framework rather than locked into one permanent double bond.

$$(D)$$ With four single bonds, chromium has formal charge $$6-4=+2$$ and each oxygen has $$6-(6+1)=-1$$, giving total charge $$-2$$. With two double bonds, chromium has formal charge $$6-6=0$$; each double-bonded oxygen is neutral and each single-bonded oxygen is $$-1$$. The latter reduces formal-charge separation, but its double bonds can be placed on different oxygens. The real ion has delocalized bonding, not bonds that switch between drawings, so no one contributor selects permanently shorter bonds.
:::
::::
