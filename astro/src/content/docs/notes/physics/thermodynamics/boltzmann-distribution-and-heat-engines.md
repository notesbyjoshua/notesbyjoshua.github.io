---
title: "Boltzmann Distribution and the Heat Engine"
description: "USAPhO notes on molecular velocity distributions, kinetic theory, thermodynamic cycles, Carnot and Otto engines, and refrigeration."
sidebar:
  order: 2
---

These notes were written in collaboration with Michael Zhao.

## The Boltzmann distribution

A small system at temperature $$T$$ can exchange energy with a large reservoir. If the system takes energy $$E_i$$, the reservoir has energy $$E_{\rm tot}-E_i$$. Its entropy changes by approximately $$-E_i/T$$ because $$\partial S_{\rm res}/\partial E=1/T$$. Since the number of reservoir microstates is proportional to $$e^{S_{\rm res}/k_B}$$, the probability of a particular system microstate is

$$
P_i=\frac{e^{-E_i/(k_BT)}}{Z},\qquad Z=\sum_i e^{-E_i/(k_BT)}.
$$

If $$g_i$$ distinct microstates share an energy, the probability of measuring that energy is $$g_iP_i$$. In continuous phase space, integrate a probability density over the desired range of positions and momenta. Integrating over unwanted coordinates gives the marginal distribution for those that remain.

## Maxwell speed distribution

In a uniform classical gas, the kinetic energy is a sum of three squared velocity components. The Boltzmann weight factors into three independent Gaussians with mean zero and variance $$k_BT/m$$. To find the **speed** distribution, count every velocity direction. The shell between radii $$v$$ and $$v+dv$$ in velocity space has volume $$4\pi v^2\,dv$$. This is why the speed density peaks at a positive speed even though each velocity component peaks at zero.

<img class="note-img note-img--w480" src="/assets/physics/usapho/thermal-distributions.svg" alt="Maxwell speed distributions showing how higher temperature broadens the distribution and shifts its peak to higher speed" loading="lazy" decoding="async" />

For $$N$$ molecules of mass $$m$$ at temperature $$T$$, the number with speeds in $$[v, v+dv]$$ is $$N(v)\,dv$$, where

$$
N(v) = 4\pi N\left(\frac{m}{2\pi k_BT}\right)^{3/2} v^2 e^{-mv^2/2k_BT},
\qquad
N = \int_0^\infty N(v)\,dv.
$$

Three characteristic speeds come from this distribution:

$$
v_p = \sqrt{\frac{2k_BT}{m}} = \sqrt{\frac{2RT}{M}}
\quad(\text{most probable}),
$$

$$
v_{\text{av}} = \frac1N\int_0^\infty v\,N(v)\,dv = \sqrt{\frac{8k_BT}{\pi m}} = \sqrt{\frac{8RT}{\pi M}},
$$

$$
\langle v^2\rangle = \frac1N\int_0^\infty v^2 N(v)\,dv = \frac{3k_BT}{m},
\qquad
v_{\text{rms}} = \sqrt{\frac{3RT}{M}}.
$$

Their fixed ratio is worth memorizing:

$$
v_p : v_{\text{av}} : v_{\text{rms}} = 1 : 1.128 : 1.225.
$$

The average translational kinetic energy per molecule is

$$
K_{\text{trans}} = \tfrac32 k_BT.
$$

Changing variables with $$E = \tfrac12 mv^2$$ gives the **Maxwell–Boltzmann energy distribution**

$$
N(E) = \frac{2N}{\sqrt\pi}\frac{1}{(k_BT)^{3/2}}\,E^{1/2}e^{-E/k_BT}.
$$

The change of variables preserves particle count, $$N(E)\,dE=N(v)\,dv$$. Combining the velocity-shell factor with $$dv/dE=1/(mv)$$ gives the factor of $$\sqrt E$$.

### Molecular flux and pressure

Let $$n_d=N/V$$ and take positive $$v_x$$ toward a small flat wall patch. In time $$dt$$ only molecules within distance $$v_xdt$$ can hit the patch. Integrating this count over positive normal velocities in the Gaussian $$f_x$$ gives the one-sided molecular flux

$$
\Gamma=n_d\int_0^\infty v_xf_x(v_x)\,dv_x
=n_d\sqrt{\frac{k_BT}{2\pi m}}=\frac14n_d\langle v\rangle.
$$

Weight each impact by the momentum $$2mv_x$$ transferred in an elastic reflection. The momentum per area per time is the pressure:

$$
p=2mn_d\int_0^\infty v_x^2f_x(v_x)\,dv_x
=mn_d\langle v_x^2\rangle=n_dk_BT.
$$

The integral over positive velocities gives half the full mean square because the Gaussian is even. This local wall argument works for containers of different shapes.

### An isothermal gas in gravity

The molecular energy now includes $$mgz$$. Its Boltzmann weight factors into the same velocity distribution at each height and a position factor that decreases exponentially. The characteristic scale height is $$H=k_BT/(mg)$$, giving

$$
n_d(z)=n_d(0)e^{-z/H},\qquad p(z)=p(0)e^{-z/H}.
$$

For a column of area $$A$$, height $$L$$, and $$N$$ molecules, integrating $$An_d(z)$$ gives $$n_d(0)=N/[AH(1-e^{-L/H})]$$. The pressure difference $$p(0)-p(L)=Nmg/A$$ supports the gas’s weight. This model assumes both $$g$$ and $$T$$ are uniform.

---

## Heat Engines

A **heat engine** uses a working substance cycling through thermodynamic processes to extract heat and produce work. Because it returns to its starting state each cycle, $$\Delta E_{\text{int}} = 0$$, so the net work equals the net heat. Drawing heat $$\lvert Q_H\rvert$$ from a hot reservoir and dumping $$\lvert Q_L\rvert$$ to a cold one,

$$
\lvert W\rvert = \lvert Q_H\rvert - \lvert Q_L\rvert,
$$

and the **efficiency** is

$$
\epsilon = \frac{\text{what you get}}{\text{what you pay for}} = \frac{\lvert W\rvert}{\lvert Q_H\rvert} = 1 - \frac{\lvert Q_L\rvert}{\lvert Q_H\rvert}.
$$

### The Carnot engine

The Carnot cycle is two isotherms (at $$T_H$$ and $$T_L$$) joined by two adiabats. On a $$T$$–$$S$$ diagram it is simply a rectangle: the isotherms are horizontal, and the adiabats are vertical (constant entropy, "isentropic", although this term is rarely used). Heat enters reversibly at $$T_H$$ and leaves reversibly at $$T_L$$, so

$$
\frac{\lvert Q_H\rvert}{T_H} = \frac{\lvert Q_L\rvert}{T_L}.
$$

Substituting into the efficiency gives the result below.

<div class="theorem-box">

**Theorem (Carnot efficiency).** A reversible engine operating between reservoirs at $$T_H$$ and $$T_L$$ has efficiency

$$
\epsilon = 1 - \frac{T_L}{T_H}.
$$

</div>

No engine operating between two reservoirs can beat this, because the Carnot cycle is fully reversible — no energy is lost to friction, turbulence, or unrestrained heat conduction.

<div class="theorem-box">

**Proof (Carnot efficiency is the maximum efficiency).** Suppose an engine X were more efficient than a Carnot engine between the same reservoirs. Use X's work output to drive a Carnot engine *backwards* as a refrigerator. The combination would move heat from cold to hot with no net work input — a perfect refrigerator — which violates the Second Law. Hence $$\epsilon_X \le \epsilon_{\text{Carnot}}$$.

</div>

<div class="theorem-box">

**Example.** A Carnot engine operates between reservoirs at $$T_H = 500\text{ K}$$ and $$T_L = 300\text{ K}$$ and absorbs $$Q_H = 1000\text{ J}$$ from the hot reservoir each cycle. Find its efficiency, work output, and heat rejected.

The efficiency is

$$
\epsilon = 1 - \frac{T_L}{T_H} = 1 - \frac{300}{500} = 0.40.
$$

So the work per cycle is $$\lvert W\rvert = \epsilon\lvert Q_H\rvert = 400\text{ J}$$, and the heat dumped is $$\lvert Q_L\rvert = \lvert Q_H\rvert - \lvert W\rvert = 600\text{ J}$$.

As a check, $$\lvert Q_H\rvert/T_H = 1000/500 = 2\text{ J/K}$$ equals $$\lvert Q_L\rvert/T_L = 600/300 = 2\text{ J/K}$$: the entropy drawn from the hot reservoir exactly matches that given to the cold one, which is the hallmark of a reversible cycle.

</div>

### A three-leg ideal-gas cycle

<div class="theorem-box">

**Example.** A monatomic gas is heated at fixed volume from $$(V_0,p_0)$$ to $$(V_0,2p_0)$$. It expands isothermally to $$(2V_0,p_0)$$, then compresses at constant pressure back to the initial state. Find its efficiency.

The first leg adds $$\tfrac32p_0V_0$$ of internal energy and does no work. The isothermal leg produces work $$2p_0V_0\ln 2$$ and absorbs an equal amount of heat. Compression costs $$p_0V_0$$ of work and rejects heat. Only the first two legs contribute to heat input, so

$$
\epsilon=\frac{2\ln 2-1}{\tfrac32+2\ln 2}\approx0.134.
$$

</div>

### Stirling, Otto, and Diesel cycles

The ideal **Stirling cycle** joins two isotherms by two constant-volume processes. With perfect regeneration, heat stored during constant-volume cooling is recovered during constant-volume heating. External heat is then exchanged only at the two reservoir temperatures and the efficiency reaches Carnot’s.

The **Otto** and **Diesel** models both compress and expand the gas reversibly and adiabatically. Otto adds heat at constant volume, while Diesel adds heat at constant pressure and the gas expands during that leg. Both reject heat at constant volume.

<img class="note-img note-img--w480" src="/assets/physics/usapho/engine-cycles.svg" alt="Pressure-volume diagrams contrasting vertical constant-volume heat input for the Otto cycle and horizontal constant-pressure heat input for the Diesel cycle" loading="lazy" decoding="async" />

Label the states $$1\to2\to3\to4\to1$$, with compression on $$1\to2$$. Define the compression ratio $$r=V_1/V_2$$ and Diesel cutoff ratio $$r_c=V_3/V_2$$. Both models reject $$nC_V(T_4-T_1)$$. In the Otto model the input is $$nC_V(T_3-T_2)$$, and the adiabats give $$T_2/T_1=T_3/T_4=r^{\gamma-1}$$. In the Diesel model the input is $$nC_p(T_3-T_2)$$, with $$T_3/T_2=r_c$$ and $$T_4/T_1=r_c^\gamma$$. Substituting gives

$$
\epsilon_{\rm Otto}=1-r^{1-\gamma},\qquad
\epsilon_{\rm Diesel}=1-r^{1-\gamma}\frac{r_c^\gamma-1}{\gamma(r_c-1)}.
$$

These formulas assume ideal gases with constant heat capacities. A compression ratio of $$10$$ and $$\gamma=1.4$$ give an ideal Otto efficiency of about $$60\%$$.

## Refrigerators and Heat Pumps

A **refrigerator** uses work to push heat from a cold reservoir to a hot one — the reverse of an engine. By the First Law,

$$
\lvert W\rvert = \lvert Q_H\rvert - \lvert Q_L\rvert.
$$

Its performance is measured by the **coefficient of performance** $$K$$, "what you want over what you pay for":

$$
K = \frac{\lvert Q_L\rvert}{\lvert W\rvert}
\quad\Longrightarrow\quad
K_{\text{Carnot}} = \frac{T_L}{T_H - T_L}.
$$

An air conditioner is a refrigerator whose cold reservoir is the room. A **heat pump** is the same machine run to *heat* a room — now the room is the hot reservoir, and the relevant quantity is $$\lvert Q_H\rvert$$.

For *cooling* (AC, refrigerator) the goal is $$Q_L$$:

$$
K_L = \frac{\lvert Q_L\rvert}{\lvert W\rvert} \le \frac{T_L}{T_H - T_L}.
$$

For *heating* (warming a house) the goal is $$Q_H$$:

$$
K_H = \frac{\lvert Q_H\rvert}{\lvert W\rvert} \le \frac{T_H}{T_H - T_L}.
$$

The upper bounds are reached in the reversible limit. For any cycle, the two are related by

$$
K_H = K_L + 1,
$$

which follows directly from $$\lvert Q_H\rvert = \lvert Q_L\rvert + \lvert W\rvert$$.

:::equations

| Idea | Relation | Conditions |
|---|---|---|
| Boltzmann weight | $$P_i=e^{-E_i/(k_BT)}/Z$$ | Probability per microstate |
| Molecular speeds | $$v_p=\sqrt{2k_BT/m},\quad\langle v\rangle=\sqrt{8k_BT/(\pi m)},\quad v_{\rm rms}=\sqrt{3k_BT/m}$$ | Classical equilibrium gas |
| Wall flux and pressure | $$\Gamma=n_d\langle v\rangle/4,\quad p=n_dk_BT$$ | One-sided flux, isotropic gas, elastic wall |
| Barometric profile | $$p(z)=p(0)e^{-mgz/(k_BT)}$$ | Uniform temperature and gravity |
| Engine efficiency | $$\epsilon=1-Q_{\rm out}/Q_{\rm in}\le 1-T_L/T_H$$ | Bound for two reservoirs, heat magnitudes |
| Otto and Diesel | $$\epsilon_{\rm Otto}=1-r^{1-\gamma},\quad\epsilon_{\rm Diesel}=1-r^{1-\gamma}(r_c^\gamma-1)/[\gamma(r_c-1)]$$ | Ideal cycles, constant heat capacities |
| Refrigerator and heat pump | $$K_L=Q_L/W_{\rm in},\quad K_H=K_L+1$$ | Reversible bound for $$K_L$$ is $$T_L/(T_H-T_L)$$ |

:::
