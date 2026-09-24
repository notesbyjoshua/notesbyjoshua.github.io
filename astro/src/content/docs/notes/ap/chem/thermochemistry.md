---
title: "Unit 6: Thermochemistry"
description: "AP Chemistry notes on thermochemistry, enthalpy, calorimetry, Hess's law, bond energies, and energy diagrams."
sidebar:
  order: 6
---

## System, surroundings, and boundaries

In modeling, the universe is split into the **system** (what you study) and the **surroundings** (everything else that can exchange energy with the system). A **closed system** exchanges energy but not matter across its boundary. An **open system** can exchange both (an open beaker). An **isolated system** exchanges neither, and this can be approximated by good calorimeter insulation.

<div class="theorem-box">

**Example.** A dissolving salt makes its beaker feel cold. Taking dissolution as the system, assign the heat signs and explain the observation.

The system absorbs heat, so $$q_{sys}>0$$. The nearby solution, beaker, and hand supply that energy, so their heat change is negative. Feeling cold reports heat leaving your hand; it does not mean the dissolving system released 'cold energy.'

</div>

---

## Energy, heat, and work

### Heat and Calorimetry

Energy is the capacity to do work or transfer heat. The total energy of an isolated universe is conserved (First Law of Thermodynamics); it is not useful to set “$$E_{\text{universe}} = 0$$” unless you have chosen a specific reference for potential energy.

**Heat** $$q$$ is energy transferred because of a temperature difference. On the AP exam the usual sign convention is from the system’s perspective: $$q_{\text{sys}} > 0$$ when heat flows into the system, $$q_{\text{sys}} < 0$$ when heat flows out. Spontaneous heat transfer between two objects in thermal contact goes from hotter to colder until thermal equilibrium (related 0th Law of Thermodynamics).

For a pure substance with nearly constant **specific heat capacity** $$c$$,

$$
q = mc\Delta T,
$$

where $$m$$ is mass and $$\Delta T$$ is temperature change. For water near room temperature, $$c \approx 4.18 \text{ J/(g}\cdot^\circ\text{C)}$$ (often $$4.184$$ in tables). A coffee-cup calorimeter at constant pressure approximates $$q_{\text{reaction}} \approx -\left(m_{\text{solution}}c_{\text{solution}}\Delta T + C_{\text{cal}}\Delta T\right)$$ for the reaction inside, where $$C_{\text{cal}}$$ is the **calorimeter constant** (energy per kelvin for the apparatus), which is like a calibration/error term because calorimeters aren't perfect insulators. Matching system and surroundings gives

$$
q_{\text{sys}} = -q_{\text{surr}}
$$

when no other work or losses matter (Conservation of energy/matter).

The central move in any calorimetry problem is this sign relationship: the heat lost by one part of the setup equals the heat gained by the other. In a coffee-cup calorimeter, the reaction is the **system** and the solution is the **surroundings**, so $$q_{\text{rxn}}=-q_{\text{solution}}$$. If the solution warms up, $$q_{\text{solution}}>0$$, which forces $$q_{\text{rxn}}<0$$—an exothermic reaction.

<div class="theorem-box">

**Example.** The same heat warms $$50.0\ \mathrm{g}$$ of water in one trial and $$100.0\ \mathrm{g}$$ in another, starting at the same temperature. Does the larger sample reach a higher final temperature because it absorbs more total energy?

It does not absorb more energy under the stated conditions: the heat supplied is the same. Since $$\Delta T=q/(mc)$$, doubling the water mass halves the temperature increase. Temperature change measures energy per heat capacity, not total energy by itself. This assumes negligible heat loss and the same specific heat in both trials.

</div>

### Two kinds of calorimeter

- A **coffee-cup (constant-pressure) calorimeter** is open to the atmosphere, so the heat it measures is $$q_p=\Delta H$$ directly. This is the standard AP setup for solution reactions, dissolving, and neutralization.
- A **bomb (constant-volume) calorimeter** seals the reaction in a rigid steel vessel, usually to burn a sample in excess oxygen. Because $$\Delta V=0$$, no $$PV$$ work is done and the measured heat is $$q_v=\Delta U$$, the internal-energy change, rather than $$\Delta H$$. Bomb calorimeters are the tool of choice for combustion and food-energy measurements.

In both, the apparatus itself absorbs some heat, accounted for by the **calorimeter constant** $$C_{\text{cal}}$$ (energy per kelvin), determined by a calibration run.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing,angles,quotes}
\begin{tikzpicture}[>=Stealth, font=\small]
\draw[rounded corners] (-4,-1.5) rectangle (-1,1.5); \draw (-3.6,1.1)--(-1.4,1.1); \draw[->] (-2.5,2) -- (-2.5,0.2); \node at (-2.5,2.25) {thermometer}; \node[align=center] at (-2.5,-2) {coffee-cup\\constant pressure\\measures $\Delta H$};
\draw[rounded corners] (1,-1.5) rectangle (4,1.5); \draw[fill=gray!20] (2.1,-0.7) rectangle (2.9,0.7); \draw (1.4,1.1)--(3.6,1.1); \node[align=center] at (2.5,-2) {bomb calorimeter\\constant volume\\measures $\Delta U$};
\node at (2.5,0) {bomb};
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** A combustion releases energy in a rigid sealed bomb calorimeter. Why is the measured reaction heat not automatically $$\Delta H$$, even if heat loss is negligible?

A rigid container does no pressure-volume work, so its constant-volume reaction heat is $$q_v=\Delta U$$, assuming no other work. Enthalpy includes the $$PV$$ term. For ideal gases at a common temperature, $$\Delta H=\Delta U+\Delta n_gRT$$. Negligible heat loss improves the heat measurement but does not change which state-function change the apparatus measures.

</div>

---

### Work and Potential Energy

Work in gas problems often means pressure–volume work (e.g. expansion of a piston). For expansion against constant external pressure,

$$
W = -P_{\text{ext}}\Delta V
$$

for work done on the system (AP-style). **Internal energy** change obeys the **First Law of Thermodynamics**:

$$
\Delta U = q + W.
$$

At constant volume (isochoric processes), $$\Delta V = 0$$ so $$W = 0$$ and $$\Delta U = q$$.

<div class="theorem-box">

**Example.** A gas absorbs $$100\ \mathrm{J}$$ of heat while expanding against its surroundings and doing $$150\ \mathrm{J}$$ of work. Can its internal energy decrease despite being heated?

Yes. With the chemistry sign convention, $$q=+100\ \mathrm{J}$$ and $$w=-150\ \mathrm{J}$$. Thus $$\Delta U=q+w=-50\ \mathrm{J}$$. More energy leaves through work than enters through heat. Heating describes one transfer mechanism, not the net change in stored energy.

</div>

---

### Phase changes and heating curves

During melting or boiling at fixed pressure, temperature stays constant while latent heat is absorbed or released:

$$
q = n\Delta H_{\text{fus}}, \qquad q = n\Delta H_{\text{vap}},
$$

with molar enthalpies of fusion and vaporization. A heating curve (temperature vs heat added) shows slopes $$1/(mc)$$ and plateaus at phase changes.

A full heating curve alternates between **sloped segments** and **flat plateaus**:

- On a **sloped segment**, a single phase is being warmed, temperature rises, and you use $$q=mc\Delta T$$ with the specific heat *of that phase* (ice, liquid water, and steam all have different $$c$$ values, which is why the slopes differ).
- On a **plateau**, two phases coexist and temperature is constant while a phase change happens. All the added energy goes into overcoming intermolecular forces (raising potential energy, not kinetic energy), so you use $$q=n\Delta H_{\text{fus}}$$ or $$q=n\Delta H_{\text{vap}}$$.

The vaporization plateau is longer than the fusion plateau for most substances because $$\Delta H_{\text{vap}}>\Delta H_{\text{fus}}$$—separating molecules completely into a gas costs more energy than just loosening them from a fixed lattice into a liquid. To find the total energy to take a substance across several phase regions, add the $$q$$ for every segment and plateau in sequence.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[axis lines=left,width=9cm,height=5.5cm,xmin=0,xmax=10,ymin=-30,ymax=130,xlabel={heat added},ylabel={temperature},xtick=\empty,ytick={0,100},grid=both,grid style={gray!15}]
\addplot[blue,very thick] coordinates {(0,-20) (2,0) (4,0) (6,100) (8,100) (10,125)};
\node at (axis cs:1,-12) {$mc\Delta T$}; \node at (axis cs:3,8) {melting}; \node at (axis cs:5,55) {$mc\Delta T$}; \node at (axis cs:7,108) {boiling};
\end{axis}
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** A $$10.0\ \mathrm{g}$$ sample of ice at $$0^\circ\mathrm{C}$$ absorbs $$4.00\ \mathrm{kJ}$$ at one atmosphere. Use $$\Delta H_{fus}=334\ \mathrm{J/g}$$ and $$c_{water}=4.18\ \mathrm{J/(g\,K)}$$ to find its final state and temperature. Why can't all the heat be used in $$q=mc\Delta T$$?

Melting requires $$10.0(334)=3340\ \mathrm{J}$$, leaving $$660\ \mathrm{J}$$ to warm the liquid. Thus $$\Delta T=660/(10.0\times4.18)=15.8\ \mathrm{K}$$, so the final sample is liquid water near $$15.8^\circ\mathrm{C}$$. The latent heat changes phase without raising temperature; applying the liquid specific heat to all $$4000\ \mathrm{J}$$ would ignore the melting step.

</div>

---

## Enthalpy

**Enthalpy** $$H$$ is defined as $$H = U + PV$$. It is a state function. For a process at constant pressure the change in enthalpy becomes:

$$
\Delta H = \Delta U + P\Delta V.
$$

However, you will usually see enthalpy in the context of heat for AP Chemistry problems, so

$$
\Delta H_{\text{rxn}} = \frac{q_{\text{sys}}}{n}.
$$

where $$n$$ is the number of moles, and enthalpy is from the perspective of the system. At constant pressure, $$\Delta H = q_p$$ for the system, so it has the same sign as $$q_{\text{sys}}$$. It has the opposite sign of the heat change measured for the surroundings in a coffee-cup calorimeter:

$$
q_{\text{rxn}} = q_{\text{sys}} = -q_{\text{surr}}.
$$

### Exothermic versus endothermic

In an **exothermic** reaction, the system evolves so that heat flows out to the surroundings: $$\Delta H < 0$$, $$q_{\text{sys}} < 0$$, and $$q_{\text{surr}} > 0$$.

In an **endothermic** reaction, the system draws heat in: $$\Delta H > 0$$, $$q_{\text{sys}} > 0$$, and $$q_{\text{surr}} < 0$$.

Always label whether $$q$$ refers to system or surroundings when you compare signs across textbooks.

<div class="theorem-box">

**Example.** Dissolving a salt makes the solution colder. Is the dissolution exothermic because the thermometer loses energy? Identify the system needed to avoid this conclusion.

Treat dissolution as the process whose enthalpy is being determined and the solution's thermal energy as the source of transferred heat. The solution cools because the dissolving process absorbs energy; the dissolution is endothermic. A negative measured temperature change gives negative heat for the cooling solution, so the inferred heat of dissolution has the opposite sign when other heat transfers are negligible.

</div>

### State functions and path

Enthalpy is a state function. **State functions** depend only on initial and final states, not the path: $$P$$, $$V$$, $$T$$, $$U$$, $$H$$, and (later) **entropy** $$S$$ and **Gibbs free energy** $$G$$. Heat $$q$$ and work $$W$$ are path-dependent; their sum $$\Delta U = q + W$$ is not.

<div class="theorem-box">

**Example.** Two routes turn the same amounts of reactants into the same products at the same temperature and pressure. One has three steps and the other one step. Can their net enthalpy changes differ?

No. Enthalpy is a state function, so only the specified initial and final states determine the net change. Individual steps may release and absorb different amounts, but their sum must agree. Different products, phases, or final temperatures would instead describe different final states.

</div>

---

## Standard enthalpies and formation

**Standard state** means specified reference conditions (For AP: $$1$$ atm for gases, $$1\text{ M}$$ for solutes in solution chemistry, pure substances in their stable form at $$25^\circ\text{C}$$ unless noted). The **standard enthalpy of formation** $$\Delta H_f^\circ$$ is $$\Delta H$$ for forming one mole of a compound from its elements in their standard states. Elements in their reference/naturally occuring forms have $$\Delta H_f^\circ = 0$$ by definition.

For any reaction,

$$
\Delta H_{\text{rxn}}^\circ = \sum \nu\,\Delta H_f^\circ(\text{products}) - \sum \nu\,\Delta H_f^\circ(\text{reactants}),
$$

where $$\nu$$ are stoichiometric coefficients. Thermochemical equations can be scaled; $$\Delta H$$ scales with the mole amounts written in the equation.

<div class="theorem-box">

**Example.** A table lists zero formation enthalpy for oxygen gas. Does this imply that breaking its O=O bond requires no energy? Explain.

Zero is the reference for the element in its standard state, not the energy of a bond. Making oxygen gas from standard-state oxygen is no change, whereas $$\mathrm{O_2(g)\rightarrow2O(g)}$$ breaks a bond and requires energy. Atomic oxygen is not the standard reference state.

</div>

---

## Hess’s law

**Hess’s law** states that $$\Delta H$$ for an overall process is the sum of $$\Delta H$$ values for steps that add up to the same net reaction—because $$H$$ is a state function. Reverse a step → flip the sign of $$\Delta H$$. Multiply a step by a factor → multiply $$\Delta H$$ by the same factor.

Because $$H$$ is a state function, the enthalpy change depends only on the initial and final states, not on the route taken. That means you can build any target reaction out of known steps and the enthalpies add—just like the legs of a trip add to the same net displacement no matter which path you walk.

A reliable strategy for combining given equations:

:::strategy
1. Identify a species that appears in only **one** of the given equations and in the **target**; orient (and if needed, flip) that equation so the species lands on the correct side.
2. **Scale** each equation so its coefficients match the target, multiplying its $$\Delta H$$ by the same factor.
3. **Add** the manipulated equations; intermediates that appear on opposite sides should cancel, leaving the target equation.
4. **Sum** the manipulated $$\Delta H$$ values to get $$\Delta H_{\text{target}}$$.
:::

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing,angles,quotes}
\begin{tikzpicture}[>=Stealth, font=\small]
\draw[->] (0,0) -- (0,4.6) node[above] {enthalpy};
\draw[thick] (1,3.8) -- (3.5,3.8) node[right] {reactants};
\draw[thick] (1,2.2) -- (3.5,2.2) node[right] {intermediate};
\draw[thick] (1,0.8) -- (3.5,0.8) node[right] {products};
\draw[->, blue, thick] (1.2,3.7) -- (1.2,0.9) node[midway,left] {overall $\Delta H$};
\draw[->, red, thick] (2.5,3.7) -- (2.5,2.3) node[midway,right] {step 1};
\draw[->, red, thick] (2.8,2.1) -- (2.8,0.9) node[midway,right] {step 2};
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** Given $$A\rightarrow B$$ with $$\Delta H=+30\ \mathrm{kJ}$$ and $$A\rightarrow C$$ with $$\Delta H=-50\ \mathrm{kJ}$$, find the enthalpy for $$2B\rightarrow2C$$.

Reverse the first step to get $$B\rightarrow A$$ at $$-30\ \mathrm{kJ}$$. Add $$A\rightarrow C$$ to get $$B\rightarrow C$$ at $$-80\ \mathrm{kJ}$$. Doubling gives $$-160\ \mathrm{kJ}$$. Reversing the arrow changes the sign; scaling the equation scales the energy.

</div>

---

## Bond enthalpies (estimates)

**Bond enthalpy** (or bond energy) is the energy required to break one mole of a bond in the gas phase (averaged over similar molecules for tabulated values). For gas-phase estimates,

$$
\Delta H_{\text{rxn}} \approx \sum D(\text{bonds broken}) - \sum D(\text{bonds formed}),
$$

using positive bond energies for each bond listed. This ignores liquids, solvents, and exact environments, so it is less accurate than calorimetry or formation cycles.

The conceptual core is a sign rule: **breaking bonds always absorbs energy** (endothermic) and **forming bonds always releases energy** (exothermic). A reaction is exothermic overall when the bonds formed in the products are collectively stronger (release more) than the bonds broken in the reactants. The formula above is just that comparison written out—broken minus formed. Note that this method only works when **every** species is in the gas phase, since tabulated bond energies assume isolated gas-phase molecules with no intermolecular forces to account for.

Bond strength also tracks bond order and length: in general a triple bond is stronger (and shorter) than a double bond, which is stronger than a single bond between the same atoms, so multiply-bonded molecules such as $$\text{N}_2$$ are very stable and costly to break.

<div class="theorem-box">

**Example.** A bond-energy estimate predicts $$-100\ \mathrm{kJ/mol}$$ for making a gaseous product. The measured value for making its liquid is more negative. Explain whether this necessarily invalidates the estimate.

Bond enthalpies estimate gas-phase bond changes. Condensation then releases additional energy through intermolecular interactions, making liquid formation more exothermic. Compare the same physical states before blaming the bond-energy model; average bond energies also introduce approximation error.

</div>

---

## Solution formation (preview)

$$\Delta H_{\text{solution}}$$ combines lattice (endothermic breakup of solid) and hydration (exothermic ion–solvent interaction) terms. A slightly endothermic $$\Delta H_{\text{solution}}$$ can still occur if entropy favors mixing (full explanation in later units). A very endothermic process may give negligible solubility unless entropy dominates strongly.

Both of those terms ultimately trace back to **Coulomb's law**: the energy of an ionic interaction scales with the product of the charges over the distance between centers,

$$
E \propto \frac{q_1 q_2}{r}.
$$

This means **lattice energy** (and therefore how much energy it costs to pull the crystal apart) is largest for ions with **high charges** and **small radii**—for example, $$\text{MgO}$$ has a far larger lattice energy than $$\text{NaCl}$$ because both ions carry a $$\pm2$$ charge and are compact. The same Coulombic reasoning explains why those small, highly charged ions also release a lot of energy on hydration. Whether dissolving is net exothermic or endothermic depends on which of the two large opposing terms wins.

Dissolving as a three-step thermodynamic cycle:

1. Separate the solute particles (break the lattice) — endothermic, $$+\Delta H_{\text{lattice}}$$.
2. Separate the solvent particles to make room — endothermic.
3. Let solute and solvent particles attract one another (hydration/solvation) — exothermic.

<div class="theorem-box">

**Example.** Lattice separation costs $$+700\ \mathrm{kJ/mol}$$ and hydration releases $$-680\ \mathrm{kJ/mol}$$. Find the dissolution enthalpy and decide whether its sign alone proves insolubility.

Adding the steps gives $$\Delta H_{soln}=+20\ \mathrm{kJ/mol}$$. Dissolution absorbs heat, but spontaneity also depends on entropy through $$\Delta G=\Delta H-T\Delta S$$. An endothermic dissolution can occur when the entropy contribution is sufficiently favorable.

</div>

---

## Vapor pressure and the Clausius–Clapeyron relation

The **Clausius–Clapeyron** equation relates vapor pressure to temperature for a liquid (using molar enthalpy of vaporization $$\Delta H_{\text{vap}}$$ as approximately constant over a modest range):

$$
\ln\left(\frac{P_2}{P_1}\right) = -\frac{\Delta H_{\text{vap}}}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right).
$$

Higher $$T$$ increases vapor pressure; stronger IMFs tend to lower vapor pressure at a given $$T$$ (see [Unit 3](/notes/ap/chem/submix/)). This formula will likely not appear on the AP test, but is good to know

<div class="theorem-box">

**Example.** An idealized vapor-pressure plot of $$\ln P$$ versus $$1/T$$ has slope $$-4800\ K$$. Determine the vaporization enthalpy and explain the negative slope.

The slope is $$-\Delta H_{vap}/R$$, so $$\Delta H_{vap}=4800(8.314)=39.9\ \mathrm{kJ/mol}$$. Increasing temperature decreases $$1/T$$ but increases vapor pressure; moving left on the graph moves upward. Using a positive slope would incorrectly predict vapor pressure falling with heating.

</div>

---


## Practice

### MCQ

::::problem
1. A gas absorbs $$350\ J$$ and does $$500\ J$$ of work on its surroundings. What is its internal-energy change?

   (A) $$+850\ J$$<br>
   (B) $$+150\ J$$<br>
   (C) $$-150\ J$$<br>
   (D) $$-850\ J$$

:::solution
Work done by the system is negative, giving $$\Delta U=q+w=350-500=-150\ J$$. Heat absorbed does not guarantee an increase in internal energy when work is also exchanged.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
2. A reaction heats $$100.0\ g$$ of solution by $$5.00^\circ C$$ in a calorimeter with heat capacity $$40.0\ \mathrm{J/K}$$. Take solution specific heat as $$4.00\ \mathrm{J/(g\,K)}$$ and neglect losses. What heat is released by the reaction?

   (A) $$2.00\ kJ$$<br>
   (B) $$2.20\ kJ$$<br>
   (C) $$1.80\ kJ$$<br>
   (D) $$0.200\ kJ$$

:::solution
Solution absorbs $$100(4)(5)=2000\ J$$ and calorimeter absorbs $$40(5)=200\ J$$. The reaction releases their sum, 2.20 kJ; its signed q is -2.20 kJ. Omitting the container underestimates the magnitude.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
3. Given $$A\rightarrow B$$ at $$+20\ kJ$$ and $$2B\rightarrow C$$ at $$-70\ kJ$$, find the enthalpy for $$C\rightarrow2A$$.

   (A) $$-90\ kJ$$<br>
   (B) $$-30\ kJ$$<br>
   (C) $$+30\ kJ$$<br>
   (D) $$+90\ kJ$$

:::solution
Double the first reaction and add the second: $$2A\rightarrow C$$ has $$40-70=-30\ kJ$$. Reverse that overall reaction to obtain +30 kJ. Both scaling and reversal must be applied.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
4. For $$\mathrm{H_2(g)+Cl_2(g)\rightarrow2HCl(g)}$$, bond energies are H-H 436, Cl-Cl 243, and H-Cl $$431\ \mathrm{kJ/mol}$$. Estimate the reaction enthalpy.

   (A) $$-183\ kJ$$<br>
   (B) $$+183\ kJ$$<br>
   (C) $$+248\ kJ$$<br>
   (D) $$-431\ kJ$$

:::solution
Breaking bonds costs $$436+243=679$$ kJ and making two H-Cl bonds releases $$2(431)=862$$ kJ. Net is $$679-862=-183$$ kJ. Forgetting the coefficient on the formed bond reverses the conclusion.

$$
\boxed{\text{A}}.
$$
:::
::::

::::problem
5. During boiling at constant pressure, heat is supplied but temperature stays constant while liquid remains. What primarily changes?

   (A) Average molecular kinetic energy increases steadily<br>
   (B) Intramolecular bonds necessarily break<br>
   (C) The substance stops absorbing energy<br>
   (D) Energy associated with intermolecular separation increases

:::solution
Added energy converts liquid to vapor by separating molecules against attractions. Constant temperature means no sustained increase in average thermal kinetic energy during the phase change. Boiling does not require decomposing the molecules.

$$
\boxed{\text{D}}.
$$
:::
::::

::::problem
6. An exothermic coffee-cup experiment loses heat to the room. If the calculation assumes no loss, what happens to the inferred reaction enthalpy per mole?

   (A) It becomes more negative<br>
   (B) It becomes less negative<br>
   (C) Its sign must become positive<br>
   (D) It is unchanged because energy is conserved

:::solution
The observed temperature increase is smaller because some released heat bypasses the measured solution. The inferred released-heat magnitude is too small, so an exothermic molar enthalpy is reported closer to zero. Conservation holds when the unmeasured room is included.

$$
\boxed{\text{B}}.
$$
:::
::::

### FRQ

::::frq{id=chem-thermochemistry-1}
7. A reaction is represented by

$$
2\text{H}_2(g)+\text{O}_2(g)\rightarrow2\text{H}_2\text{O}(l)
$$

with $$\Delta H^\circ_{\text{rxn}}=-572\ \text{kJ}$$ for the reaction as written.

   $$(A)$$ Calculate the enthalpy change for forming $$1.00\ \text{mol}$$ of $$\text{H}_2\text{O}(l)$$.

   $$(B)$$ Calculate the enthalpy change when $$4.00\ \text{mol}$$ of $$\text{H}_2(g)$$ reacts completely.

   $$(C)$$ Explain why breaking bonds is endothermic even when the overall reaction is exothermic.

   $$(D)$$ **Original extension.** If vaporizing one mole of liquid water at the stated temperature requires $$44.0\ \text{kJ}$$, calculate the reaction enthalpy when the two moles of product water are gaseous. Explain the sign of the correction.

:::solution
$$(A)$$ The reaction forms $$2$$ moles of water, so the enthalpy change must be divided by $$2$$ to find the value per mole of water:

$$
\frac{-572\ \text{kJ}}{2}=-286\ \text{kJ}.
$$

The negative sign means heat is released when water forms from hydrogen and oxygen.

$$(B)$$ The reaction as written consumes $$2$$ moles of $$\text{H}_2$$. Consuming $$4.00$$ moles doubles the reaction, so the enthalpy change also doubles:

$$
2(-572\ \text{kJ})=-1144\ \text{kJ}.
$$

$$(C)$$ Energy must be added to separate bonded atoms, so bond breaking is endothermic. The overall reaction is exothermic because forming the O-H bonds in water releases more energy than was required to break the H-H and O=O bonds. In bond-enthalpy language, $$\Delta H_{\text{rxn}}$$ is negative because the energy released by bonds formed is greater than the energy absorbed by bonds broken.

$$(D)$$ Start with the stated reaction forming liquid water, then add $$2\text{H}_2\text{O}(l)\rightarrow2\text{H}_2\text{O}(g)$$ with $$\Delta H=+88.0\ \text{kJ}$$. Hess's law gives $$\Delta H=-572+88.0=-484\ \text{kJ}$$. Vaporization absorbs energy, so forming gaseous water releases less energy than forming liquid water. The atoms and stoichiometric coefficients are unchanged, but product phase changes the enthalpy.
:::
::::

::::frq{id=chem-thermochemistry-2}
8. The 2026 AP Chemistry exam included a sodium oxide thermochemistry problem using formation enthalpy and limiting reactants. (Adapted from College Board, [2026 AP Chemistry FRQ 7](https://apcentral.collegeboard.org/media/pdf/ap26-frq-chemistry.pdf).)

   $$(A)$$ For $$4\text{Na}(s)+\text{O}_2(g)\rightarrow2\text{Na}_2\text{O}(s)$$ with $$\Delta H^\circ_{\text{rxn}}=-828\ \text{kJ}$$, calculate $$\Delta H_f^\circ$$ for $$\text{Na}_2\text{O}(s)$$.

   $$(B)$$ If $$2.00\ \text{mol}$$ Na reacts completely with excess oxygen, calculate the heat released.

   $$(C)$$ Explain why elements in their standard states have $$\Delta H_f^\circ=0$$.

   $$(D)$$ **Original extension.** React $$0.400\ \text{mol}$$ Na with $$0.0500\ \text{mol}$$ oxygen. Determine the limiting reactant, heat released, and amount of excess reactant remaining.

:::solution
$$(A)$$ The reaction forms $$2$$ moles of $$\text{Na}_2\text{O}(s)$$ from elements in their standard states, so the reaction enthalpy is twice the molar enthalpy of formation:

$$
\Delta H_f^\circ=\frac{-828\ \text{kJ}}{2}=-414\ \text{kJ/mol}.
$$

$$(B)$$ The reaction releases $$828\ \text{kJ}$$ per $$4$$ moles Na.

$$
2.00\ \text{mol Na}\times\frac{-828\ \text{kJ}}{4.00\ \text{mol Na}}=-414\ \text{kJ}.
$$

So $$414\ \text{kJ}$$ of heat is released.

$$(C)$$ Formation enthalpy measures formation from elements in their standard states. An element already in its standard state requires no formation reaction, so its assigned value is zero. This is a reference convention that lets formation enthalpies be added and subtracted consistently in Hess's law calculations.

$$(D)$$ Consuming all sodium would require $$0.400/4=0.100\ \text{mol}$$ oxygen, more than is available. Oxygen is limiting. The reaction extent relative to the written equation is $$0.0500\ \text{mol}$$, so $$q_p=(0.0500)(-828)=-41.4\ \text{kJ}$$: the system releases $$41.4\ \text{kJ}$$. Sodium consumed is $$4(0.0500)=0.200\ \text{mol}$$, leaving $$0.200\ \text{mol}$$. The enthalpy must be scaled by the limiting amount, not by all the sodium supplied.
:::
::::
