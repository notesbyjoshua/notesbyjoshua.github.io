---
title: "AC Circuits"
description: "USAPhO AC circuit notes explaining phase, RMS values, complex impedance, RLC circuits, power, transformers, rectifiers, and filters."
sidebar:
  order: 6
---

## Alternating current

In direct current, the current direction does not reverse; “DC” often also means that its magnitude is constant. An alternating current reverses direction. A purely sinusoidal AC signal has zero average, although a general periodic signal can contain both a constant DC component and an alternating part.

The circuit model here is **quasistatic**: the circuit is small compared with the electromagnetic wavelength, so propagation delays and radiation can be neglected. We still include induction and time-dependent charge storage through inductors and capacitors. Quasistatic does not mean that their voltage–current relations can be replaced by DC resistances.

### Amplitude, frequency, and phase

We will use the cosine convention:

$$
v(t)=V_0\cos(\omega t+\phi_v),\qquad
i(t)=I_0\cos(\omega t+\phi_i).
$$

The amplitudes $$V_0$$ and $$I_0$$ are peak values; peak-to-peak values are twice as large. The angular frequency, frequency, and period satisfy

$$
\omega=2\pi f,\qquad T=\frac{2\pi}{\omega}=\frac1f.
$$

The phase difference tells us whether current reaches each stage of its oscillation before or after voltage. Define

$$
\phi=\phi_v-\phi_i.
$$

Positive $$\phi$$ means voltage leads current, or equivalently current lags voltage. Negative $$\phi$$ means current leads. Using sine instead of cosine changes the phase origin, not the physics, because $$\sin\theta=\cos(\theta-\pi/2)$$. Do not mix the two conventions without converting phases.

### RMS values

The ordinary average of a sinusoidal current is zero, but its heating effect is not, since heating depends on $$i^2$$. The **root-mean-square** value captures this effect:

$$
I_{\text{rms}}=\sqrt{\frac1T\int_0^T i^2(t)\,dt}.
$$

For a sinusoid, the mean of $$\cos^2$$ over a cycle is $$1/2$$, so

$$
I_{\text{rms}}=\frac{I_0}{\sqrt2},\qquad V_{\text{rms}}=\frac{V_0}{\sqrt2}.
$$

This is the DC current that would produce the same average heating in the same resistor. The division by $$\sqrt2$$ applies to a sinusoid, not every waveform; use the integral definition otherwise.

---

## Resistors, capacitors, and inductors

Throughout this page, current enters the terminal labeled positive for each passive component’s voltage drop. This keeps $$v_R=Ri$$, $$i_C=C\,dv_C/dt$$, and $$v_L=L\,di_L/dt$$ consistent.

### Resistor: current and voltage are in phase

For an ideal resistor, Ohm’s law holds instant by instant:

$$
i_R(t)=\frac{V_0}{R}\cos(\omega t+\phi_v).
$$

Current and voltage have the same phase, and $$V_0=I_0R$$ or $$V_{\text{rms}}=I_{\text{rms}}R$$. The resistor dissipates energy throughout the cycle, regardless of current direction.

### Capacitor: current leads voltage

A capacitor’s charge is $$q=Cv_C$$, so current is determined by how quickly its voltage changes:

$$
i_C=C\frac{dv_C}{dt}
=-\omega CV_0\sin(\omega t+\phi_v)
=\omega CV_0\cos\left(\omega t+\phi_v+\frac\pi2\right).
$$

Current leads voltage by $$\pi/2$$. At a voltage maximum, charge is momentarily not changing and current is zero; when voltage crosses zero, charge is changing most rapidly and current has maximum magnitude.

Define the positive **capacitive reactance magnitude**

$$
X_C=\frac1{\omega C},\qquad I_0=\frac{V_0}{X_C}.
$$

Higher frequency or larger capacitance gives more current for the same voltage amplitude. In the DC limit an ideal capacitor becomes an open circuit after charging. Saying that AC “passes through” means the plates repeatedly charge and discharge through the external wires, not that conduction electrons cross the ideal dielectric. The charging time constant $$RC$$ from [circuits](/notes/physics/eandm/circuits/) governs the accompanying transient.

### Inductor: current lags voltage

An ideal inductor requires voltage to change its current:

$$
L\frac{di_L}{dt}=V_0\cos(\omega t+\phi_v).
$$

The purely sinusoidal response is

$$
i_L(t)=\frac{V_0}{\omega L}\sin(\omega t+\phi_v)
=\frac{V_0}{\omega L}\cos\left(\omega t+\phi_v-\frac\pi2\right).
$$

Current lags voltage by $$\pi/2$$. Voltage is largest when current changes fastest, not when current itself is largest. An isolated ideal inductor can also retain a constant current set by its initial condition; the expression above describes its AC component.

Its **inductive reactance magnitude** is

$$
X_L=\omega L,\qquad I_0=\frac{V_0}{X_L}.
$$

Higher frequency or larger inductance produces less sinusoidal current for a fixed voltage amplitude. An inductor opposes changes in **current**, not changes in the source voltage. In a DC steady state its ideal inductive voltage drop vanishes, although a real winding still has resistance.

<img class="note-img note-img--w480" src="/assets/physics/usapho/em-original/ac-phase.svg" alt="Normalized sinusoidal voltage and current for a resistor, capacitor, and inductor, showing zero, leading, and lagging current phases" loading="lazy" decoding="async" />

---

## Phasors and complex impedance

Kirchhoff’s rules still apply, but peaks of different voltages do not necessarily occur at the same time. Adding their amplitudes as ordinary numbers therefore gives the wrong total. A **phasor** represents amplitude and phase together as an arrow in the complex plane.

Use $$j=\sqrt{-1}$$ so that the imaginary unit is not confused with current $$i(t)$$. With peak-amplitude phasors,

$$
\widetilde V=V_0e^{j\phi_v},\qquad
\widetilde I=I_0e^{j\phi_i},\qquad
v(t)=\operatorname{Re}\left(\widetilde V e^{j\omega t}\right).
$$

The physical voltage is the real part; the complex notation keeps track of phase while we calculate. Since differentiation of $$e^{j\omega t}$$ multiplies it by $$j\omega$$, differential component laws become algebra:

$$
\widetilde V=Z\widetilde I,\qquad
Z_R=R,\quad Z_C=\frac1{j\omega C}=-jX_C,\quad Z_L=j\omega L=jX_L.
$$

Multiplication by $$j$$ rotates a phasor through $$+\pi/2$$; multiplication by $$-j$$ rotates it through $$-\pi/2$$. This reproduces the phase shifts derived above. **Impedance** $$Z$$ is complex, whereas its magnitude $$\lvert Z\rvert$$ is the positive amplitude ratio $$V_0/I_0$$.

Components in series have the same current, so their impedances add. Parallel branches share a voltage, so their **admittances** $$Y=1/Z$$ add:

$$
Z_{\text{series}}=\sum_k Z_k,\qquad
\frac1{Z_{\text{parallel}}}=\sum_k\frac1{Z_k}.
$$

Use complex voltages and currents in Kirchhoff’s junction and loop rules, solve algebraically, and take the real part only when returning to time-dependent quantities. Phasor diagrams and complex algebra are the geometric and algebraic versions of the same calculation.

:::warning
These phasors describe a single-frequency sinusoidal response, usually after transients have decayed in a dissipative circuit. They do not automatically enforce switching-time initial conditions. Peak and RMS phasors are both valid, but never mix them in one calculation.
:::

### Series RC example

<div class="theorem-box">

**Example.** A series circuit has $$R=100\ \Omega$$ and $$C=100\ \mu\text{F}$$, driven by $$v(t)=10\cos(100t)\ \text{V}$$. Find its steady-state current.

At $$\omega=100\ \text{rad/s}$$, $$X_C=1/(\omega C)=100\ \Omega$$. Thus

$$
Z=100-j100\ \Omega,\qquad
\lvert Z\rvert=100\sqrt2\ \Omega,\qquad \arg Z=-\frac\pi4.
$$

Dividing the voltage phasor by $$Z$$ divides its amplitude by $$\lvert Z\rvert$$ and subtracts the impedance phase:

$$
i(t)=\frac{10}{100\sqrt2}\cos\left(100t+\frac\pi4\right)\ \text{A}.
$$

The peak current is $$70.7\ \text{mA}$$ and leads the supply by $$45^\circ$$. Its RMS value is $$50.0\ \text{mA}$$, not $$70.7\ \text{mA}$$.

</div>

---

## Series RLC circuits

The same current flows through all three components, making current a convenient phase reference. The resistor’s voltage is in phase with it, the inductor’s is $$90^\circ$$ ahead, and the capacitor’s is $$90^\circ$$ behind. The latter two voltage phasors point in opposite directions, so

$$
Z=R+j\left(\omega L-\frac1{\omega C}\right),
\qquad
\lvert Z\rvert=\sqrt{R^2+(X_L-X_C)^2}.
$$

For $$R>0$$, the phase of voltage relative to current is

$$
\phi=\tan^{-1}\left(\frac{X_L-X_C}{R}\right).
$$

If the source is $$v(t)=V_0\cos(\omega t+\phi_v)$$, then

$$
i(t)=\frac{V_0}{\lvert Z\rvert}\cos(\omega t+\phi_v-\phi).
$$

<img class="note-img note-img--w480" src="/assets/physics/usapho/em-original/rlc-phasor.svg" alt="Series RLC voltage phasors: resistor voltage to the right, inductor up, capacitor down, and their vector sum" loading="lazy" decoding="async" />

When $$X_L>X_C$$ the circuit is net inductive and current lags. When $$X_C>X_L$$ it is net capacitive and current leads. The total voltage amplitude obeys

$$
V_0^2=V_{R,0}^2+(V_{L,0}-V_{C,0})^2,
$$

not $$V_0=V_{R,0}+V_{L,0}+V_{C,0}$$. Individual inductor or capacitor voltages can exceed the source amplitude because they largely cancel in the sum.

### Resonance

At $$X_L=X_C$$,

$$
\omega_0=\frac1{\sqrt{LC}},\qquad Z=R.
$$

For a fixed source amplitude, the series current reaches its maximum $$I_0=V_0/R$$ and is in phase with the source. Energy still exchanges between the capacitor and inductor; their voltage drops cancel rather than each vanishing. Resistance limits the current and dissipates the energy that the source must replace.

<div class="theorem-box">

**Example.** At a certain frequency a series circuit has $$R=30\ \Omega$$, $$X_L=80\ \Omega$$, and $$X_C=40\ \Omega$$. The supply is $$100\ \text{V rms}$$. Find the current, phase, and component voltages.

$$
Z=30+j40\ \Omega,\quad \lvert Z\rvert=50\ \Omega,\quad
I_{\text{rms}}=2.0\ \text{A}.
$$

Current lags by $$\phi=\tan^{-1}(40/30)\approx53.1^\circ$$. The component RMS voltages are

$$
V_R=60\ \text{V},\qquad V_L=160\ \text{V},\qquad V_C=80\ \text{V}.
$$

Their vector sum is $$\sqrt{60^2+(160-80)^2}=100\ \text{V}$$, agreeing with the supply.

</div>

---

## Parallel RLC circuits

In a parallel circuit, all branches share the same voltage, so use it as the phase reference. The resistor current is in phase with the voltage, the capacitor current leads by $$90^\circ$$, and the inductor current lags by $$90^\circ$$:

$$
\widetilde I=\widetilde V\left[\frac1R+j\left(\omega C-\frac1{\omega L}\right)\right].
$$

Thus the total admittance and impedance are

$$
Y=\frac1R+j\left(\omega C-\frac1{\omega L}\right),\qquad Z=\frac1Y.
$$

The source-current amplitude is

$$
I_0=V_0\sqrt{\frac1{R^2}+\left(\omega C-\frac1{\omega L}\right)^2}.
$$

For ideal parallel branches, at $$\omega_0=1/\sqrt{LC}$$ the capacitor and inductor currents cancel at the source. Their individual currents can be large, but the supply only provides the resistor current. Unlike series resonance, the source current is minimized and the input impedance maximized for this particular parallel topology. A real coil’s series resistance changes the exact result.

---

## Switching transients versus steady state

A sinusoidal particular solution does not generally satisfy an initially uncharged capacitor or an assigned initial inductor current. The complete response is

$$
\text{response}=\text{sinusoidal particular solution}+\text{natural response}.
$$

For a series RC circuit,

$$
R\frac{dq}{dt}+\frac qC=v_s(t).
$$

If $$q_{\text{ss}}(t)$$ is a sinusoidal particular solution, then

$$
q(t)=q_{\text{ss}}(t)+Ae^{-t/(RC)}
$$

also solves the equation, because the added exponential solves the homogeneous equation. The initial charge determines $$A=q(0)-q_{\text{ss}}(0)$$, and differentiating gives the current. Adding a current transient without checking the capacitor’s charge can miss this constraint.

<div class="theorem-box">

**Example.** An initially uncharged series RC circuit is connected at $$t=0$$ to $$v_s(t)=V_0\sin\omega t$$. Find the current including the transient.

Let $$a=\omega RC$$. A particular charge solution is

$$
q_{\text{ss}}(t)=\frac{CV_0}{1+a^2}(\sin\omega t-a\cos\omega t).
$$

It has $$q_{\text{ss}}(0)=-CV_0a/(1+a^2)$$, so it cannot be the complete response. Enforcing $$q(0)=0$$ gives

$$
q(t)=\frac{CV_0}{1+a^2}\left(\sin\omega t-a\cos\omega t+ae^{-t/(RC)}\right).
$$

Differentiating,

$$
i(t)=\frac{\omega CV_0}{1+a^2}\left(\cos\omega t+a\sin\omega t-e^{-t/(RC)}\right).
$$

Now $$i(0)=0$$, consistent with the initially zero source and capacitor voltages. After several time constants, the exponential disappears and the phasor result remains.

</div>

---

## Power and energy in AC circuits

Instantaneous power is always $$p(t)=v(t)i(t)$$ under the passive sign convention. Positive power means the component absorbs energy; negative power means it returns energy.

Taking current as the phase reference,

$$
i(t)=I_0\cos\omega t,\qquad v(t)=V_0\cos(\omega t+\phi).
$$

Using the product-to-sum identity,

$$
p(t)=\frac{V_0I_0}{2}\left[\cos\phi+\cos(2\omega t+\phi)\right].
$$

The second term averages to zero over a cycle, leaving

$$
P_{\text{avg}}=\frac12V_0I_0\cos\phi
=V_{\text{rms}}I_{\text{rms}}\cos\phi.
$$

The **power factor** is $$\cos\phi$$. Large RMS current does not necessarily mean large average power if much of the energy is returned each cycle.

- A resistor has $$\phi=0$$ and dissipates $$P_{\text{avg}}=I_{\text{rms}}^2R=V_{\text{rms}}^2/R$$.
- An ideal capacitor has $$\phi=-\pi/2$$ and zero average power. It stores energy $$Cv^2/2$$ while charging and returns it while discharging.
- An ideal inductor has $$\phi=+\pi/2$$ and zero average power. It stores energy $$Li^2/2$$ as current magnitude grows and returns it as that magnitude falls.

For the series RLC example above, $$\cos\phi=30/50=0.60$$, so $$P=100(2)(0.60)=120\ \text{W}$$, also equal to $$I_{\text{rms}}^2R$$. The apparent power is $$VI=200\ \text{VA}$$; it is not the dissipated power.

With RMS phasors, complex power is

$$
S=\widetilde V\widetilde I^*=P+jQ,
$$

where the star means complex conjugate and $$Q$$ is reactive power. With peak phasors, use $$S=\tfrac12\widetilde V\widetilde I^*$$ instead. For a load impedance $$Z$$, $$P=I_{\text{rms}}^2\operatorname{Re}Z$$. Taking the real parts of voltage and current separately before multiplying is not the same as multiplying the phasors.

---

## Transformers

A transformer uses a changing common flux in a core to couple two coils. The input coil has $$N_1$$ turns and the output coil has $$N_2$$ turns. In the ideal model, winding resistance, leakage flux, and core losses are negligible, and the magnetizing current is neglected.

<img class="note-img note-img--w480" src="/assets/physics/usapho/em-original/transformer.svg" alt="Primary and secondary coils around a shared magnetic core, with turns, input voltage, output voltage, and load labeled" loading="lazy" decoding="async" />

Each turn links the same flux $$\Phi$$, so Faraday’s law gives emf magnitudes proportional to the number of turns. With compatible voltage-reference polarities,

$$
\frac{V_2}{V_1}=\frac{N_2}{N_1}.
$$

More output turns give a step-up transformer; fewer give a step-down transformer. The instantaneous sign depends on winding orientation and chosen terminal polarities. These amplitude ratios work with either peak or RMS values if used consistently.

Conservation of power in the ideal transformer gives the current-magnitude ratio

$$
\frac{I_2}{I_1}=\frac{N_1}{N_2}.
$$

For a resistive load, voltage and current are in phase on each side, and $$V_1I_1=V_2I_2$$ is the transferred power. A reactive load retains its phase relationship through an ideal transformer; it does not become in phase just because a transformer is present.

An unloaded real transformer still draws a small magnetizing current, approximately inductive, plus a loss component. The idealized zero-current limit is an approximation. Soft magnetic cores reduce hysteresis loss but do not make it literally zero.

### Why raise transmission voltage?

For a fixed real power and power factor, increasing voltage reduces current. In a simplified unity-power-factor model,

$$
I=\frac PV,\qquad P_{\text{line loss}}=I^2R_{\text{line}}=\frac{P^2R_{\text{line}}}{V^2}.
$$

Doubling the transmission voltage reduces resistive loss to one quarter if the transmitted power and line resistance stay fixed. This is why generation is followed by step-up transformation for transmission and step-down transformation near the load. The class-note chain of a few to a few tens of kilovolts at generation, hundreds of kilovolts in transmission, and about $$120\ \text{V}$$ at a household outlet illustrates the scale changes; it is not a universal set of voltages or a fixed loss percentage.

AC is convenient to produce with rotating generators and to transform using a changing flux. A transformer cannot continuously transform a constant DC input by this mechanism.

### Reflected impedance and matching

A secondary load $$Z_L$$ appears at the primary as

$$
Z_{\text{in}}=\frac{\widetilde V_1}{\widetilde I_1}
=\left(\frac{N_1}{N_2}\right)^2 Z_L.
$$

One factor of the turns ratio comes from voltage and another from the inverse current ratio. A transformer therefore changes the impedance seen by a source without dissipating power in an extra resistor.

For a source with purely resistive internal resistance $$r$$ and a resistive load $$R_L$$, maximum power transfer occurs when the reflected resistance equals $$r$$:

$$
\left(\frac{N_1}{N_2}\right)^2R_L=r,
\qquad \frac{N_1}{N_2}=\sqrt{\frac r{R_L}}.
$$

<div class="theorem-box">

**Example.** A source has internal resistance $$800\ \Omega$$ and drives an $$8\ \Omega$$ load through an ideal transformer. Find the turns ratio for maximum load power.

$$
\frac{N_1}{N_2}=\sqrt{\frac{800}{8}}=10.
$$

The load looks like $$800\ \Omega$$ at the primary. If the source’s open-circuit RMS voltage is $$V_s$$, the maximum load power is $$V_s^2/(4r)$$. Equal power is lost in the source resistance at this matching point, so maximum power transfer is not maximum efficiency. The low-resistance-speaker model is an illustration of matching, not a claim that every modern audio amplifier should be matched this way.

</div>

For complex source impedance, maximum average power instead requires conjugate matching, $$Z_{\text{in}}=Z_s^*$$. A real turns ratio alone cannot generally cancel arbitrary source reactance.

---

## Rectifiers and smoothing

A diode conducts mainly in one direction. A half-wave rectifier conducts during one half-cycle; a full-wave bridge routes both half-cycles through the load in the same direction. With ideal diodes, a sinusoidal input produces a full-wave output proportional to $$\lvert\sin\omega t\rvert$$. This is unidirectional, but it is not constant DC.

Place a capacitor across the load to reduce the ripple. Near each voltage peak, the conducting diodes recharge it. As the source falls below the capacitor voltage, the diodes stop conducting and the capacitor supplies the load, approximately discharging with time constant $$R_LC$$. A larger capacitor or lighter load produces less voltage drop between peaks.

<img class="note-img note-img--w480" src="/assets/physics/usapho/em-original/rectifier.svg" alt="Full-wave rectified voltage and capacitor-smoothed output, showing recharge near peaks and droop between peaks" loading="lazy" decoding="async" />

For small ripple and approximately constant load current,

$$
\Delta V_{\text{pp}}\approx\frac{I_{\text{load}}}{f_{\text{ripple}}C}.
$$

For full-wave rectification $$f_{\text{ripple}}=2f$$; for half-wave it is $$f$$. This follows from $$\Delta Q\approx I_{\text{load}}\Delta t$$ and $$\Delta V=\Delta Q/C$$. Real diode drops and brief charging pulses also matter. The capacitor smooths the output, but it does not regulate it against every change in load.

---

## Frequency response and filters

A circuit’s **transfer function** compares output and input phasors at the same frequency:

$$
H(j\omega)=\frac{\widetilde V_{\text{out}}}{\widetilde V_{\text{in}}}.
$$

Its magnitude gives the amplitude ratio and its argument gives the phase shift. Here $$H(j\omega)$$ denotes a transfer function, not the magnetic field strength $$\vec H$$.

### RC low-pass filter

Connect a resistor in series with a capacitor and measure output across the capacitor. Assuming negligible loading, the impedance voltage divider gives

$$
H_{\text{LP}}=\frac{Z_C}{R+Z_C}=\frac1{1+j\omega RC}.
$$

At low frequency, the capacitor impedance is large and most of the input appears across it. At high frequency it is small, so the output is suppressed:

$$
\lvert H_{\text{LP}}\rvert=\frac1{\sqrt{1+(\omega RC)^2}},
\qquad \arg H_{\text{LP}}=-\tan^{-1}(\omega RC).
$$

The cutoff is $$\omega_c=1/(RC)$$, where the amplitude has fallen to $$1/\sqrt2$$ of its low-frequency value. Calling the capacitor a bypass for AC refers to the high-frequency part being diverted away from the output, not to all frequencies behaving identically.

### CR high-pass filter

Measure output across the resistor instead, with the capacitor in series at the input:

$$
H_{\text{HP}}=\frac{R}{R+Z_C}=\frac{j\omega RC}{1+j\omega RC},
\qquad
\lvert H_{\text{HP}}\rvert=\frac{\omega RC}{\sqrt{1+(\omega RC)^2}}.
$$

At low frequency the capacitor blocks most current and the resistor voltage is small. At high frequency its impedance is small and the resistor receives nearly the full input. The cutoff is again $$1/(RC)$$. For positive frequency, its phase is $$\pi/2-\tan^{-1}(\omega RC)$$.

<img class="note-img note-img--w480" src="/assets/physics/usapho/em-original/filters.svg" alt="RC low-pass and high-pass circuits and their gain curves versus normalized angular frequency" loading="lazy" decoding="async" />

### RLC band-pass response

For a series RLC circuit with output across the resistor,

$$
H_{\text{BP}}=\frac{R}{R+j(\omega L-1/(\omega C))}.
$$

Low frequencies are suppressed by the capacitor and high frequencies by the inductor. Near $$\omega_0=1/\sqrt{LC}$$, the reactive terms cancel and the output is largest. These filters have gradual roll-offs, not a sharp boundary at which a frequency suddenly disappears. Connecting a finite load changes the effective impedances and can alter the response.

---

## Fourier series and nonsinusoidal sources

A periodic waveform can be decomposed into a DC component and harmonics of its fundamental frequency. For ordinary piecewise-smooth circuit waveforms of period $$T$$, write

$$
v(t)=a_0+\sum_{n=1}^{\infty}\left[a_n\cos(n\omega_0t)+b_n\sin(n\omega_0t)\right],
\qquad \omega_0=\frac{2\pi}{T}.
$$

With this convention,

$$
a_0=\frac1T\int_0^T v(t)\,dt,
\quad a_n=\frac2T\int_0^T v(t)\cos(n\omega_0t)\,dt,
\quad b_n=\frac2T\int_0^T v(t)\sin(n\omega_0t)\,dt.
$$

The coefficients are Fourier-series integrals; no separate numerical Fourier transform is necessary. At a jump discontinuity, the series converges to the midpoint of the two limiting values rather than an arbitrarily assigned value at the jump.

For a **linear** circuit, solve the DC response and each sinusoidal response separately, using $$Z(n\omega_0)$$ or $$H(jn\omega_0)$$ for each harmonic, then add the time-domain results. The impedances change with frequency, so different harmonics acquire different amplitude changes and phase shifts.

For example, a low-pass filter can preserve the constant part of a rectified waveform while attenuating its ripple harmonics. Superposition applies to the linear filter, not to the diode rectifier itself: diodes are nonlinear, so treating every harmonic independently through the rectifier generally fails.

---

## Hysteresis loss in an iron core

A ferromagnetic core has a history-dependent $$B$$–$$H$$ relation. Even if a coil returns to the same field state after a full cycle, some supplied energy has become heat through irreversible changes in its domains.

For a long core of length $$\ell$$ and cross-sectional area $$A$$ carrying an $$N$$-turn coil, neglect winding resistance and leakage. Ampère’s law gives $$H=NI/\ell$$, while the terminal voltage is $$v=NA\,dB/dt$$. The source supplies

$$
dW=vI\,dt=NAI\,dB=(A\ell)H\,dB.
$$

Writing the core volume as $$\mathcal V=A\ell$$, the dissipated energy per cycle is

$$
W_{\text{cycle}}=\mathcal V\oint H\,dB.
$$

Its magnitude per unit volume is the enclosed area of the $$B$$–$$H$$ hysteresis loop. With $$H$$ horizontal and $$B$$ vertical, a dissipative cycle traverses this loop counterclockwise and $$\oint H\,dB>0$$. Reversing the axis order reverses that graphical orientation, so the physical point is positive dissipation, not an axis-independent “always counterclockwise” rule.

At frequency $$f$$, for a fixed loop shape, $$P_{\text{hyst}}=fW_{\text{cycle}}$$. This is separate from winding Joule heating and eddy-current loss. Soft magnetic cores with narrow loops reduce hysteresis loss; laminations mainly reduce eddy currents. The [magnetism page](/notes/physics/eandm/magnetism/#hysteresis) explains remanence and coercivity; the [University of Illinois notes on hysteresis loss](https://courses.physics.illinois.edu/phys401/sp2020/lectures/lecture13.pdf) give the same work-per-cycle interpretation.

---

## Equation summary

:::equations

| Idea | Equation | Conditions |
| --- | --- | --- |
| Frequency / RMS | $$\omega=2\pi f,\quad T=1/f,\quad V_{\text{rms}}=V_0/\sqrt2,\quad I_{\text{rms}}=I_0/\sqrt2$$ | RMS factors shown are for sinusoids |
| Component laws | $$v_R=Ri,\quad i_C=C\,dv_C/dt,\quad v_L=L\,di_L/dt$$ | Passive sign convention |
| Impedances | $$Z_R=R,\quad Z_C=1/(j\omega C),\quad Z_L=j\omega L$$ | Cosine / $$e^{j\omega t}$$ convention |
| Phasor Ohm’s law | $$\widetilde V=Z\widetilde I$$ | Same frequency and amplitude convention |
| Combining components | $$Z_s=\sum Z_k,\quad 1/Z_p=\sum 1/Z_k$$ | Series / parallel, respectively |
| Series RLC | $$Z=R+j(X_L-X_C),\quad\phi=\arg Z$$ | $$\phi=\phi_v-\phi_i$$; current lags if $$\phi>0$$ |
| Parallel RLC | $$Y=1/R+j(\omega C-1/(\omega L))$$ | Ideal separate parallel branches |
| Ideal resonance | $$\omega_0=1/\sqrt{LC}$$ | Topology determines whether source current is maximal or minimal |
| RC transient | $$q=q_{\text{ss}}+Ae^{-t/(RC)}$$ | $$A$$ fixed by initial charge |
| Average power | $$P=V_{\text{rms}}I_{\text{rms}}\cos\phi$$ | Sinusoidal voltage and current |
| Complex power | $$S=\widetilde V\widetilde I^*=P+jQ$$ | RMS phasors; insert factor $$1/2$$ for peak phasors |
| Ideal transformer | $$V_2/V_1=N_2/N_1,\quad I_2/I_1=N_1/N_2$$ | Amplitude ratios, negligible losses and magnetizing current |
| Reflected load | $$Z_{\text{in}}=(N_1/N_2)^2Z_L$$ | Ideal transformer |
| Resistive matching | $$N_1/N_2=\sqrt{r/R_L},\quad P_{\max}=V_s^2/(4r)$$ | $$V_s$$ is open-circuit RMS source voltage |
| Line loss | $$P_{\text{loss}}=I_{\text{rms}}^2R_{\text{line}}$$ | Resistive loss, not total transmitted power |
| Small rectifier ripple | $$\Delta V_{\text{pp}}\approx I_{\text{load}}/(f_{\text{ripple}}C)$$ | Approximate constant load current; $$f_{\text{ripple}}=2f$$ for full wave |
| Low-pass / high-pass | $$H_{\text{LP}}=1/(1+j\omega RC),\quad H_{\text{HP}}=j\omega RC/(1+j\omega RC)$$ | Unloaded RC / CR voltage dividers |
| Band-pass | $$H_{\text{BP}}=R/[R+j(\omega L-1/(\omega C))]$$ | Series RLC, output across $$R$$ |
| Periodic-source response | $$v(t)=a_0+\sum_{n\ge1}[a_n\cos(n\omega_0t)+b_n\sin(n\omega_0t)]$$ | In a linear circuit, solve each harmonic at its own frequency and add |
| Hysteresis loss | $$W_{\text{cycle}}=\mathcal V\oint H\,dB,\quad P_{\text{hyst}}=fW_{\text{cycle}}$$ | Core volume $$\mathcal V$$; fixed cyclic loop |

:::
