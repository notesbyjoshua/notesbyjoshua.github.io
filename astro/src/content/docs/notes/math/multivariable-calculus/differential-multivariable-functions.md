---
title: "Chapter 3: Partial Derivatives"
description: "Multivariable calculus notes on limits, partial derivatives, linearization, the chain rule, gradients, tangent planes, and constrained optimization."
status: developing
progress: 70
sidebar:
  order: 3
---

## Functions of Two or More Variables

A function $$z=f(x,y)$$ assigns one output to each allowed input pair. Its **domain** is a region in the input plane; its **graph** is a surface in three-dimensional space. These are different objects.

Find the domain by applying every restriction at once. Square roots require nonnegative radicands, logarithms require positive arguments, and denominators cannot vanish.

<div class="theorem-box">

**Example.** Find the domain of $$f(x,y)=\sqrt{9-x^2-y^2}/(y-1)$$.

The square root requires $$x^2+y^2\le9$$, and the denominator requires $$y\ne1$$. Thus the domain is the closed disk of radius $$3$$ with the portion of the line $$y=1$$ removed:

$$
D=\{(x,y):x^2+y^2\le9,\ y\ne1\}.
$$

The circular boundary belongs to the domain except at the two removed points where $$y=1$$.

</div>

A **level curve** $$f(x,y)=c$$ joins input points with the same output. It is the projection of a horizontal trace of the graph onto the input plane. For $$f=x^2+y^2$$, positive levels are circles of radius $$\sqrt c$$. Equal increases in height give smaller radial gaps as the circles move outward, reflecting a steeper surface.

For a function of three variables, $$w=f(x,y,z)$$, the input is a point in space. A level set $$f(x,y,z)=c$$ is usually a surface. We use level surfaces because the full graph would require four dimensions.

### Domain, range, and level sets

The domain contains allowed inputs; the range contains outputs that actually occur. A restriction on the inputs can change the range even when the formula stays the same. For example, squared distance takes every nonnegative value on the full plane, but only values from zero to one on the unit disk.

<div class="theorem-box">

**Example.** For $$f(x,y)=\ln(4-x^2-y^2)$$, find the domain, range, and level curve corresponding to output $$c$$.

The logarithm requires $$x^2+y^2<4$$, so the domain is the open disk of radius $$2$$. Its argument is at most $$4$$ and approaches zero near the boundary. Thus the range is $$(-\infty,\ln4]$$.

To find a level curve, solve

$$
\ln(4-x^2-y^2)=c
\quad\Longrightarrow\quad
x^2+y^2=4-e^c.
$$

For $$c<\ln4$$, this is a circle. At $$c=\ln4$$, it reduces to the origin. For larger $$c$$, it is empty. The largest value occurs at the center, and the function decreases without bound near the circular boundary.

</div>

---

## Limits and Continuity

The statement

$$
\lim_{(x,y)\to(a,b)}f(x,y)=L
$$

means the output approaches $$L$$ whenever an input in the domain approaches $$(a,b)$$ from any direction or along any path. More precisely, for every $$\varepsilon>0$$ there must be a $$\delta>0$$ such that

$$
0<\sqrt{(x-a)^2+(y-b)^2}<\delta
\quad\Longrightarrow\quad
\lvert f(x,y)-L\rvert<\varepsilon.
$$

Two paths giving different limits prove that a limit does not exist. Agreement along several paths does not prove existence; another path may behave differently.

<div class="theorem-box">

**Example.** Determine whether $$xy/(x^2+y^2)$$ has a limit at the origin.

Along $$y=0$$,

$$
\lim_{x\to0}\frac{x(0)}{x^2}=0.
$$

Along $$y=x$$,

$$
\lim_{x\to0}\frac{x^2}{2x^2}=\frac12.
$$

The limits differ, so the two-variable limit does not exist.

</div>

To prove a limit exists, look for a bound depending only on the distance to the target. Polar coordinates often help at the origin, but the bound must work for every angle, including angles that vary with radius.

For instance, away from the origin,

$$
\left\lvert\frac{x^2y}{x^2+y^2}\right\rvert
\le\lvert y\rvert\le\sqrt{x^2+y^2}.
$$

The right side approaches zero, so the squeeze theorem gives

$$
\lim_{(x,y)\to(0,0)}\frac{x^2y}{x^2+y^2}=0.
$$

A function is continuous at a point if its value exists and equals its limit there. Polynomials are continuous everywhere; quotients, roots, logarithms, and compositions are continuous wherever their usual domain conditions hold.

### When straight paths miss the problem

Testing paths is a way to disprove a limit. It is not a list of conditions that eventually proves one. Even every straight line through a point can miss behavior concentrated near a curved path. A bound that holds throughout a neighborhood is stronger because it controls all paths at once.

<div class="theorem-box">

**Example.** Determine whether $$f(x,y)=x^2y/(x^4+y^2)$$ has a limit at the origin, and explain what happens along straight lines.

Along $$y=mx$$ with fixed nonzero $$m$$,

$$
\lim_{x\to0}\frac{mx^3}{x^4+m^2x^2}
=\lim_{x\to0}\frac{mx}{x^2+m^2}=0.
$$

The horizontal and vertical axes also give zero. However, the denominator suggests balancing $$x^4$$ against $$y^2$$, so try $$y=x^2$$:

$$
\lim_{x\to0}\frac{x^4}{2x^4}=\frac12.
$$

Therefore the limit does not exist. The curved path keeps the two denominator terms comparable, while a fixed nonhorizontal line makes the $$y^2$$ term dominate near the origin.

</div>

When direct substitution works by continuity, use it. Path analysis is needed at points where the expression is undefined or continuity is uncertain, not for every multivariable limit.

---

## Partial Derivatives

With two independent inputs, there is no single slope until we say how the input point moves. If we increase $$x$$ while holding $$y=b$$, the surface reduces to the ordinary curve $$z=f(x,b)$$. Its derivative is one useful slope. Holding $$x=a$$ instead gives another trace and another slope.

These coordinate-direction measurements are the partial derivatives. They use the familiar difference quotient, with the fixed coordinate written explicitly:

$$
f_x(a,b)=\lim_{h\to0}\frac{f(a+h,b)-f(a,b)}h,
\qquad
f_y(a,b)=\lim_{h\to0}\frac{f(a,b+h)-f(a,b)}h.
$$

Geometrically, these are slopes of coordinate-direction traces through the surface. Compute them with ordinary derivative rules, treating the other inputs as constants.

For $$f(x,y)=x^2e^y+\sin(xy)$$,

$$
f_x=2xe^y+y\cos(xy),
\qquad
f_y=x^2e^y+x\cos(xy).
$$

Differentiate again to obtain higher partials. We use $$f_{xy}=(f_x)_y$$. If the mixed second partials are continuous in a neighborhood of the point, then

$$
f_{xy}=f_{yx}.
$$

For an implicit equation $$F(x,y,z)=0$$ that locally defines a differentiable function $$z=z(x,y)$$ with $$F_z\ne0$$,

$$
z_x=-\frac{F_x}{F_z},\qquad z_y=-\frac{F_y}{F_z}.
$$

:::warning
The existence of $$f_x$$ and $$f_y$$ at a point does not by itself imply continuity or differentiability there. Partial derivatives only test two directions.
:::

### Differentiating with the other input fixed

Holding an input constant does not mean deleting it. A factor involving that input remains as a constant multiplier, and a product inside a composite function still requires the chain rule. For example, differentiating an exponential involving a product brings down the fixed input when differentiating with respect to the other one.

<div class="theorem-box">

**Example.** For $$f(x,y)=x^2y+e^{xy}$$, find the first partials and verify equality of the mixed second partials.

Treating $$y$$ as fixed gives $$f_x=2xy+ye^{xy}$$. Treating $$x$$ as fixed gives $$f_y=x^2+xe^{xy}$$. Now differentiate each with respect to the other variable:

$$
f_{xy}=2x+e^{xy}+xye^{xy},
\qquad
f_{yx}=2x+e^{xy}+xye^{xy}.
$$

Both calculations give $$2x+(1+xy)e^{xy}$$. The extra exponential term comes from differentiating the multiplier as well as the exponential. Forgetting that product rule is a common source of apparently unequal mixed partials.

</div>

In applications, the variables held fixed are part of the meaning of a partial derivative. A temperature rate measured while pressure stays fixed need not agree with the rate measured while volume stays fixed. Always identify the independent inputs before interpreting the derivative.

---

## Differentiability, Differentials, and Local Linearity

In one variable, differentiability means a tangent line gives the correct first-order change near the point. For two inputs, the corresponding approximation is a plane. Its predicted height change must combine the $$x$$-change and $$y$$-change consistently, even when both happen at once.

If the plane has coordinate slopes $$f_x(a,b)$$ and $$f_y(a,b)$$, it predicts a change of $$f_x(a,b)h+f_y(a,b)k$$ for displacement $$\langle h,k\rangle$$. There may be an error, but that error must become negligible compared with the distance moved. Merely tending to zero would establish only continuity; differentiability asks the stronger question of whether a linear approximation captures the leading change.

At $$(a,b)$$, express this as

$$
f(a+h,b+k)=f(a,b)+f_x(a,b)h+f_y(a,b)k+R(h,k),
$$

where differentiability requires

$$
\lim_{(h,k)\to(0,0)}\frac{R(h,k)}{\sqrt{h^2+k^2}}=0.
$$

The remainder must become small relative to the input displacement. Continuous first partial derivatives near a point are a sufficient condition for differentiability there.

The local linear approximation is

$$
L(x,y)=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b).
$$

The differential $$df=f_x\,dx+f_y\,dy$$ estimates the actual change $$\Delta f$$ for small input changes. The differential is linear in the changes; the actual change generally includes higher-order terms.

<div class="theorem-box">

**Example.** Use linearization at $$(3,4)$$ to estimate $$\sqrt{3.02^2+3.97^2}$$.

For $$f(x,y)=\sqrt{x^2+y^2}$$, the value at $$(3,4)$$ is $$5$$ and the partial derivatives there are $$3/5$$ and $$4/5$$. Thus

$$
f(3.02,3.97)\approx5+\frac35(0.02)+\frac45(-0.03)=4.988.
$$

The negative estimated change agrees with the larger decrease in the $$y$$-coordinate.

</div>

### Estimating measurement error

Linearization is useful when input changes are known but evaluating the original function repeatedly is inconvenient. It also estimates how measurement errors affect an output. For a worst-case first-order estimate, add the magnitudes of the individual differential contributions; do not rely on cancellation unless the error directions are known.

<div class="theorem-box">

**Example.** A cylinder has radius $$r=5$$ and height $$h=10$$, measured with possible errors of at most $$0.02$$ and $$0.05$$ respectively. Estimate the largest relative error in its volume.

For $$V=\pi r^2h$$,

$$
dV=2\pi rh\,dr+\pi r^2\,dh.
$$

Divide by the nominal volume:

$$
\frac{dV}{V}=2\frac{dr}{r}+\frac{dh}{h}.
$$

Using the maximum error magnitudes gives $$2(0.02/5)+0.05/10=0.013$$, or about $$1.3\%$$. Radius error counts twice in the relative estimate because the radius is squared. This is a first-order estimate, so the small products and squares of the errors are omitted.

</div>

Differentiability guarantees that the approximation error is small relative to input distance sufficiently near the base point. It does not provide a useful numerical error bound at an arbitrary distance. Use a nearby base point with easy values and check whether the proposed changes are small on the scale of the inputs.

### Partial derivatives can exist without a linear approximation

The partial derivatives only measure the coordinate traces. To test whether they support a genuine linearization, the approximation must also work on paths between those traces.

<div class="theorem-box">

**Example.** For $$\alpha>0$$, define

$$
f_\alpha(x,y)=\begin{cases}
\dfrac{\lvert xy\rvert^\alpha}{x^2+y^2},&(x,y)\ne(0,0),\\
0,&(x,y)=(0,0).
\end{cases}
$$

Determine exactly when this function is continuous and differentiable at the origin, and find its partial derivatives there.

Both axis traces are zero, so $$f_x(0,0)=f_y(0,0)=0$$ for every positive $$\alpha$$. Those derivatives alone do not settle either of the other questions.

Let $$r=\sqrt{x^2+y^2}$$. The inequality $$2\lvert xy\rvert\le x^2+y^2$$ follows from $$(\lvert x\rvert-\lvert y\rvert)^2\ge0$$. It gives a bound valid in every direction:

$$
0\le f_\alpha(x,y)\le2^{-\alpha}r^{2\alpha-2}.
$$

The right side tends to zero if $$\alpha>1$$, proving continuity in that range. Along $$y=x\ne0$$, the function is exactly $$\tfrac12\lvert x\rvert^{2\alpha-2}$$. At $$\alpha=1$$ this stays at $$1/2$$, and for smaller $$\alpha$$ it grows without bound. Continuity therefore holds exactly for $$\alpha>1$$.

Since the candidate derivative is zero, differentiability asks whether $$f_\alpha/r\to0$$. The same bound becomes

$$
0\le\frac{f_\alpha(x,y)}r\le2^{-\alpha}r^{2\alpha-3}.
$$

This tends to zero if $$\alpha>3/2$$. The diagonal again proves necessity: the ratio there is $$\lvert x\rvert^{2\alpha-3}/(2\sqrt2)$$, which does not tend to zero at or below that threshold.

Thus partial derivatives exist for every positive $$\alpha$$, continuity requires $$\alpha>1$$, and differentiability requires $$\alpha>3/2$$. The interval between those last two thresholds gives continuous surfaces whose errors still decay too slowly for a tangent plane to give the correct linear approximation.

</div>

---

## The Chain Rule

Suppose a moving point crosses a temperature map. Its temperature can change because it moves east, because it moves north, or because of both motions together. A partial derivative gives change per unit motion along one axis, while the derivative of that coordinate gives how much motion occurs per unit time. Multiplying those rates gives that axis's contribution to temperature change per unit time.

The local linear approximation makes this precise. Over a short time, the input changes are approximately $$x'(t)\Delta t$$ and $$y'(t)\Delta t$$. Substitute them into $$\Delta z\approx f_x\Delta x+f_y\Delta y$$, divide by $$\Delta t$$, and take a limit. With differentiability of the outer function and of the two coordinate functions, the approximation error disappears, leaving

$$
\frac{dz}{dt}=f_x\frac{dx}{dt}+f_y\frac{dy}{dt}.
$$

Evaluate the partial derivatives at the current input $$(x(t),y(t))$$. With three intermediate inputs, include the third term $$f_z\,dz/dt$$ in the derivative of the outer function.

If $$x=x(u,v)$$ and $$y=y(u,v)$$, then

$$
\frac{\partial z}{\partial u}=f_x\,x_u+f_y\,y_u,
\qquad
\frac{\partial z}{\partial v}=f_x\,x_v+f_y\,y_v.
$$

The products here mean $$f_x\cdot x_u$$ and $$f_y\cdot y_u$$, not higher derivatives. A dependency diagram can help: multiply derivatives along each route from the outer output to the chosen input, then add the routes.

<div class="theorem-box">

**Example.** Let $$z=x^2y$$, $$x=t^2$$, and $$y=e^t$$. Find $$dz/dt$$.

Since $$f_x=2xy$$ and $$f_y=x^2$$,

$$
\frac{dz}{dt}=(2xy)(2t)+(x^2)e^t
=4t^3e^t+t^4e^t.
$$

Directly substituting first gives $$z=t^4e^t$$, which has the same derivative.

</div>

Implicit differentiation is another chain-rule application. If $$F(x,y(x))=0$$ and $$F_y\ne0$$, then $$F_x+F_yy'=0$$, so $$y'=-F_x/F_y$$.

### Partial versus total change

A partial derivative measures what happens when one independent input changes alone. A total derivative along a path includes every input change caused by the path parameter. The symbols look similar, but the questions differ. A quantity can decrease with one input held fixed while increasing along a path where several inputs change together.

<div class="theorem-box">

**Example.** Near $$(1,1,1)$$, the equation $$x^2+y^2+z^2+xyz=4$$ defines $$z=z(x,y)$$. Find its tangent plane and its second partial derivatives at that point. Then estimate $$z(1+t,1-t)$$ through quadratic order for small $$t$$.

Set $$F=x^2+y^2+z^2+xyz-4$$. At the point, $$F_z=2z+xy=3\ne0$$, so a smooth local graph exists. Implicit first differentiation gives $$z_x=-F_x/F_z=-1$$ and $$z_y=-1$$. The tangent plane is therefore $$z-1=-(x-1)-(y-1)$$, or $$x+y+z=3$$.

For second derivatives, the coefficients themselves change with $$z(x,y)$$. Differentiate $$F_x+F_zz_x=0$$ with respect to $$x$$, remembering that both terms are compositions:

$$
F_{xx}+2F_{xz}z_x+F_{zz}z_x^2+F_zz_{xx}=0.
$$

Here $$F_{xx}=F_{zz}=2$$ and $$F_{xz}=1$$ at the point. Thus $$2-2+2+3z_{xx}=0$$, giving $$z_{xx}=-2/3$$. Symmetry gives $$z_{yy}=-2/3$$. Differentiating the same first-derivative equation with respect to $$y$$ gives

$$
F_{xy}+F_{xz}z_y+F_{yz}z_x+F_{zz}z_xz_y+F_zz_{xy}=0.
$$

Its values yield $$1-1-1+2+3z_{xy}=0$$, so $$z_{xy}=-1/3$$.

Along $$x=1+t,y=1-t$$, the linear changes cancel. The quadratic part is

$$
\frac12\left(-\frac23t^2+2\left(-\frac13\right)t(-t)-\frac23t^2\right)
=-\frac13t^2.
$$

Hence $$z(1+t,1-t)=1-t^2/3+o(t^2)$$. The tangent plane predicts no change along this direction, but the second derivatives reveal a downward bend. The notation $$o(t^2)$$ means the remaining error divided by $$t^2$$ tends to zero.

</div>

---

## Directional Derivatives and Gradients

The partial derivatives tell us the change rates along the coordinate axes, but most paths do not follow just one axis. A small displacement $$\mathbf h$$ produces the first-order change $$f_xh_1+f_yh_2$$. This is a dot product between the displacement and the vector of partial derivatives.

We call that vector the gradient. It stores the entire linear response to displacement at a point, not just a preferred direction:

$$
\nabla f=\langle f_x,f_y\rangle
\quad\text{or}\quad
\nabla f=\langle f_x,f_y,f_z\rangle.
$$

For a unit vector $$\mathbf u$$, the directional derivative measures change per unit distance in that direction. If $$f$$ is differentiable,

$$
D_{\mathbf u}f=\nabla f\cdot\mathbf u.
$$

Normalize a supplied direction vector first. Otherwise the dot product also includes its length.

The geometric dot-product formula now explains steepest ascent. For a unit direction $$\mathbf u$$ making angle $$\theta$$ with the gradient, $$D_{\mathbf u}f=\lVert\nabla f\rVert\cos\theta$$. Turning toward the gradient increases the rate because more of the displacement aligns with the function's linear response. Turning perpendicular to it removes the first-order change.

Consequently, the maximum directional derivative is $$\lVert\nabla f\rVert$$, attained in the gradient direction when the gradient is nonzero. The minimum is $$-\lVert\nabla f\rVert$$, in the opposite direction. At a zero gradient, all directional derivatives of a differentiable function are zero, but the point need not be a maximum or minimum.

<div class="theorem-box">

**Proof (Gradient perpendicular to a level curve).** Let $$\mathbf r(t)$$ trace a level curve $$f(\mathbf r(t))=c$$. The chain rule gives

$$
0=\frac{d}{dt}f(\mathbf r(t))=\nabla f\cdot\mathbf r'(t).
$$

A nonzero gradient is therefore perpendicular to every tangent direction along the level curve. The same reasoning applies to tangent directions on a level surface.

</div>

```tikz The gradient is perpendicular to a level curve and points toward increasing values
\begin{tikzpicture}[scale=1.2]
\draw[->,gray] (-2.1,0) -- (3.2,0) node[right] {$x$};
\draw[->,gray] (0,-2.1) -- (0,2.2) node[above] {$y$};
\foreach \r in {0.6,1.2,1.8} {\draw[blue] (0,0) circle (\r);}
\draw[dashed,teal] (1.2,-1.1) -- (1.2,1.1) node[above] {tangent};
\draw[->,orange!85!black,very thick] (1.2,0) -- (2.7,0) node[above] {$\nabla f$};
\fill (1.2,0) circle (1.5pt);
\node at (-1.5,-2.45) {$f(x,y)=x^2+y^2$};
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** For $$f(x,y)=x^2+3y^2$$ at $$(1,1)$$, find the rate of change toward $$(4,5)$$ and the direction of steepest increase.

The direction from $$(1,1)$$ to $$(4,5)$$ is $$\langle3,4\rangle$$, so use $$\mathbf u=\langle3/5,4/5\rangle$$. Since $$\nabla f(1,1)=\langle2,6\rangle$$,

$$
D_{\mathbf u}f=\frac65+\frac{24}5=6.
$$

The steepest-increase unit direction is $$\langle1,3\rangle/\sqrt{10}$$, with rate $$2\sqrt{10}$$.

</div>

### A directional derivative is a one-variable derivative

At a point $$P$$, move along the line $$P+t\mathbf u$$. The directional derivative is the ordinary derivative of the resulting composition at zero:

$$
D_{\mathbf u}f(P)=\lim_{t\to0}\frac{f(P+t\mathbf u)-f(P)}t.
$$

When $$\mathbf u$$ has unit length, the parameter change measures signed distance. Applying the chain rule to this line gives the gradient dot-product formula for differentiable functions.

<div class="theorem-box">

**Example.** On the sphere $$x^2+y^2+z^2=3$$, find the unit direction of motion at $$P=(1,1,1)$$ that increases $$f=x+2y+3z$$ most rapidly, and find that rate per unit distance along the sphere.

Without the constraint, the gradient $$\mathbf g=\langle1,2,3\rangle$$ gives the best direction. But it has a component pointing off the sphere. A valid instantaneous velocity $$\mathbf u$$ must be tangent: $$\mathbf u\cdot\mathbf n=0$$ for $$\mathbf n=\langle1,1,1\rangle$$.

Decompose the gradient into its normal and tangent parts. The normal projection is

$$
\frac{\mathbf g\cdot\mathbf n}{\mathbf n\cdot\mathbf n}\mathbf n
=2\langle1,1,1\rangle,
$$

leaving the tangent vector $$\mathbf g_T=\langle-1,0,1\rangle$$. For any unit tangent direction, the normal part contributes zero to $$\mathbf g\cdot\mathbf u$$. We therefore only need to maximize $$\mathbf g_T\cdot\mathbf u$$, attained by aligning with $$\mathbf g_T$$:

$$
\mathbf u=\frac1{\sqrt2}\langle-1,0,1\rangle,
\qquad\text{maximum rate}=\sqrt2.
$$

This direction is realized by the curve $$\mathbf r(s)=P\cos(s/\sqrt3)+\sqrt3\mathbf u\sin(s/\sqrt3)$$ on the sphere. Its derivative at zero is $$\mathbf u$$, so the tangent calculation corresponds to actual allowed motion. A straight line with the same initial direction would leave the sphere after that instant.

</div>

---

## Tangent Planes and Normal Vectors

For a differentiable graph $$z=f(x,y)$$, the tangent plane at $$(a,b,f(a,b))$$ is the graph of its linearization:

$$
z-f(a,b)=f_x(a,b)(x-a)+f_y(a,b)(y-b).
$$

A normal is $$\langle-f_x,-f_y,1\rangle$$ evaluated at $$(a,b)$$.

More generally, let a surface be given by $$F(x,y,z)=c$$. If $$F$$ has continuous first partial derivatives nearby and $$\nabla F(P)\ne\mathbf0$$, then the gradient is a normal, and the tangent plane is

$$
\nabla F(P)\cdot\langle x-x_0,y-y_0,z-z_0\rangle=0.
$$

The normal line is $$\mathbf r(t)=P+t\nabla F(P)$$. If the gradient vanishes, this construction does not determine a plane; investigate the surface separately.

For example, on $$x^2+y^2+z^2=9$$ at $$(1,2,2)$$, the normal is $$\langle2,4,4\rangle$$. The tangent plane simplifies to $$x+2y+2z=9$$.

### Tangents to intersecting surfaces

If a curve lies on two regular level surfaces, its tangent is perpendicular to both surface normals. Their cross product gives a tangent direction when the normals are not parallel. This connects gradients back to the cross-product geometry of Chapter 1.

<div class="theorem-box">

**Example.** Find a tangent line to the intersection of $$x^2+y^2+z^2=6$$ and $$z=x+y$$ at $$P=(1,1,2)$$.

The point satisfies both equations: $$1+1+4=6$$ and $$2=1+1$$. Take $$F=x^2+y^2+z^2$$ and $$G=z-x-y$$. Their normals at $$P$$ are $$\langle2,2,4\rangle$$ and $$\langle-1,-1,1\rangle$$. The cross product is $$\langle6,-6,0\rangle$$, so a tangent line is

$$
\boldsymbol\ell(t)=\langle1,1,2\rangle+t\langle1,-1,0\rangle.
$$

The direction has zero dot product with both normals. Checking point membership first confirms where the local geometry is being calculated. The tangent line need not remain on either surface away from the point.

</div>

---

## Maxima and Minima of Functions of Two Variables

At an interior local extremum of a differentiable function, $$\nabla f=\mathbf0$$. Critical points also include domain points where a first partial does not exist. A critical point is only a candidate; it can be a saddle point.

Once the first-order term is zero, the next local information comes from how the slopes themselves change. For continuous second partials, the leading quadratic part near a stationary point is

$$
\frac12\left(f_{xx}h^2+2f_{xy}hk+f_{yy}k^2\right),
$$

with the derivatives evaluated at the point. If this expression is positive for every nonzero displacement, all sufficiently nearby points rise above the stationary value. If it is negative for every displacement, they lie below. If its sign depends on direction, the point is a saddle.

The mixed term matters because a path can change both inputs together. A surface may bend upward along both coordinate axes yet dip along a diagonal when that mixed term is sufficiently large. Completing the square in the quadratic expression gives a compact way to test all directions at once. For a stationary point $$(a,b)$$, compute

$$
D=f_{xx}(a,b)f_{yy}(a,b)-[f_{xy}(a,b)]^2.
$$

| Result | Classification |
| --- | --- |
| $$D>0$$ and $$f_{xx}>0$$ | Strict local minimum |
| $$D>0$$ and $$f_{xx}<0$$ | Strict local maximum |
| $$D<0$$ | Saddle point |
| $$D=0$$ | Test inconclusive |

A continuous function on a closed, bounded region attains absolute extrema. Find interior candidates, analyze every boundary piece and corner, and compare function values. An interior test alone misses boundary extrema.

<div class="theorem-box">

**Example.** Classify all critical points of $$f(x,y)=x^3-3x+y^2$$.

The equations $$f_x=3x^2-3=0$$ and $$f_y=2y=0$$ give $$(1,0)$$ and $$(-1,0)$$. Since $$f_{xx}=6x$$, $$f_{yy}=2$$, and $$f_{xy}=0$$, we have $$D=12x$$.

At $$(1,0)$$, $$D>0$$ and $$f_{xx}>0$$, so there is a local minimum with value $$-2$$. At $$(-1,0)$$, $$D<0$$, so there is a saddle point. There is no local maximum.

</div>

### Absolute extrema need a boundary calculation

The second derivative test classifies local behavior at an interior stationary point. It does not compare that point with the boundary of a region. A practical absolute-extrema calculation often combines multivariable differentiation in the interior with ordinary single-variable optimization on the boundary.

<div class="theorem-box">

**Example.** Find the absolute extrema of $$f=x^2+y^2-2x$$ on $$x^2+y^2\le4$$.

The interior equations $$2x-2=0$$ and $$2y=0$$ give $$(1,0)$$, with value $$-1$$. On the circular boundary, use $$x^2+y^2=4$$ to simplify the objective to $$4-2x$$. Since $$-2\le x\le2$$ there, the boundary minimum is $$0$$ at $$(2,0)$$ and the boundary maximum is $$8$$ at $$(-2,0)$$.

Comparing all candidates gives an absolute minimum of $$-1$$ at $$(1,0)$$ and an absolute maximum of $$8$$ at $$(-2,0)$$. The alternative form $$f=(x-1)^2+y^2-1$$ confirms the minimum geometrically.

</div>

When the second derivative determinant is zero, inspect the function rather than declaring a saddle. Both $$x^4+y^4$$ and $$x^4-y^4$$ have zero determinant at the origin, but the first has a strict minimum and the second changes sign across different directions.

---

## Lagrange Multipliers

An unconstrained maximum requires no first-order increase in any direction. A constrained maximum only rules out increase in directions that stay on the constraint. For example, a point could be the highest point on a circle even if moving straight away from the circle would increase the function further.

If $$g=c$$ defines a regular curve or surface, its tangent directions are perpendicular to $$\nabla g$$. At a constrained extremum, $$\nabla f$$ must also be perpendicular to every allowed tangent direction. Otherwise we could move along the constraint in a direction giving a positive or negative first-order change, contradicting an extremum. The two gradients must therefore point along the same normal line, possibly with opposite signs or with $$\nabla f=\mathbf0$$.

This gives the Lagrange multiplier equations:

$$
\nabla f=\lambda\nabla g,\qquad g=c.
$$

Solve these equations together, then compare the objective values. This gives candidates, not an automatic classification. The usual necessary condition assumes differentiability and $$\nabla g\ne\mathbf0$$ at the candidate. Check singular constraint points separately, along with endpoints or boundaries of the allowed portion.

For two constraints in three dimensions, use $$\nabla f=\lambda\nabla g+\mu\nabla h$$ when the constraint gradients are independent.

<div class="theorem-box">

**Example.** Find the absolute maximum and minimum of $$f(x,y,z)=xyz$$ on $$x^2+y^2+z^2=3$$, including candidates with zero coordinates.

The sphere is closed and bounded, and its constraint gradient is nonzero everywhere on it. Extrema exist and must satisfy

$$
yz=2\lambda x,\qquad xz=2\lambda y,\qquad xy=2\lambda z.
$$

First consider a zero coordinate. If $$x=0$$, the first equation gives $$yz=0$$, so at least one other coordinate is zero. The constraint then gives the six axis points $$(\pm\sqrt3,0,0)$$ and their coordinate permutations, all with objective value zero. The other zero-coordinate cases yield no additional points.

If all coordinates are nonzero, multiply the three multiplier equations by $$x,y,z$$ respectively. Their left sides all equal $$xyz\ne0$$, so $$\lambda\ne0$$ and $$x^2=y^2=z^2$$. The constraint forces each square to equal one.

There are eight remaining candidates with coordinates $$\pm1$$. Those with a positive product give value $$1$$, and those with a negative product give value $$-1$$. Comparing with the zero candidates gives the absolute maximum $$1$$ and absolute minimum $$-1$$.

As a global check, the arithmetic-geometric mean inequality gives $$x^2y^2z^2\le((x^2+y^2+z^2)/3)^3=1$$. The axis points are genuine stationary candidates, but not extrema: near any of them, small choices of the other two coordinate signs produce both positive and negative products. Dividing by coordinates at the start would have hidden these candidates and left the multiplier analysis incomplete.

</div>

### Do not divide away candidate points

The multiplier equations may include factors that can vanish. Dividing by one of those factors without checking its zero case can discard valid extrema. Keep a short case split when necessary, and always substitute every candidate into the original constraint.

<div class="theorem-box">

**Example.** Find the largest volume of a rectangular box with positive side lengths and fixed surface area $$S$$.

Maximize $$V=xyz$$ subject to $$2xy+2xz+2yz=S$$. The multiplier equations are

$$
yz=2\lambda(y+z),\quad
xz=2\lambda(x+z),\quad
xy=2\lambda(x+y).
$$

Multiply these equations by $$x,y,z$$ respectively. Their left sides all become $$xyz$$. Positivity implies $$\lambda\ne0$$, so comparing the first two gives $$z(x-y)=0$$ and therefore $$x=y$$. Comparing another pair gives $$y=z$$.

Thus the candidate is a cube with side $$\sqrt{S/6}$$ and volume $$(S/6)^{3/2}$$. To verify a global maximum, apply the arithmetic-geometric mean inequality to $$xy,xz,yz$$: their sum is $$S/2$$, so $$(xyz)^2\le(S/6)^3$$, with equality for the cube. The multiplier calculation finds the candidate, and the inequality establishes the maximum over all positive boxes.

</div>

---

:::equations
| Idea | Equation or condition |
| --- | --- |
| Implicit partials | $$z_x=-F_x/F_z,\quad z_y=-F_y/F_z,\quad F_z\ne0$$ |
| Linearization | $$L=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b)$$ |
| Differential | $$df=f_x\,dx+f_y\,dy$$ |
| Chain rule | $$\frac{d}{dt}f(\mathbf r(t))=\nabla f(\mathbf r(t))\cdot\mathbf r'(t)$$ |
| Directional derivative | $$D_{\mathbf u}f=\nabla f\cdot\mathbf u,\quad\lVert\mathbf u\rVert=1$$ |
| Level-surface tangent plane | $$\nabla F(P)\cdot(\mathbf r-P)=0,\quad\nabla F(P)\ne\mathbf0$$ |
| Quadratic change at a stationary point | $$\Delta f\approx\tfrac12(f_{xx}h^2+2f_{xy}hk+f_{yy}k^2),\quad f\in C^2$$ |
| Second derivative test | $$D=f_{xx}f_{yy}-f_{xy}^2\quad\text{at a stationary point}$$ |
| One regular constraint | $$\nabla f=\lambda\nabla g,\quad g=c$$ |
:::

## Reference

Topic and section order follows Anton, Bivens, and Davis, *Calculus: Early Transcendentals*, 12th edition, Chapter 13, renumbered as Chapter 3 here. Explanations and worked examples on this page are original study notes.
