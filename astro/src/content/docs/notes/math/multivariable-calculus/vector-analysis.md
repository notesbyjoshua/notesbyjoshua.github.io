---
title: "Chapter 5: Topics in Vector Calculus"
description: "Multivariable calculus notes on vector fields, line and surface integrals, conservative fields, flux, Green's theorem, divergence, and Stokes' theorem."
status: developing
progress: 70
sidebar:
  order: 5
---

## Vector Fields

A vector field assigns a vector to every point in a region. In three dimensions, write

$$
\mathbf F(x,y,z)=\langle P(x,y,z),Q(x,y,z),R(x,y,z)\rangle.
$$

For a velocity field, the vector gives the local direction and speed of flow. For a force field, it gives the force at that location. A sketch places arrows at sample points; their direction and length represent the field.

The field $$\langle x,y\rangle$$ points outward from the origin, while $$\langle-y,x\rangle$$ circles it counterclockwise. A gradient field has the form $$\mathbf F=\nabla\phi$$, where $$\phi$$ is a scalar potential.

A radial inverse-square field in space has the form

$$
\mathbf F(\mathbf r)=k\frac{\mathbf r}{\lVert\mathbf r\rVert^3},\qquad\mathbf r\ne\mathbf0.
$$

Its magnitude is $$\lvert k\rvert/\lVert\mathbf r\rVert^2$$. A negative $$k$$ gives attraction toward the origin.

### Divergence and curl

For a field with first partial derivatives, divergence is a scalar:

$$
\nabla\cdot\mathbf F=P_x+Q_y+R_z.
$$

To see why these matching partial derivatives occur, place a tiny rectangular box in the flow. Across its two faces perpendicular to $$x$$, the amount leaving minus the amount entering is approximately $$P_x\,dx\,dy\,dz$$. The other two face pairs contribute $$Q_y\,dx\,dy\,dz$$ and $$R_z\,dx\,dy\,dz$$. Divide the total by the small volume and let the box shrink: the remaining rate is divergence.

Positive divergence indicates more outward than inward flow near the point; negative divergence indicates the opposite. A source here means net local outflow in this mathematical sense. It does not mean that every arrow points directly away from that point.

Curl is a vector:

$$
\nabla\times\mathbf F
=\langle R_y-Q_z,\ P_z-R_x,\ Q_x-P_y\rangle.
$$

Curl comes from a different small measurement: circulation around the edges of a tiny oriented loop, divided by its area. For a horizontal rectangle, the two horizontal edges contribute approximately $$-P_y\,dx\,dy$$ because they are traversed in opposite directions at slightly different heights. The vertical edges contribute $$Q_x\,dx\,dy$$. Their sum explains the vertical curl component $$Q_x-P_y$$. Loops in the other coordinate planes give the other two components.

The direction follows the right-hand rule: its component along a chosen normal measures circulation around a small loop with the compatible positive orientation. A field can follow curved paths without nonzero curl; local circulation depends on how neighboring velocities differ, not merely whether an individual trajectory curves.

For example, $$\mathbf F=\langle-y,x,0\rangle$$ has divergence $$0$$ and curl $$\langle0,0,2\rangle$$. It rotates without producing net local outflow.

For sufficiently smooth functions,

$$
\nabla\times(\nabla\phi)=\mathbf0,
\qquad
\nabla\cdot(\nabla\times\mathbf F)=0.
$$

The identities follow by cancellation of equal mixed partial derivatives.

### Reading local behavior from derivatives

Divergence and curl describe different aspects of a field near a point. They can both vanish, both be nonzero, or behave differently from each other. Neither gives the field's magnitude. A constant nonzero field has zero divergence and zero curl because it has no local expansion or rotation, even though it can transport material across a surface.

<div class="theorem-box">

**Example.** Find the divergence and curl of $$\mathbf F=\langle xy,yz,zx\rangle$$, then evaluate them at $$(1,2,3)$$.

For divergence, differentiate each component with respect to its matching coordinate:

$$
\nabla\cdot\mathbf F=y+z+x.
$$

For curl, use the cross-coordinate derivatives:

$$
\nabla\times\mathbf F
=\langle0-y,0-z,0-x\rangle=\langle-y,-z,-x\rangle.
$$

At the point, the divergence is $$6$$ and the curl is $$\langle-2,-3,-1\rangle$$. The first is a scalar, while the second has a direction as well as magnitude. Their values refer to behavior near that point, not the total flow or circulation over an entire region.

</div>

For an inverse-square field, the denominator has a third power because the numerator already has one power of distance. Taking the magnitude removes that numerator direction and leaves the inverse-square law. This is a useful check before differentiating a radial field.

---

## Line Integrals

There are two different kinds of line integrals to keep separate.

For a wire with varying density, divide its length into short pieces. Each piece has approximate mass equal to its local density times its length. Summing and shrinking the pieces gives a scalar line integral. The curve tells us where the density is sampled; the arc-length element tells us how much wire is represented by a parameter step.

For a smooth curve $$\mathbf r(t)$$, $$a\le t\le b$$, this becomes

$$
\int_C f\,ds
=\int_a^b f(\mathbf r(t))\lVert\mathbf r'(t)\rVert\,dt.
$$

If $$f$$ is linear density, this gives the mass of a wire. With $$f=1$$ it gives length. Reversing the curve's orientation does not change this integral.

Work asks a different question. On a short displacement $$\Delta\mathbf r$$, only the force component along that displacement contributes, giving approximate work $$\mathbf F\cdot\Delta\mathbf r$$. The displacement already includes its direction and length. Substituting $$\Delta\mathbf r\approx\mathbf r'(t)\Delta t$$ produces the vector line integral:

$$
\int_C\mathbf F\cdot d\mathbf r
=\int_a^b\mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt.
$$

For a force field this is work. In components it is $$\int_C P\,dx+Q\,dy+R\,dz$$. Reversing orientation changes its sign. For piecewise smooth curves, add the integrals over the pieces.

<div class="theorem-box">

**Example.** On the quarter-circle $$\mathbf r(t)=\langle2\cos t,2\sin t\rangle$$, $$0\le t\le\pi/2$$, evaluate $$\int_C x\,ds$$ and the work of $$\mathbf F=\langle-y,x\rangle$$.

The speed is $$2$$, so the scalar integral is

$$
\int_0^{\pi/2}(2\cos t)(2)\,dt=4.
$$

For work, $$\mathbf F(\mathbf r(t))=\langle-2\sin t,2\cos t\rangle=\mathbf r'(t)$$. Hence

$$
\int_C\mathbf F\cdot d\mathbf r
=\int_0^{\pi/2}4\,dt=2\pi.
$$

Reversing the path keeps the scalar integral at $$4$$ but changes the work to $$-2\pi$$.

</div>

### Parametrize before substituting

For a vector line integral, replace every coordinate in the field by its parametrized expression, then take the dot product with the derivative of position. Mixing a field evaluated at a general point with a tangent evaluated along the curve leaves an expression that does not describe the stated path.

<div class="theorem-box">

**Example.** Evaluate $$\int_C y\,dx+x\,dy$$ from $$(0,0)$$ to $$(1,1)$$ along the parabola $$y=x^2$$, and compare it with the straight segment between the same endpoints.

For the parabola, use $$\mathbf r(t)=\langle t,t^2\rangle$$, with $$0\le t\le1$$. Then $$dx=dt$$ and $$dy=2t\,dt$$, giving

$$
\int_0^1\left(t^2+t(2t)\right)\,dt
=\int_0^13t^2\,dt=1.
$$

For the segment, use $$\mathbf q(t)=\langle t,t\rangle$$. The work becomes $$\int_0^1( t+t)\,dt=1$$. The equal answers suggest a conservative field, but two agreeing paths alone do not prove path independence. In this case the differential is exactly $$d(xy)$$, which explains why the endpoint values determine the result.

</div>

If a path has corners, give each segment its own parametrization and preserve the order of travel. A line integral over a path followed by its reverse cancels for work, while a scalar arc-length integral counts both traversals.

---

## Independence of Path; Conservative Vector Fields

A field is **conservative** if it has a potential: $$\mathbf F=\nabla\phi$$. On a piecewise smooth path from $$A$$ to $$B$$, the fundamental theorem for line integrals gives

$$
\int_C\nabla\phi\cdot d\mathbf r=\phi(B)-\phi(A).
$$

The reason a potential simplifies work is that it converts a field dotted with a tangent into an ordinary derivative. Along the path, the chain rule gives $$\nabla\phi(\mathbf r(t))\cdot\mathbf r'(t)=d(\phi(\mathbf r(t)))/dt$$. Integrating that derivative telescopes to the final potential minus the initial potential, just as the fundamental theorem of calculus does on an interval.

Path details disappear because every small contribution is a change of the same scalar quantity. A closed trip ends at its starting potential and has zero net work, even if individual portions have nonzero work. To use this theorem, the same potential must be valid along the whole path; finding a local potential on a small region does not automatically settle a path that travels around a domain hole.

On an open connected region, a continuous field is conservative exactly when its line integrals are path independent, equivalently when every closed-path integral is zero. For a field with continuous first partials, being conservative implies zero curl. The reverse implication holds on a simply connected open domain, where loops can be contracted without leaving the domain.

In two dimensions, the curl test reduces to $$P_y=Q_x$$. Check the domain before using this as a sufficient condition.

<div class="theorem-box">

**Example.** Find a potential for $$\mathbf F=\langle2xy+3,x^2+2y\rangle$$ and evaluate its work from $$(0,0)$$ to $$(1,2)$$.

Integrate the first component with respect to $$x$$:

$$
\phi=x^2y+3x+g(y).
$$

The integration term can depend on $$y$$ because it disappears under differentiation with respect to $$x$$. Match the second component:

$$
\phi_y=x^2+g'(y)=x^2+2y.
$$

Thus $$g(y)=y^2+C$$, and a potential is $$\phi=x^2y+3x+y^2$$. The work is $$\phi(1,2)-\phi(0,0)=9$$ along every allowed path.

</div>

### Why the domain matters

The field

$$
\mathbf F=\left\langle\frac{-y}{x^2+y^2},\frac{x}{x^2+y^2}\right\rangle
$$

has $$P_y=Q_x$$ everywhere in its domain, the punctured plane. But around the unit circle $$\mathbf r(t)=\langle\cos t,\sin t\rangle$$,

$$
\int_C\mathbf F\cdot d\mathbf r=\int_0^{2\pi}1\,dt=2\pi.
$$

The field is not conservative on the whole punctured plane. The hole prevents the simply connected version of the curl test from applying.

### Finding a potential in three dimensions

Integrating one component determines a potential only up to a function of the remaining coordinates. Keep that function until the other component equations determine it. Replacing it with a numerical constant too early can make a conservative field appear inconsistent.

<div class="theorem-box">

**Example.** Find a potential for $$\mathbf F=\langle2xz,y^2,x^2\rangle$$ and its work from $$(0,0,0)$$ to $$(1,3,2)$$.

Start with $$\phi_x=2xz$$. Integrating with respect to $$x$$ gives $$\phi=x^2z+g(y,z)$$. Matching the second component requires $$g_y=y^2$$, so

$$
g(y,z)=\frac{y^3}3+h(z).
$$

Finally, $$\phi_z=x^2+h'(z)$$ must equal $$x^2$$. Thus $$h$$ is constant, and a potential is

$$
\phi=x^2z+\frac{y^3}3.
$$

The work is $$\phi(1,3,2)-\phi(0,0,0)=2+9=11$$. A direct gradient check verifies all three components. Because this polynomial potential is defined throughout space, no domain hole complicates the endpoint calculation.

</div>

In mechanics, a potential energy function is often defined with the opposite sign, so force is its negative gradient. The mathematical potential used for the line-integral theorem is defined here by a positive gradient. State which convention is being used before interpreting work as a change in potential energy.

---

## Green's Theorem

Suppose a plane region is divided into many small rectangles. Add the counterclockwise circulation around every rectangle. Each interior edge appears twice, traversed in opposite directions, so its two contributions cancel. Only the circulation around the outer boundary remains, together with any boundaries around holes.

For one tiny rectangle, the circulation is approximately $$(Q_x-P_y)\Delta A$$, by the local curl calculation. Adding those contributions and refining the subdivision gives an area integral. This explains both sides of Green's theorem: local circulation accumulates over area, while internal boundary contributions cancel.

<div class="theorem-box">

**Theorem.** Suppose $$D$$ is a bounded plane region with positively oriented, piecewise smooth boundary $$C$$, and $$P,Q$$ have continuous first partial derivatives on an open set containing $$D$$ and its boundary. Then

$$
\oint_C P\,dx+Q\,dy
=\iint_D(Q_x-P_y)\,dA.
$$

</div>

Positive orientation means the region stays on your left as you follow its boundary. For a region without holes, this is counterclockwise. Around holes, the boundary is clockwise.

```tikz Positive boundary orientation keeps the region on the left, including around a hole
\begin{tikzpicture}[scale=1.05]
\fill[blue!10,even odd rule] (0,0) circle (1.8) (0,0) circle (0.65);
\draw[blue,thick] (0,0) circle (1.8);
\draw[blue,thick] (0,0) circle (0.65);
\draw[->,orange!85!black,very thick] (20:1.8) arc (20:70:1.8);
\draw[->,orange!85!black,very thick] (140:0.65) arc (140:40:0.65);
\node at (0,-1.2) {$D$};
\node at (0,0) {hole};
\node[right] at (2,1.2) {outer: counterclockwise};
\node[right] at (2,0.4) {inner: clockwise};
\end{tikzpicture}
```

Green's theorem also has a flux form. For $$\mathbf F=\langle P,Q\rangle$$ and outward unit normal $$\mathbf n$$,

$$
\oint_C\mathbf F\cdot\mathbf n\,ds
=\oint_C P\,dy-Q\,dx
=\iint_D(P_x+Q_y)\,dA.
$$

The circulation form integrates the tangential component; the flux form integrates the outward normal component. For a positive simple boundary, an area formula is

$$
A(D)=\frac12\oint_C(x\,dy-y\,dx).
$$

<div class="theorem-box">

**Example.** Let $$C$$ be the counterclockwise ellipse $$x^2/4+y^2=1$$. Find $$\oint_C-y\,dx+x\,dy$$.

Here $$Q_x-P_y=1-(-1)=2$$. The ellipse has area $$2\pi$$, so

$$
\oint_C-y\,dx+x\,dy=2A(D)=4\pi.
$$

Clockwise orientation would give $$-4\pi$$.

</div>

Do not apply Green's theorem across a singularity. The punctured-plane field from [Why the domain matters](#why-the-domain-matters) is undefined at the origin, so the theorem cannot be applied to the full disk it surrounds.

### Circulation and outward flux use different derivatives

For a plane field, the circulation form uses the difference of cross partials. The flux form uses the sum of matching partials. Decide which quantity the question asks for before choosing a formula. A field can have positive outward flux and zero circulation around the same boundary.

<div class="theorem-box">

**Example.** Let

$$
\mathbf F=\left\langle-\frac{y}{x^2+y^2}-y^3,
\frac{x}{x^2+y^2}+x^3\right\rangle.
$$

Find its circulation around the positively oriented boundary of the annulus $$1\le x^2+y^2\le4$$, then find its circulation around the outer circle alone, counterclockwise.

The field is undefined at the origin, but the annulus excludes an entire neighborhood of that point. It is smooth on an open set containing the annulus and both boundary circles, so Green's theorem applies there.

The inverse-square-denominator part has scalar curl zero away from the origin. The polynomial part contributes $$3x^2+3y^2$$. The total circulation around the annulus boundary is therefore

$$
\int_0^{2\pi}\int_1^2 3r^2r\,dr\,d\theta
=\frac{45\pi}2.
$$

This boundary includes the inner circle clockwise. To recover the outer integral alone, compute the inner contribution. On the counterclockwise unit circle, the rational part contributes $$2\pi$$. The polynomial part contributes $$\int_0^{2\pi}(\sin^4t+\cos^4t)\,dt=3\pi/2$$, using $$\sin^4t+\cos^4t=1-\tfrac12\sin^2(2t)$$. Clockwise orientation changes their sum to $$-7\pi/2$$.

Thus $$I_{\mathrm{outer}}-7\pi/2=45\pi/2$$, giving $$I_{\mathrm{outer}}=26\pi$$. Applying Green's theorem directly to the full outer disk would miss the rational part's circulation, because that disk includes the singularity. Applying it to the actual annulus is valid and keeps the missing boundary contribution explicit.

</div>

For a region with a hole, include every boundary component with the positive orientation relative to the region. The integral over the outer curve alone is not generally equal to the integral of curl over the remaining region. The inner boundary accounts for the part removed, with its clockwise orientation producing the needed sign.

---

## Surface Integrals

A thin shell is spread over a surface rather than a plane region. Its mass still comes from adding density times small patch area, but the area is measured along the tilted or curved shell. First evaluate the density at the point of the shell, then use the surface-area element derived in Chapter 4.

The scalar being accumulated and the area stretching are separate parts of the setup. Changing the surface may change both: the density's coordinate values change, and a unit area in the parameter plane can correspond to a larger patch of shell.

For a regular parametrization $$\mathbf r(u,v)$$ covering $$S$$ once,

$$
\iint_S f\,dS
=\iint_D f(\mathbf r(u,v))\lVert\mathbf r_u\times\mathbf r_v\rVert\,du\,dv.
$$

Use it for quantities such as the mass of a thin shell with area density $$f$$. For $$f=1$$, it gives the surface area. Orientation does not affect a scalar surface integral.

For a graph $$z=g(x,y)$$,

$$
\iint_S f\,dS
=\iint_D f(x,y,g(x,y))\sqrt{1+g_x^2+g_y^2}\,dA.
$$

<div class="theorem-box">

**Example.** A shell is the patch $$z=x+y$$ above $$0\le x,y\le1$$, with area density $$\delta=z+1$$. Find its mass.

The surface factor is $$\sqrt3$$ and the density becomes $$x+y+1$$. Thus

$$
m=\sqrt3\int_0^1\int_0^1(x+y+1)\,dy\,dx=2\sqrt3.
$$

Using only the projected area would miss the factor $$\sqrt3$$.

</div>

### Matching the area element to the surface

A surface integral has two substitutions: evaluate the scalar quantity on the surface, and replace surface area by the appropriate parameter-area factor. A graph formula and a parametric formula describe the same geometry, but their integration domains and area factors belong to different coordinate descriptions.

<div class="theorem-box">

**Example.** Find the mass of the spherical shell $$x^2+y^2+z^2=a^2$$ with area density $$\delta=z^2$$, where $$a>0$$.

Use spherical surface parameters with fixed radius:

$$
\mathbf r(\phi,\theta)
=\langle a\sin\phi\cos\theta,a\sin\phi\sin\theta,a\cos\phi\rangle.
$$

The area factor is $$a^2\sin\phi$$, while the density becomes $$a^2\cos^2\phi$$. Hence

$$
m=\int_0^{2\pi}\int_0^\pi
 a^4\cos^2\phi\sin\phi\,d\phi\,d\theta
=\frac{4\pi a^4}3.
$$

The substitution $$u=\cos\phi$$ evaluates the inner integral. The density is largest near the poles and zero at the equator, so multiplying the total area by a single point's density would not work. Symmetry does show that the center of mass is the origin, even though the density is not constant.

</div>

---

## Applications of Surface Integrals; Flux

Imagine fluid crossing a small flat window. Motion parallel to the window carries fluid along it without crossing. Motion normal to it crosses most efficiently. If the local velocity is $$\mathbf F$$ and the chosen unit normal is $$\mathbf n$$, the signed crossing speed is the scalar projection $$\mathbf F\cdot\mathbf n$$.

Over a short time $$dt$$, the volume passing through a small patch of area $$\Delta S$$ is approximately $$(\mathbf F\cdot\mathbf n)\Delta S\,dt$$. Divide by time, add the patches, and take a limit. This gives the flux integral

$$
\iint_S\mathbf F\cdot\mathbf n\,dS.
$$

Here $$\mathbf n$$ is the chosen unit normal. Positive flux means flow in the chosen normal direction; negative flux means flow opposite it. For a velocity field, the integral gives volume flow rate.

For a parametrized surface, the vector area element combines the normal and area factor:

$$
\mathbf n\,dS=\pm(\mathbf r_u\times\mathbf r_v)\,du\,dv.
$$

Choose the sign to match the requested orientation. You do not need to normalize the cross product because its magnitude already supplies the area factor.

For an upward-oriented graph $$z=g(x,y)$$,

$$
\mathbf n\,dS=\langle-g_x,-g_y,1\rangle\,dA.
$$

For downward orientation, negate this vector. A surface needs a consistent choice of normal to define flux globally. The usual formulas apply to orientable, piecewise smooth surfaces.

<div class="theorem-box">

**Example.** Find the upward flux of $$\mathbf F=\langle0,0,z\rangle$$ through $$z=4-x^2-y^2$$ above the disk $$x^2+y^2\le4$$.

An upward vector area element is $$\langle2x,2y,1\rangle\,dA$$. On the surface,

$$
\mathbf F\cdot\langle2x,2y,1\rangle=4-x^2-y^2.
$$

Thus

$$
\iint_S\mathbf F\cdot\mathbf n\,dS
=\int_0^{2\pi}\int_0^2(4-r^2)r\,dr\,d\theta=8\pi.
$$

</div>

### Choosing the normal sign

An orientation is a choice attached to the whole surface. For a graph, check the vertical component of the cross product; for a cylinder or sphere, check whether it points toward or away from the axis or center. One sample point often determines the sign for a connected regular patch, provided the chosen normal varies continuously.

<div class="theorem-box">

**Example.** Find the outward flux of $$\mathbf F=\langle xz,yz,z\rangle$$ through the curved cone $$z=\sqrt{x^2+y^2}$$ for $$0\le z\le2$$. Orient it outward from the solid inside the cone and below $$z=2$$.

Parametrize the surface by $$\mathbf r(r,\theta)=\langle r\cos\theta,r\sin\theta,r\rangle$$, with $$0\le r\le2$$ and one full turn of $$\theta$$. The cross product in parameter order is

$$
\mathbf r_r\times\mathbf r_\theta
=\langle-r\cos\theta,-r\sin\theta,r\rangle.
$$

This points toward the cone's interior, as its radial components point toward the axis. Reverse it to obtain the outward vector area factor $$\langle r\cos\theta,r\sin\theta,-r\rangle$$. A zero cross product at the single vertex does not affect this piecewise surface integral.

On the cone, the field is $$\langle r^2\cos\theta,r^2\sin\theta,r\rangle$$. Its dot product with the outward area factor is $$r^3-r^2$$, giving

$$
\text{flux}=\int_0^{2\pi}\int_0^2(r^3-r^2)\,dr\,d\theta
=\frac{8\pi}3.
$$

The integrand is negative below $$r=1$$ and positive above it. The chosen outward normal has a downward component, so upward flow can contribute negatively even when the horizontal components point outward. The net result combines both effects.

After studying the divergence theorem, this can be checked by adding the top disk. The divergence is $$2z+1$$, so the closed-cone flux is $$\int_0^2(2z+1)\pi z^2\,dz=32\pi/3$$. The top disk contributes $$8\pi$$, leaving $$8\pi/3$$ for the side.

</div>

Do not multiply by an additional surface-area factor after using the cross product as the vector area element. Its length already contains that factor. Using a unit normal instead is equally valid, but then the scalar area element must be supplied separately.

---

## The Divergence Theorem

The local box interpretation of divergence extends to a whole solid by cancellation. Divide the solid into small boxes and add their outward fluxes. A shared face is outward from one box and inward from its neighbor, so those contributions cancel. The surviving faces approximate the solid's outer boundary.

Inside each box, divergence times volume approximates its net outward flux. The sum of those local measurements becomes a volume integral. The divergence theorem therefore connects an accumulation of local outflow within a solid to the net flow across the boundary enclosing it.

<div class="theorem-box">

**Theorem.** Let $$E$$ be a bounded solid with piecewise smooth closed boundary $$\partial E$$ oriented outward. If $$\mathbf F$$ has continuous first partial derivatives on an open set containing $$E$$ and its boundary, then

$$
\iint_{\partial E}\mathbf F\cdot\mathbf n\,dS
=\iiint_E\nabla\cdot\mathbf F\,dV.
$$

</div>

Interior flux cancels between adjacent small pieces: flow leaving one piece enters the next. Only the outer boundary remains. This explains why divergence measures local net outward flow.

The surface must be closed. For an open surface, add a cap to make a closed boundary, apply the theorem, then subtract the cap's flux with its outward orientation.

<div class="theorem-box">

**Example.** Find the outward flux of $$\mathbf F=\langle x,y,z\rangle$$ through the sphere $$x^2+y^2+z^2=a^2$$, where $$a>0$$.

The divergence is $$3$$. Therefore

$$
\iint_S\mathbf F\cdot\mathbf n\,dS
=3\left(\frac43\pi a^3\right)=4\pi a^3.
$$

As a direct check, $$\mathbf F=a\mathbf n$$ on the sphere, so the flux is $$a$$ times the surface area $$4\pi a^2$$.

</div>

A field singular inside the solid does not satisfy the theorem's hypotheses. Remove the singular region and include its new boundary before applying the theorem.

### Closing an open surface with a cap

The divergence theorem applies to the whole boundary of a solid. If the requested surface is only part of that boundary, make the subtraction explicit. The cap's outward normal is determined by the enclosed solid, which may be opposite to the direction that first looks convenient in the picture.

<div class="theorem-box">

**Example.** Find the outward flux of $$\mathbf F=\langle x,y,z^2\rangle$$ through the paraboloid patch $$z=4-x^2-y^2$$ with $$z\ge1$$, outward from the solid below that patch and above $$z=1$$.

Close the patch with the disk at $$z=1$$. Its radius is $$\sqrt3$$ because that plane meets the paraboloid where $$x^2+y^2=3$$. The outward direction on the curved patch is upward, while the bottom disk points downward.

The divergence is $$2+2z$$. Horizontal slices of the solid have area $$\pi(4-z)$$, so the total closed-surface flux is

$$
\iiint_E(2+2z)\,dV
=\pi\int_1^4(2+2z)(4-z)\,dz
=27\pi.
$$

On the bottom disk, $$\mathbf F\cdot\mathbf n=-z^2=-1$$, giving cap flux $$-3\pi$$. Thus the requested curved-patch flux is $$27\pi-(-3\pi)=30\pi$$.

To check directly, the upward vector area factor is $$\langle2x,2y,1\rangle$$. On the patch its dot product with the field is $$2(x^2+y^2)+(4-x^2-y^2)^2$$. Polar integration gives

$$
2\pi\int_0^{\sqrt3}\left(2r^2+(4-r^2)^2\right)r\,dr=30\pi.
$$

Both approaches require the same geometry, but the divergence route reduces the field differentiation and the integral to a single height variable. The cap subtraction is essential: the theorem first gives flux through the whole closed boundary.

</div>

For a solid with an internal cavity, the outward normal on the cavity wall points into the cavity. It points away from the material of the solid, even though it points toward the cavity's center. This is the three-dimensional counterpart of clockwise orientation around a hole in Green's theorem.

---

## Stokes' Theorem

Green's theorem used small loops lying in a plane. A curved surface can also be divided into small oriented patches, each approximately flat. Curl dotted with the patch normal measures local circulation per unit area in that patch's plane. Adding the patch circulations cancels every shared edge when neighboring orientations agree, leaving only the surface boundary.

This is why a surface integral of curl can replace a line integral around a space curve. The compatible orientation is part of the cancellation: reversing a patch alone would make its shared edges reinforce instead of cancel. Stokes' theorem gives the precise relation.

<div class="theorem-box">

**Theorem.** Let $$S$$ be an oriented, piecewise smooth surface with boundary $$C$$. If $$\mathbf F$$ has continuous first partial derivatives on an open set containing $$S$$, then

$$
\oint_C\mathbf F\cdot d\mathbf r
=\iint_S(\nabla\times\mathbf F)\cdot\mathbf n\,dS,
$$

where the boundary direction matches the surface normal by the right-hand rule.

</div>

Curl measures circulation per unit area in the small-patch limit. As with divergence, contributions along internal boundaries cancel when patches are joined.

For a horizontal disk with upward normal, its boundary runs counterclockwise viewed from above. Reversing the normal reverses the induced boundary direction. When choosing another spanning surface, preserve the boundary and its orientation, and check that the field is smooth on the replacement surface.

<div class="theorem-box">

**Example.** Find the circulation of $$\mathbf F=\langle-y,x,z\rangle$$ around the circle $$x^2+y^2=4$$ in $$z=3$$, counterclockwise viewed from above.

Choose the flat disk in $$z=3$$ with upward normal. Since

$$
\nabla\times\mathbf F=\langle0,0,2\rangle,
$$

the circulation is

$$
\iint_D2\,dA=2(4\pi)=8\pi.
$$

The $$z$$-component of the original field contributes no work along this horizontal boundary.

</div>

:::strategy
For work on an open path, check for a potential first. For circulation around a plane boundary, consider Green's theorem; for a space boundary, consider Stokes' theorem. For flux through a closed surface, consider the divergence theorem. Before calculating, check the domain, boundary, and orientation required by the theorem.
:::

### Choosing a convenient spanning surface

Stokes' theorem allows the spanning surface to change because the circulation is tied to its oriented boundary. A curved surface can often be replaced by a flat disk or triangle with a simpler normal. The replacement still needs to lie in a region where the field is sufficiently smooth.

<div class="theorem-box">

**Example.** The curve $$C$$ is the intersection of the paraboloid $$z=x^2+y^2$$ with the plane $$z=2+x$$. For $$\mathbf F=\langle-yz,xz,xy\rangle$$, find the circulation around $$C$$ clockwise as viewed from above.

The curve is the boundary of a patch of the paraboloid, but the flat plane patch has a simpler normal. First find its projection by equating the heights:

$$
x^2+y^2=2+x
\quad\Longrightarrow\quad
\left(x-\frac12\right)^2+y^2=\frac94.
$$

The projected region is a disk centered at $$(1/2,0)$$ with area $$9\pi/4$$. For the plane graph $$z=2+x$$, the upward vector area factor is $$\langle-1,0,1\rangle\,dA$$. That normal induces counterclockwise orientation from above, so we will negate the resulting integral to match the requested direction.

The curl is

$$
\nabla\times\mathbf F
=\langle0,-2y,2z\rangle.
$$

Its dot product with the upward factor is $$2z=4+2x$$ on the plane. By symmetry about $$x=1/2$$, the average of $$x$$ over the disk is $$1/2$$. Thus the upward-oriented surface integral is $$5(9\pi/4)=45\pi/4$$. For the clockwise boundary, the answer is

$$
\oint_C\mathbf F\cdot d\mathbf r=-\frac{45\pi}4.
$$

The replacement surface has the same geometric boundary and lies in a region where the polynomial field is smooth. Those facts permit the replacement; matching the orientation determines the sign. The original curve need not be parametrized to perform this calculation.

</div>

---

:::equations
| Idea | Equation or condition |
| --- | --- |
| Divergence | $$\nabla\cdot\mathbf F=P_x+Q_y+R_z$$ |
| Curl | $$\nabla\times\mathbf F=\langle R_y-Q_z,P_z-R_x,Q_x-P_y\rangle$$ |
| Scalar line integral | $$\int_C f\,ds=\int_a^b f(\mathbf r(t))\lVert\mathbf r'(t)\rVert\,dt$$ |
| Work | $$\int_C\mathbf F\cdot d\mathbf r=\int_a^b\mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt$$ |
| Potential theorem | $$\int_A^B\nabla\phi\cdot d\mathbf r=\phi(B)-\phi(A)$$ |
| Green, positive boundary | $$\oint_C P\,dx+Q\,dy=\iint_D(Q_x-P_y)\,dA$$ |
| Green, outward flux | $$\oint_C P\,dy-Q\,dx=\iint_D(P_x+Q_y)\,dA$$ |
| Surface area element | $$dS=\lVert\mathbf r_u\times\mathbf r_v\rVert\,du\,dv$$ |
| Oriented surface element | $$\mathbf n\,dS=\pm(\mathbf r_u\times\mathbf r_v)\,du\,dv$$ |
| Divergence, closed outward boundary | $$\iint_{\partial E}\mathbf F\cdot\mathbf n\,dS=\iiint_E\nabla\cdot\mathbf F\,dV$$ |
| Stokes, compatible orientations | $$\oint_{\partial S}\mathbf F\cdot d\mathbf r=\iint_S(\nabla\times\mathbf F)\cdot\mathbf n\,dS$$ |

The integral theorems require the smoothness and domain conditions stated in their sections.
:::

## Reference

Topic and section order follows Anton, Bivens, and Davis, *Calculus: Early Transcendentals*, 12th edition, Chapter 15, renumbered as Chapter 5 here. Explanations and worked examples on this page are original study notes.
