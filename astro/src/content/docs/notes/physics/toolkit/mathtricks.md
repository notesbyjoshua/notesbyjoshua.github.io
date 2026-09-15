---
title: "Math Tricks"
description: "Physics notes on math tricks for problem solving, including algebra shortcuts, approximations, units, and graph reasoning."
sidebar:
  order: 1
---

## Common integrals to know

Integrals are one of the most common things in physics, and usually come in a few standard forms.

### General integrals

$$
\int x^n\,dx=\frac{x^{n+1}}{n+1}\ (n\neq-1),\qquad
\int \frac{dx}{x}=\ln\lvert x \rvert,
$$

$$
\int e^{ax}\,dx=\frac{1}{a}e^{ax}.
$$

Many integrals show up commonly when deriving certain values:

$$
\int\frac{x\,dx}{(x^2+a^2)^{3/2}}=-\frac{1}{\sqrt{x^2+a^2}}+C,
$$

$$
\int\frac{dx}{(x^2+a^2)^{3/2}}=\frac{x}{a^2\sqrt{x^2+a^2}}+C,
$$

and

$$
\int\frac{dx}{\sqrt{x^2+a^2}}=\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C.
$$

For rotational inertia and center-of-mass calculations, remember that the integral is usually just continuous addition:

$$
M=\int dm,\qquad \vec r_{\mathrm{cm}}=\frac{1}{M}\int \vec r\,dm,
\qquad I=\int r_\perp^2\,dm.
$$

An arbitrary constant $$C$$ should be added to every indefinite integral.

### Trigonometric integrals

$$
\int \sin x\,dx=-\cos x,\qquad \int\cos x\,dx=\sin x,\qquad
\int \frac{dx}{a^2+x^2}=\frac{1}{a}\arctan\frac{x}{a}.
$$

The identities

$$
\sin^2x=\frac{1-\cos 2x}{2},\qquad
\cos^2x=\frac{1+\cos 2x}{2},\qquad
\sin x\cos x=\frac{\sin 2x}{2}
$$

turn products and squares into easy integrals. Over a full period, the average of $$\sin^2x$$ or $$\cos^2x$$ is $$\tfrac12$$, which is why RMS values carry a factor $$1/\sqrt2$$:

$$
\int_0^{2\pi}\sin^2x\,dx=\int_0^{2\pi}\cos^2x\,dx=\pi.
$$

### Special integrals

A few less common integrals show up in thermodynamics, statistical mechanics, diffraction, and gravitation problems:

$$
\int_0^\infty e^{-ax^2}\,dx=\frac12\sqrt{\frac{\pi}{a}}\quad(a>0;\ \text{Gaussian}),\qquad
\int_0^\infty x^n e^{-x}\,dx=n!\quad(n=0,1,2,\ldots;\ \text{Gamma}).
$$

The full Gaussian integral is

$$
\int_{-\infty}^{\infty}e^{-ax^2}\,dx=\sqrt{\frac{\pi}{a}},
$$

and its value is usually used directly rather than rederived during a problem.

### Integration techniques

The form of the integrand usually suggests a first move. Here is how to use each technique.

#### Symmetry

Before integrating, check what happens when $$x$$ changes to $$-x$$. An odd function has $$f(-x)=-f(x)$$, so its positive and negative contributions cancel over symmetric limits. An even function has $$f(-x)=f(x)$$, so you can integrate one half and double it.

For example, if $$a>0$$,

$$
\int_{-a}^{a}\left(\frac{x}{(x^2+a^2)^{3/2}}+x^2\right)\,dx
=0+2\int_0^a x^2\,dx=\frac{2a^3}{3}.
$$

The first term disappears without an antiderivative. This is the same cancellation used when opposite charge elements produce equal and opposite field components.

#### Substitution

Choose a new variable that absorbs a repeated expression. For $$a>0$$, consider

$$
I=\int_0^L\frac{x\,dx}{(x^2+a^2)^{3/2}}.
$$

Set $$u=x^2+a^2$$, so $$du=2x\,dx$$. Change the limits as well: $$x=0$$ gives $$u=a^2$$, and $$x=L$$ gives $$u=L^2+a^2$$. Then

$$
I=\frac12\int_{a^2}^{L^2+a^2}u^{-3/2}\,du
=\left[-u^{-1/2}\right]_{a^2}^{L^2+a^2}
=\frac1a-\frac{1}{\sqrt{L^2+a^2}}.
$$

If the numerator lacks the needed factor of $$x$$, a trig substitution may work better. For $$\int dx/\sqrt{x^2+a^2}$$, set $$x=a\tan\theta$$ so the square root becomes $$a\sec\theta$$ on $$-\pi/2<\theta<\pi/2$$. The integral reduces to $$\int\sec\theta\,d\theta$$ and gives the logarithmic form listed above.

#### Integration by parts

The product rule, $$d(uv)=u\,dv+v\,du$$, rearranges to

$$
\int u\,dv=uv-\int v\,du.
$$

Use it when differentiating one factor makes the remaining integral simpler. For an exponentially decaying signal with decay rate $$\gamma>0$$,

$$
\int_0^\infty t e^{-\gamma t}\,dt,
$$

choose $$u=t$$ and $$dv=e^{-\gamma t}dt$$. Then $$du=dt$$ and $$v=-e^{-\gamma t}/\gamma$$, giving

$$
\int_0^\infty t e^{-\gamma t}\,dt
=\left[-\frac{t e^{-\gamma t}}{\gamma}\right]_0^\infty
+\frac1\gamma\int_0^\infty e^{-\gamma t}\,dt
=\frac{1}{\gamma^2}.
$$

The boundary term vanishes because the exponential decays faster than $$t$$ grows. LIATE—logarithmic, inverse trig, algebraic, trig, exponential—is a useful order to try when choosing $$u$$, but the goal is always to simplify the new integral.

#### Differentiating with respect to a parameter

Sometimes you already know a related integral. Differentiating it can bring down the extra factor you need. Start with the Gaussian integral

$$
I(a)=\int_0^\infty e^{-ax^2}\,dx=\frac{\sqrt\pi}{2}a^{-1/2},\qquad a>0.
$$

Differentiating with respect to $$a$$ gives

$$
I'(a)=-\int_0^\infty x^2e^{-ax^2}\,dx
=-\frac{\sqrt\pi}{4}a^{-3/2}.
$$

Therefore,

$$
\int_0^\infty x^2e^{-ax^2}\,dx=\frac{\sqrt\pi}{4a^{3/2}}.
$$

The differentiation and integration can be exchanged here because the integrand and its derivative decay sufficiently fast for positive $$a$$. For variable integration limits, include their boundary terms using Leibniz's rule.

#### Units and limiting checks

These checks help assess an integral's answer. In the substitution example, the integrand times $$dx$$ has units of inverse length, matching $$1/a-1/\sqrt{L^2+a^2}$$.

When $$L\ll a$$, the denominator is nearly $$a^3$$, so the integral should approach $$L^2/(2a^3)$$. Expanding the exact result gives

$$
\frac1a-\frac{1}{\sqrt{L^2+a^2}}
\approx\frac1a-\frac1a\left(1-\frac{L^2}{2a^2}\right)
=\frac{L^2}{2a^3}.
$$

When $$L\to0$$ it vanishes, and when $$L\to\infty$$ it approaches $$1/a$$. These checks catch missing powers, signs, and constants.

---

## Small value approximations

When doing physics problems, we use the small angle approximation for simplification. For $$\lvert x \rvert \ll 1$$:

| Function | Approximation |
|---|---|
| $$(1+x)^n$$ | $$1+nx$$ |
| $$e^x$$ | $$1+x$$ |
| $$\ln(1+x)$$ | $$x$$ |
| $$\sin x$$ | $$x$$ |
| $$\cos x$$ | $$1-\tfrac12 x^2$$ |
| $$\tan x$$ | $$x$$ |
| $$\dfrac{1}{1-x}$$ | $$1+x$$ |

The binomial one, $$(1+x)^n\approx 1+nx$$, is useful throughout physics: it linearizes square roots ($$\sqrt{1+x}\approx 1+\tfrac{x}{2}$$), reciprocals, and many other complicated polynomial expressions. In practice, *factor out the large quantity first* so that the expansion parameter is small. As an example,

$$
\frac{1}{\sqrt{R^2+x^2}}=\frac{1}{R}\frac{1}{\sqrt{1+(x/R)^2}}\approx\frac{1}{R}\left(1-\frac{x^2}{2R^2}\right)\quad (x\ll R).
$$

<div class="theorem-box">

**Example.** Two equal masses $$M$$ are fixed a distance $$2a$$ apart. A much smaller mass $$m$$ lies on their perpendicular bisector, a distance $$y$$ from the midpoint, where $$\lvert y\rvert\ll a$$. Find the small mass's approximate acceleration and its oscillation frequency.

The horizontal gravitational forces cancel. The vertical acceleration is

$$
a_y=-\frac{2GMy}{(a^2+y^2)^{3/2}}.
$$

The useful small quantity is not $$y$$ itself but $$y^2/a^2$$. Factor out $$a^2$$ before expanding:

$$
(a^2+y^2)^{-3/2}=a^{-3}\left(1+\frac{y^2}{a^2}\right)^{-3/2}
\approx a^{-3}\left(1-\frac{3y^2}{2a^2}\right).
$$

Because the numerator already contains $$y$$, the correction is third order. To first order,

$$
a_y\approx-\frac{2GM}{a^3}y.
$$

This has the SHM form $$\ddot y=-\omega^2y$$, so

$$
\omega=\sqrt{\frac{2GM}{a^3}}.
$$

The creative step is recognizing that an inverse-power gravitational expression becomes a spring law after expanding about the midpoint.

</div>

---

## Taylor expansions

Sometimes, when you have $$a \ll b$$, you can perform a Taylor expansion at $$x = 0$$ (this is how we derive all of the small value approximations above!). The general expansion of a function about $$x=0$$ (a *Maclaurin series*) is

$$
f(x)=f(0)+f'(0)\,x+\frac{f''(0)}{2!}x^2+\frac{f'''(0)}{3!}x^3+\cdots
$$

If you are doing oscillations/SHM calculations, you need to take up to the second derivative (quadratic) term, and if you are doing any other calculations you usually only need to take up to the first derivative (linear) term.

<div class="theorem-box">

**Example.** Why does a stable equilibrium cause SHM?

Take any potential $$U(x)$$ with a stable equilibrium at $$x_0$$. Expand about $$x_0$$:

$$
U(x)\approx U(x_0)+\underbrace{U'(x_0)}_{=\,0}(x-x_0)+\frac12 U''(x_0)(x-x_0)^2.
$$

The constant doesn't affect forces, and the linear term is zero at equilibrium, so near $$x_0$$

$$
U(x)\approx \text{const}+\tfrac12 k_{\text{eff}}(x-x_0)^2,\qquad k_{\text{eff}}=U''(x_0).
$$

This is a spring potential with effective spring constant $$U''(x_0)$$, so the system oscillates with $$\omega=\sqrt{U''(x_0)/m}$$. *Any* smooth potential looks like a harmonic oscillator near its minimum — this is why SHM is everywhere, and why USAPhO loves asking for "the frequency of small oscillations."

As an example, a pendulum has $$U(\theta)=mgL(1-\cos\theta)\approx \tfrac12 mgL\,\theta^2$$ for small $$\theta$$ (keeping the quadratic term), giving $$\omega=\sqrt{g/L}$$.

</div>

---

## Coordinate Systems

Choose coordinates that follow the symmetry of the problem. A good coordinate system makes boundaries constant-coordinate surfaces and points one basis vector along the direction in which the system changes.


### Polar coordinates

Use polar coordinates for motion confined to a plane around a fixed point: circular tracks, central-force orbits, rotating rods, or circular area integrals. A circle becomes the simple condition $$r=R$$. If the path and forces instead follow straight perpendicular directions, Cartesian coordinates may be easier.

Polar coordinates describe a point in a plane using its distance $$r$$ from the origin and angle $$\theta$$ from the positive $$x$$-axis:

$$
x=r\cos\theta,\qquad y=r\sin\theta,\qquad dA=r\,dr\,d\theta.
$$

The basis vectors $$\hat r$$ and $$\hat\theta$$ rotate as the particle moves. Their derivatives are

$$
\frac{d\hat r}{dt}=\dot\theta\hat\theta,
\qquad
\frac{d\hat\theta}{dt}=-\dot\theta\hat r.
$$

Therefore,

$$
\vec v=\dot r\hat r+r\dot\theta\hat\theta,
$$

$$
\vec a=(\ddot r-r\dot\theta^2)\hat r+(r\ddot\theta+2\dot r\dot\theta)\hat\theta.
$$

<div class="theorem-box">

**Example.** A bead slides freely on a straight radial rod rotating at constant angular speed $$\omega$$ in a horizontal plane. Find the equation governing its distance $$r$$ from the pivot.

In Cartesian coordinates, both the rod and its constraint force constantly change direction. In polar coordinates the constraint is simply $$\theta=\omega t$$, so $$\dot\theta=\omega$$ and $$\ddot\theta=0$$. The rod's force is perpendicular to the rod, so there is no radial force. The radial component of Newton's second law is

$$
0=m(\ddot r-r\omega^2),
$$

or

$$
\ddot r=\omega^2r.
$$

The coordinate choice eliminates the unknown constraint force from the equation we need.

</div>

### Spherical coordinates

Use spherical coordinates when distances and boundaries are measured from one center: spheres, shells, radial density distributions, and point-charge or gravitational fields. For full spherical symmetry the angular integrals give $$4\pi$$, leaving a single radial integral. A hemisphere uses a restricted polar-angle range.

Spherical coordinates use distance $$r$$ from the origin, polar angle $$\theta$$ measured down from the positive $$z$$-axis, and azimuthal angle $$\phi$$ around the $$z$$-axis:

$$
x=r\sin\theta\cos\phi,\qquad
y=r\sin\theta\sin\phi,\qquad
z=r\cos\theta.
$$

The volume element and area element on a sphere are

$$
dV=r^2\sin\theta\,dr\,d\theta\,d\phi,
\qquad
dA_{r}=r^2\sin\theta\,d\theta\,d\phi.
$$

For a spherically symmetric scalar field $$f(r)$$,

$$
\nabla f=\frac{df}{dr}\hat r,
\qquad
\nabla^2f=\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{df}{dr}\right).
$$

<div class="theorem-box">

**Example.** A sphere of radius $$R$$ has density $$\rho(r)=\rho_0r/R$$. Find its total mass.

Because the density depends only on distance from the center, spherical shells are constant-density surfaces. Using $$dV=4\pi r^2dr$$ after integrating over the angles,

$$
M=\int\rho\,dV
=4\pi\int_0^R\frac{\rho_0r}{R}r^2\,dr
=\frac{4\pi\rho_0}{R}\left[\frac{r^4}{4}\right]_0^R
=\pi\rho_0R^3.
$$

In Cartesian coordinates, the same integral would require a spherical boundary and a density containing $$\sqrt{x^2+y^2+z^2}$$.

</div>

### Cylindrical coordinates

Use cylindrical coordinates for symmetry about an axis: long wires, pipes, coaxial capacitors, rotating cylinders, and disks or stacks of disks. A cylindrical wall is $$s=R$$, while flat end caps are constant $$z$$. This separates distance from the axis from height along it.

Cylindrical coordinates combine polar coordinates in the $$xy$$-plane with an ordinary vertical coordinate:

$$
x=s\cos\phi,\qquad y=s\sin\phi,\qquad z=z,
$$

where $$s$$ is the perpendicular distance from the $$z$$-axis. The volume element and common surface elements are

$$
dV=s\,ds\,d\phi\,dz,
$$

$$
dA_{s}=s\,d\phi\,dz,\qquad
dA_z=s\,ds\,d\phi.
$$

Using $$s$$ rather than $$r$$ avoids confusing cylindrical distance from the axis with spherical distance from the origin.

<div class="theorem-box">

**Example.** A solid cylinder of radius $$R$$, length $$L$$, and uniform density $$\rho$$ rotates about its symmetry axis. Find its moment of inertia.

Every mass element's perpendicular distance from the axis is simply $$s$$. Therefore,

$$
I=\int s^2\,dm
=\rho\int_0^L\int_0^{2\pi}\int_0^R s^2(s\,ds\,d\phi\,dz).
$$

The limits are all constant, so

$$
I=\rho L(2\pi)\frac{R^4}{4}
=\frac12(\rho\pi R^2L)R^2
=\frac12MR^2.
$$

</div>

---

## Vector Algebra

Vectors show up a lot on USAPhO, so it is especially handy to know how to do vector algebra.

### Notations

A vector $$\vec a$$ has components $$\vec a=(a_x,a_y,a_z)=a_x\hat i+a_y\hat j+a_z\hat k$$, where $$\hat i,\hat j,\hat k$$ are unit vectors along the axes. Its **magnitude** (or **norm**) is $$\lvert \vec a \rvert =\sqrt{a_x^2+a_y^2+a_z^2}$$, and the **unit vector** in its direction is $$\hat a=\vec a/ \lvert \vec a \rvert$$. Throughout, $$\theta$$ denotes the angle between the two vectors being combined.

### Dot product

<div class="theorem-box">

**Definition (Dot product).** The dot product is one way to multiply two vectors, and result in a scalar quantity. The formula is given by: $$\vec a \cdot \vec b = a_x b_x + a_y b_y + a_z b_z$$

</div>

**Properties**:

1. $$\vec a \cdot \vec b = \lvert \vec a\rvert \lvert \vec b \rvert\cos\theta$$
2. $$\vec b \cdot \vec a = \vec a \cdot \vec b$$
3. $$\vec a \cdot \vec a = \lvert \vec a \rvert^2$$
4. If $$\vec a \perp \vec b$$, then $$\vec a \cdot \vec b = 0$$

The dot product acts like a **projection**: $$\vec a\cdot\hat b$$ is the component of $$\vec a$$ along the direction of $$\vec b$$. This is why work is $$W=\vec F\cdot\vec d$$ and flux is $$\vec E\cdot\vec A$$, since both measure components along a specific direction.

### Cross product

<div class="theorem-box">

**Definition (Cross product).** The cross product is one way to multiply two vectors, and result in another vector, whose direction is perpendicular to the first two. You find the direction based on the right-hand rule (as described in AP Physics C). The formula is given by the determinant

$$
\vec a\times\vec b=
\begin{vmatrix}\hat i&\hat j&\hat k\\ a_x&a_y&a_z\\ b_x&b_y&b_z\end{vmatrix}
=(a_yb_z-a_zb_y)\,\hat i+(a_zb_x-a_xb_z)\,\hat j+(a_xb_y-a_yb_x)\,\hat k.
$$

</div>

**Properties**:

1. $$\lvert \vec a\times\vec b \rvert =\lvert \vec a\rvert \lvert \vec b \rvert\sin\theta$$ — the magnitude equals the area of the parallelogram spanned by the two vectors.
2. $$\vec b\times\vec a=-\,\vec a\times\vec b$$ (anticommutative — order matters!)
3. $$\vec a\times\vec a=\vec 0$$, and more generally $$\vec a\times\vec b=\vec 0$$ if $$\vec a\parallel\vec b$$.
4. The result is perpendicular to *both* inputs, with direction set by the right-hand rule.

To apply the **right-hand rule**, point the fingers of your right hand along the first vector, curl them through the smaller angle toward the second vector, and point your thumb perpendicular to the plane. Your thumb gives the direction of $$\vec a\times\vec b$$. Reversing the order reverses the direction. For vectors in the page, counterclockwise rotation from the first vector to the second gives a result out of the page, while clockwise rotation gives a result into the page.

<img class="note-img note-img--w480" src="/assets/physics/usapho/comments/right-hand-rule.svg" alt="Right-hand rule showing fingers curling from vector a toward vector b and the thumb pointing in the direction of a cross b" loading="lazy" decoding="async" />

The cross product denotes a "rotational" or perpendicular quantity: torque $$\vec\tau=\vec r\times\vec F$$, angular momentum $$\vec L=\vec r\times\vec p$$, and magnetic force $$\vec F=q\vec v\times\vec B$$ are all cross products.

### Triple product and other vector formulas

Often times, problems require a combination of the dot and cross products.

The **scalar triple product** gives a signed volume:

$$
\vec a\cdot(\vec b\times\vec c)
=\vec b\cdot(\vec c\times\vec a)
=\vec c\cdot(\vec a\times\vec b).
$$

Its magnitude is the volume of the parallelepiped spanned by the three vectors. Swapping any two vectors changes the sign. If the triple product is zero, the vectors are coplanar.

The **vector triple product** follows the BAC–CAB rule:

$$
\vec a\times(\vec b\times\vec c)
=\vec b(\vec a\cdot\vec c)-\vec c(\vec a\cdot\vec b).
$$

Cross products are not associative, so parentheses matter. Two other useful identities are

$$
(\vec a\times\vec b)\cdot(\vec c\times\vec d)
=(\vec a\cdot\vec c)(\vec b\cdot\vec d)
-(\vec a\cdot\vec d)(\vec b\cdot\vec c),
$$

$$
\lvert\vec a\times\vec b\rvert^2
=\lvert\vec a\rvert^2\lvert\vec b\rvert^2-(\vec a\cdot\vec b)^2.
$$

<div class="theorem-box">

**Example.** A particle of charge $$q$$ moves with velocity $$\vec v$$ in a uniform magnetic field $$\vec B$$. Using $$\vec F=q\vec v\times\vec B$$, find $$d\vec F/dt$$ when no other forces act, and show that the acceleration rotates about $$\vec B$$.

Since $$\vec B$$ is constant,

$$
\frac{d\vec F}{dt}=q\frac{d\vec v}{dt}\times\vec B
=\frac{q}{m}\vec F\times\vec B
=\frac{q^2}{m}(\vec v\times\vec B)\times\vec B.
$$

Apply the vector triple product with the parentheses in this order:

$$
(\vec v\times\vec B)\times\vec B
=\vec B(\vec v\cdot\vec B)-\vec vB^2
=-B^2\vec v_\perp.
$$

Therefore,

$$
\frac{d\vec F}{dt}=-\frac{q^2B^2}{m}\vec v_\perp.
$$

The force changes toward the center of the circular perpendicular motion while the component of velocity parallel to $$\vec B$$ stays constant. This is the vector form of helical motion.

</div>

---

## Complex numbers for oscillations

Sometimes, you have to think outside of the real numbers. As you may remember from precalculus, any sinusoid can be written as the real part of a complex exponential, using **Euler's formula**

$$
e^{i\theta}=\cos\theta+i\sin\theta.
$$

So $$A\cos(\omega t+\phi)=\mathrm{Re}\big(A e^{i\phi}\,e^{i\omega t}\big)$$. Differentiation then becomes *multiplication* by $$i\omega$$, which turns the differential equations of oscillations and AC circuits into ordinary algebra. Adding two waves of the same frequency becomes adding two complex numbers ("phasors") tip-to-tail, which can avoid hefty trig identities.

<div class="theorem-box">

**Example.** Two perpendicular simple harmonic motions have the same angular frequency:

$$
x(t)=A\cos\omega t,
\qquad
y(t)=A\cos\left(\omega t+\frac{2\pi}{3}\right).
$$

Find the amplitude and phase of the motion along the line $$u=(x+y)/\sqrt2$$.

Represent each cosine by its complex amplitude. The complex amplitude of $$u$$ is

$$
\tilde U=\frac{A}{\sqrt2}\left(1+e^{i2\pi/3}\right).
$$

Using $$1+e^{i\alpha}=2\cos(\alpha/2)e^{i\alpha/2}$$,

$$
\tilde U=\frac{A}{\sqrt2}e^{i\pi/3}.
$$

Taking the real part at the end gives

$$
u(t)=\frac{A}{\sqrt2}\cos\left(\omega t+\frac{\pi}{3}\right).
$$

Thus the projected motion has amplitude $$A/\sqrt2$$ and phase $$\pi/3$$. The phasor sum avoids expanding and recombining several sine and cosine terms.

</div>

---

## Problem-solving strategy

Once the physics is set up, the question becomes *which mathematical tool to reach for*. A quick decision tree:

:::strategy
1. **A small parameter appears** (a ratio $$x\ll 1$$, a tiny angle, $$v\ll c$$): linearize with the small-value approximations, leading with $$(1+x)^n\approx 1+nx$$. Factor out the large quantity *first* so the leftover is genuinely small.
2. **You need the next correction, or are near an equilibrium**: Taylor/Maclaurin expand, $$f(x)=f(0)+f'(0)x+\tfrac12 f''(0)x^2+\cdots$$. For small oscillations keep the quadratic term and read off $$\omega=\sqrt{U''(x_0)/m}$$; otherwise the linear term usually suffices.
3. **A linear ODE with constant coefficients** (oscillations, AC circuits, driven systems): recognize the standard form. Restoring force linear in displacement gives $$\ddot x=-\omega^2 x$$; a single decay/growth rate gives $$\dot y=-ky$$. Write down the known solution instead of re-deriving it.
4. **Sinusoids, phase lags, or interference**: go complex with $$e^{i\theta}=\cos\theta+i\sin\theta$$, write the signal as $$\mathrm{Re}(Ae^{i\phi}e^{i\omega t})$$, and turn $$d/dt$$ into multiplication by $$i\omega$$. Add same-frequency waves as phasors rather than juggling trig identities.
5. **A nonlinear or "rate" ODE**: try separation of variables, $$\int dy/g(y)=\int f(t)\,dt$$, then integrate. Handles nonlinear drag, draining tanks, and most rate problems.
6. **An integral that looks hopeless**: check symmetry first, then try substitution, integration by parts, or differentiation with respect to a parameter. Recognize the common field integrals and the Gaussian and Gamma integrals on sight.
7. **The geometry has circular, spherical, or axial symmetry**: switch coordinates before writing the integral or equations of motion. Polar coordinates follow planar rotation, spherical coordinates follow distance from a point, and cylindrical coordinates follow distance from an axis.
8. **A quantity with direction**: use the dot product for a projection and the cross product for a perpendicular or rotational quantity. Use scalar triple products for volumes or coplanarity and BAC–CAB to simplify nested cross products.
:::

:::mistakes
- Expanding *before* factoring out the large quantity, so the "small" term isn't actually small and the approximation is invalid.
- Keeping only the linear Taylor term for an oscillation problem — at a potential minimum $$U'(x_0)=0$$, so the quadratic term is the *leading* one and dropping it loses all the physics.
- Forgetting to take $$\mathrm{Re}(\cdots)$$ at the end of a complex-exponential calculation, or mixing real and complex amplitudes midway.
- Treating the cross product as commutative: $$\vec b\times\vec a=-\vec a\times\vec b$$, and order matters for the right-hand-rule direction.
- Reaching for brute-force integration when a symmetry argument or a standard form kills the integral instantly.
- Using Cartesian coordinates when the boundary is a circle, sphere, or cylinder, which turns constant limits into complicated functions.
- Misidentifying the ODE pattern — e.g. forcing a separable or nonlinear equation into the $$\ddot x=-\omega^2x$$ mold and quoting a sinusoid that doesn't apply.
- Treating cross products as associative. In general, $$(\vec a\times\vec b)\times\vec c\neq\vec a\times(\vec b\times\vec c)$$.
:::
