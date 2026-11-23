---
title: "Entropy"
description: "USAPhO notes on the second law, reversible and irreversible processes, entropy calculations, and the statistical meaning of entropy."
sidebar:
  order: 3
---

These notes were written in collaboration with Michael Zhao.

## Entropy and the Second Law of Thermodynamics

A warm object cools in contact with a colder one. Energy conservation would also allow the same amount of energy to flow the other way, so the first law alone cannot predict which process occurs. The second law supplies that direction, and **entropy** $$S$$ lets us calculate it.

### Reversibility and the second law

A process is reversible if it can be undone while restoring both the system and its surroundings. The system must pass through equilibrium states in the ideal limit, and effects such as friction and heat flow across a finite temperature difference must be absent. Free expansion, friction, and heat conduction across a finite temperature difference are all irreversible. An isothermal expansion can be reversible if the gas stays arbitrarily close to equilibrium with the reservoir and the piston moves without friction.

The **Kelvin–Planck statement** rules out a cyclic device whose sole effect is converting heat from one reservoir entirely into work. The **Clausius statement** rules out a cyclic device whose sole effect is transferring heat from a colder reservoir to a hotter one. A work-free refrigerator could return the heat rejected by an ordinary engine to its hot reservoir, leaving only the conversion of hot-reservoir heat into work. Conversely, a perfect one-reservoir engine could drive an ordinary refrigerator with no external work. Either device would violate both statements. A perpetual-motion machine of the first kind violates energy conservation, while one of the second kind violates the second law.

### Calculating entropy changes

For a reversible process,

$$
\Delta S = \int_i^f \frac{\delta Q_{\rm rev}}{T},
$$

and for a reversible *isothermal* transfer,

$$
\Delta S = \frac QT.
$$

Entropy is a **state property**, so any reversible path between the same equilibrium endpoints gives the same $$\Delta S$$. For a simple compressible system at fixed particle number, combining reversible heat $$T\,dS$$ and reversible work on the gas $$-p\,dV$$ gives

$$
dU=T\,dS-p\,dV.
$$

This equation relates neighboring equilibrium states. For an ideal gas, substitute $$dU=nC_V\,dT$$ and $$p/T=nR/V$$. Integrating with constant heat capacities gives

$$
\Delta S = nC_V\ln\frac{T_f}{T_i} + nR\ln\frac{V_f}{V_i}
= nC_p\ln\frac{T_f}{T_i} - nR\ln\frac{p_f}{p_i}.
$$

Specializing: $$\Delta S = nR\ln(V_f/V_i)$$ for an isothermal process, $$nC_V\ln(T_f/T_i)$$ for isochoric, and $$nC_p\ln(T_f/T_i)$$ for isobaric.

For instance, connect two equal-temperature states with volumes $$V_i$$ and $$V_f>V_i$$ by first cooling at fixed volume to $$T'=T_i V_i/V_f$$, then expanding at constant pressure until the gas is back at $$T_i$$. The first leg contributes $$nC_V\ln(T'/T_i)$$ and the second contributes $$nC_p\ln(T_i/T')$$. Their sum is $$n(C_p-C_V)\ln(V_f/V_i)=nR\ln(V_f/V_i)$$, the same change as for a reversible isothermal expansion.

To find $$\Delta S$$ for an **irreversible** process (like free expansion), invent any reversible process connecting the same two states and compute $$\Delta S$$ along it — since $$S$$ is a state function, the answer carries over.

<div class="theorem-box">

**Theorem (Second Law of Thermodynamics).** The total entropy of an isolated system never decreases:

$$
\Delta S \ge 0,
$$

</div>

Equality holds in the reversible limit. A system that exchanges heat can lose entropy, so include the surroundings when testing the second law. For an amount of heat $$\delta Q>0$$ flowing from an object at $$T_H$$ to one at $$T_L<T_H$$, the combined entropy change is

$$
dS_{\rm total}=\delta Q\left(\frac1{T_L}-\frac1{T_H}\right)>0.
$$

The colder object gains more entropy than the hotter object loses. For a cyclic engine between a hot and a cold reservoir the working substance returns to its initial entropy, leaving $$\Delta S_{\rm total}=Q_L/T_L-Q_H/T_H$$ with positive heat magnitudes. Equality gives the Carnot relation.

<div class="theorem-box">

**Example.** One mole of an ideal gas free-expands into a vacuum until its volume doubles. Find the entropy change of the gas and of the universe.

Free expansion is irreversible, so we cannot integrate $$dQ/T$$ along the actual path. But entropy is a state function, and the endpoints have the same temperature ($$\Delta T = 0$$ for a free expansion). So connect them with a *reversible isothermal* expansion, for which

$$
\Delta S_{\text{gas}} = nR\ln\frac{V_f}{V_i} = (1)(8.31)\ln 2 \approx 5.76\text{ J/K}.
$$

The surroundings exchanged no heat ($$Q = 0$$ in the real process), so $$\Delta S_{\text{surr}} = 0$$ and

$$
\Delta S_{\text{univ}} = 5.76\text{ J/K} > 0,
$$

confirming the process is irreversible — exactly what the second law demands.

</div>

### Maximum work and reversibility

Compare two paths between the same equilibrium states with heat exchanged only with a reservoir at temperature $$T_0$$. The total entropy change is $$S_{\rm gen}=\Delta S-Q/T_0$$. With work output positive, the first law gives $$W_{\rm out}=Q-\Delta U$$, hence

$$
W_{\rm out}=T_0\Delta S-\Delta U-T_0S_{\rm gen}.
$$

If a reversible path is available under these constraints, it has $$S_{\rm gen}=0$$ and delivers the most work. For an ideal-gas expansion between equal-temperature states at $$T_0$$, free expansion delivers zero work, whereas reversible isothermal expansion delivers $$nRT_0\ln(V_f/V_i)$$. The difference is the work lost to irreversibility.

---

## A Statistical View of Entropy

Microscopically, entropy counts arrangements. Every individual **microstate** of an isolated system is equally probable, but the **configurations** (macroscopic descriptions, e.g. "how many molecules in the left half") are not, because some configurations correspond to far more microstates.

For $$N$$ molecules split as $$N_1$$ and $$N_2$$ between two halves of a box, the **multiplicity** is

$$
w = \frac{N!}{N_1!\,N_2!}.
$$

This is sharply peaked at the even split: for $$N \sim 10^{22}$$ the configuration with the molecules essentially evenly distributed dominates so overwhelmingly that we never observe spontaneous compression into one half.

**Boltzmann's entropy** ties this to the macroscopic definition:

$$
S = k_B\ln w.
$$

This explains the two combination rules — probabilities of independent subsystems multiply, while their entropies add — and the change in entropy between two configurations is

$$
\Delta S = k_B\ln\frac{\Omega_f}{\Omega_i}.
$$

For large factorials, **Stirling's approximation** for factorials is used to approximate entropy:

$$
\ln N! \approx N\ln N - N.
$$

A "spread out" configuration has higher multiplicity, hence higher entropy, than an ordered one ($$w_{\text{resting}} > w_{\text{swirling}}$$, so $$S_{\text{resting}} > S_{\text{swirling}}$$) — the statistical statement of the Second Law.

### Counting states of a monatomic ideal gas

A molecule’s position contributes a factor proportional to $$V$$ in phase space. Its thermal momentum width in each direction scales as $$\sqrt{mk_BT}$$, so the three momentum dimensions contribute a factor proportional to $$T^{3/2}$$ at fixed molecular mass. For $$N$$ identical molecules, exchanging two labels does not create a new physical state. The classical phase-space count therefore includes a factor $$1/N!$$. With the quantum phase-space cell size, the dilute monatomic gas has the Sackur–Tetrode entropy

$$
S=Nk_B\left[\ln\left(\frac{V}{N}\left(\frac{2\pi mk_BT}{h^2}\right)^{3/2}\right)+\frac52\right].
$$

At fixed $$N$$ its change is $$Nk_B\ln(V_f/V_i)+\tfrac32Nk_B\ln(T_f/T_i)$$, matching the thermodynamic formula. In a reversible adiabat the expansion opens more position states, but the gas cools and the thermal momentum range shrinks. The two contributions cancel because $$TV^{2/3}$$ stays constant.

### Mixing identical and distinct gases

Take away the partition between two equal samples of the same gas at the same temperature and density. Counting the two samples as distinct would give an apparent entropy gain of $$2Nk_B\ln 2$$. The $$1/N!$$ correction removes this artifact. The combined gas has the same $$V/N$$ and temperature, so its entropy is just the sum of the initial entropies. This resolves Gibbs’ mixing paradox.

For two distinguishable ideal gases, each species really does gain access to the entire container. At fixed temperature, each contributes $$N_i k_B\ln(V_f/V_i)$$. For two equal samples, each species doubles its accessible volume and the total mixing entropy is $$2Nk_B\ln 2$$.

:::equations

| Idea | Relation | Conditions |
|---|---|---|
| Entropy change | $$\Delta S=\int_i^f\delta Q_{\rm rev}/T$$ | Use a reversible path between the endpoints |
| Fundamental relation | $$dU=T\,dS-p\,dV$$ | Equilibrium, simple compressible system, fixed particle number |
| Ideal gas | $$\Delta S=nC_V\ln(T_f/T_i)+nR\ln(V_f/V_i)$$ | Constant $$C_V$$ |
| Second law | $$S_{\rm gen}=\Delta S_{\rm total}\ge0$$ | Include surroundings to form an isolated total system |
| Lost work | $$W_{\rm rev}-W_{\rm out}=T_0S_{\rm gen}$$ | Fixed endpoints and a single reservoir at $$T_0$$, when a reversible path exists |
| Microstates | $$S=k_B\ln\Omega,\quad\Delta S=k_B\ln(\Omega_f/\Omega_i)$$ | Equally weighted accessible microstates |

:::
