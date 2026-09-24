---
title: "Unit 5: Kinetics"
description: "AP Chemistry notes on reaction rates, rate laws, mechanisms, catalysts, collision theory, and integrated rate laws."
sidebar:
  order: 5
---

## Collision theory and the molecular picture

**Collision theory** requires that molecules actually collide, that a collision carries at least the **activation energy** $$E_a$$, and that the partners meet with a geometry that allows the relevant bonds to rearrange. A compact way to think about rate is that it scales with three factors:

$$
\text{rate} \propto N \times f_E \times f_O.
$$

Here $$N$$ is roughly the number of collisions per unit time (collision frequency), $$f_E$$ is the fraction of collisions with enough energy to surmount the barrier, and $$f_O$$ is the fraction with favorable orientation (sometimes folded into a steric factor in $$A$$).

Raising temperature increases $$N$$ (faster motion, more frequent collisions) and sharply increases $$f_E$$ (the high-energy tail of the speed distribution grows). Increasing concentration in a fixed volume raises $$N$$ because more particles occupy the same space. A catalyst mainly increases $$f_E$$ for the catalyzed path by offering a lower activation energy; it does not change $$\Delta H$$ for the overall conversion. Changing physical state—for example, grinding a solid to increase surface area or improving mixing—raises effective collision frequency or exposes more reactive sites.

### The Maxwell–Boltzmann distribution

The reason temperature has such a strong effect on rate is captured by the **Maxwell–Boltzmann distribution**, a curve showing the fraction of particles (vertical axis) at each kinetic energy (horizontal axis). At any temperature, only the particles to the **right of $$E_a$$**—those in the high-energy tail—can react on collision. That tail area is exactly $$f_E$$.

Key features of the curve:

- The distribution starts at the origin, rises to a peak (the **most probable** kinetic energy), and trails off with a long tail toward high energy; the area under the whole curve is fixed (it represents all the particles).
- **Raising the temperature** broadens and flattens the curve and shifts the peak to higher energy. The peak height drops, but the tail beyond $$E_a$$ grows dramatically—so a small rise in $$T$$ can sharply increase the fraction of effective collisions.
- A **catalyst does not move the curve**; instead it lowers $$E_a$$ (shifts the threshold line left), which puts a larger fraction of the *same* distribution above the barrier.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[axis lines=left, width=9cm, height=5cm, xmin=0, xmax=8, ymin=0, ymax=0.75, xlabel={molecular speed or energy}, ylabel={fraction}, xtick=\empty, ytick=\empty]
\addplot[blue, very thick, samples=200, domain=0:8] {0.9*x^2*exp(-1.1*x)};
\addplot[red, very thick, samples=200, domain=0:8] {0.28*x^2*exp(-0.45*x)};
\addplot[dashed, thick] coordinates {(4.8,0) (4.8,0.65)};
\node[blue] at (axis cs:1.7,0.55) {$T_1$};
\node[red] at (axis cs:4.0,0.42) {$T_2>T_1$};
\node[anchor=south] at (axis cs:4.8,0.65) {$E_a$};
\end{axis}
\end{tikzpicture}
```

**Homogeneous catalysis** places the catalyst in the same phase as the reactants (solution catalysis is common). **Heterogeneous catalysis** uses a different phase, often a solid surface where adsorption aligns molecules for reaction. **Acid–base catalysis** is a major special case: $$\text{H}^+$$, $$\text{OH}^-$$, or other acids and bases can protonate or deprotonate substrates, stabilizing transition states and speeding steps without being consumed in the net equation.

<div class="theorem-box">

**Example.** Two equal-sized samples of the same gas are compared at different temperatures. A student says the hotter distribution must have a taller peak because more molecules can react. Explain the error.

Each curve represents the same total number of molecules, so its total area stays fixed. Heating broadens the distribution and shifts its peak toward higher energy, generally lowering its height while increasing the area above a fixed activation energy. The reactive fraction is an area beyond the threshold, not the height of the curve at its most probable energy. Suitable orientation is still required for reaction.

</div>

---

## Factors affecting rate (summary)

Concentration raises collision frequency $$N$$ and enters the rate law directly. Temperature raises the **number of collisions and the frequency of effective collisions**. Surface area and physical state (powder versus lump, mixing, phase contact) **increase the rate of collision**. Catalysts (homogeneous, heterogeneous, or acid–base) **increases the frequency of effective collisions**.

<div class="theorem-box">

**Example.** Equal masses of a solid react with excess acid at the same temperature, one powdered and one in a single chunk. Predict which finishes first and whether the theoretical product amount changes.

Powder exposes more surface sites at once, so it usually reacts faster. Equal amounts of the same limiting solid produce the same theoretical amount of product. Faster conversion does not mean a larger stoichiometric yield when both trials eventually react completely.

</div>

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

The negative sign on reactants makes rate a positive quantity as written. Note that $$d$$ represents the derivative, or the measure of the rate of change. If you watch one species by itself, the sign of $$d[\text{X}]/dt$$ tells you whether it is being used up (negative for a reactant whose concentration falls) or formed (positive for a product). The stoichiometric factors convert those individual slopes into a single rate for the whole reaction.

In lab data you often measure average rate over an interval (slope of a chord on a concentration–time graph). Instantaneous rate is the slope of the tangent at one time—the limit as $$\Delta t \to 0$$ and the quantity that appears in calculus-based rate laws.

<div class="theorem-box">

**Example.** During $$2A\rightarrow B$$, $$[A]$$ drops by $$0.060\ M$$ in $$20.0\ \mathrm{s}$$. A student reports product formation at $$0.0030\ M/s$$. Find the error.

Reactant disappearance is $$0.060/20.0=0.0030\ M/s$$, but two A produce one B. Thus $$\Delta[B]/\Delta t=0.0015\ M/s$$. The normalized reaction rate equals $$-\tfrac12\Delta[A]/\Delta t$$, not the unadjusted disappearance rate.

</div>

---

## Rate laws and the rate constant

Experiment determines how rate depends on concentration. The differential rate law (or simply **rate law**) has the form

$$
\text{rate} = k[\text{A}]^m[\text{B}]^n[\text{C}]^p \cdots
$$

Here $$k$$ is the **rate constant** (units depend on overall order), and $$m, n, p, \ldots$$ are the orders with respect to each reactant. Those exponents are *not* taken from the balanced equation unless the reaction is a single **elementary step** (see mechanisms below). Overall reaction order is the sum $$m + n + p + \cdots$$.

At fixed temperature and with the same catalyst, $$k$$ does not depend on concentrations or, for gases, on pressure independently of concentration. Concentration enters through the powers $$[\text{A}]^m$$ etc. Changing pressure in a gas-phase system often changes concentrations and therefore rate, but it does not change $$k$$ itself. Temperature and catalysts change $$k$$.

The **method of initial rates** compares initial rates while varying one reactant’s initial concentration at a time. Holding other concentrations fixed, if doubling $$[\text{A}]$$ multiplies the initial rate by $$2^m$$, $$m$$ is the order of $$A$$. More generally, for two trials where only $$[\text{A}]$$ changes,

$$
m = \frac{\ln(\text{rate}_1 / \text{rate}_2)}{\ln([\text{A}]_1 / [\text{A}]_2)},
$$

with nearest-integer order a common simplification on exams when data are clean. Repeat for each reactant, then substitute any one run’s data to solve for $$k$$.

Units of $$k$$ follow from $$\text{rate}$$ in $$\text{M/s}$$ (molarity per second) and the concentration powers. Examples for a single reactant $$\text{A}$$:

- Zeroth order ($$\text{rate} = k$$): $$k$$ in $$\text{M}\cdot\text{s}^{-1}$$
- First order ($$\text{rate} = k[\text{A}]$$): $$k$$ in $$\text{s}^{-1}$$
- Second order ($$\text{rate} = k[\text{A}]^2$$): $$k$$ in $$\text{M}^{-1}\cdot\text{s}^{-1}$$

Note that rate always has the units of $$\frac{M}{s}$$ and concentration always has the units of $$M$$.

<div class="theorem-box">

**Example.** Doubling both A and B multiplies rate by eight; doubling only A multiplies it by four. Derive a rate law and predict the effect of halving B alone.

With $$r=k[A]^m[B]^n$$, the second trial gives $$2^m=4$$, so $$m=2$$. The joint change gives $$2^{2+n}=8$$, so $$n=1$$. Therefore $$r=k[A]^2[B]$$ and halving B halves the rate. Changing two concentrations at once needs a second comparison to separate their effects.

</div>

---

## Integrated rate laws and graphs

Integrating the differential law links concentration to time. Let $$[\text{A}]_0$$ be the initial concentration of the species tracked in the simplified one-reactant forms below.

Zeroth order:

$$
[\text{A}] - [\text{A}]_0 = -kt
$$

Equivalently $$[\text{A}] = [\text{A}]_0 - kt$$. A plot of $$[\text{A}]$$ versus $$t$$ is linear with slope $$-k$$.

First order:

$$
\ln[\text{A}] - \ln[\text{A}]_0 = -kt \quad\text{or}\quad \ln\!\left(\frac{[\text{A}]}{[\text{A}]_0}\right) = -kt.
$$

A plot of $$\ln[\text{A}]$$ versus $$t$$ is linear with slope $$-k$$.

Second order:

$$
\frac{1}{[\text{A}]} - \frac{1}{[\text{A}]_0} = kt.
$$

A plot of $$1/[\text{A}]$$ versus $$t$$ is linear with slope $$k$$.

Which graph is linear is a standard way to infer order from concentration–time data. **Half-life** $$t_{1/2}$$ is the time for $$[\text{A}]$$ to drop to half its initial value:

$$
\text{zero:}\quad t_{1/2} = \frac{[\text{A}]_0}{2k}
$$

$$
\text{first:}\quad t_{1/2} = \frac{\ln 2}{k} \approx \frac{0.693}{k}
$$

$$
\text{second:}\quad t_{1/2} = \frac{1}{k[\text{A}]_0}
$$

For zero order, half-life **shrinks** as $$[\text{A}]_0$$ decreases. For first order (including many nuclear decay kinetics), $$t_{1/2}$$ is constant throughout the reaction—independent of $$[\text{A}]_0$$. For second order, half-life **grows** as $$[\text{A}]_0$$ decreases.

Putting it together, here is the standard comparison for a single reactant $$\text{A}$$. Identifying which plot is a straight line is the most reliable way to read the order off real concentration–time data:

| Order | Rate law | Integrated form | Linear plot | Slope | Units of $$k$$ | Half-life |
| --- | --- | --- | --- | --- | --- | --- |
| Zero | $$\text{rate}=k$$ | $$[\text{A}]=[\text{A}]_0-kt$$ | $$[\text{A}]$$ vs $$t$$ | $$-k$$ | $$\text{M}\cdot\text{s}^{-1}$$ | $$\dfrac{[\text{A}]_0}{2k}$$ |
| First | $$\text{rate}=k[\text{A}]$$ | $$\ln[\text{A}]=\ln[\text{A}]_0-kt$$ | $$\ln[\text{A}]$$ vs $$t$$ | $$-k$$ | $$\text{s}^{-1}$$ | $$\dfrac{0.693}{k}$$ |
| Second | $$\text{rate}=k[\text{A}]^2$$ | $$\dfrac{1}{[\text{A}]}=\dfrac{1}{[\text{A}]_0}+kt$$ | $$\dfrac{1}{[\text{A}]}$$ vs $$t$$ | $$+k$$ | $$\text{M}^{-1}\cdot\text{s}^{-1}$$ | $$\dfrac{1}{k[\text{A}]_0}$$ |

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\pgfplotsset{smallplot/.style={width=4cm,height=3.1cm,axis lines=left,xtick=\empty,ytick=\empty,xlabel={time}}}
\begin{axis}[smallplot,ylabel={$[A]$},title={zero order}] \addplot[blue,very thick,domain=0:4]{4-x}; \end{axis}
\begin{axis}[smallplot,at={(4.6cm,0)},ylabel={$\ln[A]$},title={first order}] \addplot[blue,very thick,domain=0:4]{4-x}; \end{axis}
\begin{axis}[smallplot,at={(9.2cm,0)},ylabel={$1/[A]$},title={second order}] \addplot[blue,very thick,domain=0:4]{1+x}; \end{axis}
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** A reactant falls from $$0.800$$ to $$0.400\ M$$ in 10 seconds, then to $$0.200\ M$$ in another 20 seconds. Is a constant first-order half-life consistent with these data?

No. Successive half-lives increase from 10 to 20 seconds. For second-order decay, $$1/[A]$$ increases by $$1.25\ M^{-1}$$ in 10 seconds and $$2.50\ M^{-1}$$ in 20 seconds, giving the same slope $$0.125\ M^{-1}s^{-1}$$. The data instead support second-order behavior.

</div>

---

## Arrhenius equation

The **Arrhenius equation** relates the rate constant to temperature:

$$
k = A e^{-E_a/(RT)}.
$$

$$A$$ is the pre-exponential factor (collision frequency and orientation factors); $$R = 8.314 \text{ J/(mol}\cdot\text{K)}$$ when $$E_a$$ is in $$\text{J/mol}$$; $$T$$ is kelvin.

The logarithmic linear form is

$$
\ln k = -\frac{E_a}{R}\cdot\frac{1}{T} + \ln A.
$$

A plot of $$\ln k$$ versus $$1/T$$ has slope $$-E_a/R$$ and intercept $$\ln A$$. The two-point relation is

$$
\ln\frac{k_2}{k_1} = -\frac{E_a}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right).
$$

For the same reaction under the same conditions, a larger $$k$$ always goes with a higher temperature, because $$e^{-E_a/(RT)}$$ increases when $$T$$ increases. A modest rise in $$T$$ can change $$k$$ dramatically because it sits in an exponential.

<div class="theorem-box">

**Example.** Two reactions have equal rate constants at $$300\ K$$ but different activation energies. Under the Arrhenius model with fixed pre-exponential factors, which rate constant increases by the larger factor when heated?

From $$\ln(k_2/k_1)=E_a(1/T_1-1/T_2)/R$$, the temperature factor is positive when heated. Larger $$E_a$$ gives a larger logarithmic increase. A larger barrier means stronger temperature sensitivity, not necessarily a larger absolute rate constant at the original temperature.

</div>

---

## Reaction mechanisms

Many balanced equations are net processes built from simpler **elementary steps**. Each elementary step has a **molecularity**—the number of reactant particles that must collide in that step (unimolecular, bimolecular, termolecular in the rare cases textbooks treat). For an elementary step only, rate-law exponents match stoichiometric coefficients for that step.

A **reaction mechanism** proposes a sequence of such steps. Species produced in one step and consumed in another, never appearing in the net equation, are **intermediates**. A **catalyst** is regenerated after the cycle; an intermediate is made and then used up. **Transition states** (or **activated complexes**) are high-energy configurations at barrier maxima along the path; they are not stable intermediates you bottle.

The **rate-determining step** (RDS) is the slowest step; it has the highest activation energy in the sequence and usually controls the observed rate law. If the first step is slow, its elementary law often appears directly in the experimental rate law (exponents from that step’s stoichiometry). Steps after the RDS do not change the concentration dependence of the rate law (they only consume intermediates as they leak out of the bottleneck).

If the experimental rate law does not match the stoichiometry of the overall equation, you infer multiple steps and a slow step that controls rate.

<div class="theorem-box">

**Example.** A proposed mechanism is $$A+B\rightarrow I$$ followed by $$I+B\rightarrow P$$. Identify the intermediate and overall reaction, and decide whether the overall equation alone proves a second-order dependence on B.

Adding steps cancels I and gives $$A+2B\rightarrow P$$. I is an intermediate because it forms and is consumed. Overall coefficients do not determine the rate law; the slow step and any preceding equilibrium must be specified before assigning concentration exponents.

</div>

---

## Pre-equilibrium and deriving rate laws

When the RDS is not the first step, a common pattern is a fast, reversible early step followed by a slow step. The early step sets up **pre-equilibrium**: forward and reverse rates of that step are large, so an equilibrium constant $$K$$ links intermediates to reactant concentrations. You write the rate law from the RDS (using its elementary exponents), then substitute for any intermediate using the equilibrium expression from the fast step so that only overall reactants (and catalysts if present) appear in the final law. A more general **steady-state approximation** treats $$d[\text{intermediate}]/dt \approx 0$$ when the intermediate is consumed as fast as it forms; AP problems often give setups where pre-equilibrium is enough.

Example mechanism:

1. $$\text{A} + \text{B} \rightleftharpoons \text{I}$$ fast
2. $$\text{I} + \text{C} \longrightarrow \text{D}$$ slow

The slow elementary step gives

$$
\text{rate} = k_2[\text{I}][\text{C}].
$$

Because the intermediate $$\text{I}$$ should not appear in the final experimental rate law, use the fast pre-equilibrium:

$$
K = \frac{[\text{I}]}{[\text{A}][\text{B}]}
\qquad\Rightarrow\qquad
[\text{I}] = K[\text{A}][\text{B}].
$$

Substitution gives

$$
\text{rate} = k_2K[\text{A}][\text{B}][\text{C}] = k_{\text{obs}}[\text{A}][\text{B}][\text{C}].
$$

### Catalytic cycles

A **catalytic cycle** is a mechanism where the catalyst is consumed in an early elementary step and regenerated in a later step. The catalyst cancels from the net equation, but it can still appear in the rate law because its concentration affects how much of the faster pathway is available.

Simple acid-catalyzed pattern:

1. $$\text{S} + \text{H}^+ \rightleftharpoons \text{SH}^+$$ fast
2. $$\text{SH}^+ \longrightarrow \text{P} + \text{H}^+$$ slow or product-forming

Adding the steps cancels $$\text{H}^+$$, so acid is not consumed overall. However, increasing $$[\text{H}^+]$$ can increase $$[\text{SH}^+]$$ and raise the observed rate.

For heterogeneous catalysts, the same cycle idea happens on a surface:

1. Reactants **adsorb** to active sites.
2. Bonds weaken or orient correctly on the surface.
3. Products form and **desorb**, freeing the active site.

Catalyst poisoning occurs when another species binds strongly to active sites and blocks the cycle. Finely divided catalysts usually work faster because they expose more surface area and therefore more active sites.

<div class="theorem-box">

**Example.** Consider $$\mathrm{C+A\rightarrow I}$$ followed by $$\mathrm{I+B\rightarrow C+P}$$. Identify the catalyst and intermediate, derive the net reaction, and explain why neither belongs in its stoichiometric equation.

C is consumed and then regenerated, so it is the catalyst. I is formed and then consumed, so it is the intermediate. Adding the steps cancels both and gives $$\mathrm{A+B\rightarrow P}$$. Although the catalyst is absent from the net equation, its concentration can affect the rate; cancellation from stoichiometry does not imply kinetic irrelevance.

</div>

---

## Reaction coordinate diagrams

A **reaction coordinate** diagram plots energy versus progress from reactants to products. If reactants lie higher in energy than products, the net reaction is exothermic ($$\Delta H < 0$$ in the usual convention); if products lie higher, it is endothermic ($$\Delta H > 0$$). Forward and reverse activation energies $$E_{a,\text{fwd}}$$ and $$E_{a,\text{rev}}$$ are measured from each side up to the transition state. For a simple one-step profile,

$$
E_{a,\text{fwd}} - E_{a,\text{rev}} = \Delta H.
$$

A catalyst lowers $$E_{a,\text{fwd}}$$ and $$E_{a,\text{rev}}$$ by about the same amount (same pathway lowering for forward and reverse), so it speeds approach to equilibrium but does not change $$\Delta H$$ or the equilibrium constant at fixed $$T$$.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[axis lines=left,width=9cm,height=5.5cm,xmin=0,xmax=10,ymin=0,ymax=8,xtick=\empty,ytick=\empty,xlabel={reaction progress},ylabel={energy}]
\addplot[blue,very thick,samples=160,domain=0:10]{2+4*exp(-0.45*(x-4)^2)-0.08*x};
\addplot[red,dashed,very thick,samples=160,domain=0:10]{2+2.4*exp(-0.45*(x-4)^2)-0.08*x};
\addplot[dashed] coordinates {(0.7,2) (4,6)};
\addplot[dashed] coordinates {(9.3,1.25) (4,6)};
\node at (axis cs:1,2.4) {reactants}; \node at (axis cs:4,6.5) {TS}; \node at (axis cs:8.8,1.6) {products};
\node[red] at (axis cs:5.8,3.7) {catalyzed};
\end{axis}
\end{tikzpicture}
```

### Multi-step profiles

A reaction coordinate diagram for a **multi-step** mechanism has one "hill" per elementary step, with a **valley** between hills for each **intermediate** (a real, if short-lived, species that sits in a local energy minimum). The number of peaks tells you the number of elementary steps; the number of valleys between reactants and products tells you the number of intermediates.

The **tallest peak** corresponds to the step with the largest activation energy—the **rate-determining step**. Reading these diagrams lets you connect the energy picture directly to the mechanism: a high first hill followed by a low second hill means the first step is rate-determining, and the observed rate law should reflect that step's stoichiometry.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[axis lines=left,width=9cm,height=5.5cm,xmin=0,xmax=10,ymin=0,ymax=8,xtick=\empty,ytick=\empty,xlabel={reaction progress},ylabel={energy}]
\addplot[blue,very thick,samples=220,domain=0:10]{2+3.2*exp(-0.7*(x-2.7)^2)+5*exp(-0.7*(x-6.7)^2)-1.1*exp(-0.9*(x-4.6)^2)-0.05*x};
\node at (axis cs:2.7,5.6) {TS 1}; \node at (axis cs:6.7,7.1) {TS 2};
\node at (axis cs:4.6,1.9) {intermediate};
\node[anchor=west] at (axis cs:6.9,6.1) {rate-determining step};
\end{axis}
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** A two-step energy profile has reactants at $$0$$, the first transition state at $$50$$, an intermediate at $$-30$$, the second transition state at $$40$$, and products at $$-60\ \mathrm{kJ/mol}$$. Which forward step has the larger barrier?

The first barrier is $$50-0=50\ \mathrm{kJ/mol}$$. The second is $$40-(-30)=70\ \mathrm{kJ/mol}$$, even though its peak is lower on the page. Each barrier is measured from the preceding minimum. With comparable prefactors, the second elementary step has the smaller rate constant, though the overall observed rate also depends on intermediate concentration. The net enthalpy is $$-60\ \mathrm{kJ/mol}$$, not either barrier height.

</div>

---

## Transition state and catalysis (summary)

Along the reaction coordinate, the **transition state** (or **activated complex**) sits at an energy maximum separating reactants from products—the peak that must be crossed for the rearrangement to complete.

A **catalyst** provides an alternative pathway with lower activation energy. It is regenerated by the end of the cycle and does not appear in the net reaction. A catalyst increases $$k$$ (both forward and reverse for a reversible path) and speeds approach to equilibrium but does not change $$\Delta G^\circ$$ or the equilibrium constant for a given reaction at fixed $$T$$.

<div class="theorem-box">

**Example.** A catalyst lowers the forward barrier by $$15\ \mathrm{kJ/mol}$$ for a reaction with unchanged reactants and products. Explain whether it can lower the products' enthalpy as well.

A catalyst changes the route between the same initial and final states; it does not change their enthalpies. In a simple one-barrier picture the reverse barrier also falls by 15, leaving $$E_{a,fwd}-E_{a,rev}=\Delta H$$ unchanged. Faster product formation does not imply a different reaction enthalpy.

</div>

---

## Kinetics vs equilibrium (preview)

For a reversible elementary reaction, forward and reverse rates balance at equilibrium, linking rate constants to an equilibrium constant in simple cases. The [equilibrium notes](/notes/ap/chem/equilibrium/) develop this connection. Kinetics describes how fast a reaction proceeds; equilibrium describes the composition it approaches under fixed conditions.

<div class="theorem-box">

**Example.** A reaction has a very large equilibrium constant but no detectable conversion during a short experiment. Explain why both observations can be true.

Large K says products dominate at equilibrium. A high activation barrier can prevent the system from reaching that composition on the experimental timescale. A catalyst can shorten that timescale but cannot make K larger at the same temperature.

</div>

---


## Practice

### MCQ

::::problem
1. Doubling A alone quadruples rate, while doubling both A and B increases rate eightfold. What is the overall reaction order?

   (A) 1<br>
   (B) 2<br>
   (C) 3<br>
   (D) 4

:::solution
A is second order because $$2^m=4$$. B contributes the remaining factor of two, so it is first order. The sum of the exponents is three; the factor of eight is not itself the order.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
2. For $$2A\rightarrow B$$, A disappears at $$0.040\ M/s$$. What is the formation rate of B?

   (A) $$0.080\ M/s$$<br>
   (B) $$0.040\ M/s$$<br>
   (C) $$0.020\ M/s$$<br>
   (D) $$0.010\ M/s$$

:::solution
Two A are consumed per B formed, so $$d[B]/dt=-\tfrac12d[A]/dt=0.020\ M/s$$. Rates for different species require the stoichiometric coefficients even when the kinetic order is unknown.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
3. A first-order reactant falls from $$0.800$$ to $$0.200\ M$$ in $$40.0\ s$$. How much additional time is needed to reach $$0.0500\ M$$?

   (A) 10.0 s<br>
   (B) 20.0 s<br>
   (C) 40.0 s<br>
   (D) 80.0 s

:::solution
Each fourfold drop takes two half-lives. The first interval establishes a 20.0 s half-life, so the second fourfold drop also takes 40.0 s. Constant first-order half-life does not mean constant absolute concentration loss.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
4. For a second-order decay, which change follows when initial concentration doubles at fixed temperature?

   (A) Initial rate doubles and half-life doubles<br>
   (B) Initial rate quadruples and half-life halves<br>
   (C) Initial rate quadruples and half-life is unchanged<br>
   (D) Initial rate is unchanged and half-life halves

:::solution
The law $$r=k[A]^2$$ makes initial rate four times larger. The second-order half-life $$1/(k[A]_0)$$ becomes half as long. The constant k stays fixed because temperature and reaction conditions otherwise stay fixed.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
5. For a fast pre-equilibrium $$A+B\rightleftharpoons I$$ followed by slow $$I+A\rightarrow P$$, which rate law follows?

   (A) $$k[A][B]$$<br>
   (B) $$k[I]$$ only<br>
   (C) $$k[A][B]^2$$<br>
   (D) $$k[A]^2[B]$$

:::solution
Slow-step rate is $$k_2[I][A]$$ and pre-equilibrium gives $$[I]=K_1[A][B]$$. Substitution yields $$k_2K_1[A]^2[B]$$. The observed law must eliminate the intermediate.

$$
\boxed{\text{D}}.
$$
:::
::::

::::problem
6. A one-step reaction has forward activation energy 75 and enthalpy change $$-25\ \mathrm{kJ/mol}$$. A catalyst lowers the transition-state energy by $$20\ \mathrm{kJ/mol}$$. What is the catalyzed reverse barrier?

   (A) $$80\ \mathrm{kJ/mol}$$<br>
   (B) $$55\ \mathrm{kJ/mol}$$<br>
   (C) $$30\ \mathrm{kJ/mol}$$<br>
   (D) $$100\ \mathrm{kJ/mol}$$

:::solution
Uncatalyzed reverse barrier is $$75-(-25)=100$$. Lowering the transition state by 20 makes it 80. The products' energy stays fixed; the catalyzed forward barrier is 55 and $$55-80=-25$$ still holds.

$$
\boxed{\text{A}}.
$$
:::
::::

### FRQ

::::frq{id=chem-kinetics-1}
7. A first-order decomposition has rate constant $$k=0.0300\ \text{s}^{-1}$$.

   $$(A)$$ Calculate the half-life.

   $$(B)$$ If the initial concentration is $$0.800\ M$$, calculate the concentration after $$60.0\ \text{s}$$.

   $$(C)$$ Explain how the slope of a graph of $$\ln[A]$$ versus time is related to $$k$$.

   $$(D)$$ **Original extension.** Calculate the time required for $$90.0\%$$ of the reactant to decompose. Would doubling the initial concentration change this time? Justify mathematically.

:::solution
$$(A)$$ For a first-order reaction,

$$
t_{1/2}=\frac{0.693}{k}.
$$

Thus

$$
t_{1/2}=\frac{0.693}{0.0300}=23.1\ \text{s}.
$$

The units are seconds because the rate constant has units of $$\text{s}^{-1}$$ for a first-order reaction.

$$(B)$$ Use the integrated rate law:

$$
\ln[A]_t=\ln[A]_0-kt.
$$

Equivalently,

$$
[A]_t=[A]_0e^{-kt}=0.800e^{-(0.0300)(60.0)}.
$$

$$
[A]_t=0.132\ M.
$$

This is less than the initial $$0.800\ M$$, which is reasonable because the reactant is decomposing over time.

$$(C)$$ For a first-order reaction, a graph of $$\ln[A]$$ versus time is linear with slope

$$
\boxed{-k}.
$$

The negative slope shows that $$[A]$$ decreases as time increases. The magnitude of the slope gives the rate constant, so a steeper negative line means a faster first-order reaction.

$$(D)$$ When $$90.0\%$$ has decomposed, $$[A]_t/[A]_0=0.100$$. Thus $$t=-\ln(0.100)/(0.0300\ \text{s}^{-1})=76.8\ \text{s}$$. The integrated law depends on the fraction remaining, so doubling the initial concentration does not change this time at fixed temperature. It does double the initial rate $$k[A]_0$$. A larger absolute rate is therefore compatible with the same time to consume a given fraction.
:::
::::

::::frq{id=chem-kinetics-2}
8. The 2026 AP Chemistry exam included a kinetics question using concentration-time data and a graph of natural log of concentration. (Adapted from College Board, [2026 AP Chemistry FRQ 2](https://apcentral.collegeboard.org/media/pdf/ap26-frq-chemistry.pdf).)

   $$(A)$$ Explain how concentration-time data can support that a reaction is first order in a reactant.

   $$(B)$$ If a plot of $$\ln[A]$$ versus time has slope $$-0.0150\ \text{s}^{-1}$$, identify $$k$$.

   $$(C)$$ Calculate the half-life for the reaction.

   $$(D)$$ **Original extension.** A second run starts at twice the original reactant concentration but at the same temperature. Compare its initial rate, half-life, and slope on a plot of $$\ln[A]$$ versus time.

:::solution
$$(A)$$ If a plot of $$\ln[A]$$ versus time is linear, the data support a first-order relationship in $$A$$. Equivalently, the concentration should decrease by the same fraction over equal time intervals. A plot of $$[A]$$ versus time or $$1/[A]$$ versus time would be used to test zero-order or second-order behavior, so the linear graph identifies the order.

$$(B)$$ For a first-order reaction, the slope is $$-k$$, so

$$
k=0.0150\ \text{s}^{-1}.
$$

The sign of $$k$$ is positive; the negative sign belongs to the slope because the concentration is decreasing.

$$(C)$$

$$
t_{1/2}=\frac{0.693}{k}=\frac{0.693}{0.0150}=46.2\ \text{s}.
$$

For a first-order reaction, this half-life is constant, meaning every $$46.2\ \text{s}$$ the concentration is cut in half regardless of the starting concentration.

$$(D)$$ A linear $$\ln[A]$$ plot indicates first-order behavior, so the initial rate $$k[A]_0$$ doubles. The half-life remains $$\ln 2/0.0150=46.2\ \text{s}$$ because it does not depend on the initial concentration. The slope remains $$-k=-0.0150\ \text{s}^{-1}$$; only the vertical intercept increases, by $$\ln 2$$. Changing the amount of reactant does not itself change the rate constant.
:::
::::
