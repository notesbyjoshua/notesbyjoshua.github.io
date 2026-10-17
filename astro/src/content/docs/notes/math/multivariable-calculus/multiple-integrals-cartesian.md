---
title: "Chapter 4: Multiple Integrals"
description: "Multivariable calculus notes on double and triple integrals, polar and spherical coordinates, surface area, Jacobians, mass, and centers of gravity."
status: developing
progress: 70
sidebar:
  order: 4
---

## Double Integrals

A double integral adds contributions over a plane region. Divide a region $$R$$ into small pieces of area $$\Delta A_i$$, choose a point $$(x_i^*,y_i^*)$$ in each piece, and form

$$
\sum_i f(x_i^*,y_i^*)\Delta A_i.
$$

When these sums approach a common value as the largest piece diameter approaches zero, the limit is $$\iint_R f\,dA$$. A continuous function on a closed rectangle is integrable.

If $$f\ge0$$, the integral gives volume below the graph and above the region. If $$f$$ changes sign, it gives signed volume. Area itself is $$A(R)=\iint_R1\,dA$$.

The definition adds contributions over many tiny patches, but a direct limit of a two-dimensional sum is rarely a convenient calculation. Instead, collect all patches in a thin vertical strip first. Integrating in $$y$$ adds up a cross section of the solid at fixed $$x$$; integrating those cross sections in $$x$$ adds the whole solid. Collecting horizontal strips reverses the roles.

This is the geometric reason an iterated integral can evaluate a double integral. Fubini's theorem makes the passage from sums to repeated integration valid under suitable integrability assumptions. For continuous $$f$$ on $$R=[a,b]\times[c,d]$$, it gives

$$
\iint_Rf\,dA
=\int_a^b\int_c^d f(x,y)\,dy\,dx
=\int_c^d\int_a^b f(x,y)\,dx\,dy.
$$

In the inner integral, hold the outer variable constant. Evaluate the inner bounds before proceeding to the outer integration. If an integrand factors as $$g(x)h(y)$$ on a rectangle, its integral factors into the product of the two single integrals.

The average value over a region of positive area is

$$
f_{\mathrm{avg}}=\frac1{A(R)}\iint_Rf\,dA.
$$

<div class="theorem-box">

**Example.** Find the average value of $$f(x,y)=x+2y$$ on $$0\le x\le2$$, $$0\le y\le1$$.

First integrate:

$$
\int_0^2\int_0^1(x+2y)\,dy\,dx
=\int_0^2(x+1)\,dx=4.
$$

The rectangle has area $$2$$, so $$f_{\mathrm{avg}}=4/2=2$$.

</div>

### Accumulation, cancellation, and units

The units of a double integral come from multiplying the integrand's units by area. A height function integrated over a horizontal region gives volume. Area density integrated over a region gives mass. A temperature function integrated over area gives temperature times area, so divide by the area to recover an average temperature.

Linearity works as it did for single integrals: constants can be factored out and sums can be integrated term by term. Integrals over adjacent regions also add, provided their interiors do not overlap. This lets us divide a complicated region into manageable pieces without changing the quantity being measured.

<div class="theorem-box">

**Example.** On the square $$-1\le x,y\le1$$, find the signed integral of $$f(x,y)=x$$ and the total volume between its graph and the horizontal plane.

The signed integral is

$$
\int_{-1}^1\int_{-1}^1x\,dy\,dx
=2\int_{-1}^1x\,dx=0.
$$

Positive and negative heights cancel. For total volume, use the absolute height instead:

$$
\iint_R\lvert x\rvert\,dA
=2\int_{-1}^1\lvert x\rvert\,dx=2.
$$

The zero signed integral does not mean there is no solid between the graph and the plane. It records cancellation between two equal-volume pieces on opposite sides of that plane.

</div>

Symmetry can shorten a calculation before any antiderivative is taken. An odd integrand cancels over a region symmetric in the relevant coordinate. Check both the integrand and the region: an odd expression does not cancel if only one side of the region is included.

---

## Double Integrals over Nonrectangular Regions

The bounds describe the region, independently of the integrand. For a region between two graphs of $$y$$,

$$
R=\{(x,y):a\le x\le b,\ g_1(x)\le y\le g_2(x)\},
$$

use vertical slices:

$$
\iint_R f\,dA=\int_a^b\int_{g_1(x)}^{g_2(x)}f(x,y)\,dy\,dx.
$$

For a region between graphs of $$x$$, use horizontal slices:

$$
\iint_R f\,dA=\int_c^d\int_{h_1(y)}^{h_2(y)}f(x,y)\,dx\,dy.
$$

Some regions require splitting because the upper, lower, left, or right boundary changes. To reverse integration order, reconstruct the region and slice it the other way. Swapping the differentials while keeping the bounds usually changes the problem.

<div class="theorem-box">

**Example.** Evaluate $$\int_0^1\int_x^1 e^{y^2}\,dy\,dx$$ by reversing the order.

The bounds describe $$0\le x\le y\le1$$. A horizontal slice has $$0\le x\le y$$, so

$$
\int_0^1\int_x^1e^{y^2}\,dy\,dx
=\int_0^1\int_0^y e^{y^2}\,dx\,dy
=\int_0^1ye^{y^2}\,dy
=\frac{e-1}2.
$$

The original inner integral has no elementary antiderivative. Changing the order makes the calculation straightforward.

</div>

```tikz The same triangle can be sliced vertically or horizontally
\begin{tikzpicture}[scale=3]
\fill[blue!10] (0,0) -- (0,1) -- (1,1) -- cycle;
\draw[->,gray] (-0.08,0) -- (1.2,0) node[right] {$x$};
\draw[->,gray] (0,-0.08) -- (0,1.2) node[above] {$y$};
\draw[blue,thick] (0,0) -- (1,1) -- (0,1) -- cycle;
\draw[orange!85!black,very thick] (0.35,0.35) -- (0.35,1);
\draw[teal,very thick] (0,0.7) -- (0.7,0.7);
\node[below right] at (0.7,0.65) {$y=x$};
\node[above] at (0.55,1) {$y=1$};
\node[below] at (1,0) {$1$};
\node[below left] at (0,0) {$0$};
\end{tikzpicture}
```

:::strategy
Sketch the boundary curves, mark their intersections, and choose a typical slice. Read its starting and ending coordinates directly from the sketch. The outer bounds cover the full range of slices; inner bounds describe one slice.
:::

### Choosing an order from the region

When the boundary consists of two curves, solve for their intersection points first. These determine the outer interval, but they do not by themselves tell you which curve is on top. Test an interior coordinate or use the sketch before writing the inner bounds. Incorrectly reversing upper and lower limits gives a negative integral even for a positive integrand.

<div class="theorem-box">

**Example.** Find the area enclosed by $$y=x^2$$ and $$y=2-x$$. Set it up in both orders, explaining why one order requires splitting the region.

The intersections satisfy $$x^2=2-x$$, giving $$x=-2,1$$. Between those points the line is above the parabola, so vertical slices give one integral:

$$
A=\int_{-2}^1\int_{x^2}^{2-x}1\,dy\,dx
=\int_{-2}^1(2-x-x^2)\,dx=\frac92.
$$

For horizontal slices, the parabola supplies $$-\sqrt y\le x\le\sqrt y$$, while staying below the line requires $$x\le2-y$$. Both conditions must hold. The left boundary is always $$-\sqrt y$$; the right boundary is the smaller of $$\sqrt y$$ and $$2-y$$.

Those two right-boundary candidates switch at $$y=1$$. The region extends from the parabola's vertex at $$y=0$$ to the higher intersection at $$y=4$$. Thus the reversed order is

$$
A=\int_0^1\int_{-\sqrt y}^{\sqrt y}1\,dx\,dy
+\int_1^4\int_{-\sqrt y}^{2-y}1\,dx\,dy.
$$

The first integral is $$4/3$$ and the second is $$19/6$$, again totaling $$9/2$$. Using the line as the right boundary for all heights would wrongly include points outside the parabola at the bottom. Using the positive square-root branch for all heights would include points beyond the line at the top. The split records a real change in which boundary a horizontal slice reaches first.

</div>

If the inside antiderivative looks difficult, consider changing order before introducing a special function or numerical approximation. The useful question is whether a different slicing makes the integrand simpler to integrate or the boundary simpler to describe; these goals do not always favor the same order.

---

## Double Integrals in Polar Coordinates

Polar coordinates suit circular regions and expressions involving $$x^2+y^2$$:

$$
x=r\cos\theta,\qquad y=r\sin\theta.
$$

The coordinate formulas change positions, but an integral also needs the physical area represented by a small coordinate rectangle. An angular step has no fixed length: the same angle spans a larger arc farther from the origin. At radius $$r$$, that arc is approximately $$r\,d\theta$$ long.

Multiplying by radial thickness gives the first-order area $$r\,dr\,d\theta$$. More explicitly, an annular sector of angle $$\Delta\theta$$ between radii $$r$$ and $$r+\Delta r$$ has exact area $$\tfrac12((r+\Delta r)^2-r^2)\Delta\theta$$. Its leading term is $$r\Delta r\Delta\theta$$; the extra term is of higher order in the radial thickness. Thus

$$
dA=r\,dr\,d\theta.
$$

For a region with $$\alpha\le\theta\le\beta$$ and $$r_1(\theta)\le r\le r_2(\theta)$$,

$$
\iint_Rf(x,y)\,dA
=\int_\alpha^\beta\int_{r_1(\theta)}^{r_2(\theta)}
f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta.
$$

Change the integrand, bounds, and area element together. The factor $$r$$ is part of the area element even when the original integrand is $$1$$.

<div class="theorem-box">

**Example.** Find the volume below $$z=4-x^2-y^2$$ and above the disk $$x^2+y^2\le4$$.

The height becomes $$4-r^2$$, and the disk has $$0\le r\le2$$, $$0\le\theta\le2\pi$$. Thus

$$
V=\int_0^{2\pi}\int_0^2(4-r^2)r\,dr\,d\theta
=2\pi\left[2r^2-\frac{r^4}4\right]_0^2
=8\pi.
$$

</div>

### Radial bounds may depend on angle

A disk centered at the origin gives constant radial bounds, but a shifted circle usually does not. Convert the boundary equation first and then decide which angles produce the desired region. Using a negative radial bound would conflict with the nonnegative-radius convention used in these notes.

<div class="theorem-box">

**Example.** Find the area inside $$x^2+y^2\le2x$$ using polar coordinates.

Completing the square identifies a disk centered at $$(1,0)$$ with radius $$1$$. Substituting polar coordinates into its boundary gives $$r^2=2r\cos\theta$$, hence $$r=2\cos\theta$$ away from the origin. The disk is swept by rays with $$-\pi/2\le\theta\le\pi/2$$:

$$
A=\int_{-\pi/2}^{\pi/2}\int_0^{2\cos\theta}r\,dr\,d\theta
=2\int_{-\pi/2}^{\pi/2}\cos^2\theta\,d\theta=\pi.
$$

This agrees with the geometric area of the radius-one disk. Using all angles from zero to a full turn with the same radial formula would introduce negative upper bounds and would not describe the region under our convention.

</div>

When both integrand and region depend only on distance from the origin, the angular integral often contributes a constant factor. For a full circular region that factor is one full turn; for a sector it is the sector angle. The radial integral must still include the extra factor from the area element.

### A radial integrand with a nontrivial antiderivative

Polar coordinates can simplify the integrand as well as the boundary. An exponential involving squared distance becomes an exponential in the radial variable, and the area factor supplies exactly the extra radial factor needed for substitution.

<div class="theorem-box">

**Example.** Evaluate $$\iint_D e^{-(x^2+y^2)}\,dA$$ on the disk $$x^2+y^2\le a^2$$, where $$a>0$$.

The circular region and squared-distance integrand both favor polar coordinates:

$$
\iint_D e^{-(x^2+y^2)}\,dA
=\int_0^{2\pi}\int_0^a e^{-r^2}r\,dr\,d\theta.
$$

Use the derivative of $$-r^2$$ to integrate radially:

$$
2\pi\left[-\frac12e^{-r^2}\right]_0^a
=\pi(1-e^{-a^2}).
$$

The answer is positive and increases with the disk radius, as expected for a positive integrand over an expanding region. It stays below $$\pi$$ because the exponential decreases rapidly away from the origin. Trying to integrate with respect to a rectangular coordinate first would hide this simple substitution.

</div>

---

## Surface Area; Parametric Surfaces

A double integral over a horizontal base counts projected area. A tilted surface patch has more area than its projection because one or both directions across it climb as well as move horizontally. We need to account for that extra length locally, then add the corrected patch areas.

For a graph, the coordinate slopes determine the tilt. Over a tiny horizontal step in $$x$$, the surface displacement is approximately $$\langle dx,0,f_xdx\rangle$$; over a step in $$y$$ it is approximately $$\langle0,dy,f_ydy\rangle$$. These two directions span a tangent parallelogram. Its cross-product magnitude supplies the area factor proved below.

For $$z=f(x,y)$$ with continuous first partials over $$R$$,

$$
A=\iint_R\sqrt{1+f_x^2+f_y^2}\,dA.
$$

This measures surface area, not the volume below the graph.

More generally, a parametrized surface has position

$$
\mathbf r(u,v)=\langle x(u,v),y(u,v),z(u,v)\rangle.
$$

A small parameter rectangle maps to a surface patch whose two approximate edge vectors are $$\mathbf r_u\,du$$ and $$\mathbf r_v\,dv$$. These generally are neither perpendicular nor unit length. Multiplying their magnitudes would ignore the angle between them. The cross product accounts for their lengths and that angle together, giving

$$
dS=\lVert\mathbf r_u\times\mathbf r_v\rVert\,du\,dv,
\qquad
A=\iint_D\lVert\mathbf r_u\times\mathbf r_v\rVert\,du\,dv.
$$

Use a parametrization that covers the surface once, apart from boundary overlaps, and is regular where needed: $$\mathbf r_u\times\mathbf r_v\ne\mathbf0$$. Otherwise the integral may count repeated coverage.

<div class="theorem-box">

**Proof (Area element for a graph).** Parametrize the graph by $$\mathbf r(x,y)=\langle x,y,f(x,y)\rangle$$. Then

$$
\mathbf r_x=\langle1,0,f_x\rangle,\qquad
\mathbf r_y=\langle0,1,f_y\rangle,
$$

so

$$
\mathbf r_x\times\mathbf r_y=\langle-f_x,-f_y,1\rangle.
$$

Taking its magnitude gives the factor $$\sqrt{1+f_x^2+f_y^2}$$.

</div>

For example, the patch $$z=2x-y$$ over a rectangle of area $$3$$ has area $$3\sqrt6$$ because the area factor is constantly $$\sqrt{1+4+1}$$.

### A parametrization is a map from a parameter region

The parameters describe where a surface patch comes from. Holding one fixed gives a curve on the surface; varying both fills the patch. Bounds in the parameter plane are therefore part of the surface description. The same formula with different bounds can cover a patch, a whole surface, or the same surface multiple times.

<div class="theorem-box">

**Example.** Find the lateral area of the cylinder $$x^2+y^2=a^2$$ between $$z=0$$ and $$z=h$$, where $$a,h>0$$, using a surface parametrization.

Use angle and height:

$$
\mathbf r(\theta,z)=\langle a\cos\theta,a\sin\theta,z\rangle,
\qquad0\le\theta\le2\pi,\quad0\le z\le h.
$$

The tangent vectors are $$\mathbf r_\theta=\langle-a\sin\theta,a\cos\theta,0\rangle$$ and $$\mathbf r_z=\langle0,0,1\rangle$$. Their cross product has magnitude $$a$$, so

$$
A=\int_0^{2\pi}\int_0^h a\,dz\,d\theta=2\pi ah.
$$

This counts only the curved side because the parametrization does not include the top and bottom disks. Those caps would require two additional patches, each of area $$\pi a^2$$.

</div>

A cylinder's side cannot be represented by a single-valued height function over the full horizontal disk. A parametric representation avoids that difficulty. For an upper hemisphere, a graph is possible, but its derivatives become unbounded at the equator; spherical parameters can give a cleaner calculation.

---

## Triple Integrals

A triple integral accumulates over a solid region $$E$$. In particular,

$$
V(E)=\iiint_E1\,dV.
$$

If the solid lies between $$z=g_1(x,y)$$ and $$z=g_2(x,y)$$ above a base $$R$$, then

$$
\iiint_Ef\,dV
=\iint_R\int_{g_1(x,y)}^{g_2(x,y)}f(x,y,z)\,dz\,dA.
$$

Other orders are possible. In an iterated integral, the innermost bounds may depend on the two outer variables, the middle bounds may depend on the outermost variable, and the outermost bounds are constants.

<div class="theorem-box">

**Example.** Find the volume of the first-octant tetrahedron bounded by $$x+y+z=2$$ and the coordinate planes.

For fixed $$x,y$$, height runs from $$z=0$$ to $$z=2-x-y$$. Its projection is $$0\le x\le2$$, $$0\le y\le2-x$$. Therefore

$$
V=\int_0^2\int_0^{2-x}\int_0^{2-x-y}1\,dz\,dy\,dx
=\frac12\int_0^2(2-x)^2\,dx
=\frac43.
$$

</div>

### Project first, then fill the solid

For an integral with vertical integration innermost, project the solid onto the horizontal plane. A point belongs to that projection only if a vertical line above it meets the solid. Then determine the bottom and top surfaces along that line. The boundary of the projection often comes from setting those surfaces equal.

<div class="theorem-box">

**Example.** Find the volume between $$z=x^2+y^2$$ and $$z=2-x^2-y^2$$.

The surfaces meet when $$x^2+y^2=1$$. Inside that disk, the upper paraboloid has height $$2-r^2$$ and the lower one has height $$r^2$$. Cylindrical coordinates give

$$
V=\int_0^{2\pi}\int_0^1\int_{r^2}^{2-r^2}r\,dz\,dr\,d\theta.
$$

Integrating vertically first leaves the difference of the two heights:

$$
V=2\pi\int_0^1(2-2r^2)r\,dr=\pi.
$$

The thickness vanishes at the outer circle, so the bounds pass a useful geometric check. Extending the radial interval beyond one would reverse which paraboloid is on top and would no longer describe the enclosed solid with these bounds.

</div>

A triple integral of a nonconstant function uses exactly the same region bounds as the volume integral. The bounds describe where accumulation occurs; the integrand describes what is accumulated there. Keeping these roles separate makes it easier to reuse a correct setup for volume, mass, or a moment.

---

## Triple Integrals in Cylindrical and Spherical Coordinates

Cylindrical coordinates retain the polar area factor and add vertical thickness:

$$
x=r\cos\theta,\quad y=r\sin\theta,\quad z=z,
\qquad dV=r\,dz\,dr\,d\theta.
$$

Choose them for cylinders, cones, and surfaces where $$x^2+y^2$$ appears. The integration order can change, but the factor $$r$$ remains.

In spherical coordinates, with $$\phi$$ measured from the positive $$z$$-axis,

$$
x=\rho\sin\phi\cos\theta,\quad
y=\rho\sin\phi\sin\theta,\quad
z=\rho\cos\phi,
$$

$$
dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta.
$$

The three small lengths are approximately $$d\rho$$, $$\rho\,d\phi$$, and $$\rho\sin\phi\,d\theta$$. Their product explains the scale factor.

A full ball of radius $$a$$ uses $$0\le\rho\le a$$, $$0\le\phi\le\pi$$, and $$0\le\theta\le2\pi$$. The upper hemisphere uses $$0\le\phi\le\pi/2$$. A cone from the origin often gives a constant bound on $$\phi$$.

<div class="theorem-box">

**Example.** A uniform solid lies inside $$x^2+y^2+z^2\le2z$$ and above $$z=\sqrt{x^2+y^2}$$. Find its volume and centroid using spherical coordinates.

Completing the square shows the sphere has center $$(0,0,1)$$ and radius one. Spherical substitution gives $$\rho^2\le2\rho\cos\phi$$, so a ray runs from the origin to $$\rho=2\cos\phi$$. The upper cone corresponds to $$\phi=\pi/4$$; being above it means $$0\le\phi\le\pi/4$$. Every azimuth is allowed.

The sphere is shifted, so its radial upper bound depends on angle. The volume is

$$
V=\int_0^{2\pi}\int_0^{\pi/4}\int_0^{2\cos\phi}
\rho^2\sin\phi\,d\rho\,d\phi\,d\theta
=\frac{16\pi}3\int_0^{\pi/4}\cos^3\phi\sin\phi\,d\phi=\pi.
$$

Rotational symmetry gives $$\overline x=\overline y=0$$. To find the height, weight each volume element by $$z=\rho\cos\phi$$:

$$
\iiint_Ez\,dV
=\int_0^{2\pi}\int_0^{\pi/4}\int_0^{2\cos\phi}
\rho^3\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta
=8\pi\int_0^{\pi/4}\cos^5\phi\sin\phi\,d\phi
=\frac{7\pi}6.
$$

For a uniform solid the constant density cancels, giving centroid $$(0,0,7/6)$$. This lies above the sphere's center because the cone removes more material from the lower part. The moment formula is developed further in the centers-of-gravity section; here it uses the same bounds as volume, with one extra factor of height.

</div>

### Choosing cylindrical or spherical coordinates

Cylindrical coordinates are often convenient when vertical bounds are easy to isolate and the horizontal projection is circular. Spherical coordinates are often convenient when rays from the origin meet the boundary at a simple distance. A spherical boundary alone does not force spherical coordinates; a shifted sphere or several intersecting surfaces can make another choice easier.

<div class="theorem-box">

**Example.** Evaluate $$\iiint_B(x^2+y^2+z^2)\,dV$$ over the ball of radius $$a>0$$ centered at the origin.

The integrand becomes $$\rho^2$$. The region is described by $$0\le\rho\le a$$, $$0\le\phi\le\pi$$, and $$0\le\theta\le2\pi$$. Including the volume factor gives

$$
\iiint_B(x^2+y^2+z^2)\,dV
=\int_0^{2\pi}\int_0^\pi\int_0^a
\rho^4\sin\phi\,d\rho\,d\phi\,d\theta
=\frac{4\pi a^5}5.
$$

The power $$a^5$$ matches the units: the integrand contributes length squared and the volume element contributes length cubed. Dividing by the ball's volume gives the average squared distance from the origin, $$3a^2/5$$.

</div>

For a region between two cones, find the polar angle of each cone and use the interval between those angles. For a region outside a smaller sphere and inside a larger concentric sphere, use two radial bounds. Translating every boundary separately is safer than trying to recognize a memorized combination of shapes.

---

## Change of Variables in Multiple Integrals; Jacobians

Polar coordinates work because their coordinate curves fit circular geometry. We can use the same idea for other boundaries: choose new variables whose constant-value curves match the region. For example, if the boundaries are hyperbolas $$xy=\text{constant}$$, the product $$xy$$ is a promising new variable.

Changing coordinates stretches small areas. To find the amount, move a small distance in the $$u$$-direction while fixing $$v$$; the physical displacement is approximately $$\langle x_u,y_u\rangle du$$. A small $$v$$-step similarly gives $$\langle x_v,y_v\rangle dv$$. The signed area spanned by those two edges is their determinant times $$du\,dv$$.

This determinant is the Jacobian of $$x=x(u,v),y=y(u,v)$$:

$$
J=\frac{\partial(x,y)}{\partial(u,v)}
=\begin{vmatrix}x_u&x_v\\y_u&y_v\end{vmatrix}
=x_uy_v-x_vy_u.
$$

Under a continuously differentiable, one-to-one transformation with nonzero Jacobian in the interior, mapping $$D$$ onto $$R$$,

$$
\iint_Rf(x,y)\,dA
=\iint_Df(x(u,v),y(u,v))\lvert J\rvert\,du\,dv.
$$

Boundary degeneracies such as the polar origin are allowed in the usual piecewise version of this theorem. The absolute value keeps area positive when the transformation reverses orientation.

For triple integrals, use the absolute value of the corresponding $$3\times3$$ determinant $$\partial(x,y,z)/\partial(u,v,w)$$.

<div class="theorem-box">

**Example.** Let $$R$$ be bounded by $$x+y=0$$, $$x+y=2$$, $$x-y=0$$, and $$x-y=4$$. Evaluate $$\iint_R(x+y)\,dA$$.

Set $$u=x+y$$ and $$v=x-y$$. Then $$0\le u\le2$$ and $$0\le v\le4$$. Solving for the original variables gives

$$
x=\frac{u+v}2,\qquad y=\frac{u-v}2,
\qquad J=-\frac12.
$$

Therefore

$$
\iint_R(x+y)\,dA
=\int_0^2\int_0^4u\left(\frac12\right)\,dv\,du=4.
$$

Notice that the area factor is the Jacobian of the inverse formulas we actually substituted. Using $$\partial(u,v)/\partial(x,y)$$ instead would give the reciprocal factor.

</div>

### The Jacobian measures local stretching

The columns of the derivative matrix describe how small changes in the new coordinates move a point in the original plane. Their determinant is the signed area of the resulting small parallelogram. Taking its magnitude gives the area scale factor. A linear transformation has a constant Jacobian, while polar coordinates stretch more at larger radii.

<div class="theorem-box">

**Example.** In the first quadrant, $$R$$ is bounded by $$xy=1$$, $$xy=4$$, $$x/y=1$$, and $$x/y=9$$. Choose a change of variables and evaluate $$\iint_R(x/y)\,dA$$.

The product and ratio are constant on the boundaries, so choose $$u=\sqrt{xy}$$ and $$v=\sqrt{x/y}$$. Positivity makes these single-valued, and the inverse formulas are especially simple:

$$
x=uv,\qquad y=\frac uv,
\qquad1\le u\le2,\quad1\le v\le3.
$$

Check the inverse by multiplying and dividing: $$xy=u^2$$ and $$x/y=v^2$$. This confirms both the transformed bounds and the transformed integrand. The Jacobian is

$$
\frac{\partial(x,y)}{\partial(u,v)}
=\begin{vmatrix}v&u\\1/v&-u/v^2\end{vmatrix}
=-\frac{2u}v.
$$

Since $$u,v>0$$, its magnitude is $$2u/v$$. Therefore

$$
\iint_R\frac xy\,dA
=\int_1^2\int_1^3v^2\frac{2u}v\,dv\,du
=\left(\int_1^22u\,du\right)\left(\int_1^3v\,dv\right)=12.
$$

The transformation changes orientation, as indicated by the negative determinant, but the scalar integral remains positive. The first-quadrant restriction matters: without it, these new variables would not distinguish points in opposite quadrants, and a single rectangle with this inverse would not cover the entire region.

</div>

When composing substitutions, multiply the Jacobian factors in the same direction as the maps. If you computed the determinant for the reverse map, invert it where nonzero before using it as the area factor for the forward substitution.

---

## Centers of Gravity Using Multiple Integrals

For a finite collection of point masses, the center coordinate is a weighted average: $$\overline x=(\sum x_im_i)/(\sum m_i)$$. A lamina can be approximated by many small pieces, treating each piece as a point mass. Its mass is approximately density times area, $$\delta(x_i,y_i)\Delta A_i$$.

Replacing the two sums in that weighted average by their limiting integrals gives the center-of-mass formulas. A first moment weights each piece by its signed coordinate, so pieces on opposite sides of an axis can balance. Dividing by total mass identifies the single coordinate at which the same total mass would have the same first moment.

For area density $$\delta(x,y)\ge0$$ and positive total mass,

$$
m=\iint_R\delta\,dA,
\qquad
M_x=\iint_Ry\delta\,dA,
\qquad
M_y=\iint_Rx\delta\,dA.
$$

The center of mass is

$$
\overline x=\frac{M_y}{m},\qquad
\overline y=\frac{M_x}{m}.
$$

The subscripts name the axis of the moment: distance from the $$x$$-axis is measured by $$y$$. With constant density, the center of mass is the geometric centroid. Symmetry helps only when both the region and the density share that symmetry.

For volume density $$\delta(x,y,z)$$, use triple integrals:

$$
m=\iiint_E\delta\,dV,\qquad
(\overline x,\overline y,\overline z)
=\frac1m\left(\iiint_E x\delta\,dV,\iiint_E y\delta\,dV,\iiint_E z\delta\,dV\right).
$$

In a uniform gravitational field, the center of gravity agrees with the center of mass.

A moment of inertia weights mass by squared distance from an axis. For a lamina in the $$xy$$-plane,

$$
I_x=\iint_Ry^2\delta\,dA,\qquad
I_y=\iint_Rx^2\delta\,dA,\qquad
I_z=I_x+I_y.
$$

<div class="theorem-box">

**Example.** A lamina occupies the upper unit half-disk with density $$\delta(x,y)=y$$. Find its mass, center of mass, and moment of inertia about the horizontal diameter.

Density is nonnegative here and increases with height. The region is symmetric left-to-right, and density has the same symmetry, so $$\overline x=0$$. Symmetry does not determine the vertical coordinate because the density changes vertically.

Use $$0\le r\le1$$ and $$0\le\theta\le\pi$$. Density becomes $$r\sin\theta$$, and the area element contributes a separate factor of $$r$$:

$$
m=\int_0^\pi\int_0^1r^2\sin\theta\,dr\,d\theta=\frac23.
$$

To find $$\overline y$$, the moment about the horizontal diameter weights mass by an additional $$y$$:

$$
M_x=\iint_Ry\delta\,dA
=\int_0^\pi\int_0^1r^3\sin^2\theta\,dr\,d\theta=\frac\pi8.
$$

Thus $$\overline y=M_x/m=3\pi/16$$. For comparison, a uniform upper half-disk has centroid height $$4/(3\pi)$$; weighting the upper part more heavily raises the height, as expected.

Inertia uses squared distance from the diameter, introducing two factors of $$y$$ in addition to the density factor:

$$
I_x=\iint_Ry^2\delta\,dA
=\int_0^\pi\int_0^1r^4\sin^3\theta\,dr\,d\theta
=\frac15\cdot\frac43=\frac4{15}.
$$

Mass, first moment, and inertia use identical region bounds. Their different physical meanings appear in the extra coordinate factors in the integrand.

</div>

### Mass changes which points receive more weight

A centroid is a geometric average of position. A center of mass is a density-weighted average. Increasing density on one side shifts the center toward that side even if the boundary remains symmetric. A common constant density cancels between every first moment and the total mass, so a uniform lamina's center does not depend on the numerical value of that constant.

<div class="theorem-box">

**Example.** A uniform lamina of density $$\delta_0>0$$ occupies the right triangle $$x\ge0$$, $$y\ge0$$, $$x+y\le a$$. Find its center of mass and moment of inertia about the $$x$$-axis.

The mass is $$m=\delta_0a^2/2$$. The moment used to find the horizontal coordinate is

$$
M_y=\delta_0\int_0^a\int_0^{a-x}x\,dy\,dx
=\frac{\delta_0a^3}6.
$$

The region and density are symmetric under exchanging the coordinates, so $$M_x=M_y$$. Thus $$\overline x=\overline y=a/3$$.

For inertia, squared distance from the $$x$$-axis is $$y^2$$:

$$
I_x=\delta_0\int_0^a\int_0^{a-x}y^2\,dy\,dx
=\frac{\delta_0}3\int_0^a(a-x)^3\,dx
=\frac{\delta_0a^4}{12}.
$$

The center coordinates have units of length, while inertia has units of mass times length squared. These unit checks distinguish a first moment from a moment of inertia even when the integrals look similar.

</div>

---

:::equations
| Idea | Equation or condition |
| --- | --- |
| Area; volume | $$A=\iint_R1\,dA,\quad V=\iiint_E1\,dV$$ |
| Average value | $$f_{\mathrm{avg}}=\iint_Rf\,dA/A(R)$$ |
| Polar area | $$dA=r\,dr\,d\theta$$ |
| Graph surface area | $$dS=\sqrt{1+f_x^2+f_y^2}\,dA$$ |
| Parametric surface area | $$dS=\lVert\mathbf r_u\times\mathbf r_v\rVert\,du\,dv$$ |
| Cylindrical volume | $$dV=r\,dz\,dr\,d\theta$$ |
| Spherical volume | $$dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta,\quad0\le\phi\le\pi$$ |
| Change of variables | $$dA=\lvert\partial(x,y)/\partial(u,v)\rvert\,du\,dv$$ |
| Center of mass | $$\overline x=\int x\,dm/m,\quad\overline y=\int y\,dm/m,\quad\overline z=\int z\,dm/m$$ |
| Lamina inertia | $$I_x=\iint_R y^2\delta\,dA,\quad I_y=\iint_R x^2\delta\,dA,\quad I_z=I_x+I_y$$ |
:::

## Reference

Topic and section order follows Anton, Bivens, and Davis, *Calculus: Early Transcendentals*, 12th edition, Chapter 14, renumbered as Chapter 4 here. Explanations and worked examples on this page are original study notes.
