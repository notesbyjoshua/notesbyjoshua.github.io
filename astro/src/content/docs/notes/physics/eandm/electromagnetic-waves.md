---
title: "Maxwell’s Equations and Electromagnetic Waves"
description: "USAPhO notes on displacement current, Maxwell’s equations, electromagnetic waves, polarization, radiation pressure, and the electromagnetic spectrum."
sidebar:
  order: 7
---

## Why Ampère’s law needs a new term

Draw a loop around the wire charging a capacitor. A flat surface bounded by the loop cuts the wire and encloses its current. A bulging surface with the same boundary can pass between the plates, where no charge crosses the vacuum gap. The same circulation of $$\vec B$$ must work for both surfaces. Ordinary Ampère’s law, which counts only conduction current, cannot do that during charging.

<img class="note-img note-img--w480" src="/assets/physics/usapho/displacement-current.svg" alt="Two surfaces with the same boundary around a charging wire, one intersecting the wire and one passing through the capacitor gap" loading="lazy" decoding="async" />

In the ideal parallel-plate picture, neglecting fringing, $$\Phi_E=EA=Q/\varepsilon_0$$ through the gap. Differentiating gives $$\varepsilon_0\,d\Phi_E/dt=dQ/dt=I$$. Maxwell’s **displacement current** contributes the missing term to the gap calculation:

$$
\oint_C\vec B\cdot d\vec\ell=\mu_0 I_S+\mu_0\varepsilon_0\frac{d\Phi_E}{dt}.
$$

In general, charge continuity gives $$\nabla\cdot\vec J=-\partial_t\rho$$. Gauss’s law gives $$\rho=\varepsilon_0\nabla\cdot\vec E$$. Combining them shows that $$\vec J+\varepsilon_0\partial_t\vec E$$ has zero divergence, so its flux is the same through any two surfaces with the same oriented boundary. In macroscopic matter the corresponding form is $$\nabla\times\vec H=\vec J_f+\partial_t\vec D$$.

<div class="theorem-box">

**Example.** A circular parallel-plate capacitor of radius $$a$$ charges at rate $$I$$. Assuming a uniform axial electric field between the plates and negligible fringing, find the azimuthal magnetic field a distance $$r<a$$ from the axis in the gap.

The electric flux through a concentric circle of radius $$r$$ is the fraction $$r^2/a^2$$ of the flux through the plate area. The displacement current enclosed is therefore $$Ir^2/a^2$$. Symmetry gives $$2\pi rB_\phi=\mu_0Ir^2/a^2$$, so $$B_\phi=\mu_0Ir/(2\pi a^2)$$. Curl your fingers around the increasing electric flux to obtain the circulation direction.

</div>

---

## Maxwell’s equations

The two Gauss laws describe sources of flux. The two circulation laws describe how currents and changing fields produce curl. In SI units, with charge and current densities $$\rho$$ and $$\vec J$$, the vacuum-form equations are

| Law | Integral form | Local form |
|---|---|---|
| Electric Gauss law | $$\oint_{\partial V}\vec E\cdot d\vec A=Q_V/\varepsilon_0$$ | $$\nabla\cdot\vec E=\rho/\varepsilon_0$$ |
| Magnetic Gauss law | $$\oint_{\partial V}\vec B\cdot d\vec A=0$$ | $$\nabla\cdot\vec B=0$$ |
| Faraday law | $$\oint_C\vec E\cdot d\vec\ell=-d\Phi_B/dt$$ | $$\nabla\times\vec E=-\partial_t\vec B$$ |
| Ampère–Maxwell law | $$\oint_C\vec B\cdot d\vec\ell=\mu_0 I_S+\mu_0\varepsilon_0d\Phi_E/dt$$ | $$\nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\partial_t\vec E$$ |

These integral circulation laws use a fixed loop and surface. The local equations and the same integral laws also apply outside the quasistatic limit. At large distances, the time-dependent fields at the integration surface have to be found from propagation and boundary conditions.

The fields act on matter through the Lorentz force. For a particle, $$\vec F=q(\vec E+\vec v\times\vec B)$$. In a continuous distribution this becomes force per volume $$\vec f=\rho\vec E+\vec J\times\vec B$$. An observer at rest with a point charge measures only an electric field. An observer moving relative to it generally measures both an electric and a magnetic field. Their six components belong to a single electromagnetic field tensor and mix under Lorentz transformations.

### How the wave equation follows

In charge-free, current-free space, take the curl of Faraday’s law and substitute Ampère–Maxwell:

$$
\nabla\times(\nabla\times\vec E)
=-\partial_t(\nabla\times\vec B)
=-\mu_0\varepsilon_0\,\partial_t^2\vec E.
$$

The identity $$\nabla\times(\nabla\times\vec E)=\nabla(\nabla\cdot\vec E)-\nabla^2\vec E$$ reduces the left side to $$-\nabla^2\vec E$$ because the electric divergence is zero. Repeating for $$\vec B$$ gives

$$
\nabla^2\vec E=c^{-2}\partial_t^2\vec E,\qquad
\nabla^2\vec B=c^{-2}\partial_t^2\vec B,\qquad
c=\frac1{\sqrt{\mu_0\varepsilon_0}}.
$$

These have the same form as the mechanical wave equation, but the propagating quantities are fields. No charge or material medium is needed in the region through which the wave travels.

---

## Plane waves, polarization, and radiation

For a sinusoidal plane wave traveling in the $$+\hat z$$ direction, take $$\vec E=E_0\hat x\cos(kz-\omega t)$$. Faraday’s law relates the spatial derivative of $$E_x$$ to the time derivative of $$B_y$$, giving $$kE_0=\omega B_0$$. Since $$\omega=ck$$, the fields are in phase with $$B_0=E_0/c$$. In vector form,

$$
\vec B=\frac1c\hat k\times\vec E,\qquad
\vec E\perp\vec B,\qquad \vec E\times\vec B\parallel\hat k.
$$

The **polarization** describes the electric field at a fixed point. With two perpendicular transverse components in phase, their sum oscillates along a fixed direction and is linearly polarized. Equal amplitudes with a quarter-cycle phase offset give a rotating electric vector of constant magnitude, or circular polarization. Other combinations generally trace an ellipse. State which direction you are viewing along when describing clockwise rotation.

It is convenient to write $$\vec E=\operatorname{Re}[\widetilde{\vec E}\,e^{i(\vec k\cdot\vec r-\omega t)}]$$. The two complex components of $$\widetilde{\vec E}$$ specify amplitudes and phases. Maxwell’s equations are linear, so plane waves of different directions and frequencies can be added to satisfy source and boundary conditions.

An accelerating charge can radiate. In a short dipole antenna, oscillating current moves charge back and forth between the ends, creating an oscillating electric dipole. Its far-field radiation is strongest across the dipole and vanishes along its axis. The outgoing fronts are approximately spherical at large distances from a localized source. Over a small patch far away, the front is nearly flat, so the plane-wave relations apply locally. An [oscillating LC circuit](/notes/physics/eandm/ac-circuits/#free-oscillation-in-an-lc-or-rlc-circuit) provides a model for the periodic motion of charge that drives the antenna.

---

## Energy, momentum, and radiation pressure

Capacitance and inductance give familiar examples of energy stored in fields. In vacuum the energy density and energy flux are

$$
u=\frac{\varepsilon_0 E^2}{2}+\frac{B^2}{2\mu_0},\qquad
\vec S=\frac1{\mu_0}\vec E\times\vec B.
$$

The **Poynting vector** $$\vec S$$ gives energy crossing a unit area normal to the flow per unit time. Taking the divergence of $$\vec E\times\vec B$$ and substituting the two curl equations gives

$$
\partial_t u+\nabla\cdot\vec S=-\vec J\cdot\vec E.
$$

Field energy in a region can decrease as it leaves through the surface or as the field transfers energy to charges. For a plane wave, $$B=E/c$$ makes the electric and magnetic energy densities equal and gives $$S=cu$$. A sinusoid has mean squared field $$E_0^2/2$$, so its average intensity is $$I=\tfrac12 c\varepsilon_0 E_0^2$$. A source radiating isotropically with power $$P$$ instead gives $$I=P/(4\pi r^2)$$ far away because the same power crosses larger spheres.

An electromagnetic wave also carries momentum, with density $$\vec g=\vec S/c^2$$. At normal incidence, absorbing energy $$U$$ transfers momentum $$U/c$$. Perfect reflection transfers $$2U/c$$ because the outgoing momentum reverses. Dividing momentum transfer by area and time gives

$$
p_{\rm abs}=\frac Ic,\qquad p_{\rm refl}=\frac{2I}{c}.
$$

For example, at intensity $$600\ \mathrm{W/m^2}$$ a perfectly reflecting surface normal to the beam experiences pressure $$4.0\times10^{-6}\ \mathrm{Pa}$$.

### The electromagnetic spectrum

Frequency sets the photon energy $$hf$$, while intensity sets the energy arriving per area per time. Both matter when radiation interacts with materials. Conducting antennas respond to radio and microwave fields through driven currents. Microwave heating instead depends on dielectric loss, including the delayed response of polar molecules such as water. Infrared couples strongly to many molecular motions and is important in thermal radiation. Visible light and ultraviolet can drive electronic transitions, and high-energy ultraviolet, X-rays, and gamma rays can ionize matter. X-rays and gamma rays overlap in photon energy, so their names often distinguish how they were produced. These bands shade into each other.

| Band | Example of the underlying interaction |
|---|---|
| Very low frequency | At household power-line frequencies the vacuum wavelength is thousands of kilometers, so near a small circuit induction is often the useful description. |
| Radio | An antenna converts a changing field to an electrical signal. AM varies the carrier amplitude and FM varies its frequency. |
| Microwaves | Radar uses reflections to locate objects. In an oven the field drives polarization in food, and dielectric loss converts part of its energy into heat. |
| Infrared | Thermal cameras detect emitted radiation. Molecular vibrations also leave absorption bands used to identify materials. |
| Visible and ultraviolet | Electronic transitions absorb or emit photons in these bands. The shorter wavelength of ultraviolet is also useful in lithography. |
| X-rays and gamma rays | Differential absorption gives X-ray images, and interference from crystal planes gives diffraction patterns. Nuclear transitions are one source of gamma rays. |

---

## Equation summary

:::equations

| Idea | Relation | Conditions |
|---|---|---|
| Displacement current | $$I_d=\varepsilon_0\,d\Phi_E/dt$$ | Fixed surface in vacuum |
| Wave speed | $$c=(\mu_0\varepsilon_0)^{-1/2}=\omega/k$$ | Vacuum plane wave |
| Field directions | $$\vec B=\hat k\times\vec E/c$$ | Wave traveling along $$\hat k$$ |
| Energy transport | $$\vec S=\vec E\times\vec B/\mu_0,\quad\partial_tu+\nabla\cdot\vec S=-\vec J\cdot\vec E$$ | Vacuum-form fields and sources |
| Intensity | $$I=\tfrac12 c\varepsilon_0 E_0^2$$ | Sinusoidal plane wave, peak $$E_0$$ |
| Radiation pressure | $$p_{\rm abs}=I/c,\quad p_{\rm refl}=2I/c$$ | Normal incidence, perfect absorption or reflection |

:::
