---
title: "Chapter 2: Vector-Valued Functions"
description: "Multivariable calculus notes on space curves, vector derivatives, arc length, tangent and normal vectors, curvature, motion, and Kepler's laws."
status: developing
progress: 70
sidebar:
  order: 2
---

## Introduction to Vector-Valued Functions

A vector-valued function assigns a vector to each parameter value:

$$
\mathbf r(t)=\langle x(t),y(t),z(t)\rangle.
$$

When we treat this as a position vector, its tip traces a space curve. The domain is the intersection of the component domains. The parameter also determines the direction and rate at which the curve is traced.

To identify a curve, look for relations between its coordinates. For $$\mathbf r(t)=\langle a\cos t,a\sin t,bt\rangle$$ with $$a>0$$ and $$b\ne0$$, the identity $$x^2+y^2=a^2$$ places the curve on a cylinder. Meanwhile, $$z$$ changes steadily. The result is a helix with vertical change $$2\pi b$$ per turn as $$t$$ increases.

A curve may also be described as the intersection of two surfaces. To parametrize such an intersection, use one surface to choose coordinates, then substitute into the other.

<div class="theorem-box">

**Example.** Parametrize the intersection of $$x^2+y^2=4$$ and $$z=x+y$$, tracing it once.

Use $$x=2\cos t$$ and $$y=2\sin t$$ for the cylinder. The plane then determines $$z$$:

$$
\mathbf r(t)=\langle2\cos t,2\sin t,2\cos t+2\sin t\rangle,
\qquad0\le t\le2\pi.
$$

The endpoints agree, so this is a closed curve. Its projection onto the $$xy$$-plane is traced counterclockwise when viewed from above.

</div>

### The path does not determine the motion

Eliminating a parameter gives a geometric relation, but it can hide the parameter interval, direction, and number of times the curve is traced. For example, $$\langle\cos t,\sin t\rangle$$ and $$\langle\cos(2t),\sin(2t)\rangle$$ both lie on the unit circle. On the interval from zero to one full turn, the second parametrization completes two revolutions. A curve sketch should therefore include an arrow and the starting point whenever the motion matters.

The component domains must also hold simultaneously. A square root in one coordinate may impose a lower bound, while a logarithm in another excludes an endpoint that the square root would allow. Decide this before discussing limits or tangent vectors.

<div class="theorem-box">

**Example.** Find the domain of $$\mathbf r(t)=\langle\sqrt{t+1},\ln(3-t),1/(t-1)\rangle$$. Determine whether the curve has a finite limit as $$t\to1$$.

The first coordinate requires $$t\ge-1$$, the second requires $$t<3$$, and the third excludes $$t=1$$. Their intersection is

$$
[-1,1)\cup(1,3).
$$

As $$t\to1$$, the first two coordinates approach finite values, but $$1/(t-1)$$ becomes unbounded with opposite signs on the two sides. A vector limit requires all component limits to exist, so the curve has no finite limit there. We cannot repair this by assigning a new position at $$t=1$$.

</div>

When a curve is defined by intersecting surfaces, check the parametrization in both original equations. This catches the common mistake of satisfying the cylinder equation while forgetting the second surface or its restricted portion.

---

## Calculus of Vector-Valued Functions

The derivative starts with the same question as in single-variable calculus: how does the output change for a small change in the input? Here the output change is a vector. The difference $$\mathbf r(t+h)-\mathbf r(t)$$ points along a secant through two nearby positions. Dividing by $$h$$ accounts for the parameter interval; as it shrinks, the secant direction approaches the tangent direction, provided the derivative exists and is nonzero.

Because subtracting and dividing a vector act componentwise, taking this limit is the same as taking the derivative of each coordinate. The same reasoning reduces continuity and integration to the components:

$$
\mathbf r'(t)=\langle x'(t),y'(t),z'(t)\rangle,
\qquad
\int\mathbf r(t)\,dt
=\left\langle\int x(t)\,dt,\int y(t)\,dt,\int z(t)\,dt\right\rangle.
$$

An indefinite vector integral includes a constant vector. The derivative points in the direction of motion when it is nonzero. At $$t=t_0$$, a tangent line is

$$
\boldsymbol\ell(s)=\mathbf r(t_0)+s\mathbf r'(t_0).
$$

The product rules retain the type and order of each product:

$$
\frac{d}{dt}(\mathbf u\cdot\mathbf v)
=\mathbf u'\cdot\mathbf v+\mathbf u\cdot\mathbf v',
$$

$$
\frac{d}{dt}(\mathbf u\times\mathbf v)
=\mathbf u'\times\mathbf v+\mathbf u\times\mathbf v'.
$$

The chain rule is $$\frac{d}{dt}\mathbf r(g(t))=\mathbf r'(g(t))g'(t)$$.

<div class="theorem-box">

**Proof (Derivative of a constant-length vector).** Suppose $$\lVert\mathbf r(t)\rVert=c$$. Then $$\mathbf r\cdot\mathbf r=c^2$$. Differentiating gives

$$
2\mathbf r\cdot\mathbf r'=0.
$$

Thus a nonzero derivative is perpendicular to the radius vector. For motion on a sphere centered at the origin, velocity lies in the tangent plane.

</div>

### Tangents and initial conditions

The vector derivative comes from displacement divided by parameter change. For small $$h$$, the displacement from $$\mathbf r(t)$$ to $$\mathbf r(t+h)$$ is approximately $$h\mathbf r'(t)$$. This is why the derivative determines the tangent direction. Its magnitude depends on the chosen parameter, so the same tangent line can be described by many different nonzero direction vectors.

<div class="theorem-box">

**Example.** For $$\mathbf r(t)=\langle t^2,t^3,2t\rangle$$, find the tangent line at $$t=1$$ and determine where that line meets the plane $$z=0$$.

Evaluate position and derivative separately:

$$
\mathbf r(1)=\langle1,1,2\rangle,\qquad
\mathbf r'(t)=\langle2t,3t^2,2\rangle,
\qquad\mathbf r'(1)=\langle2,3,2\rangle.
$$

The tangent line is $$\boldsymbol\ell(s)=\langle1,1,2\rangle+s\langle2,3,2\rangle$$. Its height is $$2+2s$$, so it meets $$z=0$$ at $$s=-1$$ and the point $$(-1,-2,0)$$. This is a point on the tangent line, not necessarily on the original curve; local agreement does not mean the entire line lies on the curve.

</div>

<div class="theorem-box">

**Example.** A particle has $$\mathbf v(t)=\langle2t,\cos t,3\rangle$$ and $$\mathbf r(0)=\langle1,2,-1\rangle$$. Find its position.

Integrate each coordinate and retain a separate constant in each:

$$
\mathbf r(t)=\langle t^2+C_1,\sin t+C_2,3t+C_3\rangle.
$$

The initial position gives $$C_1=1$$, $$C_2=2$$, and $$C_3=-1$$. Hence $$\mathbf r(t)=\langle t^2+1,\sin t+2,3t-1\rangle$$. Differentiating recovers velocity, and substituting zero recovers the specified starting point.

</div>

---

## Change of Parameter; Arc Length

Two parametrizations may describe the same geometric curve with different speeds or orientations. If $$t=g(u)$$, then

$$
\frac{d\mathbf r}{du}=\frac{d\mathbf r}{dt}\frac{dt}{du}.
$$

A change with $$g'(u)>0$$ preserves orientation, while one with $$g'(u)<0$$ reverses it. For a regular change of parameter, require $$g'\ne0$$. A smooth parametrization here has a continuous, nonzero derivative.

To measure the length, join nearby sampled points with short straight segments. The displacement over a small interval $$\Delta t$$ is approximately $$\mathbf r'(t)\Delta t$$, so its length is approximately $$\lVert\mathbf r'(t)\rVert\Delta t$$. Summing those nonnegative lengths gives a Riemann sum. The limiting integral is therefore

$$
L=\int_a^b\lVert\mathbf r'(t)\rVert\,dt.
$$

Define arc length from a fixed starting parameter $$a$$ by

$$
s(t)=\int_a^t\lVert\mathbf r'(u)\rVert\,du.
$$

For a smooth parametrization, $$ds/dt>0$$, so we can locally solve for $$t$$ in terms of $$s$$. A parametrization by arc length has unit speed: $$\lVert d\mathbf r/ds\rVert=1$$.

<div class="theorem-box">

**Example.** For $$\mathbf r(t)=\langle3\cos t,3\sin t,4t\rangle$$, find the length of one turn and reparametrize using arc length measured from $$t=0$$.

The derivative has magnitude

$$
\lVert\mathbf r'(t)\rVert=\sqrt{9\sin^2t+9\cos^2t+16}=5.
$$

One turn, $$0\le t\le2\pi$$, has length $$10\pi$$. Since $$s=5t$$, the arc-length parametrization is

$$
\mathbf r(s)=\left\langle3\cos\frac s5,3\sin\frac s5,\frac{4s}5\right\rangle,
\qquad0\le s\le10\pi.
$$

</div>

### Length, distance, and changes of parameter

Arc length adds the magnitudes of small displacements. Endpoint distance takes the magnitude only after the displacements have been added, so cancellation can occur. A particle returning to its starting point has zero displacement but can travel a positive distance. This is the same distinction as total distance versus net change in single-variable motion.

<div class="theorem-box">

**Example.** For $$\mathbf r(t)=\langle t,t^2,\tfrac23t^3\rangle$$ on $$0\le t\le1$$, find its length, the point reached halfway along the curve, and an arc-length description without explicitly solving a cubic.

Velocity is $$\langle1,2t,2t^2\rangle$$, so the speed simplifies more than its three components suggest:

$$
v(t)=\sqrt{1+4t^2+4t^4}=1+2t^2.
$$

The expression inside the root is a perfect square, and its positive square root is valid throughout the interval. Consequently,

$$
s(t)=\int_0^t(1+2u^2)\,du=t+\frac23t^3,
\qquad L=s(1)=\frac53.
$$

Half the length corresponds to $$s=5/6$$, not necessarily half the parameter interval. The time satisfies $$4t^3+6t-5=0$$. This cubic is strictly increasing because its derivative is $$12t^2+6>0$$, and its values at zero and one have opposite signs, so there is exactly one solution in the interval.

Newton's method gives $$t\approx0.65014$$, placing the halfway point at approximately $$(0.65014,0.42268,0.18320)$$. In particular, $$t=1/2$$ would reach only $$s=7/12$$, less than half the total length.

For a parametrization by distance, define $$t=t(s)$$ as the unique solution of $$s=t+2t^3/3$$ and write $$\mathbf R(s)=\mathbf r(t(s))$$ on $$0\le s\le5/3$$. No explicit cubic formula is needed. Differentiating the defining relation gives

$$
\frac{dt}{ds}=\frac1{1+2t^2},\qquad
\lVert\mathbf R'(s)\rVert=v(t)\frac{dt}{ds}=1.
$$

This verifies unit speed directly. An implicitly defined inverse can be completely adequate for the geometry.

</div>

To reverse a path on $$a\le t\le b$$ while keeping the same parameter interval, use $$\widetilde{\mathbf r}(u)=\mathbf r(a+b-u)$$. Its derivative has the opposite sign, but its speed has the same magnitude at the corresponding point. Substitution in the length integral shows that reversal changes orientation without changing length.

An arc-length parameter is particularly useful when comparing two motions along the same path. It removes the choice of clock, leaving the geometry expressed in terms of actual distance along the curve.

---

## Unit Tangent, Normal, and Binormal Vectors

Velocity mixes two effects: the direction the path follows and the rate at which it is traversed. Dividing by speed removes the second effect, leaving a unit vector that follows the direction of travel. This lets us study the geometry without confusing a faster traversal with a sharper turn:

$$
\mathbf T=\frac{\mathbf r'}{\lVert\mathbf r'\rVert}.
$$

The tip of $$\mathbf T$$ always stays on the unit sphere. As the curve bends, $$\mathbf T$$ changes direction rather than length, so its derivative is perpendicular to it. Normalizing that derivative picks out the direction toward which the tangent is turning. This is the principal normal, not an arbitrary vector perpendicular to the curve.

The two directions then determine a local plane of bending. Their cross product supplies its normal, the binormal. Where $$\mathbf T'\ne\mathbf0$$, these definitions are

$$
\mathbf N=\frac{\mathbf T'}{\lVert\mathbf T'\rVert},
\qquad
\mathbf B=\mathbf T\times\mathbf N.
$$

These three vectors form a perpendicular unit frame. The normal points toward the local bend. The binormal is perpendicular to the **osculating plane**, which is spanned by $$\mathbf T$$ and $$\mathbf N$$. The normal plane is perpendicular to $$\mathbf T$$; the rectifying plane is spanned by $$\mathbf T$$ and $$\mathbf B$$.

:::warning
Normalizing $$\mathbf r''$$ does not generally give $$\mathbf N$$. Acceleration can have a tangential component. Compute $$\mathbf T$$ and differentiate it, or first remove the tangential component of acceleration.
:::

For the helix $$\mathbf r(t)=\langle3\cos t,3\sin t,4t\rangle$$ from the arc-length section,

$$
\mathbf T=\frac15\langle-3\sin t,3\cos t,4\rangle,
\qquad
\mathbf N=\langle-\cos t,-\sin t,0\rangle,
$$

$$
\mathbf B=\frac15\langle4\sin t,-4\cos t,3\rangle.
$$

```tikz Tangent and principal normal on the parabola at (1,1)
\begin{tikzpicture}[scale=1.15]
\draw[->,gray] (-0.7,0) -- (2.3,0) node[right] {$x$};
\draw[->,gray] (0,-0.3) -- (0,3.3) node[above] {$y$};
\draw[blue,thick,domain=-0.5:1.7,samples=60] plot (\x,{\x*\x});
\draw[->,orange!85!black,very thick] (1,1) -- (1.55,2.1) node[right] {$\mathbf T$};
\draw[->,teal,very thick] (1,1) -- (-0.1,1.55) node[left] {$\mathbf N$};
\fill (1,1) circle (1.5pt) node[below right] {$(1,1)$};
\node[right,blue] at (1.7,2.9) {$y=x^2$};
\end{tikzpicture}
```

At a point where $$\mathbf T'=\mathbf0$$, this definition of the principal normal does not apply. In particular, a straight line has a constant tangent and no distinguished principal normal.

### Finding the local planes

The tangent, normal, and binormal are attached to a point on the curve. Once their directions are known, equations of the associated planes come from the point-normal form in Chapter 1. A plane's name tells us which direction is perpendicular to it, but that direction need not be the principal normal. In particular, the normal plane has normal $$\mathbf T$$.

<div class="theorem-box">

**Example.** For $$\mathbf r(t)=\langle t,t^2,\tfrac23t^3\rangle$$, find the moving frame, curvature, and osculating plane at $$t=1$$. Also find the center of the osculating circle.

The point is $$P=(1,1,2/3)$$. At that time, velocity is $$\mathbf v=\langle1,2,2\rangle$$ and acceleration is $$\mathbf a=\langle0,2,4\rangle$$. The speed is $$3$$, giving $$\mathbf T=\langle1,2,2\rangle/3$$.

Acceleration is not perpendicular to velocity here: $$\mathbf v\cdot\mathbf a=12$$. Its tangential component is $$12/3=4$$. Subtract that part to isolate the direction of bending:

$$
\mathbf a-4\mathbf T
=\frac13\langle-4,-2,4\rangle,
\qquad
\lVert\mathbf a-4\mathbf T\rVert=2.
$$

Normalizing this vector gives $$\mathbf N=\langle-2,-1,2\rangle/3$$. The binormal is then

$$
\mathbf B=\mathbf T\times\mathbf N=\frac13\langle2,-2,1\rangle.
$$

To calculate curvature independently, $$\mathbf v\times\mathbf a=\langle4,-4,2\rangle$$ has magnitude $$6$$. Thus $$\kappa=6/3^3=2/9$$. The plane of bending has normal $$\mathbf B$$, so the osculating plane is

$$
2(x-1)-2(y-1)+\left(z-\frac23\right)=0,
\qquad 2x-2y+z=\frac23.
$$

The osculating circle's radius is $$1/\kappa=9/2$$. Its center is reached by moving that far from $$P$$ in direction $$\mathbf N$$:

$$
C=P+\frac1\kappa\mathbf N
=\left(-2,-\frac12,\frac{11}3\right).
$$

The center lies in the osculating plane, which checks that the computed normal and binormal are consistent. Normalizing acceleration itself would have mixed the speed change into the bending direction and produced the wrong circle.

</div>

Because $$\mathbf T\cdot\mathbf T=1$$, differentiating gives $$\mathbf T\cdot\mathbf T'=0$$. This proves that the principal normal, when defined, is perpendicular to the tangent. It is a consequence of constant length, not a special feature of the helix.

---

## Curvature

A sharply bending path turns a traveler through a large angle over a short distance. To measure that, compare unit tangent vectors at two nearby positions. Their difference records a change of direction without being affected by how large the original velocity vectors were. Divide by the distance traveled, then take a limit.

This defines curvature as the magnitude of change of the unit tangent per unit arc length. The chain rule converts distance-based differentiation into differentiation in the parameter:

$$
\kappa=\left\lVert\frac{d\mathbf T}{ds}\right\rVert
=\frac{\lVert\mathbf T'(t)\rVert}{\lVert\mathbf r'(t)\rVert}.
$$

It is useful to remove the derivative of a normalized vector from the calculation. The cross-product formula below does this by discarding the part of acceleration that only changes speed.

<div class="theorem-box">

**Proof (Cross-product formula for curvature).** Write $$\mathbf r'=v\mathbf T$$, where $$v=\lVert\mathbf r'\rVert>0$$. Differentiation gives $$\mathbf r''=v'\mathbf T+v\mathbf T'$$. Taking a cross product with velocity kills the first term:

$$
\mathbf r'\times\mathbf r''=v^2\mathbf T\times\mathbf T'.
$$

Since $$\mathbf T$$ is a unit vector perpendicular to $$\mathbf T'$$, the magnitude on the right is $$v^2\lVert\mathbf T'\rVert$$. Dividing by $$v^3$$ leaves $$\lVert\mathbf T'\rVert/v$$, exactly the arc-length definition of curvature.

</div>

Thus, for a twice continuously differentiable regular space curve,

$$
\kappa=\frac{\lVert\mathbf r'\times\mathbf r''\rVert}{\lVert\mathbf r'\rVert^3}.
$$

For a graph $$y=f(x)$$, this becomes

$$
\kappa=\frac{\lvert f''(x)\rvert}{\left(1+[f'(x)]^2\right)^{3/2}}.
$$

A circle of radius $$R$$ has curvature $$1/R$$. Where $$\kappa>0$$, the osculating circle has radius $$1/\kappa$$ and center $$\mathbf r+\mathbf N/\kappa$$. It matches the curve's tangent and curvature at that point.

For that radius-three helix with vertical component $$4t$$, $$\lVert\mathbf T'\rVert=3/5$$ and the speed is $$5$$, so $$\kappa=3/25$$. Its speed and curvature are both constant even though its velocity changes direction.

### Curvature should not depend on speed

A driver can travel along the same road quickly or slowly, but the road's bend does not change. The derivative $$d\mathbf T/dt$$ alone mixes bending with speed: a faster traveler encounters more change of direction per second. Dividing by $$ds/dt$$ gives change per unit distance and removes that dependence.

<div class="theorem-box">

**Example.** For the ellipse $$\mathbf r(t)=\langle3\cos t,2\sin t,0\rangle$$, find where curvature is largest and smallest, then find the osculating circle at $$(3,0)$$.

The velocity and acceleration are

$$
\mathbf r'=\langle-3\sin t,2\cos t,0\rangle,
\qquad
\mathbf r''=\langle-3\cos t,-2\sin t,0\rangle.
$$

Their cross product is constantly $$\langle0,0,6\rangle$$, but the speed is not constant. Thus

$$
\kappa(t)=\frac6{(9\sin^2t+4\cos^2t)^{3/2}}
=\frac6{(4+5\sin^2t)^{3/2}}.
$$

The denominator is smallest when $$\sin t=0$$, so the maximum curvature is $$3/4$$ at $$(\pm3,0)$$. It is largest when $$\sin^2t=1$$, so the minimum curvature is $$2/9$$ at $$(0,\pm2)$$. The ends of the longer axis are the sharper bends.

At $$(3,0)$$ the tangent points upward and the principal normal points left. The curvature radius is $$4/3$$, so the circle's center is $$(3-4/3,0)=(5/3,0)$$. Its equation is

$$
\left(x-\frac53\right)^2+y^2=\frac{16}9.
$$

The ellipse's horizontal semiaxis is $$3$$, but the osculating radius there is only $$4/3$$. Curvature describes local bending; it is not the distance from the curve to the center of the ellipse.

</div>

The cross-product formula is convenient when differentiating the normalized tangent would create a long quotient. If $$\mathbf r'\times\mathbf r''=\mathbf0$$ at a regular point, curvature is zero there. That does not force the whole curve to be a line; it only says the tangent has no first-order change with respect to arc length at that point.

---

## Motion Along a Curve

When $$t$$ is time, position, velocity, acceleration, and speed are

$$
\mathbf r(t),\qquad \mathbf v=\mathbf r',\qquad
\mathbf a=\mathbf r'',\qquad v=\lVert\mathbf v\rVert.
$$

Integrate acceleration to recover velocity, then integrate velocity to recover position. Each integration introduces a constant vector fixed by an initial condition.

For constant acceleration,

$$
\mathbf v(t)=\mathbf v_0+t\mathbf a,
\qquad
\mathbf r(t)=\mathbf r_0+t\mathbf v_0+\frac12t^2\mathbf a.
$$

For projectile motion near Earth's surface without drag, choose upward $$z$$ and $$\mathbf a=\langle0,0,-g\rangle$$ with constant $$g>0$$.

Acceleration changes both speed and direction. Where the tangent-normal frame exists,

$$
\mathbf a=\frac{dv}{dt}\mathbf T+\kappa v^2\mathbf N.
$$

The signed tangential component is $$a_T=(\mathbf v\cdot\mathbf a)/v$$. The normal component is nonnegative:

$$
a_N=\kappa v^2=\frac{\lVert\mathbf v\times\mathbf a\rVert}{v}.
$$

<div class="theorem-box">

**Example.** A particle follows $$\mathbf r(t)=\langle t,t^2,0\rangle$$. Find its speed, curvature, and tangential and normal acceleration components at $$t=1$$.

At that instant, $$\mathbf v=\langle1,2,0\rangle$$ and $$\mathbf a=\langle0,2,0\rangle$$. Therefore

$$
v=\sqrt5,\qquad
\kappa=\frac2{5\sqrt5},\qquad
a_T=\frac4{\sqrt5},\qquad a_N=\frac2{\sqrt5}.
$$

As a check, $$a_T^2+a_N^2=4=\lVert\mathbf a\rVert^2$$.

</div>

### Deriving the acceleration components

Write velocity as $$\mathbf v=v\mathbf T$$, separating speed from direction. The product rule gives

$$
\mathbf a=v'\mathbf T+v\mathbf T'.
$$

Since $$\mathbf T'=\kappa v\mathbf N$$, the second term becomes $$\kappa v^2\mathbf N$$. The tangent component changes speed, while the normal component turns the velocity. A negative tangential component means the particle is slowing down at that instant, regardless of the signs of its coordinates.

<div class="theorem-box">

**Example.** A particle follows $$\mathbf r(t)=\langle3\cos(2t),3\sin(2t),0\rangle$$. Find its speed and acceleration, and explain how it can accelerate without speeding up.

Differentiating gives

$$
\mathbf v=\langle-6\sin(2t),6\cos(2t),0\rangle,
\qquad
\mathbf a=\langle-12\cos(2t),-12\sin(2t),0\rangle.
$$

The speed is constantly $$6$$, so $$a_T=0$$. The path is a circle of radius $$3$$, with curvature $$1/3$$, giving $$a_N=(1/3)(6^2)=12$$. The acceleration points toward the center. It changes the direction of velocity continuously even though the magnitude stays fixed.

</div>

For projectile problems, solve the vertical coordinate for the event time first, then use that same time in the horizontal coordinates. Reject negative times or roots outside the stated motion interval. If launch and landing heights differ, a memorized equal-height range formula will not apply, but the component equations still do.

The normal acceleration formula also gives a geometric check on units: curvature has units of inverse length, so multiplying it by speed squared gives length per time squared, the units of acceleration.

### Projectile motion from unequal heights

With constant downward acceleration, the vertical coordinate is quadratic in time while the horizontal coordinates are linear. The impact condition supplies the time; the horizontal coordinates then give the landing location. Find the velocity at that same time if the question asks for impact speed or direction.

<div class="theorem-box">

**Example.** A particle starts at $$(0,0,5)$$ with initial velocity $$\langle6,8,10\rangle$$ and constant acceleration $$\langle0,0,-10\rangle$$. Find when and where it reaches $$z=0$$, and find its impact speed.

Integrating the acceleration with the initial conditions gives

$$
\mathbf r(t)=\langle6t,8t,5+10t-5t^2\rangle,
\qquad
\mathbf v(t)=\langle6,8,10-10t\rangle.
$$

The height equation reduces to $$t^2-2t-1=0$$. Its roots are $$1\pm\sqrt2$$, and only $$t=1+\sqrt2$$ occurs after launch. The landing point is

$$
\left(6(1+\sqrt2),8(1+\sqrt2),0\right).
$$

At impact, the vertical velocity is $$-10\sqrt2$$. Therefore the speed is

$$
\sqrt{6^2+8^2+(-10\sqrt2)^2}=10\sqrt3.
$$

The negative vertical component indicates downward motion, but speed is positive. The horizontal speed stays at $$10$$ throughout the flight. The launch height is positive, so the particle spends longer in flight than it would if it landed back at its launch height. This is why the event equation must use the actual landing plane.

</div>

---

## Kepler's Laws of Planetary Motion

In the ideal two-body model, the relative position vector obeys

$$
\mathbf r''=-\frac{\mu}{\lVert\mathbf r\rVert^3}\mathbf r,
\qquad \mu=G(M+m).
$$

If the central mass is treated as fixed and the orbiting mass is negligible, use $$\mu\approx GM$$. This model ignores other bodies and non-gravitational forces.

The force is central, so the specific angular momentum $$\mathbf h=\mathbf r\times\mathbf v$$ is constant:

$$
\frac{d\mathbf h}{dt}
=\mathbf v\times\mathbf v+\mathbf r\times\mathbf a=\mathbf0.
$$

For a nonradial orbit, $$\mathbf h\ne\mathbf0$$, and motion stays in the plane perpendicular to $$\mathbf h$$. In that plane, the area swept out per unit time is

$$
\frac{dA}{dt}=\frac12\lVert\mathbf r\times\mathbf v\rVert
=\frac12\lVert\mathbf h\rVert.
$$

This proves the equal-areas law: the particle moves faster near the attracting body and slower farther away.

To see where the conic equation comes from, work in the orbital plane using polar coordinates $$r,\theta$$. Choose its positive normal so the constant scalar angular momentum $$h=r^2\dot\theta$$ is positive. Resolving acceleration along the radius gives

$$
\ddot r-r\dot\theta^2=-\frac\mu{r^2}.
$$

The term $$-r\dot\theta^2$$ comes from the turning of the radial direction itself. It remains even for a circular orbit where $$r$$ is constant; omitting it would confuse radial acceleration with the second derivative of radial distance.

Use $$u(\theta)=1/r$$ to change the independent variable from time to angle. Angular-momentum conservation gives $$\dot\theta=hu^2$$. Applying the chain rule yields

$$
\dot r=-h\frac{du}{d\theta},\qquad
\ddot r=-h^2u^2\frac{d^2u}{d\theta^2}.
$$

Substituting into the radial equation and dividing by the nonzero factor $$u^2$$ reduces it to

$$
\frac{d^2u}{d\theta^2}+u=\frac\mu{h^2}.
$$

Its solutions are a constant plus a combination of sine and cosine. Combining those terms into a phase-shifted cosine gives $$u=(\mu/h^2)(1+e\cos(\theta-\theta_0))$$, where $$e\ge0$$ measures the oscillation amplitude relative to the constant term. Taking the reciprocal gives the conic equation below.

For nonradial inverse-square motion,

$$
r=\frac{p}{1+e\cos(\theta-\theta_0)},
\qquad p=\frac{\lVert\mathbf h\rVert^2}{\mu}.
$$

The conic depends on eccentricity: $$0\le e<1$$ gives an ellipse, $$e=1$$ a parabola, and $$e>1$$ a hyperbola. Kepler's first law concerns the bound elliptical case, with the attracting center at a focus.

The constant angular momentum explains the sweep rate, but it does not by itself determine which conic occurs. That comes from solving the inverse-square equation of motion. The orbit equation above records that solution; its denominator changes the radial distance with direction. For $$e<1$$ it stays positive and bounded away from zero, giving a closed orbit. At $$e=1$$ it can vanish in one direction, and the orbit is no longer bounded.

For an ellipse with semimajor axis $$a$$ and semiminor axis $$b$$, the period $$T_{\mathrm{orb}}$$ follows from its area and the constant areal speed:

$$
T_{\mathrm{orb}}=\frac{2\pi ab}{\lVert\mathbf h\rVert}.
$$

For the conic above, the nearest and farthest radii are $$p/(1+e)$$ and $$p/(1-e)$$. Their average is the semimajor axis, so $$a=p/(1-e^2)$$. Since $$p=h^2/\mu$$, this gives $$h^2=\mu a(1-e^2)$$. Together with the ellipse identity $$b^2=a^2(1-e^2)$$, substitution in the period formula cancels the eccentricity and gives Kepler's third law:

$$
T_{\mathrm{orb}}^2=\frac{4\pi^2}{\mu}a^3.
$$

The proportionality constant is the same for orbits with the same $$\mu$$. The specific mechanical energy is $$\varepsilon=v^2/2-\mu/r$$; escape requires $$\varepsilon\ge0$$, giving the minimum escape speed $$v_{\mathrm{esc}}=\sqrt{2\mu/r}$$.

### Reading the orbital model

The position vector in the orbital equation points from the attracting center to the orbiting body. Its length changes along an ellipse. The acceleration is always inward, but it is not generally parallel to the velocity or the principal normal. Away from the nearest and farthest points of an elliptical orbit, gravity can change speed as well as turn the path.

The equal-areas law does not say equal arc lengths are covered in equal times. A short distance from the attracting center gives a narrow triangle for a given small arc, so a larger transverse speed is needed to keep the swept area per unit time constant. This is why an orbiting body speeds up near its closest approach.

<div class="theorem-box">

**Example.** An elliptical orbit has nearest and farthest distances $$r_p=a(1-e)$$ and $$r_a=a(1+e)$$, with eccentricity $$e=1/3$$. Find the ratio of the speeds at those points and compare its period with an orbit of semimajor axis $$a/4$$ around the same central mass.

At nearest and farthest approach, radial distance is momentarily stationary, so velocity is perpendicular to the radius. Conservation of angular momentum becomes

$$
r_pv_p=r_av_a.
$$

Therefore

$$
\frac{v_p}{v_a}=\frac{r_a}{r_p}
=\frac{1+1/3}{1-1/3}=2.
$$

For the periods, use the ratio form of Kepler's third law. The common factor involving $$\mu$$ cancels:

$$
\frac{T_a}{T_{a/4}}=\left(\frac{a}{a/4}\right)^{3/2}=8.
$$

The eccentricity affects the speed variation but does not appear in the period once the semimajor axis and gravitational parameter are fixed.

</div>

Escape speed comes from setting the specific energy to zero. It is the threshold for reaching arbitrarily large distance with no leftover speed in this ideal model. A bound elliptical orbit has negative specific energy; a nonradial zero-energy orbit is parabolic, and positive energy gives a hyperbolic orbit. These statements refer to the two-body model, rather than trajectories disturbed by other bodies.

---

:::equations
| Idea | Equation or condition |
| --- | --- |
| Tangent line | $$\boldsymbol\ell(s)=\mathbf r(t_0)+s\mathbf r'(t_0),\quad\mathbf r'(t_0)\ne\mathbf0$$ |
| Arc length | $$L=\int_a^b\lVert\mathbf r'(t)\rVert\,dt$$ |
| Arc-length parameter | $$s(t)=\int_a^t\lVert\mathbf r\prime(u)\rVert\,du$$ |
| Moving frame | $$\mathbf T=\mathbf r'/\lVert\mathbf r'\rVert,\quad\mathbf N=\mathbf T'/\lVert\mathbf T'\rVert,\quad\mathbf B=\mathbf T\times\mathbf N$$ |
| Curvature | $$\kappa=\lVert\mathbf r'\times\mathbf r''\rVert/\lVert\mathbf r'\rVert^3$$ |
| Acceleration | $$\mathbf a=v'\mathbf T+\kappa v^2\mathbf N$$ |
| Constant acceleration | $$\mathbf r=\mathbf r_0+t\mathbf v_0+\tfrac12t^2\mathbf a$$ |
| Areal speed | $$dA/dt=\lVert\mathbf h\rVert/2,\quad\mathbf h=\mathbf r\times\mathbf v$$ |
| Inverse-square orbit | $$r=p/(1+e\cos(\theta-\theta_0)),\quad p=\lVert\mathbf h\rVert^2/\mu$$ |
| Elliptical period | $$T_{\mathrm{orb}}^2=4\pi^2a^3/\mu$$ |
| Escape speed | $$v_{\mathrm{esc}}=\sqrt{2\mu/r}$$ |
:::

## Reference

Topic and section order follows Anton, Bivens, and Davis, *Calculus: Early Transcendentals*, 12th edition, Chapter 12, renumbered as Chapter 2 here. Explanations and worked examples on this page are original study notes.
