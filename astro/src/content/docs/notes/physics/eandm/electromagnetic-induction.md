---
title: "Electromagnetic Induction"
description: "Learn USAPhO induction through Faraday’s law, moving rods, back emf, induced electric fields, RL transients, and magnetic energy."
sidebar:
  order: 5
---

## Faraday’s law and induced emf

Moving a magnet into a conducting loop can produce a current without a battery. So can changing the current in a nearby coil, even when neither coil moves. What these experiments share is a changing **magnetic flux** through the circuit.

Choose a positive direction around the loop and use the right-hand rule to choose its positive area normal. Faraday’s law gives the signed electromotive force, or **emf**, around that loop:

$$
\mathcal E=-\frac{d\Phi_B}{dt},\qquad \Phi_B=\int_S\vec B\cdot d\vec A.
$$

Emf is energy supplied per unit charge around a circuit, measured in volts, despite the word “force” in its name. It can exist in an open circuit, but a sustained conduction current requires a closed conducting path. If the loop has resistance $$R$$ and its self-inductance is negligible, $$I=\mathcal E/R$$.

For $$N$$ turns linked by the same flux, the emfs add. Define the **flux linkage** $$\lambda=N\Phi_B$$, distinguishing it from the flux through just one turn:

$$
\mathcal E=-\frac{d\lambda}{dt}=-N\frac{d\Phi_B}{dt}.
$$

For a uniform field and a flat loop, $$\Phi_B=BA\cos\theta$$. Flux can change because the field changes, the loop’s area changes, the loop rotates, or the loop moves through a nonuniform field. Translating a rigid loop entirely within a uniform, steady field does not change its flux.

### Lenz’s law and the minus sign

**Lenz’s law** says that the induced current produces flux opposing the **change** in the original flux. If an outward field is increasing, the induced current produces an inward field. If the outward field is decreasing, the induced current produces an outward field to oppose that decrease.

It is not generally correct to say that the induced field opposes the original field. Nor does a negative emf mean the current is physically “negative”: it means the emf points opposite the loop direction you chose.

:::strategy
1. Identify the original flux direction and whether that flux is increasing or decreasing.
2. Find the induced field direction that opposes the change.
3. Curl your right-hand fingers around the loop with your thumb along that induced field. Your fingers give conventional current.
4. Use the flux derivative for the magnitude, keeping the same orientation convention throughout.
:::

---

## Motional emf

### A rod sliding on rails

Consider a conducting rod of length $$\ell$$ moving right at speed $$v$$ along two rails. A resistor closes the circuit on the left, and a uniform magnetic field points into the page. The loop area increases at rate $$\ell v$$, so the inward flux increases.

<img class="note-img note-img--w480" src="/assets/physics/usapho/em-original/sliding-rod.svg" alt="Rod moving right on rails in an inward magnetic field, with upward current in the rod and a leftward magnetic drag force" loading="lazy" decoding="async" />

Lenz’s law requires an outward induced field, giving counterclockwise current, upward through the rod. The emf magnitude is

$$
\lvert\mathcal E\rvert=B\frac{dA}{dt}=B\ell v.
$$

Here the motional contribution is concentrated in the moving rod, which acts as the source driving the rest of the circuit. The formula assumes the rod, its velocity, and the field are mutually perpendicular. More generally, for a moving wire segment,

$$
\mathcal E_{a\to b}=\int_a^b(\vec u\times\vec B)\cdot d\vec\ell,
$$

where $$\vec u$$ is the local velocity of the wire, not the carrier’s drift velocity.

### Charge separation in an isolated rod

Even without a closed circuit, the moving rod’s charges feel $$q\vec u\times\vec B$$. In the diagram, positive charges are pushed upward and electrons downward, leaving the top end positive. The separated charges create a downward electric field that grows until it balances the magnetic force along the rod:

$$
\vec E+\vec u\times\vec B=0,\qquad E=vB.
$$

The resulting end-to-end potential difference has magnitude $$\lvert\Delta V\rvert=E\ell=B\ell v$$. Connecting the rod to the rails allows charges to circulate, so the rod continuously separates charge while the external mechanical agent keeps it moving.

### Where the electrical energy comes from

Once current flows, the rod experiences a magnetic force opposite its motion. For total resistance $$R$$ and negligible inductance,

$$
I=\frac{B\ell v}{R},\qquad F_B=I\ell B=\frac{B^2\ell^2v}{R}.
$$

To maintain constant speed, an external force must balance that drag. Its mechanical power becomes Joule heating:

$$
P_{\text{ext}}=F_Bv=\mathcal E I=I^2R.
$$

This does not mean the magnetic force does work on individual charges. A carrier’s laboratory velocity includes both the rod velocity and its drift along the rod. The magnetic force’s power contributions along these two motions cancel because $$q(\vec v_{\text{carrier}}\times\vec B)\cdot\vec v_{\text{carrier}}=0$$. The external force supplies the energy; the magnetic interaction couples the mechanical motion to the electrical current.

<div class="theorem-box">

**Example.** A $$0.40\ \text{m}$$ rod moves at $$3.0\ \text{m/s}$$ through a $$0.50\ \text{T}$$ field. The closed circuit has resistance $$2.0\ \Omega$$. Find its emf, current, required pulling force, and heating power.

$$
\mathcal E=B\ell v=0.60\ \text{V},\qquad I=\frac{0.60}{2.0}=0.30\ \text{A}.
$$

The pull must balance magnetic drag:

$$
F_{\text{ext}}=BI\ell=0.060\ \text{N}.
$$

Both energy calculations agree:

$$
F_{\text{ext}}v=0.18\ \text{W}=I^2R.
$$

</div>

### Back emf in a motor

Reverse the energy flow by connecting a voltage source $$V_0$$ that drives current through the rod and makes the magnetic force push it right. As the rod accelerates, its motional emf opposes the supply. If the total resistance is $$r$$ and inductive transients are negligible,

$$
V_0-B\ell v-Ir=0,\qquad I=\frac{V_0-B\ell v}{r}.
$$

The driving force falls as speed rises:

$$
F_{\text{drive}}=B\ell I=\frac{B\ell}{r}(V_0-B\ell v).
$$

At startup, $$v=0$$, so the current and force are largest: $$I_{\text{stall}}=V_0/r$$ and $$F_{\text{stall}}=B\ell V_0/r$$. With a resisting load, steady speed occurs when drive and load forces balance. With no load or losses, the limiting speed is $$V_0/(B\ell)$$. A rotating motor has the analogous back emf proportional to angular speed.

The winding resistance still obeys Ohm’s law, but the whole motor is not just that resistance: $$V_0=Ir+\mathcal E_{\text{back}}$$. Its input power splits into heating and mechanical output,

$$
V_0I=I^2r+\mathcal E_{\text{back}}I.
$$

Although force decreases with speed, mechanical power $$Fv$$ need not decrease. It is zero at stall because the motor is not moving.

---

## Electric fields produced by changing magnetic fields

A stationary loop can have induced emf too. Here the charges do not need the conductor to move: a changing magnetic field produces a circulating electric field that acts through $$\vec F=q\vec E$$.

For a fixed path,

$$
\oint_C\vec E\cdot d\vec\ell
=-\frac{d}{dt}\int_S\vec B\cdot d\vec A,
\qquad \nabla\times\vec E=-\frac{\partial\vec B}{\partial t}.
$$

This electric field is **nonconservative**. Its closed-loop integral need not vanish, so it cannot be described everywhere by a single scalar potential with $$\vec E=-\nabla V$$. A charge can receive energy over a complete circuit even though it returns to its starting position. The field exists whether or not a conducting loop is placed there.

The induced field forms circles in an axially symmetric example, but arbitrary induced fields need not have simple circular or closed field lines. Usually Faraday’s law gives the circulation more easily than the full local field.

### A changing field in a cylindrical region

<div class="theorem-box">

**Example.** A uniform field $$\vec B=B(t)\hat z$$ fills a long cylindrical region of radius $$R$$ and is negligible outside. Find the induced azimuthal electric field at radius $$r$$, assuming axial symmetry.

Choose counterclockwise circulation viewed from positive $$z$$, so the positive normal is $$+\hat z$$. Symmetry makes the azimuthal component $$E_\phi$$ constant around each circle. For $$r<R$$, the enclosed flux is $$\pi r^2B$$:

$$
2\pi rE_\phi=-\pi r^2\frac{dB}{dt}.
$$

For $$r>R$$, only the field-filled area $$\pi R^2$$ contributes. Thus

$$
E_\phi(r)=
\begin{cases}
-\dfrac r2\dfrac{dB}{dt},&r\le R,\\[6pt]
-\dfrac{R^2}{2r}\dfrac{dB}{dt},&r\ge R.
\end{cases}
$$

An increasing outward field gives $$E_\phi<0$$, meaning clockwise circulation. The electric field remains nonzero outside the field-filled region because those larger loops still enclose changing flux. Its magnitude grows linearly inside and falls as $$1/r$$ outside.

</div>

<img class="note-img note-img--w480" src="/assets/physics/usapho/em-original/induced-field.svg" alt="Clockwise induced electric-field circles around an increasing outward magnetic field, including a circle outside the field-filled cylinder" loading="lazy" decoding="async" />

### Eddy currents

In a bulk conductor, induced electric fields drive circulating currents through many possible paths rather than through a single wire loop. These are **eddy currents**. Their magnetic effect opposes the flux change that produces them, and their resistance dissipates energy as heat. This accounts for magnetic braking and some heating in transformer cores. Laminating a core into insulated thin sheets interrupts large current loops and reduces that loss.

An electric field does not “oppose a magnetic field” as a vector; the two are different quantities. Lenz’s law refers to the flux produced by the resulting current opposing the original flux **change**.

### Moving and stationary descriptions

For a moving material loop in the ordinary quasistatic circuit setting, both mechanisms enter the emf:

$$
\mathcal E=\oint_{C(t)}(\vec E+\vec u\times\vec B)\cdot d\vec\ell
=-\frac{d\Phi_B}{dt}.
$$

The division between electric and magnetic effects depends on reference frame. A loop moving relative to a stationary magnet can be described using magnetic forces in the magnet’s frame; in the loop’s frame the transformed electric field contributes. The fields and currents transform consistently, so these descriptions do not contradict one another. This does not mean that every electric field, including fields from surface charges, is zero in the magnet’s frame.

---

## Self-inductance and inductors

A current creates magnetic flux through its own circuit. Changing that current changes the flux, producing an emf in the same circuit. This is **self-induction**. For fixed geometry and a linear magnetic response, flux linkage is proportional to current:

$$
\lambda=LI,\qquad \mathcal E_{\text{self}}=-L\frac{dI}{dt}.
$$

The constant $$L$$ is the inductance, measured in henries: $$1\ \text{H}=1\ \text{V}\cdot\text{s/A}$$. An inductor opposes a **change in current**. When current increases, its induced emf opposes the current; when current decreases, its emf supports the existing current.

### Inductance of a long solenoid

For $$N$$ turns, length $$\ell$$, and cross-sectional area $$A$$, the vacuum-core field is $$B=\mu_0 NI/\ell$$. Each turn links flux $$BA$$, giving

$$
\lambda=NBA=\frac{\mu_0N^2A}{\ell}I,
\qquad L=\frac{\mu_0N^2A}{\ell}=\mu_0n^2A\ell.
$$

The square dependence on $$N$$ has two causes: more turns produce a stronger field, and more turns link that field. A linear core can replace $$\mu_0$$ by an appropriate permeability when the field approximation remains valid. Saturation and hysteresis make a constant-$$L$$ model unreliable for a general ferromagnetic core.

### Terminal voltage and sign convention

Let positive current enter terminal $$a$$ and leave $$b$$, and define the voltage drop $$v_L=V_a-V_b$$. This **passive sign convention** gives

$$
v_L=L\frac{dI}{dt}.
$$

The terminal voltage drop and the internally induced emf have opposite signs; mixing them is a common source of errors. If the winding has resistance $$r$$, its total terminal drop is $$v=L\,dI/dt+rI$$.

A finite voltage cannot cause an instantaneous current jump in an ideal finite inductor. Under constant voltage $$V_0$$ and zero resistance,

$$
I(t)=I(0)+\frac{V_0}{L}t.
$$

There is no finite steady current in this ideal zero-resistance case. With resistance present, a DC steady state has $$dI/dt=0$$, so only the resistive voltage drop remains.

---

## RL transients

Connect an initially unenergized inductor $$L$$ in series with resistance $$R$$ and a DC source $$V_0$$. Kirchhoff’s loop equation is

$$
L\frac{dI}{dt}+RI=V_0.
$$

Initially the inductor takes the entire source voltage, so $$dI/dt=V_0/L$$. As current rises, the resistor’s drop grows, leaving less voltage across the inductor and slowing the increase. Eventually $$I\to V_0/R$$.

<div class="theorem-box">

**Proof (RL current growth).** The final current is $$I_\infty=V_0/R$$. Write the equation in terms of the difference from that value:

$$
\frac{d(I-I_\infty)}{dt}=-\frac RL(I-I_\infty).
$$

The difference decays exponentially. Applying $$I(0)=0$$ gives

$$
I(t)=\frac{V_0}{R}\left(1-e^{-t/\tau}\right),\qquad \tau=\frac LR.
$$

After one time constant the current is about $$63\%$$ of its final value. A larger inductance slows the response; the effective resistance in the inductor’s current path determines $$R$$.

</div>

<img class="note-img note-img--w480" src="/assets/physics/usapho/em-original/rl-response.svg" alt="Normalized RL current growth and decay, with the one-time-constant values marked" loading="lazy" decoding="async" />

If the source is removed while a closed discharge path of resistance $$R$$ remains, the current decays as

$$
I(t)=I_0e^{-t/\tau}.
$$

Opening the current path without providing a discharge route is different: the inductor can produce a large voltage, limited in practice by capacitance, insulation breakdown, or an arc. Do not force the current to jump to zero while also assuming a finite voltage.

---

## Magnetic energy

During current growth, some source energy is stored in the inductor rather than immediately dissipated. With the passive sign convention, its absorbed power is

$$
p_L=v_LI=LI\frac{dI}{dt}.
$$

Integrating from zero current for constant $$L$$ gives

$$
U_L=\int_0^I LI'\,dI'=\frac12LI^2.
$$

When the current decreases, $$p_L<0$$ and the inductor returns stored energy to the circuit. An ideal inductor stores energy; its winding resistance dissipates energy.

For the long vacuum solenoid, substitute $$L=\mu_0n^2A\ell$$ and $$I=B/(\mu_0n)$$:

$$
U_L=\frac{B^2}{2\mu_0}A\ell.
$$

The magnetic energy density in vacuum is therefore

$$
u_B=\frac{B^2}{2\mu_0}.
$$

For a linear, isotropic, nondispersive medium without hysteresis, $$u_B=\tfrac12\vec B\cdot\vec H$$. This simple stored-energy expression does not capture irreversible losses in a hysteretic core; those are discussed in [AC circuits](/notes/physics/eandm/ac-circuits/#hysteresis-loss-in-an-iron-core).

---

## AC generators

A generator uses external mechanical work to rotate a coil in a magnetic field. For $$N$$ turns of area $$A$$ in uniform field $$B$$, let the angle between the normal and the field be $$\theta=\omega t$$. Then

$$
\lambda=NBA\cos\omega t,
\qquad \mathcal E=-\frac{d\lambda}{dt}=NBA\omega\sin\omega t.
$$

The peak emf is $$\mathcal E_0=NBA\omega$$. It is zero when flux is at an extremum, because the flux is momentarily not changing, and largest when the flux passes through zero most rapidly. The same result follows by adding the motional emfs on the two active sides of a rectangular coil.

This is an alternating **emf** even with an open output. Once a load is connected, the current depends on that load and may be out of phase with the emf. A generator uses slip rings to retain the alternating polarity; a DC motor’s split-ring commutator instead reverses its coil connections each half-turn. Continue with [AC circuits](/notes/physics/eandm/ac-circuits/) for phase, impedance, and power.

---

## Equation summary

:::equations

| Idea | Equation | Conditions |
| --- | --- | --- |
| Faraday’s law | $$\mathcal E=-d\lambda/dt,\quad\lambda=N\Phi_B$$ | Same flux per turn; right-hand-rule orientation |
| Motional emf | $$\mathcal E_{a\to b}=\int_a^b(\vec u\times\vec B)\cdot d\vec\ell$$ | Rigid perpendicular rod: magnitude $$B\ell v$$ |
| Generator rod | $$I=B\ell v/R,\quad F_B=B^2\ell^2v/R,\quad F_{\text{ext}}v=I^2R$$ | Constant speed, negligible self-inductance |
| Motor back emf | $$I=(V_0-B\ell v)/r,\quad F_{\text{drive}}=B\ell I$$ | Quasisteady sliding-rod motor model |
| Fixed-path induction | $$\oint\vec E\cdot d\vec\ell=-d\Phi_B/dt$$ | Nonconservative induced electric field |
| Cylindrical field region | $$E_\phi=-\frac r2\dot B\ (r\le R),\quad E_\phi=-\frac{R^2}{2r}\dot B\ (r\ge R)$$ | Uniform axial field inside radius $$R$$ |
| Self-inductance | $$\lambda=LI,\quad\mathcal E_{\text{self}}=-L\,dI/dt$$ | Fixed geometry, linear response |
| Long solenoid | $$L=\mu_0N^2A/\ell$$ | Vacuum core, negligible end effects |
| Inductor voltage drop | $$v_L=L\,dI/dt$$ | Current enters the terminal labeled positive |
| Constant applied voltage | $$I(t)=I(0)+V_0t/L$$ | Ideal inductor, no series resistance |
| RL response | $$\tau=L/R,\quad I_{\text{on}}=\frac{V_0}{R}(1-e^{-t/\tau}),\quad I_{\text{off}}=I_0e^{-t/\tau}$$ | Initially zero current for turn-on; closed resistive path for decay |
| Stored energy | $$U_L=\frac12LI^2,\quad u_B=\frac{B^2}{2\mu_0}$$ | Constant $$L$$; energy density in vacuum |
| Rotating-coil generator | $$\mathcal E=NBA\omega\sin\omega t$$ | Uniform field, constant angular speed |

:::
