---
layout: default
title: "Unit 5: Kinetics"
parent: AP Chemistry
nav_order: 5
permalink: /notes/ap/chem/kinetics/
---

# Unit 5: Kinetics

**Chemical kinetics** asks how fast a reaction proceeds and *why* that speed changes with conditions. It is distinct from [thermochemistry]({{ '/notes/ap/chem/thermochemistry/' | relative_url }}) (energy changes and a first look at spontaneity) and from [equilibrium]({{ '/notes/ap/chem/equilibrium/' | relative_url }}) (where a reversible process ends up). Balanced equations from [Unit 4]({{ '/notes/ap/chem/chemrxns/' | relative_url }}) supply stoichiometry; kinetics supplies rates, rate laws, and mechanisms.

---

## Reaction rate

The **reaction rate** measures how quickly reactant concentrations fall or product concentrations rise. For a generic reaction

$$
a\text{A} + b\text{B} \longrightarrow c\text{C} + d\text{D},
$$

a common convention ties all species to one rate expression:

$$
\text{rate} = -\frac{1}{a}\frac{d[\text{A}]}{dt} = -\frac{1}{b}\frac{d[\text{B}]}{dt} = +\frac{1}{c}\frac{d[\text{C}]}{dt} = +\frac{1}{d}\frac{d[\text{D}]}{dt}.
$$

The negative sign on reactants makes rate a positive quantity as written. In lab data you often measure average rate over an interval (slope of a chord on a concentration–time graph). Instantaneous rate is the slope of the tangent at one time—the limit as $$\Delta t \to 0$$ and the quantity that appears in calculus-based rate laws.

---

## Rate laws and the rate constant

Experiment determines how rate depends on concentration. The differential rate law (or simply **rate law**) has the form

$$
\text{rate} = k[\text{A}]^m[\text{B}]^n\cdots
$$

Here $$k$$ is the **rate constant** (units depend on overall order), and $$m, n, \ldots$$ are the orders with respect to each reactant. Those exponents are *not* taken from the balanced equation unless the reaction is a single **elementary step** (see mechanisms below). Overall order is the sum $$m + n + \cdots$$.

The **method of initial rates** compares initial rates while varying one reactant’s initial concentration at a time. Holding other concentrations fixed, if doubling $$[\text{A}]$$ multiplies the initial rate by $$2^m$$, you read off $$m$$. Repeat for each reactant, then substitute any one run’s data to solve for $$k$$.

Units of $$k$$ follow from $$\text{rate}$$ in $$\text{M/s}$$ (molarity per second) and the concentration powers. Examples for a single reactant $$\text{A}$$:

- Zero order ($$\text{rate} = k$$): $$k$$ in $$\text{M}\cdot\text{s}^{-1}$$
- First order ($$\text{rate} = k[\text{A}]$$): $$k$$ in $$\text{s}^{-1}$$
- Second order ($$\text{rate} = k[\text{A}]^2$$): $$k$$ in $$\text{M}^{-1}\cdot\text{s}^{-1}$$

---

## Integrated rate laws and graphs

Integrating the differential law links concentration to time. Let $$[\text{A}]_0$$ be the initial concentration of the species tracked in the simplified one-reactant forms below.

Zero order:

$$
[\text{A}] = [\text{A}]_0 - kt
$$

A plot of $$[\text{A}]$$ versus $$t$$ is linear with slope $$-k$$.

First order:

$$
\ln[\text{A}] = -kt + \ln[\text{A}]_0
$$

A plot of $$\ln[\text{A}]$$ versus $$t$$ is linear with slope $$-k$$.

Second order:

$$
\frac{1}{[\text{A}]} = kt + \frac{1}{[\text{A}]_0}
$$

A plot of $$1/[\text{A}]$$ versus $$t$$ is linear with slope $$k$$.

Which graph is linear is a standard way to infer order from concentration–time data. **Half-life** $$t_{1/2}$$ is the time for $$[\text{A}]$$ to drop to half its initial value:

$$
\text{zero:}\quad t_{1/2} = \frac{[\text{A}]_0}{2k}
$$

$$
\text{first:}\quad t_{1/2} = \frac{\ln 2}{k}
$$

$$
\text{second:}\quad t_{1/2} = \frac{1}{k[\text{A}]_0}
$$

Only for first order is $$t_{1/2}$$ independent of $$[\text{A}]_0$$—a fact often used to identify nuclear decay kinetics and analogous processes.

---

## Collision model and activation energy

**Collision theory** pictures reaction as molecules colliding with enough kinetic energy and suitable orientation. Raising temperature increases the fraction of collisions whose energy exceeds a threshold called the **activation energy** $$E_a$$. The **Arrhenius equation** relates the rate constant to temperature:

$$
k = A e^{-E_a/(RT)}
$$

$$A$$ is the pre-exponential factor (related to collision frequency and steric factors); $$R$$ is the gas constant ($$8.314 \text{ J/(mol}\cdot\text{K)}$$ when $$E_a$$ is in $$\text{J/mol}$$); $$T$$ is kelvin.

A two-point form avoids knowing $$A$$:

$$
\ln\frac{k_2}{k_1} = -\frac{E_a}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right).
$$

A plot of $$\ln k$$ versus $$1/T$$ is linear with slope $$-E_a/R$$. A modest temperature increase can change $$k$$ sharply because it sits in an exponential.

---

## Reaction mechanisms

Many balanced equations are net processes built from simpler **elementary steps**. Each elementary step has its own **molecularity** (how many reactant particles collide in that step) and obeys rate-law exponents equal to stoichiometric coefficients for that step only.

A **reaction mechanism** proposes a sequence of such steps. Species produced in one step and consumed in another, never appearing in the net equation, are **intermediates**. The **rate-determining step** (slowest step) often dominates the observed rate law; faster steps before it may reach **pre-equilibrium** with their precursors in some textbook mechanisms.

If the experimental rate law does not match the stoichiometry of the overall equation, you infer multiple steps and a slow step that controls rate. Fast steps after the slow step do not change the rate law’s concentration dependence (they only consume intermediates as they form).

---

## Transition state and catalysis

Along the reaction coordinate, the system passes through a high-energy configuration called the **transition state** (or **activated complex**). It is not a stable intermediate with a measurable concentration in the usual introductory picture; it sits at an energy maximum between reactants and products.

A **catalyst** provides an alternative pathway with lower activation energy. It is regenerated by the end of the cycle and does not appear in the net reaction. Homogeneous catalysts share the phase with reactants; heterogeneous catalysts (often solids) provide a surface where adsorption and orientation increase rate. A catalyst increases $$k$$ (both forward and reverse for a reversible path) and speeds approach to equilibrium but does not change $$\Delta G^\circ$$ or the equilibrium constant for a given reaction at fixed $$T$$.

---

## Factors affecting rate (summary)

Concentration enters through the rate law; higher reactant concentrations typically raise rate for positive orders. Temperature raises $$k$$ through the Arrhenius factor. Surface area matters especially for heterogeneous systems (e.g. solid reactant as powder versus a single lump). Catalysts lower $$E_a$$. Inhibitors or poisons can block active sites or consume intermediates, slowing rate without necessarily appearing in the simplest textbook rate law.

---

## Kinetics vs equilibrium (preview)

For a reversible elementary reaction, forward and reverse rates balance at equilibrium, linking rate constants to an equilibrium constant in simple cases. The full story belongs with [equilibrium]({{ '/notes/ap/chem/equilibrium/' | relative_url }}); here the essential point is that kinetics answers “how fast” while equilibrium answers “how far” under constant conditions.
