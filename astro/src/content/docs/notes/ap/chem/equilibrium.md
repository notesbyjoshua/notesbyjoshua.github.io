---
title: "Unit 7: Equilibrium"
description: "AP Chemistry notes on equilibrium, reaction quotients, equilibrium constants, ICE tables, Le Chatelier's principle, and solubility."
sidebar:
  order: 7
---

## Chemical Equilibrium

Most reactions we have looked at previously were **irreversible reactions**, or reactions that can only go one way (forward). A **reversible reaction** can run in both directions (forward and backwards). In a **closed system** (no escape of matter), the forward reaction consumes reactants and forms products, while the reverse reaction does the opposite. **Chemical equilibrium** is reached when the **rate of the forward reaction** equals the **rate of the reverse reaction**. At that point:

- **Concentrations** (or for gases, **partial pressures**) remain **constant** over time (they are **not** necessarily equal to one another)
- The system is **dynamic**: molecules still react, but there is **no net** change in amounts. This is different from a **completed** or **irreversible** reaction, where at least one reactant is effectively exhausted and the process does not establish a lasting balance between forward and reverse paths at ordinary conditions.

The approach to equilibrium has a characteristic shape: starting from pure reactants, the **forward rate** is high (reactant concentrations are large) and the **reverse rate** is zero. As products build up, the forward rate falls and the reverse rate rises until the two are **equal**—from that moment on, concentrations level off and stay flat. "Equal rates" does *not* mean "equal concentrations": the equilibrium mixture can favor either reactants or products depending on $$K$$.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[width=9cm,height=4cm,xmin=0,xmax=8,ymin=0,ymax=5,axis lines=left,xtick=\empty,ytick=\empty,xlabel={time},ylabel={concentration}]
\addplot[blue,very thick,samples=120,domain=0:8]{1.5+3*exp(-0.55*x)};
\addplot[red,very thick,samples=120,domain=0:8]{3.7-2.2*exp(-0.55*x)};
\node[blue] at (axis cs:1.4,3.7) {reactants}; \node[red] at (axis cs:5,3.2) {products};
\end{axis}
\begin{axis}[at={(0,-3.8cm)},width=9cm,height=4cm,xmin=0,xmax=8,ymin=0,ymax=5,axis lines=left,xtick=\empty,ytick=\empty,xlabel={time},ylabel={rate}]
\addplot[blue,very thick,samples=120,domain=0:8]{1.8+2.2*exp(-0.55*x)};
\addplot[red,very thick,samples=120,domain=0:8]{1.8-1.4*exp(-0.55*x)};
\node at (axis cs:5.6,1.8) {equal rates};
\end{axis}
\end{tikzpicture}
```

**Homogeneous** equilibrium means all reacting species are in the same phase (e.g. all gases, or all in one solution). **Heterogeneous** equilibrium includes **pure solids** or **pure liquids** as separate phases; their activities are taken as constant and they are **omitted** from the equilibrium expression (see below).

<div class="theorem-box">

**Example.** In a sealed vessel at equilibrium, product concentration is twice reactant concentration. A student says the reverse rate must therefore be twice the forward rate. Evaluate the claim.

Equilibrium requires equal forward and reverse rates, not equal concentrations. Different rate constants and concentration dependences allow unequal amounts while the two rates balance. Constant measured concentrations establish no net change; they do not imply that molecular reactions have stopped.

</div>

---

## Equilibrium constant $$K_c$$

For a balanced reaction in solution (molar concentrations in $$\text{mol/L}$$),

$$
j\text{A} + k\text{B} \rightleftharpoons l\text{C} + m\text{D},
$$

the **equilibrium constant** in terms of concentration is

$$
K_c = \frac{[\text{C}]^l [\text{D}]^m}{[\text{A}]^j [\text{B}]^k},
$$

where each $$[]$$ is the equilibrium molarity raised to the power of the **stoichiometric coefficient**. Only **aqueous** solutes or gases appear in $$K_c$$, since the concentrations of pure solids/liquids do not change, and therefore are always assumed to be 1. In addition, $$K_c$$ will not change unless temperature changes, so $$K_c$$ is only **temperature-dependent**.

On the AP exam, $$K$$ is treated as a dimensionless ratio by implicitly comparing each concentration to a **standard reference** (standard state). Regardless, you should still use the same algebraic form when you set up problems.

### Extreme $$K_c$$ value rules

**Orders of magnitude** help you judge extent (at a given temperature):

- If $$K_c$$ is very large (e.g. $$K_c \gg 1$$, sometimes textbook thresholds like $$K_c > 10^{10}$$), the **forward** reaction is **product-favored** at equilibrium—substantial conversion to products. This usually means that the forward reaction is approximately an **irreversible** reaction
- If $$K_c$$ is very small (e.g. $$K_c \ll 1$$, sometimes $$K_c < 10^{-10}$$), the mixture stays **reactant-heavy**, meaning that the reaction basically did not start at all.

These cutoffs are rules of thumb; what matters is comparing $$Q$$ to $$K$$ and interpreting $$K$$ relative to $$1$$.

<div class="theorem-box">

**Example.** A reaction has $$K_c=10^{12}$$ but produces no detectable product during a short observation. Must either the measurement or the equilibrium constant be wrong?

No. The large constant predicts a product-favored equilibrium composition, not the time needed to reach it. A large activation barrier can make the forward rate extremely small. A catalyst could help the mixture approach equilibrium faster without changing $$K_c$$. Thermodynamic preference and observable reaction speed answer different questions.

</div>

### Manipulating $$K$$ for related equations

- **Reverse reaction:**
  $$
  K_{c,\text{reverse}} = \frac{1}{K_{c,\text{forward}}}.
  $$
- **Multiply the whole equation by an integer $$n$$:**
  $$
  K_c' = (K_c)^n
  $$
- **Add sequential steps** (all at the same temperature): the overall $$K$$ is the **product** of the step constants:
  $$
  K_{\text{overall}} = K_1 \times K_2 \times \cdots
  $$

<div class="theorem-box">

**Example.** For $$A\rightleftharpoons2B$$, $$K=9$$. Find K for $$B\rightleftharpoons\tfrac12 A$$ and explain why taking only the reciprocal is insufficient.

Reversing gives $$2B\rightleftharpoons A$$ with constant $$1/9$$. Dividing all coefficients by two takes its square root, giving $$K'=1/3$$. The equilibrium expression has both its numerator/denominator and its exponents changed.

</div>

---

## Equilibrium in the gas phase: $$K_p$$

For gas-phase equilibria it is often convenient to use **partial pressures** (in atmospheres on the AP exam, unless stated otherwise). For

$$
j\text{A}(g) + k\text{B}(g) \rightleftharpoons l\text{C}(g) + m\text{D}(g),
$$

define

$$
K_p = \frac{(P_{\text{C}})^l (P_{\text{D}})^m}{(P_{\text{A}})^j (P_{\text{B}})^k}.
$$

Only gaseous species appear (since aqueous solutions and pure solids/liquids do not have partial pressures). From the ideal gas law, $$P = (\text{n/V})RT = MRT$$ for a gas (M = molarity). The standard relationship is

$$
K_p = K_c (RT)^{\Delta n_{\text{gas}}},
$$

where $$\Delta n_{\text{gas}}$$ is difference between the amount of moles of products and reactants (from the balanced equation), and $$R$$ must be **consistent** with the pressure units used (e.g. $$R = 0.0821\ \text{L·atm/(mol·K)}$$ when $$P$$ is in atm).

<div class="theorem-box">

**Example.** For $$\mathrm{N_2O_4(g)\rightleftharpoons2NO_2(g)}$$, a student sets $$K_p=K_c$$ because all species are gases. Identify the missing factor.

The change in gas mole coefficients is $$\Delta n=2-1=1$$. With the usual textbook unit convention, $$K_p=K_c(RT)$$. Equality would follow for $$\Delta n=0$$, not merely from all species being gaseous. Temperature must be expressed in kelvin and R must match pressure units.

</div>

---

## Reaction quotient $$Q$$

The **reaction quotient** has the **same algebraic form** as $$K$$, but it uses concentrations or pressures at any instant, not necessarily at equilibrium.

For concentrations:

$$
Q_c = \frac{[\text{C}]^l [\text{D}]^m}{[\text{A}]^j [\text{B}]^k}.
$$

### Interpreting $$Q_c$$ vs $$K_c$$

- If $$Q < K$$, the ratio of products to reactants is **too small** for equilibrium; the system shifts **right** (toward products).
- If $$Q > K$$, the ratio is **too large**; the system shifts **left** (toward reactants).
- If $$Q = K$$, the system is **at equilibrium**.

A useful trick is to line up $$K$$ and $$Q$$ alphabetically (so $$K$$ on the left and $$Q$$ on the right), and whatever direction the sign goes (e.g. < (less than) goes left) is the direction the reaction goes.

The same logic applies to $$Q_p$$ and $$K_p$$ for gases.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing,angles,quotes}
\begin{tikzpicture}[>=Stealth, font=\small]
\draw[->, thick] (-4,0) -- (4,0) node[right] {$Q$};
\draw[very thick] (0,-0.25) -- (0,0.25) node[above] {$Q=K$};
\node[align=center] at (-2,0.7) {$Q<K$\\shift right\\toward products};
\node[align=center] at (2,0.7) {$Q>K$\\shift left\\toward reactants};
\draw[->, blue, thick] (-3,-0.7) -- (-0.4,-0.7); \draw[->, red, thick] (3,-0.7) -- (0.4,-0.7);
\end{tikzpicture}
```

A **catalyst** speeds both forward and reverse rates equally, so it **does not change** $$K$$ or the equilibrium position - it only shortens the time needed to reach equilibrium.

<div class="theorem-box">

**Example.** For $$A\rightleftharpoons2B$$, an equilibrium mixture is suddenly compressed to half its volume at fixed temperature. Compare the new Q with K before any reaction occurs.

Both concentrations double, so $$Q'=\frac{(2[B])^2}{2[A]}=2K$$. The reverse reaction is favored, reducing B and forming A. Tracking the concentration powers explains the shift without assuming that every compression favors reactants.

</div>

---

## Gibbs free energy and equilibrium

The link between standard Gibbs free energy change and the equilibrium constant (same temperature) is

$$
\Delta G^\circ = -RT \ln K,
$$

where $$K$$ is $$K_c$$ or $$K_p$$ according to how the reaction is expressed, and *must match* the standard-state convention your course uses. For many AP problems, $$K$$ is $$K_c$$ for solution chemistry and $$K_p$$ when all species are gases and the expression is written in pressures. The Gibbs free energy value determines if a reaction is spontaneous, which is talked about more in [Unit 9](/notes/ap/chem/thermoelectro/).

Qualitative connections (at standard conditions, using $$K$$ relative to $$1$$):

- If $$K > 1$$, then $$\Delta G^\circ < 0$$: the forward reaction is **thermodynamically favorable (spontaneous)** under standard conditions.
- If $$K < 1$$, then $$\Delta G^\circ > 0$$: the reverse direction is favored under standard conditions and the forward reaction is **not spontaneous**.
- If $$K = 1$$, then $$\Delta G^\circ = 0$$, meaning the reaction is **at equilibrium**.

For *nonstandard* conditions, the reaction quotient enters:

$$
\Delta G = \Delta G^\circ + RT \ln Q.
$$

At equilibrium, $$Q = K$$ and $$\Delta G = 0$$, which recovers $$\Delta G^\circ = -RT \ln K$$. Here $$R$$ is the gas constant ($$8.314\ \text{J/(mol·K)}$$ when using joules), and $$T$$ is kelvin.

### The van’t Hoff equation

Le Châtelier’s principle says that $$K$$ changes with *temperature* only, and the **van’t Hoff equation** makes that dependence quantitative. It follows from the way $$\Delta G^\circ = -RT\ln K$$ combines with $$\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$$ when you ask how $$K$$ must move if $$T$$ changes (treating $$\Delta H^\circ$$ and $$\Delta S^\circ$$ as *approximately constant* over a modest temperature range: a standard AP assumption unless a problem says otherwise).

If $$K_1$$ and $$K_2$$ are equilibrium constants (*same* kind: both $$K_c$$ or both $$K_p$$, matching how the reaction is written) at absolute temperatures $$T_1$$ and $$T_2$$, then

$$
\ln\frac{K_2}{K_1} = -\frac{\Delta H^\circ}{R}\left(\frac{1}{T_2}-\frac{1}{T_1}\right) = \frac{\Delta H^\circ}{R}\left(\frac{1}{T_1}-\frac{1}{T_2}\right).
$$

Here $$\Delta H^\circ$$ is the *standard enthalpy change* for the reaction as written (see [Unit 6: Thermochemistry](/notes/ap/chem/thermochemistry/)). Use $$R = 8.314\ \text{J/(mol·K)}$$ when $$\Delta H^\circ$$ is in **joules per mole** of reaction as written.

**Sign check:** if the forward reaction is *endothermic* ($$\Delta H^\circ > 0$$) and $$T_2 > T_1$$, then $$K_2 > K_1$$—warming *increases* $$K$$, matching the picture that heat acts like a *reactant* in an endothermic forward process. If the forward reaction is *exothermic* ($$\Delta H^\circ < 0$$), raising $$T$$ *decreases* $$K$$.

The **differential** form (useful conceptually and in derivations) is

$$
\frac{d\ln K}{dT} = \frac{\Delta H^\circ}{RT^2},
$$

which shows that sensitivity of $$\ln K$$ to temperature is *larger* when $$\Delta H^\circ$$ is large and when $$T$$ is *low* (through the $$1/T^2$$ factor in how small $$\Delta T$$ steps accumulate).

<div class="theorem-box">

**Example.** For an endothermic reaction, $$\Delta H^\circ=+40.0\ \mathrm{kJ/mol}$$ and $$K_1=2.00$$ at $$300\ K$$. Estimate K at $$330\ K$$, assuming constant reaction enthalpy, and distinguish this change from a catalyst's effect.

Use $$\ln(K_2/K_1)=-(40000/8.314)(1/330-1/300)=1.46$$. Thus $$K_2=2.00e^{1.46}\approx8.59$$. Heating favors the endothermic direction and changes equilibrium composition. A catalyst instead speeds the approach to equilibrium at a given temperature without changing its constant.

</div>

---

## Le Châtelier’s principle

**Le Châtelier’s principle** is a qualitative rule: if a **stress** disturbs an equilibrium, the system shifts in the direction that **partially counteracts** the stress (new equilibrium is established; $$K$$ is unchanged unless **temperature** changes).

Typical stresses:

- **Concentration:** Adding a **reactant** shifts toward **products**; removing a product does the same. Adding **product** shifts toward **reactants**.
- **Pressure (gases):** Reducing volume increases total pressure; the system shifts toward the side with **fewer moles of gas** (if any). Adding an **inert gas** at **constant volume** does **not** change partial pressures of reactants/products—**no** shift. At **constant pressure**, adding inert gas increases volume and can shift the equilibrium; AP questions usually emphasize the constant-volume case.
- **Temperature:** $$K$$ **changes** with temperature. Treat **heat** as part of the reaction: for an **endothermic** forward reaction ($$\Delta H > 0$$), **raising** $$T$$ favors the **forward** direction (larger $$K$$ if the forward reaction is endothermic). For an **exothermic** forward reaction ($$\Delta H < 0$$), **raising** $$T$$ favors the **reverse** direction (smaller $$K$$). **Cooling** favors the exothermic direction.

Since $$K$$ depends on $$T$$, **do not** treat temperature like a simple concentration stress when you need a **numerical** $$K$$: use the correct $$K$$ for the new temperature if given, compute $$K_2$$ from $$K_1$$ with the **van’t Hoff equation** (previous section), or reason qualitatively from $$\Delta H$$.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing,angles,quotes}
\begin{tikzpicture}[>=Stealth, font=\small]
\node[draw, rounded corners, fill=blue!8] (stress) at (0,2) {stress applied};
\node[draw, rounded corners, fill=green!8] (shift) at (0,0.7) {system shifts to reduce stress};
\node[draw, rounded corners] (conc) at (-3,-0.8) {concentration};
\node[draw, rounded corners] (temp) at (0,-0.8) {temperature};
\node[draw, rounded corners] (press) at (3,-0.8) {pressure / volume};
\draw[->, thick] (stress) -- (shift); \draw[->, thick] (shift) -- (conc); \draw[->, thick] (shift) -- (temp); \draw[->, thick] (shift) -- (press);
\node[align=center] at (-3,-1.8) {consume added species\\or replace removed species};
\node[align=center] at (0,-1.8) {treat heat like\\reactant or product};
\node[align=center] at (3,-1.8) {favor fewer or more\\gas moles};
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** Inert gas is added to an ideal-gas equilibrium mixture at fixed temperature and fixed volume. Total pressure rises. Must equilibrium shift toward fewer gas molecules?

No. Each reacting species still has the same $$n_iRT/V$$ partial pressure, so Q stays equal to K. Total pressure alone is insufficient. If instead volume increased at fixed total pressure, reacting-species partial pressures would change and a shift could occur.

</div>

---

## ICE tables

**ICE** stands for **Initial**, **Change**, **Equilibrium**. You use a table to organize amounts (or concentrations) for one reversible process.

**Setup:**

1. Write a **balanced** equation.
2. **Initial** row: given starting concentrations (after any mixing).
3. **Change** row: express unknown change as $$x$$ (or a multiple like $$2x$$ from stoichiometry): reactants **lose** ($$-jx$$, etc.) and products **gain** ($$+lx$$, etc.), although you could swap the signs and have the same result. Note that if one side is 0, it can't lose any concentration, so it must have a positive change!
4. **Equilibrium** row: Initial + Change.

**Rules and tips:**

- Omit **pure solids** and **pure liquids** from the table if they do not define the solution volume.
- If a reactant is **limiting**, one species may be **consumed completely** before equilibrium in a sequential sense; still check whether the reaction can **proceed in reverse** from that state (ICE applies to the equilibrium stage you model).
- **Small $$K$$** (product-poor): equilibrium lies left; $$x$$ may be negligible compared to initial concentrations—**verify** with the **5% rule** (or exact quadratic) when your course allows.
- **Large $$K$$:** equilibrium lies right; sometimes you assume **complete** reaction first, then **back-react** a small amount.

### The small-$$x$$ approximation and the 5% rule

When $$K$$ is small, very little reactant converts, so a term like $$0.500-x$$ in the denominator is barely changed by $$x$$. Approximating $$0.500-x\approx0.500$$ turns an otherwise-quadratic (or worse) equation into one you can solve by simple algebra. The approximation is considered valid when

$$
\frac{x}{[\text{A}]_0}\times100\% \le 5\%,
$$

i.e. $$x$$ is at most $$5\%$$ of the initial concentration it was subtracted from. If the computed $$x$$ fails this test, the approximation is too rough—go back and solve the **quadratic** exactly (or iterate). As a rough guide, the approximation is usually safe when $$[\text{A}]_0/K \gtrsim 400$$.


| Step | Reactants | Products |
| --- | --- | --- |
| Initial | starting concentrations | starting concentrations |
| Change | subtract according to stoichiometry | add according to stoichiometry |
| Equilibrium | initial plus change | initial plus change |

For $$aA+bB\rightleftharpoons cC+dD$$, changes usually look like $$-ax$$, $$-bx$$, $$+cx$$, and $$+dx$$.

<div class="theorem-box">

**Example.** For $$\mathrm{A\rightleftharpoons B+C}$$, start with $$[A]=0.100\ M$$ and no products, with $$K_c=0.0100$$. Test the small-change approximation and calculate the physical root if it fails.

Assuming $$0.100-x\approx0.100$$ gives $$x=\sqrt{0.0100(0.100)}=0.0316\ M$$, or $$31.6\%$$ depletion, so the assumption fails. Instead solve $$x^2/(0.100-x)=0.0100$$, giving $$x^2+0.0100x-0.00100=0$$ and $$x=0.0270\ M$$. The negative root is unphysical because products start at zero. A small numerical K is not enough by itself; the change must be small relative to the starting concentration.

</div>

---

## Solubility equilibrium and $$K_{sp}$$

You might remember the solubility rules from Unit 4. For a **sparingly soluble** ionic solid (basically anything that is considered "insoluble" to water), dissolution is an equilibrium. For example,

$$
\text{A}_m\text{B}_l(s) \rightleftharpoons m\,\text{A}^{a+}(aq) + l\,\text{B}^{b-}(aq).
$$

The **solubility product** is

$$
K_{sp} = [\text{A}^{a+}]^m [\text{B}^{b-}]^l.
$$

The solid (precipitate) does **not** appear in $$K_{sp}$$. This is equivalent to $$K_c$$ but for a dissolution.

### Setting up ICE tables for $$K_{sp}$$

Setting up an ICE table for $$K_{sp}$$ is slightly different from a normal ICE table procedure.

**Setup:**

1. Write a **balanced** equation for solubility (remember that the solid is ALWAYS on the left side).
2. **Initial** row: given starting concentrations (after any mixing). For the concentration of the solid, just write "solid" in that box.
3. **Change** row: This is the same as a regular ICE table.
4. **Equilibrium** row: This is the same as a regular ICE table, except write "solid" for initial for the precipitate.

<div class="theorem-box">

**Example.** For $$\mathrm{Ag_2CrO_4}$$ dissolving in pure water, why is an ICE row of $$+s$$ for both ions incorrect? Write the correct expression.

Each dissolved formula unit produces two silver ions and one chromate ion. Thus the concentration changes are $$+2s$$ for $$\mathrm{Ag^+}$$ and $$+s$$ for $$\mathrm{CrO_4^{2-}}$$. With no initial ions, $$K_{sp}=(2s)^2(s)=4s^3$$. The coefficient affects both the concentration produced and the exponent in the equilibrium expression; these are separate consequences of the same balanced equation.

</div>

### Molar solubility

**Molar solubility** ($$s$$) is the number of **moles of solid** that dissolve per liter of solution to reach saturation (under stated conditions). If one formula unit of $$\text{A}_m\text{B}_l$$ produces $$m$$ ions of $$\text{A}$$ and $$l$$ ions of $$\text{B}$$, then at saturation

$$
[\text{A}^{a+}] = ms, \qquad [\text{B}^{b-}] = ls,
$$

and

$$
K_{sp} = (ms)^m (ls)^l = m^m\, l^l\, s^{m+l}.
$$

Solve for $$s$$ given $$K_{sp}$$, or $$K_{sp}$$ given $$s$$. In an ICE table, the molar solubility is equivalent to the $$x$$ value.

<div class="theorem-box">

**Example.** Two salts have the same numerical $$K_{sp}=1.0\times10^{-12}$$. One dissociates as $$\mathrm{AB}$$ and the other as $$\mathrm{AB_2}$$. Are their molar solubilities equal in pure water?

No. For $$\mathrm{AB}$$, $$K_{sp}=s^2$$ gives $$s=1.0\times10^{-6}\ M$$. For $$\mathrm{AB_2}$$, $$K_{sp}=s(2s)^2=4s^3$$ gives $$s=6.3\times10^{-5}\ M$$. Equal equilibrium constants do not imply equal formula-unit solubilities when dissociation stoichiometries differ. This assumes neither ion undergoes a significant additional reaction.

</div>

### Ion product and precipitation

The **ion product** $$Q_{sp}$$ uses **current** ion concentrations in the $$K_{sp}$$ expression (same form as $$K_{sp}$$).

- If $$Q_{sp} < K_{sp}$$, the solution is *unsaturated*; more solid can dissolve.
- If $$Q_{sp} = K_{sp}$$, the solution is *saturated* (at equilibrium with solid, if present).
- If $$Q_{sp} > K_{sp}$$, *precipitation* occurs until $$Q_{sp}$$ drops to $$K_{sp}$$ (assuming equilibrium can be reached).

<div class="theorem-box">

**Example.** Equal volumes of $$2.0\times10^{-5}\ M$$ silver nitrate and $$2.0\times10^{-5}\ M$$ sodium chloride are mixed. With $$K_{sp}(\mathrm{AgCl})=1.8\times10^{-10}$$, does precipitation begin?

Mixing doubles each solution's volume, so both ion concentrations become $$1.0\times10^{-5}\ M$$ before any reaction. The ion product is $$Q=(1.0\times10^{-5})^2=1.0\times10^{-10}<K_{sp}$$, so precipitation is not predicted. Using the unmixed concentrations gives a false supersaturation result. Dilution must be accounted for before comparing $$Q$$ with $$K_{sp}$$.

</div>

### Common-ion effect

If one of the ions is already present from another source (**common ion**), its higher initial concentration shifts dissolution **left**, **lowering** molar solubility compared to pure water. ICE-style reasoning applies: treat initial $$[\text{A}^{a+}]$$ or $$[\text{B}^{b-}]$$ as nonzero before the solid dissolves further.

<div class="theorem-box">

**Example.** Solid AgCl is present in saturated solution. Add NaCl without appreciably changing the volume. Does the silver concentration decrease because $$K_{sp}$$ decreases?

The temperature is unchanged, so $$K_{sp}$$ remains constant. Added chloride initially makes $$Q=[\mathrm{Ag^+}][\mathrm{Cl^-}]$$ too large, causing precipitation until the product again equals $$K_{sp}$$. The new equilibrium has less dissolved silver and more chloride. Concentrations change to satisfy the same constant, rather than changing the constant to fit the disturbance.

</div>

### Selective precipitation

**Selective precipitation** separates ions by adding a reagent that forms salts with **very different** $$K_{sp}$$ values. The ion whose $$Q_{sp}$$ exceeds its $$K_{sp}$$ **first** (lowest $$K_{sp}$$ or favorable stoichiometry) precipitates preferentially as concentration is raised—used analytically and conceptually on the exam.

<div class="theorem-box">

**Example.** Two cations form 1:1 salts with anion X. Their initial concentrations are $$[M^+]=0.100\ M$$ and $$[N^+]=0.00100\ M$$, with $$K_{sp}(MX)=10^{-8}$$ and $$K_{sp}(NX)=10^{-9}$$. Which salt begins precipitating first as X is added slowly?

The thresholds are $$[X^-]=10^{-8}/0.100=10^{-7}\ M$$ for MX and $$10^{-9}/0.00100=10^{-6}\ M$$ for NX. MX precipitates first despite its larger solubility-product constant. Precipitation onset depends on both the constant and the available cation concentration, not on ranking constants alone. These thresholds assume negligible dilution and no other significant reactions.

</div>

---

## Complex ions and formation constants

A **complex ion** consists of a **central metal cation** (Lewis acid) bound to **ligands** (Lewis bases) that donate electron pairs (learn more about acids/bases in [Unit 8](/notes/ap/chem/acidbase/)). In a solution, stepwise binding equilibria exist; textbooks often emphasize an overall **formation** (stability) constant $$K_f$$ for

$$
\text{M}^{n+} + x\,\text{L} \rightleftharpoons \text{ML}_x^{n+},
$$

with

$$
K_f = \frac{[\text{ML}_x^{n+}]}{[\text{M}^{n+}][\text{L}]^x},
$$

matching the form of $$K_c$$ for that net reaction (charges and stoichiometry depend on the specific complex). A **larger** $$K_f$$ means the complex is **more stable** (more product-favored at equilibrium). If ligand is in large excess and $$K_f$$ is large, it is often reasonable to assume **complete** formation for stoichiometry purposes—check problem assumptions.

The **dissociation** constant $$K_d$$ for breaking the complex apart is the **reciprocal** of $$K_f$$ for the same net forward/back pairing:

$$
K_f = \frac{1}{K_d}.
$$

**Coordination number** is the number of donor atoms bound to the metal; common geometries include **linear** (2), **tetrahedral** or **square planar** (4), and **octahedral** (6).

---

:::checklist

1. **Balance** the equation and identify **phase** of each species.
2. Write $$K_c$$, $$K_p$$, or $$K_{sp}$$ **omitting pure solids/liquids** (and solvent water in dilute aqueous $$K_c$$ unless specified).
3. Compute **$$Q$$** if asked whether the system shifts; compare to $$K$$.
4. Use **ICE** for unknown equilibrium concentrations; watch **stoichiometric** multiples of $$x$$.
5. Remember *temperature* changes $$K$$; *catalyst* does not. For two temperatures, relate $$K_1$$ and $$K_2$$ with the **van’t Hoff equation** if $$\Delta H^\circ$$ is known (or given).
6. For solubility, track **common ions**, **$$Q_{sp}$$ vs $$K_{sp}$$**, and **complex formation**, which can *increase* solubility by tying up a metal ion (e.g. $$\text{AgCl}$$ dissolving more in ammonia).

:::

The same equilibrium-constant methods apply to **acid–base** ($$K_a$$, $$K_b$$, $$K_w$$) and **buffers** in the next unit—only the chemical reaction and symbols change.

<div class="theorem-box">

**Example.** Excess ligand binds dissolved metal ions from a sparingly soluble salt. Explain why total dissolved metal can rise while the free-metal concentration remains very small.

The ligand removes free metal ions by forming a complex. This lowers the ion product for dissolution, allowing more solid to dissolve. The solubility expression uses free metal ions, whereas total dissolved metal includes both free and complexed forms. Treating those concentrations as identical misses the effect.

</div>

---

:::equations

| Idea | Equation | Conditions |
| --- | --- | --- |
| Equilibrium and quotient | $$K_c=\frac{[C]^c[D]^d}{[A]^a[B]^b}$$ | For $$aA+bB\rightleftharpoons cC+dD$$; Q uses current values; omit pure solids and liquids. |
| Direction | $$Q<K: \text{forward}$$; $$Q>K: \text{reverse}$$ | Compare at the same temperature and with consistent conventions. |
| Related reactions | $$K_{reverse}=K^{-1}$$; $$K_{scaled}=K^\alpha$$; $$K_{sum}=K_1K_2$$ | Scale every coefficient by $$\alpha$$; multiply constants when adding reactions. |
| Gas equilibrium | $$K_p=K_c(RT)^{\Delta n_g}$$ | Textbook concentration/pressure convention; ideal gases. |
| Free energy | $$\Delta G^\circ=-RT\ln K$$; $$\Delta G=RT\ln(Q/K)$$ | Thermodynamic K and Q are dimensionless activity ratios. |
| Temperature dependence | $$\ln(K_2/K_1)=-\Delta H^\circ(1/T_2-1/T_1)/R$$ | Approximately constant reaction enthalpy, T in kelvin. |
| Solubility | $$K_{sp}=[M]^a[X]^b$$ | For $$M_aX_b(s)\rightleftharpoons aM+bX$$ with charges understood; use free-ion concentrations. |
| Pure-water molar solubility | $$K_{sp}=(as)^a(bs)^b$$ | No initial ions and no significant competing reactions. |
| Complex formation | $$K_f=[ML_n]/([M][L]^n)$$ | Use free ligand and free metal, not analytical totals. |
| Combined dissolution | $$K_{net}=K_{sp}K_f$$ | Applies when adding the specified dissolution and complexation reactions once cancels free metal. |

:::

## Practice

### MCQ

::::problem
1. For $$\mathrm{A(g)\rightleftharpoons2B(g)}$$, an equilibrium mixture is compressed to half its volume at fixed temperature. Then enough inert gas is added at fixed volume to double the total pressure again. Before reaction occurs, what is Q?

   (A) $$K/2$$<br>
   (B) $$K$$<br>
   (C) $$2K$$<br>
   (D) $$4K$$

:::solution
Compression doubles each reacting concentration, giving $$Q'=(2[B])^2/(2[A])=2K$$. Adding inert gas at fixed volume changes neither reacting concentration nor partial pressure. Only the compression changes Q; total pressure alone is not the relevant variable.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
2. For $$A\rightleftharpoons2B$$, $$K_1=4.00$$; for $$B\rightleftharpoons C$$, $$K_2=3.00$$. What is K for $$C\rightleftharpoons\tfrac12 A$$?

   (A) $$1/36$$<br>
   (B) $$1/6$$<br>
   (C) $$6$$<br>
   (D) $$36$$

:::solution
Twice the second reaction added to the first gives $$A\rightleftharpoons2C$$ with $$K=4.00(3.00)^2=36$$. Reversing and halving coefficients gives $$K'=36^{-1/2}=1/6$$. Reaction scaling changes exponents, not a numerical multiplier in front of K.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
3. For $$\mathrm{MX_2(s)\rightleftharpoons M^{2+}+2X^-}$$, $$K_{sp}=4.0\times10^{-12}$$. What is the approximate molar solubility in $$0.0100\ M$$ NaX, neglecting other reactions?

   (A) $$4.0\times10^{-8}\ M$$<br>
   (B) $$1.0\times10^{-4}\ M$$<br>
   (C) $$4.0\times10^{-10}\ M$$<br>
   (D) $$2.0\times10^{-5}\ M$$

:::solution
Use $$K_{sp}=s(0.0100+2s)^2$$, not the pure-water expression. Neglecting 2s gives $$s=4.0\times10^{-12}/10^{-4}=4.0\times10^{-8}\ M$$. The added $$2s=8.0\times10^{-8}\ M$$ is negligible beside 0.0100 M, validating the approximation.

$$
\boxed{\text{A}}.
$$
:::
::::

::::problem
4. For $$\mathrm{AB(s)\rightleftharpoons A^++B^-}$$, $$K_{sp}=1.0\times10^{-8}$$. Only $$2.0\times10^{-5}\ \mathrm{mol}$$ solid is added to $$1.00\ \mathrm{L}$$ pure water. What is the final state if no other reactions occur?

   (A) Some solid remains and both ions are $$10^{-4}\ M$$<br>
   (B) Some solid remains and both ions are $$2.0\times10^{-5}\ M$$<br>
   (C) All dissolves and Ksp falls to $$4.0\times10^{-10}$$<br>
   (D) All dissolves and $$Q=4.0\times10^{-10}<K_{sp}$$

:::solution
Complete dissolution supplies only $$2.0\times10^{-5}\ M$$ of each ion, giving $$Q=4.0\times10^{-10}$$. This is below saturation, so all the available solid dissolves. The constant stays fixed; equality with Ksp requires equilibrium with solid present, which the small sample cannot establish.

$$
\boxed{\text{D}}.
$$
:::
::::

::::problem
5. At a fixed temperature, $$K=0.0100$$ for a reaction and its current quotient is $$Q=1.00\times10^{-4}$$. What is $$\Delta G/(RT)$$?

   (A) $$+4.61$$<br>
   (B) $$-4.61$$<br>
   (C) $$+9.21$$<br>
   (D) $$-9.21$$

:::solution
Actual free energy is $$\Delta G=RT\ln(Q/K)$$. The ratio is 0.0100, whose natural logarithm is -4.61. Although $$\Delta G^\circ/(RT)=-\ln K=+4.61$$, the prepared mixture favors the forward reaction.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
6. Given $$\mathrm{MX(s)\rightleftharpoons M^++X^-}$$ with $$K_{sp}=10^{-10}$$ and $$\mathrm{M^++2L\rightleftharpoons ML_2^+}$$ with $$K_f=10^{12}$$, what is K for $$\mathrm{MX(s)+2L\rightleftharpoons ML_2^++X^-}$$?

   (A) $$10^{-22}$$<br>
   (B) $$10^{-2}$$<br>
   (C) $$10^2$$<br>
   (D) $$10^{22}$$

:::solution
Adding the reactions cancels free metal ions, and their equilibrium constants multiply: $$K=K_{sp}K_f=10^2$$. Complex formation can therefore promote dissolution. Free-metal concentration in the solubility expression must not be replaced by total dissolved metal concentration.

$$
\boxed{\text{C}}.
$$
:::
::::

### FRQ

::::frq{id=chem-equilibrium-challenge-1}
7. For $$\mathrm{A(g)\rightleftharpoons2B(g)}$$, $$K_c=0.360$$ at a fixed temperature. A 1.00 L vessel initially contains 0.500 mol A and no B. Gases behave ideally.

   $$(A)$$ Set up an ICE expression and calculate both equilibrium concentrations without assuming a small change.

   $$(B)$$ Double the vessel volume at constant temperature. Calculate Q immediately after expansion and predict the direction of net reaction.

   $$(C)$$ Calculate the new equilibrium concentrations. Determine whether the final concentration of B exceeds its value before expansion.

   $$(D)$$ At the new equilibrium, add inert gas at fixed volume and temperature. Compare the effects on total pressure, B partial pressure, Q, and K.

:::solution
$$(A)$$ Let x M of A dissociate. Then $$[A]=0.500-x$$, $$[B]=2x$$, and $$4x^2/(0.500-x)=0.360$$. The quadratic $$4x^2+0.360x-0.180=0$$ has physical root $$x=0.17185\ M$$. Thus $$[A]=0.3281\ M$$ and $$[B]=0.3437\ M$$, retaining guard digits for the later parts. Depletion is about 34% of the initial A, so a small-x shortcut would be inappropriate.

$$(B)$$ Both concentrations halve before any reaction occurs. Thus $$Q'=([B]/2)^2/([A]/2)=K_c/2=0.180$$. Because Q is below K, the forward reaction forms more B. K remains 0.360 because temperature is unchanged.

$$(C)$$ The conserved A-equivalent concentration after expansion is $$[A]+[B]/2=0.250\ M$$. Write $$[B]=2y$$ and $$[A]=0.250-y$$, giving $$4y^2/(0.250-y)=0.360$$. The physical root is $$y=0.11160\ M$$, so $$[B]=0.2232\ M$$ and $$[A]=0.1384\ M$$. B rises from its immediately diluted concentration of 0.1719 M but remains below its pre-expansion value 0.3437 M. A shift toward product does not automatically restore the old concentration.

$$(D)$$ Total pressure rises because total gas moles increase. B partial pressure remains $$n_BRT/V$$ with all three quantities unchanged. Reacting concentrations and Q therefore stay fixed, as does K. There is no net shift in this ideal fixed-volume case, even though a pressure gauge records an increase.
:::
::::

::::frq{id=chem-equilibrium-challenge-2}
8. A solution initially contains $$0.0100\ M$$ silver ions and $$0.0100\ M$$ lead(II) ions. Chloride is added slowly with negligible volume change. Use $$K_{sp}(\mathrm{AgCl})=1.8\times10^{-10}$$ and $$K_{sp}(\mathrm{PbCl_2})=1.6\times10^{-5}$$. Ignore complex formation unless specified.

   $$(A)$$ Find the chloride concentration at which each solid would first precipitate if its metal concentration remained at the initial value. Identify the first precipitate.

   $$(B)$$ Just before lead chloride starts to precipitate, calculate the free silver concentration and the percentage of initial silver removed.

   $$(C)$$ A separate saturated AgCl sample is exposed to a ligand L with $$K_f=1.0\times10^7$$ for $$\mathrm{Ag^++2L\rightleftharpoons AgL_2^+}$$. Derive the equilibrium constant for $$\mathrm{AgCl(s)+2L\rightleftharpoons AgL_2^++Cl^-}$$.

   $$(D)$$ Explain why adding excess ligand can increase total dissolved silver while free silver remains small. Would this improve precipitation-based removal of silver?

:::solution
$$(A)$$ For AgCl, $$[Cl^-]_{crit}=K_{sp}/[Ag^+]=1.8\times10^{-8}\ M$$. For lead chloride, $$[Cl^-]_{crit}=\sqrt{K_{sp}/[Pb^{2+}]}=\sqrt{1.6\times10^{-3}}=0.0400\ M$$. Silver chloride precipitates first. The different chloride exponents require different calculations; comparing Ksp values alone is not the method.

$$(B)$$ At $$[Cl^-]=0.0400\ M$$, equilibrium with AgCl gives $$[Ag^+]=1.8\times10^{-10}/0.0400=4.5\times10^{-9}\ M$$. The fraction remaining is $$4.5\times10^{-9}/0.0100=4.5\times10^{-7}$$. Thus $$99.999955\%$$ has been removed in this idealized model. This describes a very effective separation, not literally zero residual silver.

$$(C)$$ Add dissolution and complex formation; free silver cancels. The constants multiply, giving $$K=K_{sp}K_f=(1.8\times10^{-10})(1.0\times10^7)=1.8\times10^{-3}$$. Its expression is $$[AgL_2^+][Cl^-]/[L]^2$$ under the dilute-solution approximation. The solid has unit activity and is omitted.

$$(D)$$ Ligand binds free silver into the complex, lowering the dissolution ion product and allowing more solid to dissolve. Total dissolved silver includes $$[Ag^+]+[AgL_2^+]$$, whereas Ksp uses only free $$[Ag^+]$$. Strong complexation therefore tends to oppose removal as a solid, keeping silver dissolved even when a calculation based only on total metal concentration would predict precipitation. It would not improve this precipitation-based separation.
:::
::::
