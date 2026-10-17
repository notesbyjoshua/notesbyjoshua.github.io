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

:::equations

| Idea | Equation | Conditions |
| --- | --- | --- |
| Reaction rate | $$r=-\frac1a\frac{d[A]}{dt}=\frac1p\frac{d[P]}{dt}$$ | For $$aA\rightarrow pP$$; distinguish species rates. |
| Experimental rate law | $$r=k[A]^m[B]^n$$; $$r_2/r_1=([A]_2/[A]_1)^m([B]_2/[B]_1)^n$$ | Compare trials at the same temperature. |
| Zero-order decay | $$[A]_t=[A]_0-kt$$; $$t_{1/2}=[A]_0/(2k)$$ | For $$-d[A]/dt=k$$ over the valid concentration range. |
| First-order decay | $$\ln([A]_t/[A]_0)=-kt$$; $$t_{1/2}=\ln2/k$$ | For $$-d[A]/dt=k[A]$$; apply any instantaneous dilution separately. |
| Second-order decay | $$1/[A]_t=1/[A]_0+kt$$; $$t_{1/2}=1/(k[A]_0)$$ | For $$-d[A]/dt=k[A]^2$$, with k defined for disappearance of A. |
| Arrhenius | $$k=Ae^{-E_a/(RT)}$$; $$\ln(k_2/k_1)=-E_a(1/T_2-1/T_1)/R$$ | Fixed mechanism and approximately constant prefactor; use kelvin. |
| Fast pre-equilibrium | $$K_1=[I]/([A][B])$$ | For $$A+B\rightleftharpoons I$$; substitute into the slow-step law. |
| Pseudo-first-order | $$k_{obs}=k[B]$$ | For $$-d[A]/dt=k[A][B]$$ with B effectively constant. |
| Barrier comparison | $$E_{a,f}-E_{a,r}=\Delta H$$ | For a shared transition state on an enthalpy profile. |

:::

## Practice

### MCQ

::::problem
1. At fixed temperature, doubling A and halving B doubles the initial rate. Tripling A and doubling B increases it eighteenfold. Which rate law fits both experiments?

   (A) $$k[A][B]$$<br>
   (B) $$k[A]^2[B]$$<br>
   (C) $$k[A][B]^2$$<br>
   (D) $$k[A]^2[B]^2$$

:::solution
For orders m and n, $$2^m(1/2)^n=2$$ and $$3^m2^n=18$$. The first gives $$m-n=1$$; substituting into the second gives $$3\times6^n=18$$, so $$n=1$$ and $$m=2$$. Neither experiment isolates one reactant, so both ratios must be used together.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
2. A first-order reactant starts at $$0.800\ M$$ with $$k=0.0200\ \mathrm{s^{-1}}$$. After $$20.0\ \mathrm{s}$$, its solution is instantly diluted to twice the volume without changing temperature. What is its concentration at $$50.0\ \mathrm{s}$$ from the start?

   (A) $$0.294\ M$$<br>
   (B) $$0.220\ M$$<br>
   (C) $$0.147\ M$$<br>
   (D) $$0.0736\ M$$

:::solution
Before dilution, concentration is $$0.800e^{-0.0200(20.0)}$$. Dilution halves it, then first-order decay continues for 30.0 s. Combining factors gives $$[A]=0.400e^{-0.0200(50.0)}=0.147\ M$$. Dilution changes concentration but not k or the elapsed reaction time.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
3. For $$-d[A]/dt=k[A]^2$$, concentration falls from $$0.600$$ to $$0.300\ M$$ in $$25.0\ \mathrm{s}$$. What additional time is required to reach $$0.100\ M$$?

   (A) $$25.0\ \mathrm{s}$$<br>
   (B) $$50.0\ \mathrm{s}$$<br>
   (C) $$75.0\ \mathrm{s}$$<br>
   (D) $$100.\ \mathrm{s}$$

:::solution
The reciprocal-concentration slope is $$k=(1/0.300-1/0.600)/25.0=0.0667\ \mathrm{M^{-1}s^{-1}}$$. From 0.300 to 0.100 M, $$\Delta t=(10.0-3.333)/0.0667=100.\ \mathrm{s}$$. Second-order half-lives grow as concentration decreases; equal concentration fractions do not require equal times.

$$
\boxed{\text{D}}.
$$
:::
::::

::::problem
4. For $$r=k[A][B]$$, B is held in large excess. A plot of $$\ln[A]$$ against time has slope $$-0.0400\ \mathrm{s^{-1}}$$ when $$[B]=0.200\ M$$. What slope is expected at $$[B]=0.0500\ M$$ at the same temperature?

   (A) $$-0.0100\ \mathrm{s^{-1}}$$<br>
   (B) $$-0.0400\ \mathrm{s^{-1}}$$<br>
   (C) $$-0.0800\ \mathrm{s^{-1}}$$<br>
   (D) $$-0.160\ \mathrm{s^{-1}}$$

:::solution
The apparent first-order constant is $$k_{obs}=k[B]$$. The first trial gives $$k=0.0400/0.200=0.200\ \mathrm{M^{-1}s^{-1}}$$. The second therefore has $$k_{obs}=0.0100\ \mathrm{s^{-1}}$$. A first-order-looking trace under excess-B conditions does not establish a truly first-order overall law.

$$
\boxed{\text{A}}.
$$
:::
::::

::::problem
5. Reactions X and Y have equal rate constants at $$300\ K$$. Their activation energies are 60.0 and $$30.0\ \mathrm{kJ/mol}$$, respectively. Assuming each follows Arrhenius behavior with a temperature-independent prefactor, what is approximately $$k_X/k_Y$$ at $$330\ K$$? Use $$R=8.314\ \mathrm{J/(mol\,K)}$$.

   (A) $$0.335$$<br>
   (B) $$1.00$$<br>
   (C) $$2.98$$<br>
   (D) $$8.91$$

:::solution
Subtract the two temperature-ratio equations. Since the initial constants match, $$\ln(k_X/k_Y)=(60000-30000)(1/300-1/330)/R=1.09$$. Thus the ratio is about 2.98. The higher-barrier reaction is more temperature-sensitive; equal constants at one temperature do not imply equal prefactors.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
6. For fast $$\mathrm{C+A\rightleftharpoons I}$$ with equilibrium constant K followed by slow $$\mathrm{I+B\rightarrow C+P}$$ with constant $$k_2$$, which result is consistent with the mechanism?

   (A) C is an intermediate and $$r=k_2[A][B]$$<br>
   (B) C is a catalyst and $$r=k_2K[C][A][B]$$<br>
   (C) I is a catalyst and $$r=k_2[I][B]$$ is the fully eliminated law<br>
   (D) C is a catalyst and changing its concentration changes the overall equilibrium constant

:::solution
C is consumed then regenerated, while I is formed then consumed. Pre-equilibrium gives $$[I]=K[C][A]$$, so the slow-step rate becomes $$k_2K[C][A][B]$$. The catalyst can change the rate without changing the equilibrium constant for the net reaction $$A+B\rightleftharpoons P$$.

$$
\boxed{\text{B}}.
$$
:::
::::

### FRQ

::::frq{id=chem-kinetics-challenge-1}
7. A reaction has rate law $$r=k[A]^m[B]^n$$. Three initial-rate trials give: trial 1, $$[A]=0.100\ M$$, $$[B]=0.200\ M$$, $$r=0.00400\ \mathrm{M/s}$$; trial 2, $$[A]=0.200\ M$$, $$[B]=0.100\ M$$, $$r=0.00800\ \mathrm{M/s}$$; trial 3, $$[A]=0.300\ M$$, $$[B]=0.400\ M$$, $$r=0.0720\ \mathrm{M/s}$$. Temperature is constant.

   $$(A)$$ Determine m and n using both independent rate ratios.

   $$(B)$$ Calculate k with units and predict the initial rate at $$[A]=0.150\ M$$ and $$[B]=0.300\ M$$.

   $$(C)$$ Evaluate the mechanism fast $$A+B\rightleftharpoons I$$, then slow $$I+A\rightarrow P$$. Derive its predicted rate law and state whether agreement proves the mechanism.

   $$(D)$$ For that net reaction, calculate the initial disappearance rate of A under the conditions in part B if r is the product-formation rate. Explain the coefficient's role.

:::solution
$$(A)$$ Trials 2 and 1 give $$2=2^m(1/2)^n$$, so $$m-n=1$$. Trials 3 and 1 give $$18=3^m2^n$$. Substituting $$m=n+1$$ gives $$18=3(6^n)$$, hence $$n=1$$ and $$m=2$$. The law is $$r=k[A]^2[B]$$; no trial comparison changes only one reactant, so a single ratio is insufficient.

$$(B)$$ Trial 1 gives $$k=0.00400/((0.100)^2(0.200))=2.00\ \mathrm{M^{-2}s^{-1}}$$. The predicted rate is $$2.00(0.150)^2(0.300)=0.0135\ \mathrm{M/s}$$. The units follow from dividing M/s by M cubed, not from assuming every rate constant has units of inverse seconds.

$$(C)$$ The slow step predicts $$r=k_2[I][A]$$. Pre-equilibrium gives $$[I]=K_1[A][B]$$, producing $$r=k_2K_1[A]^2[B]$$, consistent with the measured orders. The intermediate I cancels from the net reaction $$2A+B\rightarrow P$$. Agreement supports this mechanism but does not prove uniqueness; different mechanisms can generate the same rate law.

$$(D)$$ The net equation consumes two A for each P formed, so $$-d[A]/dt=2r=0.0270\ \mathrm{M/s}$$. The rate law predicts the defined reaction rate, whereas the species disappearance rate includes its stoichiometric coefficient. The coefficient 2 in the overall equation does not by itself prove second order in A; that order came from the experiments and is explained by the proposed mechanism.
:::
::::

::::frq{id=chem-kinetics-challenge-2}
8. A colored reactant A is the only absorber at a chosen wavelength. After blank correction, its absorbances at 0, 40.0, and 80.0 s are 0.800, 0.400, and 0.200. Path length and temperature are fixed, and Beer-Lambert behavior is linear. A separate run at a higher temperature has first-order rate constant twice the original value.

   $$(A)$$ Use the data to support a first-order model and calculate k. Explain what additional evidence would strengthen the inference.

   $$(B)$$ At 80.0 s, the solution is instantly diluted to three times its volume. Calculate the absorbance at 120.0 s at the original temperature and path length.

   $$(C)$$ The two temperatures are 300 and 315 K. Estimate the activation energy using $$R=8.314\ \mathrm{J/(mol\,K)}$$ and a fixed Arrhenius prefactor.

   $$(D)$$ If an uncorrected constant absorbance of 0.050 were present, would a plot of the logarithm of raw absorbance remain exactly linear? Explain the late-time effect.

:::solution
$$(A)$$ Absorbance is proportional to concentration, and the same fraction, one-half, remains after each 40.0 s interval. This supports constant half-life and first-order decay. Thus $$k=\ln2/40.0=0.0173\ \mathrm{s^{-1}}$$. More time points giving a straight line of $$\ln A_{abs}$$ versus time, with no systematic residual pattern, would provide a stronger test than only three measurements.

$$(B)$$ Dilution changes absorbance immediately from 0.200 to $$0.200/3=0.0667$$. Another 40.0 s is one half-life, so absorbance falls to $$0.0333$$ at 120.0 s. The reaction constant is unchanged by this dilution in the assumed first-order model; the concentration jump must be applied separately from time decay.

$$(C)$$ The two-temperature equation gives $$\ln2=(E_a/R)(1/300-1/315)$$. Therefore $$E_a=8.314\ln2/(1/300-1/315)=3.63\times10^4\ \mathrm{J/mol}=36.3\ \mathrm{kJ/mol}$$. Absolute temperatures and a joule-compatible R are required. Doubling k at this temperature interval does not imply a universal doubling for every 15 K increase.

$$(D)$$ Raw absorbance would be $$A_{raw}=A_{solute}+0.050$$. The logarithm of that sum is not the logarithm of the exponentially decaying solute plus a constant. At late times, raw absorbance approaches 0.050 rather than zero, and its logarithm levels off. A late-time straight-line fit would then underestimate the magnitude of the first-order decay slope.
:::
::::
