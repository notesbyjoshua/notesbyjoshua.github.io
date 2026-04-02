---
layout: default
title: "Unit 6: Thermochemistry"
parent: AP Chemistry
nav_order: 6
permalink: /notes/ap/chem/thermochemistry/
---

# Unit 6: Thermochemistry

**Thermochemistry** studies heat flow associated with chemical reactions and physical changes (melting, vaporization, dissolving). It is the chemical face of the **first law of thermodynamics** and sets up **enthalpy** reasoning used again in [equilibrium]({{ '/notes/ap/chem/equilibrium/' | relative_url }}), [acid–base]({{ '/notes/ap/chem/acidbase/' | relative_url }}), and [thermodynamics / electrochemistry]({{ '/notes/ap/chem/thermoelectro/' | relative_url }}). Balanced equations and stoichiometry from [Unit 4]({{ '/notes/ap/chem/chemrxns/' | relative_url }}) carry mole ratios directly into thermochemical calculations.

---

## System, surroundings, and boundaries

In modeling, the universe is split into the **system** (what you study) and the **surroundings** (everything else that can exchange energy with the system). A **closed system** exchanges energy but not matter across its boundary. An **open system** can exchange both (an open beaker). An **isolated system** exchanges neither, and this can be approximated by good calorimeter insulation.

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

---

### Phase changes and heating curves

During melting or boiling at fixed pressure, temperature stays constant while latent heat is absorbed or released:

$$
q = n\Delta H_{\text{fus}}, \qquad q = n\Delta H_{\text{vap}},
$$

with molar enthalpies of fusion and vaporization. A heating curve (temperature vs heat added) shows slopes $$1/(mc)$$ and plateaus at phase changes.

---

## Temperature, kinetic energy, and the Maxwell–Boltzmann distribution

Temperature (in Kelvin) is proportional to the average translational kinetic energy of ideal-gas molecules:

$$
\overline{KE}_{\text{mol}} = \frac{3}{2}RT, \qquad \overline{KE}_{\text{molecule}} = \frac{3}{2} k_B T,
$$ (as seen also in [Unit 3]({{ '/notes/ap/chem/submix/' | relative_url }}))

with Boltzmann’s constant $$k_B \approx 1.38 \times 10^{-23} \text{ J/K}$$. Individual molecules span a distribution of speeds; a **Maxwell–Boltzmann** curve plots fraction versus speed or energy. Lighter gases at the same $$T$$ have higher average speed, and raising $$T$$ broadens the curve and increases the fraction with energy above a given activation energy.

Macroscopic kinetic energy $$\frac{1}{2}mv^2$$ applies to bulk motion; do not confuse it with thermal motion of molecules inside a sample.

---

## Enthalpy

**Enthalpy** $$H$$ is defined as $$H = U + PV$$. It is a state function. For a process at constant pressure the change in enthalpy becomes:

$$
\Delta H = \Delta U + P\Delta V.
$$

However, you will usually see enthalpy in the context of heat for AP Chemistry problems, so

$$
\Delta H = - \frac{q_surr}{n}.
$$

where $$n$$ is the number of moles, and enthalpy is from the perspective of the system. Note taht $$\Delta H$$ will have opposite sign conventions compared to $$q$$ (as defined in an AP context).

### Exothermic versus endothermic

In an **exothermic** reaction, the system evolves so that heat flows out to the surroundings: $$\Delta H < 0$$, $$q_{\text{sys}} < 0$$, and $$q_{\text{surr}} > 0$$.

In an **endothermic** reaction, the system draws heat in: $$\Delta H > 0$$, $$q_{\text{sys}} > 0$$, and $$q_{\text{surr}} < 0$$.

Always label whether $$q$$ refers to system or surroundings when you compare signs across textbooks.

### State functions and path

Enthalpy is a state function. **State functions** depend only on initial and final states, not the path: $$P$$, $$V$$, $$T$$, $$U$$, $$H$$, and (later) **entropy** $$S$$ and **Gibbs free energy** $$G$$. Heat $$q$$ and work $$W$$ are path-dependent; their sum $$\Delta U = q + W$$ is not.

---

## Standard enthalpies and formation

**Standard state** means specified reference conditions (For AP: $$1$$ atm for gases, $$1\text{ M}$$ for solutes in solution chemistry, pure substances in their stable form at $$25^\circ\text{C}$$ unless noted). The **standard enthalpy of formation** $$\Delta H_f^\circ$$ is $$\Delta H$$ for forming one mole of a compound from its elements in their standard states. Elements in their reference/naturally occuring forms have $$\Delta H_f^\circ = 0$$ by definition.

For any reaction,

$$
\Delta H_{\text{rxn}}^\circ = \sum \nu\,\Delta H_f^\circ(\text{products}) - \sum \nu\,\Delta H_f^\circ(\text{reactants}),
$$

where $$\nu$$ are stoichiometric coefficients. Thermochemical equations can be scaled; $$\Delta H$$ scales with the mole amounts written in the equation.

---

## Hess’s law

**Hess’s law** states that $$\Delta H$$ for an overall process is the sum of $$\Delta H$$ values for steps that add up to the same net reaction—because $$H$$ is a state function. Reverse a step → flip the sign of $$\Delta H$$. Multiply a step by a factor → multiply $$\Delta H$$ by the same factor.

---

## Bond enthalpies (estimates)

**Bond enthalpy** (or bond energy) is the energy required to break one mole of a bond in the gas phase (averaged over similar molecules for tabulated values). For gas-phase estimates,

$$
\Delta H_{\text{rxn}} \approx \sum D(\text{bonds broken}) - \sum D(\text{bonds formed}),
$$

using positive bond energies for each bond listed. This ignores liquids, solvents, and exact environments, so it is less accurate than calorimetry or formation cycles.

---

## Solution formation (preview)

$$\Delta H_{\text{solution}}$$ combines lattice (endothermic breakup of solid) and hydration (exothermic ion–solvent interaction) terms. A slightly endothermic $$\Delta H_{\text{solution}}$$ can still occur if entropy favors mixing (full explanation in later units). A very endothermic process may give negligible solubility unless entropy dominates strongly.

---

## Vapor pressure and the Clausius–Clapeyron relation

The **Clausius–Clapeyron** equation relates vapor pressure to temperature for a liquid (using molar enthalpy of vaporization $$\Delta H_{\text{vap}}$$ as approximately constant over a modest range):

$$
\ln\left(\frac{P_2}{P_1}\right) = -\frac{\Delta H_{\text{vap}}}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right).
$$

Higher $$T$$ increases vapor pressure; stronger IMFs tend to lower vapor pressure at a given $$T$$ (see [Unit 3]({{ '/notes/ap/chem/submix/' | relative_url }})). This formula will likely not appear on the AP test, but is good to know