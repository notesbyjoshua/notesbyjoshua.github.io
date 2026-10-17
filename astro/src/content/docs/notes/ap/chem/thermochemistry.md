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

:::equations

| Idea | Equation | Conditions |
| --- | --- | --- |
| First law | $$\Delta U=q+w$$ | Heat entering and work done on the system are positive. |
| Pressure-volume work | $$w=-P_{ext}\Delta V$$ | Constant external pressure; expansion work is negative. |
| Sensible heat | $$q=mc\Delta T$$; $$q_{cal}=C_{cal}\Delta T$$ | No phase change during this step. |
| Calorimetry | $$q_{rxn}=-(mc+C_{cal})\Delta T$$ | Neglect heat loss; add other heat recipients if present. |
| Heat loss | $$q_{captured}=(1-f)\lvert q_{rxn}\rvert$$ | f is the fraction of released heat lost outside the measured surroundings. |
| Phase change | $$q=n\Delta H_{phase}$$ | Use molar phase enthalpy; temperature stays at the transition value during coexistence. |
| Enthalpy and internal energy | $$q_p=\Delta H$$; $$q_v=\Delta U$$; $$\Delta H=\Delta U+\Delta n_gRT$$ | Only pressure-volume work; final relation assumes ideal gases at a common T. |
| Hess's law | $$\Delta H_{net}=\sum_j\alpha_j\Delta H_j$$ | Reversal makes $$\alpha_j$$ negative; scaling coefficients scales enthalpy. |
| Formation data | $$\Delta H_{rxn}^\circ=\sum_p\nu_p\Delta H_{f,p}^\circ-\sum_r\nu_r\Delta H_{f,r}^\circ$$ | Standard-state elements have zero formation enthalpy by convention. |
| Bond estimate | $$\Delta H\approx\sum D_{broken}-\sum D_{formed}$$ | Average gas-phase bond energies; correct phase changes separately. |
| Dissolution | $$\Delta H_{soln}=\Delta H_{separation}+\Delta H_{mixing}$$ | Include both solute and solvent separation when using this partition. |
| Clausius-Clapeyron | $$\ln(P_2/P_1)=-\Delta H_{vap}(1/T_2-1/T_1)/R$$ | Approximately constant vaporization enthalpy and ideal vapor. |

:::

## Practice

### MCQ

::::problem
1. A gas absorbs $$500.\ \mathrm{J}$$ while expanding from $$2.00$$ to $$5.00\ \mathrm{L}$$ against $$1.50\ \mathrm{atm}$$. Use $$1\ \mathrm{L\,atm}=101.3\ \mathrm{J}$$. What is its internal-energy change?

   (A) $$+956\ \mathrm{J}$$<br>
   (B) $$-456\ \mathrm{J}$$<br>
   (C) $$+44.2\ \mathrm{J}$$<br>
   (D) $$-44.2\ \mathrm{J}$$

:::solution
Expansion gives $$w=-P_{ext}\Delta V=-(1.50)(3.00)(101.3)=-455.85\ \mathrm{J}$$. Then $$\Delta U=q+w=500.-455.85\approx+44.2\ \mathrm{J}$$. Most of the absorbed heat leaves as work; adding its magnitude would use the wrong sign.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
2. A reaction heats $$100.0\ \mathrm{g}$$ of solution by $$3.00\ K$$ in a calorimeter with heat capacity $$40.0\ \mathrm{J/K}$$. The solution's specific heat is $$4.00\ \mathrm{J/(g\,K)}$$ and $$0.0200\ \mathrm{mol}$$ reacts. What is the molar reaction enthalpy, neglecting heat loss?

   (A) $$-66.0\ \mathrm{kJ/mol}$$<br>
   (B) $$-60.0\ \mathrm{kJ/mol}$$<br>
   (C) $$+66.0\ \mathrm{kJ/mol}$$<br>
   (D) $$-6.00\ \mathrm{kJ/mol}$$

:::solution
Both solution and apparatus warm: $$q_{surr}=(100.0\times4.00+40.0)(3.00)=1320\ \mathrm{J}$$. Reaction heat has the opposite sign, so $$\Delta H=-1.320/0.0200=-66.0\ \mathrm{kJ/mol}$$. Omitting the calorimeter undercounts the released heat.

$$
\boxed{\text{A}}.
$$
:::
::::

::::problem
3. Given $$A\rightarrow2B$$ with $$\Delta H=+40.0\ \mathrm{kJ}$$ and $$B+C\rightarrow D$$ with $$\Delta H=-70.0\ \mathrm{kJ}$$, what is the enthalpy for $$2D\rightarrow A+2C$$?

   (A) $$-100.\ \mathrm{kJ}$$<br>
   (B) $$-30.0\ \mathrm{kJ}$$<br>
   (C) $$+30.0\ \mathrm{kJ}$$<br>
   (D) $$+100.\ \mathrm{kJ}$$

:::solution
Adding the first equation to twice the second gives $$A+2C\rightarrow2D$$ with $$40.0-140.=-100.\ \mathrm{kJ}$$. Reversing gives +100 kJ. Both the intermediate coefficient and the final arrow direction affect the result.

$$
\boxed{\text{D}}.
$$
:::
::::

::::problem
4. Combustion of one mole of a fuel to form two moles of gaseous water has $$\Delta H=-800.\ \mathrm{kJ}$$. Water's vaporization enthalpy is $$44.0\ \mathrm{kJ/mol}$$ at the same temperature. How much heat is released by burning $$0.250\ \mathrm{mol}$$ fuel to liquid water?

   (A) $$178\ \mathrm{kJ}$$<br>
   (B) $$222\ \mathrm{kJ}$$<br>
   (C) $$200.\ \mathrm{kJ}$$<br>
   (D) $$244\ \mathrm{kJ}$$

:::solution
Condensing two moles of product water contributes $$-88.0\ \mathrm{kJ}$$ per mole fuel. The liquid-product reaction therefore has $$\Delta H=-888\ \mathrm{kJ/mol}$$. A quarter mole releases $$0.250(888)=222\ \mathrm{kJ}$$; the requested heat released is a positive magnitude.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
5. At $$300\ K$$, a rigid bomb measures $$\Delta U=-100.0\ \mathrm{kJ}$$ for $$\mathrm{A(g)+2B(g)\rightarrow C(g)}$$ as written. For ideal gases, what is $$\Delta H$$? Use $$R=8.314\ \mathrm{J/(mol\,K)}$$.

   (A) $$-95.0\ \mathrm{kJ}$$<br>
   (B) $$-100.0\ \mathrm{kJ}$$<br>
   (C) $$-105.0\ \mathrm{kJ}$$<br>
   (D) $$-102.5\ \mathrm{kJ}$$

:::solution
The gas mole change is $$1-3=-2$$. Thus $$\Delta H=\Delta U+\Delta n_gRT=-100.0+(-2)(8.314)(300)/1000=-105.0\ \mathrm{kJ}$$. Constant-volume heat measures internal energy; converting to enthalpy requires the gas-mole correction.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
6. Two equal-mass samples of the same substance start at its melting point. X is all solid; Y is half solid and half liquid. The same heat, sufficient to melt X completely and warm it, is added to each without loss. Which finishes hotter?

   (A) Y, because less of its added energy is required for melting<br>
   (B) X, because it initially contains more solid bonds<br>
   (C) Equal temperatures, because the heat inputs match<br>
   (D) Cannot be predicted even if heat capacities and melting enthalpy are positive

:::solution
Y needs only half as much latent heat to finish melting. With identical masses and final liquid heat capacities, more of Y's equal heat input remains for raising temperature. Equal heat input yields equal temperature changes only when the initial phase states and heat capacities permit that comparison.

$$
\boxed{\text{A}}.
$$
:::
::::

### FRQ

::::frq{id=chem-thermochemistry-challenge-1}
7. Mix 50.0 mL of 1.00 M HCl with 75.0 mL of 0.500 M NaOH in a coffee-cup calorimeter. Both start at $$22.00^\circ\mathrm{C}$$ and the mixture reaches $$25.50^\circ\mathrm{C}$$. Take solution density as $$1.00\ \mathrm{g/mL}$$, specific heat as $$4.00\ \mathrm{J/(g\,K)}$$, and calorimeter heat capacity as $$30.0\ \mathrm{J/K}$$. Assume additive volumes.

   $$(A)$$ Identify the limiting reactant and calculate the moles of water formed by neutralization.

   $$(B)$$ Calculate the heat absorbed by the solution and calorimeter, then infer the molar neutralization enthalpy.

   $$(C)$$ Suppose 15.0% of the released reaction heat escaped to the room before the peak temperature was recorded. Correct the inferred molar enthalpy.

   $$(D)$$ If the same reactant amounts were used in a calorimeter with twice the original heat capacity, predict whether the observed temperature rise would halve. Assume no heat loss and use the uncorrected measured heat for this comparison.

:::solution
$$(A)$$ Acid supplies $$0.0500(1.00)=0.0500\ \mathrm{mol}$$ hydronium, while base supplies $$0.0750(0.500)=0.0375\ \mathrm{mol}$$ hydroxide. The 1:1 net reaction $$\mathrm{H^++OH^-\rightarrow H_2O}$$ makes hydroxide limiting. Water formed is 0.0375 mol, with 0.0125 mol excess acid remaining.

$$(B)$$ The temperature rise is 3.50 K. Solution heat is $$125.0(4.00)(3.50)=1750\ \mathrm{J}$$ and calorimeter heat is $$30.0(3.50)=105\ \mathrm{J}$$. Reaction heat is their negative sum, -1855 J. Dividing by 0.0375 mol reacted gives $$\Delta H=-49.5\ \mathrm{kJ/mol}$$ water formed. Dividing by total acid supplied would include acid that did not react.

$$(C)$$ The measured surroundings gained only 85.0% of the reaction's released energy. Thus the true released magnitude is $$1855/0.850=2182\ \mathrm{J}$$, not 1855 multiplied by 1.15. The corrected enthalpy is $$-2.182/0.0375=-58.2\ \mathrm{kJ/mol}$$. Heat loss makes the uncorrected exothermic value too close to zero.

$$(D)$$ The original combined heat capacity is $$125.0(4.00)+30.0=530\ \mathrm{J/K}$$. Doubling only the calorimeter contribution gives $$500+60.0=560\ \mathrm{J/K}$$. The same 1855 J would produce $$\Delta T=1855/560=3.31\ K$$, not 1.75 K. Only one part of the total heat capacity doubled, while the much larger solution contribution stayed fixed.
:::
::::

::::frq{id=chem-thermochemistry-challenge-2}
8. For ethanol combustion, $$\mathrm{C_2H_5OH(l)+3O_2(g)\rightarrow2CO_2(g)+3H_2O(l)}$$ has $$\Delta H^\circ=-1367\ \mathrm{kJ/mol}$$ ethanol. Standard formation enthalpies are $$-393.5\ \mathrm{kJ/mol}$$ for carbon dioxide and $$-285.8\ \mathrm{kJ/mol}$$ for liquid water. At the same temperature, vaporizing water requires $$44.0\ \mathrm{kJ/mol}$$.

   $$(A)$$ Determine ethanol's standard formation enthalpy and write its formation reaction from standard-state elements.

   $$(B)$$ Calculate the combustion enthalpy if all product water is vapor instead of liquid.

   $$(C)$$ Burn 0.200 mol ethanol with 0.450 mol oxygen. Find the heat released when water is liquid and the ethanol remaining, assuming complete consumption of the limiting reactant.

   $$(D)$$ For the liquid-water reaction at 298 K, calculate $$\Delta U^\circ$$ per mole ethanol assuming ideal gases and only pressure-volume work. Use $$R=8.314\ \mathrm{J/(mol\,K)}$$.

:::solution
$$(A)$$ Products contribute $$2(-393.5)+3(-285.8)=-1644.4\ \mathrm{kJ/mol}$$. With oxygen's formation enthalpy zero, $$-1367=-1644.4-\Delta H_f^\circ(ethanol)$$, so $$\Delta H_f^\circ=-277.4\ \mathrm{kJ/mol}$$. The formation reaction is $$\mathrm{2C(graphite)+3H_2(g)+\tfrac12O_2(g)\rightarrow C_2H_5OH(l)}$$. It must form exactly one mole of ethanol.

$$(B)$$ Add $$\mathrm{3H_2O(l)\rightarrow3H_2O(g)}$$, with enthalpy $$3(44.0)=132.0\ \mathrm{kJ}$$. Hess's law then gives $$\Delta H=-1367+132.0=-1235\ \mathrm{kJ/mol}$$. Gaseous products retain the energy that would have been released on condensation, so combustion to vapor is less exothermic.

$$(C)$$ Full consumption of the ethanol would require 0.600 mol oxygen, so oxygen is limiting. Ethanol consumed is $$0.450/3=0.150\ \mathrm{mol}$$, leaving 0.0500 mol. The system releases $$0.150(1367)=205\ \mathrm{kJ}$$. Scaling enthalpy by the initial 0.200 mol ethanol would overstate the reaction extent.

$$(D)$$ Gas coefficients change from three moles oxygen to two moles carbon dioxide, so $$\Delta n_g=-1$$; the liquids do not count. Since $$\Delta H=\Delta U+\Delta n_gRT$$, $$\Delta U=-1367-(-1)(8.314)(298)/1000=-1364.5\ \mathrm{kJ/mol}$$. The distinction reflects the pressure-volume contribution, not a failure of energy conservation.
:::
::::
