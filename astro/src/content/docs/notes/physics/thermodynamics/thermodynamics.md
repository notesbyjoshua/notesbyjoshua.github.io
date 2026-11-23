---
title: "Thermodynamics Introduction"
description: "Physics notes on thermodynamics, temperature, heat transfer, ideal gases, work, internal energy, and the laws of thermodynamics."
sidebar:
  order: 1
---

---

This page is written in collaboration with Michael Zhao.

---

## Temperature and the Zeroth Law of Thermodynamics

<div class="theorem-box">

**Theorem (Zeroth Law of Thermodynamics).** If systems $$A$$ and $$B$$ are each in thermal equilibrium with a third system $$C$$, then $$A$$ and $$B$$ are in thermal equilibrium with each other.

</div>

This is what lets temperature be a well-defined property: a thermometer (system $$C$$) can be used to compare any two systems. Two systems placed in thermal contact eventually reach the same temperature.

The temperature scales are related by

$$
T_C = T - 273.15,
\qquad
T_F = 1.8\,T_C + 32,
$$

where $$T$$ is in kelvin. The triple point of water defines the kelvin,

$$
T_{\text{tr}} = 273.16\text{ K}.
$$

A **constant-volume gas thermometer** measures temperature through the pressure of a fixed volume of gas, read off as a height difference $$h$$ in a mercury manometer. Extrapolating the pressure of a dilute gas to zero defines absolute zero.

## Thermal Expansion

Most materials expand when heated due to the increased motion of its atoms. For a solid, the change in any length is

$$
\Delta L = \alpha L\,\Delta T,
$$

where $$\alpha$$ is the **coefficient of linear expansion**.

For an **isotropic** solid (same material everywhere) the fractional change $$\Delta L/L = \alpha\,\Delta T$$ is the same for every line in the body — length, thickness, face diagonal, body diagonal, and the diameter of a hole punched in it. The expansion behaves like a photographic enlargement in three dimensions. Consequently, area and volume scale as

$$
\Delta A = 2\alpha A\,\Delta T,
\qquad
\Delta V = 3\alpha V\,\Delta T.
$$

A common trap: a hole in a plate gets *larger* when the plate is heated, not smaller, because every line lengthens in the same ratio.

For a liquid we describe expansion by volume directly,

$$
\Delta V = \beta V\,\Delta T,
$$

where $$\beta$$ is the **coefficient of volume expansion** (so $$\beta = 3\alpha$$ for an isotropic solid). Water is the famous exception to $$\beta > 0$$: between $$0^\circ\text{C}$$ and about $$4^\circ\text{C}$$ it *contracts* on heating, reaching maximum density (minimum specific volume) near $$4^\circ\text{C}$$. This is due to IMFs and other chemical properties that won't be discussed here.

Thermal expansion comes from the *asymmetry* of the interatomic potential energy curve $$U(r)$$. Near the equilibrium separation $$r_0$$ the well is steeper on the close-in side than on the far side. As temperature and vibrational energy rise, the average separation $$\langle r\rangle$$ creeps outward even though $$r_0$$ does not change. A perfectly symmetric (parabolic) well would give no expansion.

A **bimetallic strip** bonds two metals with different $$\alpha$$ (e.g. brass and steel). Heating bends the strip toward the lower-$$\alpha$$ metal; coiling it into a helix turns this into a thermometer or thermostat switch.

<div class="theorem-box">

**Example.** Railroad track is laid in $$25\text{ m}$$ steel segments at $$10^\circ\text{C}$$. How wide must the expansion gap between consecutive segments be so the rails do not buckle when the temperature rises to $$50^\circ\text{C}$$? Take $$\alpha_{\text{steel}} = 1.1\times 10^{-5}\ ^\circ\text{C}^{-1}$$.

Each segment lengthens by

$$
\Delta L = \alpha L\,\Delta T = (1.1\times 10^{-5})(25)(40) = 1.1\times 10^{-2}\text{ m}.
$$

So a gap of about $$11\text{ mm}$$ is needed. Note that we used the installed length and the temperature *change* (the size of a degree is the same in $$^\circ\text{C}$$ and $$^\circ\text{K}$$); the absolute temperature never enters.

</div>

## The Ideal Gas

<div class="theorem-box">

**Theorem (Ideal Gas Law).** Pressure, volume, temperature, and amount of gas are tied together by

$$
PV = nRT = Nk_BT.
$$

</div>

Here

$$
k_B = 1.38\times 10^{-23}\text{ J/K},
\qquad
N_A = 6.02\times 10^{23}\text{ mol}^{-1},
\qquad
N = nN_A,
$$

and the molar gas constant is

$$
R = k_B N_A = 8.31\text{ J/(mol·K)}.
$$

$$n$$ is the number of moles of gas (see AP Chemistry for more information), $$N$$ is the number of particles, $$P$$ is pressure, $$V$$ is volume, $$T$$ is temperature (in Kelvin), $$N_A$$ is **Avogadro's number**, and $$k_B$$ is **Boltzmann's constant**.

The model rests on a handful of assumptions:

1. The gas is made of particles in random motion obeying Newton's laws (no quantum effects).
2. The number of molecules is very large.
3. The molecules occupy a negligible fraction of the container volume.
4. No forces act on a molecule except during collisions (with walls or other molecules).
5. All collisions are elastic and of negligible duration.

### Brownian motion

Robert Brown observed fine particles suspended in a fluid jittering randomly. Einstein modeled this as the cumulative effect of molecular bombardment: for a sphere of radius $$a$$ suspended in a gas of viscosity $$\eta$$,

$$
\langle(\Delta x)^2\rangle = \frac{RT}{3\pi\eta a N_A}\,\Delta t.
$$

Note that $$\langle\rangle$$ denotes the average. Jean Baptiste Perrin used measurements of $$\langle(\Delta x)^2\rangle$$ to deduce $$N_A \sim 6\times 10^{23}$$. Qualitatively, a larger $$N_A$$ would mean the bombardment on opposite sides nearly balances (less jitter); a smaller $$N_A$$ would mean bigger fluctuations.

### Pressure from kinetic theory

Treating wall collisions as elastic momentum reversals and extrapolating from one dimension to three gives

$$
p = \tfrac13 \rho \langle v^2\rangle,
$$

where $$\rho$$ is the mass density. Solving for the root-mean-square speed,

$$
v_{\text{rms}} = \sqrt{\langle v^2\rangle} = \sqrt{\frac{3p}{\rho}} = \sqrt{\frac{3k_BT}{m}} = \sqrt{\frac{3RT}{M}}.
$$

<div class="theorem-box">

**Example.** Find the rms speed of nitrogen molecules ($$\text{N}_2$$, molar mass $$M = 0.028\text{ kg/mol}$$) in air at $$T = 300\text{ K}$$.

Using $$v_{\text{rms}} = \sqrt{3RT/M}$$,

$$
v_{\text{rms}} = \sqrt{\frac{3(8.31)(300)}{0.028}} = \sqrt{2.67\times 10^{5}} \approx 517\text{ m/s}.
$$

This is comfortably faster than the speed of sound in air ($$\sim 340\text{ m/s}$$), which makes sense — sound propagates through the same molecular collisions, just slower than the typical molecular speed.

</div>

### Mean free path

A molecule sweeps out a cylinder as it moves; treating it as having effective diameter $$2d$$ (all other molecules being points) and counting collisions gives the **mean free path**

$$
\lambda = \frac{V}{N\pi d^2}.
$$

Two refinements: using $$pV = Nk_BT$$ converts this to

$$
\lambda = \frac{k_BT}{\pi d^2 p},
$$

and accounting for the fact that the *relative* speed between molecules exceeds the average speed introduces a factor of $$\sqrt 2$$:

$$
\lambda = \frac{k_BT}{\sqrt2\,\pi d^2 p}.
$$

### Real gases

For real gases the ideal gas law is the first term of the **virial expansion**

$$
pV = nRT\left[1 + B_1\frac{n}{V} + B_2\left(\frac nV\right)^2 + \cdots\right],
$$

which reduces to the ideal gas law as the density $$n/V \to 0$$. The **van der Waals equation** corrects separately for molecular volume and intermolecular attraction:

$$
\left(p + \frac{an^2}{V^2}\right)(V - nb) = nRT.
$$

The constant $$a>0$$ for attractive forces: a molecule approaching the wall is pulled back by the others behind it, softening its impact and lowering the pressure. The constant $$b$$ accounts for the finite volume the molecules themselves occupy.

## Heat and Heat Transfer

**Heat** is energy that flows between a system and its environment *because of a temperature difference*. By convention $$Q>0$$ when heat flows into the system. Heat and work are *not* state functions (quantities whose values do not depend on the path). A system does not "contain" heat or work; these describe energy transfer during a process between states.

### Conduction

For a slab of thickness $$\Delta x$$ and cross-section $$A$$, the rate of heat flow is

$$
H = kA\frac{\Delta T}{\Delta x},
$$

where $$k$$ is the **thermal conductivity** (units W/m·K). In differential form,

$$
H = -kA\frac{dT}{dx},
$$

with the minus sign because heat flows down the temperature gradient. For a rod of length $$L$$ between fixed temperatures $$T_H > T_L$$,

$$
H = kA\frac{T_H - T_L}{L}.
$$

Building materials are rated by the **R-value** (thermal resistance)

$$
R = \frac Lk.
$$

Conductances in series add like resistances (same $$H$$, temperature drops add); in parallel the areas add.

<div class="theorem-box">

**Example.** Two slabs with thicknesses $$L_1, L_2$$ and conductivities $$k_1, k_2$$ are stacked face to face. The outer faces are held at $$T_1$$ and $$T_2$$ (with $$T_2 > T_1$$). In steady state, find the rate of heat flow and the interface temperature $$T_x$$.

In steady state no energy piles up at the interface, so the same $$H$$ flows through both slabs:

$$
H = \frac{k_1 A (T_x - T_1)}{L_1} = \frac{k_2 A (T_2 - T_x)}{L_2}.
$$

Solving the right-hand equality for $$T_x$$ and substituting back gives a result that looks exactly like resistors in series — the thermal resistances $$L/k$$ add:

$$
H = \frac{A(T_2 - T_1)}{\dfrac{L_1}{k_1} + \dfrac{L_2}{k_2}},
\qquad
T_x = \frac{k_1 L_2\,T_1 + k_2 L_1\,T_2}{k_1 L_2 + k_2 L_1}.
$$

The same idea extends to any number of layers: just sum all the $$L_i/k_i$$ in the denominator.

</div>

### Convection and radiation

**Convection** transfers heat through bulk fluid motion: warmed fluid expands, becomes less dense, and rises while cooler fluid sinks, setting up a circulation.

**Radiation** transfers energy by electromagnetic waves, requiring no medium. Every object emits radiation depending on its temperature; the power radiated scales as the fourth power of the Kelvin temperature (see [Stellar Physics](/notes/physics/modern-stellar/stellarphys/)). Earth's average temperature levels off near $$300\text{ K}$$ because at that temperature it radiates energy away as fast as it absorbs it from the Sun.

### Heat capacity and latent heat

The **heat capacity** of a body and the **specific heat** of its material are

$$
C = \frac{Q}{\Delta T},
\qquad
c = \frac Cm = \frac{Q}{m\,\Delta T}.
$$

Therefore the heat to change temperature is

$$
Q = mc \Delta T,
\qquad
Q = m\int_{T_i}^{T_f} c\,dT
$$

if $$c$$ varies with temperature. For a phase change at constant temperature, the **latent heat** (heat of transformation) gives

$$
Q = Lm,
$$

with $$L_f$$ for fusion (melting/freezing) and $$L_v$$ for vaporization (boiling/condensing).

A useful empirical fact: the molar heat capacity (specific heat times molar mass) of most solids approaches about $$25\text{ J/(mol·K)}$$ at high temperature (the Dulong–Petit value), falling off toward zero at low temperature.

<div class="theorem-box">

**Example.** How much heat is needed to turn $$50\text{ g}$$ of ice at $$-10^\circ\text{C}$$ into water at $$20^\circ\text{C}$$? Use $$c_{\text{ice}} = 2100\ \text{J/(kg·K)}$$, $$c_{\text{water}} = 4186\ \text{J/(kg·K)}$$, and $$L_f = 3.34\times 10^{5}\ \text{J/kg}$$.

Do the problem in three stages — never melt and warm in one step, because melting happens at constant temperature.

1. Warm the ice from $$-10^\circ\text{C}$$ to $$0^\circ\text{C}$$: $$\;Q_1 = mc_{\text{ice}}\,\Delta T = (0.050)(2100)(10) = 1050\text{ J}.$$
2. Melt the ice at $$0^\circ\text{C}$$: $$\;Q_2 = mL_f = (0.050)(3.34\times 10^{5}) = 16{,}700\text{ J}.$$
3. Warm the meltwater from $$0^\circ\text{C}$$ to $$20^\circ\text{C}$$: $$\;Q_3 = mc_{\text{water}}\,\Delta T = (0.050)(4186)(20) = 4186\text{ J}.$$

The total is

$$
Q = Q_1 + Q_2 + Q_3 \approx 2.2\times 10^{4}\text{ J} = 22\text{ kJ}.
$$

The melting step requires much more heat because latent heats are typically much larger than the heat for a modest temperature change.

</div>

When the temperature difference $$\Delta T$$ between a body and its surroundings is small, the cooling rate is proportional to that difference:

$$
\frac{d\,\Delta T}{dt} = -A\,\Delta T
\quad\Longrightarrow\quad
\Delta T = \Delta T_0\,e^{-At}.
$$

The excess temperature decays exponentially. This is **Newton's Law of Cooling**.

## The First Law of Thermodynamics

<div class="theorem-box">

**Theorem (First Law of Thermodynamics).** Energy is conserved when we count both heat and work:

$$
\Delta E_{\text{int}} = Q + W.
$$

</div>

In this sign convention, $$Q$$ is the heat added *to* the system and $$W$$ is the work done *on* the system, so both positive $$Q$$ and positive $$W$$ raise the internal energy.

:::warning
Some texts write $$\Delta E_{\text{int}} = Q - W$$ with $$W$$ as work done *by* the gas; be careful which convention a problem uses.
:::

### Work done on a gas

The work done *on* the gas during a volume change is

$$
W = -\int p\,dV.
$$

The sign is the subtle part: when the gas expands ($$dV>0$$) it does positive work on its surroundings, so negative work is done *on* the gas. On a $$pV$$ diagram the magnitude of the work is the area under the curve, and **work is path-dependent** — different paths between the same endpoints give different work.

The internal energy of an ideal gas depends only on temperature. With $$f$$ degrees of freedom (talked about in the next section),

$$
E_{\text{int}} = \frac f2 nRT,
\qquad
\Delta E_{\text{int}} = \frac f2 nR\,\Delta T = nC_V\,\Delta T.
$$

### Degrees of freedom and equipartition

The total kinetic energy of a molecule splits among independent quadratic terms (translational, rotational, and for some molecules vibrational):

$$
K = \tfrac12 mv_x^2 + \tfrac12 mv_y^2 + \tfrac12 mv_z^2 + \tfrac12 I_x\omega_x^2 + \tfrac12 I_y\omega_y^2 + \cdots
$$

The **equipartition theorem** says each independent degree of freedom carries an average energy $$\tfrac12 k_BT$$. Therefore

$$
E_{\text{int}} = N\left(\frac f2 k_BT\right) = \frac f2 nRT,
$$

with

- monatomic gas: $$f = 3$$, so $$E_{\text{int}} = \tfrac32 nRT$$;
- diatomic gas: $$f = 5$$ (3 translational + 2 rotational), so $$E_{\text{int}} = \tfrac52 nRT$$;
- polyatomic gas (nonlinear): $$f = 6$$, so $$E_{\text{int}} = 3nRT$$.

A linear molecule like $$\text{CO}_2$$ has no kinetic energy for rotation about its own axis, so that mode does not count. Vibration adds further degrees of freedom at high temperature.

### Molar heat capacities of an ideal gas

How much heat raises the temperature depends on how the heat is added.

At constant volume no work is done, so

$$
Q = \Delta E_{\text{int}},
\qquad
C_V = \frac{Q}{n\,\Delta T} = \frac{\Delta E_{\text{int}}}{n\,\Delta T} = \frac f2 R.
$$

At constant pressure the gas also does expansion work. Substituting $$Q = nC_p\Delta T$$ and $$W = -nR\Delta T$$ into the first law (with $$\Delta E_{\text{int}}$$ the same as the constant-volume path between the same isotherms) gives **Mayer's relation**:

$$
C_p = C_V + R.
$$

The ratio of heat capacities,

$$
\gamma = \frac{C_p}{C_V},
$$

is called the adiabatic gas constant and controls adiabatic processes. Collecting values:

| Gas | $$C_V$$ | $$C_p$$ | $$\gamma$$ |
|---|---|---|---|
| Monatomic | $$\tfrac32 R = 12.5$$ | $$\tfrac52 R = 20.8$$ | $$5/3 \approx 1.67$$ |
| Diatomic | $$\tfrac52 R = 20.8$$ | $$\tfrac72 R = 29.1$$ | $$7/5 = 1.40$$ |
| Polyatomic | $$\tfrac72 R = 24.9$$ | $$4R = 33.3$$ | $$4/3 \approx 1.33$$ |

(Heat capacities in J/(mol·K).)

## Thermodynamic Processes

Each type of process is a different constraint applied to the first law. The table at the end summarizes them.

### Isochoric (constant volume)

No volume change means no work:

$$
W = 0,
\qquad
\Delta E_{\text{int}} = Q = nC_V\,\Delta T.
$$

All heat goes into internal energy.

### Isobaric (constant pressure)

$$
W = -p\,\Delta V,
\qquad
Q = nC_p\,\Delta T,
\qquad
\Delta E_{\text{int}} = Q + W.
$$

### Isothermal (constant temperature)

For an ideal gas $$\Delta E_{\text{int}} = 0$$, so $$Q = -W$$. The path is a hyperbola $$pV = \text{const}$$, and

$$
W = -\int_{V_i}^{V_f} p\,dV = -nRT\ln\frac{V_f}{V_i}.
$$

This work is negative when the gas expands ($$V_f > V_i$$) and positive when it is compressed.

### Adiabatic (no heat flow)

With $$Q = 0$$,

$$
\Delta E_{\text{int}} = W.
$$

The gas follows

$$
pV^\gamma = \text{const},
\qquad
TV^{\gamma-1} = \text{const},
\qquad
T^\gamma p^{1-\gamma} = \text{const}.
$$

Since $$\gamma > 1$$, an adiabat is steeper than an isotherm through the same point, so an adiabatic expansion does less work and cools the gas. Carrying out the integral,

$$
W = -\int_{V_i}^{V_f} p\,dV = \frac{1}{\gamma-1}\left(p_fV_f - p_iV_i\right).
$$

<div class="theorem-box">

**Example.** A diatomic ideal gas ($$\gamma = 7/5$$) initially at $$T_i = 300\text{ K}$$ is compressed adiabatically to half its volume. Find the final temperature.

Along an adiabat $$TV^{\gamma-1}$$ is constant, so

$$
T_f = T_i\left(\frac{V_i}{V_f}\right)^{\gamma-1} = 300\,(2)^{0.4}.
$$

Since $$2^{0.4} = e^{0.4\ln 2} \approx 1.32$$,

$$
T_f \approx 300(1.32) \approx 396\text{ K}.
$$

The gas heats up even though no heat was added — all of the compression work went into internal energy. This is the principle behind a diesel engine igniting fuel without a spark plug.

</div>

### Cyclical and free expansion

Over a complete **cycle** the system returns to its initial state, so $$\Delta E_{\text{int}} = 0$$ and $$Q = -W$$: the net heat absorbed equals the net work done by the gas, which is the area enclosed by the cycle on a $$pV$$ diagram.

In a **free expansion** a gas rushes into vacuum: no work is done ($$W=0$$) and no heat is exchanged ($$Q=0$$), so $$\Delta E_{\text{int}} = 0$$ and for an ideal gas $$\Delta T = 0$$. This is an irreversible, nonequilibrium process — the $$pV$$ path is not even well defined between the endpoints, though the endpoints themselves are equilibrium states, and cannot be reversed (unless you vacuum the surroundings) because gas will flow from high pressure to low pressure.

### Thermodynamic process summary table

Underlined results apply to ideal gases only.

| Process | Restriction | First law | Other results |
|---|---|---|---|
| All | none | $$\Delta E_{\text{int}} = Q + W$$ | $$\underline{\Delta E_{\text{int}} = nC_V\Delta T}$$, $$W = -\int p\,dV$$ |
| Adiabatic | $$Q = 0$$ | $$\Delta E_{\text{int}} = W$$ | $$\underline{W = (p_fV_f - p_iV_i)/(\gamma-1)}$$ |
| Constant volume | $$W = 0$$ | $$\Delta E_{\text{int}} = Q$$ | $$Q = nC_V\Delta T$$ |
| Constant pressure | $$\Delta p = 0$$ | $$\Delta E_{\text{int}} = Q + W$$ | $$W = -p\Delta V$$, $$Q = nC_p\Delta T$$ |
| Isothermal | $$\Delta E_{\text{int}} = 0$$ | $$Q = -W$$ | $$\underline{W = -nRT\ln(V_f/V_i)}$$ |
| Cycle | $$\Delta E_{\text{int}} = 0$$ | $$Q = -W$$ | |
| Free expansion | $$Q = W = 0$$ | $$\Delta E_{\text{int}} = 0$$ | $$\underline{\Delta T = 0}$$ |

---

## Problem-solving strategy

Read the process first, then pick the constraint that turns the first law into something solvable:

:::strategy
1. **Heating/cooling or a phase change, no gas process**: Stack $$Q = mc\,\Delta T$$ for each temperature change and $$Q = Lm$$ for each phase change, and add (do the stages separately — never melt and warm in one step). For mixtures set $$\sum Q = 0$$.
2. **Conduction / steady-state heat flow**: Use $$H = kA(T_H - T_L)/L$$, treat layers as thermal resistances $$R = L/k$$ in series (add $$L_i/k_i$$) and areas in parallel; the same $$H$$ flows through every series layer.
3. **A named gas process**: Apply $$\Delta E_{\text{int}} = Q + W$$ with the matching constraint — isochoric $$W=0$$, isobaric $$W=-p\,\Delta V$$, isothermal $$\Delta E_{\text{int}}=0$$ so $$W=-nRT\ln(V_f/V_i)$$, adiabatic $$Q=0$$ with $$pV^\gamma=\text{const}$$ and $$W=(p_fV_f-p_iV_i)/(\gamma-1)$$. Always $$\Delta E_{\text{int}} = nC_V\Delta T$$.
4. **Cycle on a $$pV$$ diagram**: $$\Delta E_{\text{int}}=0$$ over the cycle, so net $$\lvert W\rvert$$ = enclosed area = net heat; add up $$Q$$ leg by leg for efficiency.
:::

:::mistakes
- Sign convention: this page uses $$\Delta E_{\text{int}} = Q + W$$ with $$W$$ done *on* the gas, so gas expansion gives $$W<0$$. Check which convention a problem uses before plugging in.
- $$Q = nC_V\Delta T$$ only at constant volume and $$Q = nC_p\Delta T$$ only at constant pressure, but $$\Delta E_{\text{int}} = nC_V\Delta T$$ holds for *any* ideal-gas process.
- Use the right degrees of freedom $$f$$ (3 monatomic, 5 diatomic, 6 nonlinear polyatomic); the wrong $$f$$ corrupts $$C_V$$, $$C_p$$, and $$\gamma$$.
- In thermal-expansion problems a hole gets *larger* when heated, and only the temperature *change* matters — $$^\circ\text{C}$$ and K give the same $$\Delta T$$.
:::
