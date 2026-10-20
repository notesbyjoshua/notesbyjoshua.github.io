---
title: "Chapter 1: Three-Dimensional Space and Introduction to Vectors"
description: "Multivariable calculus notes on 3D coordinates, vector products, projections, lines, planes, quadric surfaces, and coordinate systems."
status: developing
progress: 70
sidebar:
  order: 1
---

## Rectangular Coordinates in 3D

A point $$P$$ gives a position, which we can describe using different coordinate systems. A common choice is the Cartesian (rectangular) system, with $$P=(x,y,z)$$. $$x$$, $$y$$, and $$z$$ denote the distance from a plane, or basically an infinite horizontal sheet. The coordinate planes are $$z=0$$ (the $$xy$$-plane), $$y=0$$ (the $$xz$$-plane), and $$x=0$$ (the $$yz$$-plane). To picture a point, locate $$(x,y,0)$$ first, then move vertically by $$z$$.

```tikz Locating a point by its horizontal projection and vertical displacement
\begin{tikzpicture}[x={(-0.7cm,-0.4cm)},y={(1cm,0cm)},z={(0cm,1cm)},scale=1.25]
\draw[->] (0,0,0) -- (3,0,0) node[below] {$x$};
\draw[->] (0,0,0) -- (0,3,0) node[right] {$y$};
\draw[->] (0,0,0) -- (0,0,3) node[above] {$z$};
\draw[dashed,gray] (2,0,0) -- (2,2,0) -- (0,2,0);
\draw[dashed,gray] (0,0,0) -- (2,2,0);
\draw[blue,thick,->] (2,2,0) -- (2,2,2);
\draw[orange!85!black,thick,->] (0,0,0) -- (2,2,2);
\fill (2,2,0) circle (1pt) node[below right] {$(x,y,0)$};
\fill (2,2,2) circle (1.4pt) node[right] {$P=(x,y,z)$};
\node[below left] at (0,0,0) {$O$};
\end{tikzpicture}
```

The distance between $$P=(x_1,y_1,z_1)$$ and $$Q=(x_2,y_2,z_2)$$ follows from the Pythagorean theorem:

$$
d(P,Q)=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}.
$$

One of the most common types of shapes found in 3D planes is a **spherical surface**. A sphere is the set of points a fixed distance $$R>0$$ from a center $$(a,b,c)$$, so its equation is

$$
(x-a)^2+(y-b)^2+(z-c)^2=R^2.
$$

Complete the square to find the center and radius when the equation is expanded.

A **cylindrical surface** forms when a 3D circle is extended along parallel lines. If an equation leaves out one coordinate, that coordinate is free. For example, $$x^2+y^2=9$$ describes a circular cylinder extending in both directions along the $$z$$-axis.

<div class="theorem-box">

**Example.** Identify the surface $$x^2+y^2+z^2-4x+6z=3$$ and find its center and radius.

Group the terms and complete the squares:

$$
(x-2)^2-4+y^2+(z+3)^2-9=3,
$$

so

$$
(x-2)^2+y^2+(z+3)^2=16.
$$

This is a sphere with center $$(2,0,-3)$$ and radius $$4$$.

</div>

In two dimensions, fixing one coordinate usually leaves a line. In three dimensions, it leaves a plane because two coordinates can still vary. For example, $$x=2$$ contains every point $$(2,y,z)$$. Adding $$y=-1$$ leaves the line $$(2,-1,z)$$, and adding $$z=3$$ selects a single point. Counting the remaining free coordinates is a useful first check when an equation is hard to picture.

The distinction between a surface and a solid also comes from the equation. Equality in the sphere equation gives only the boundary. Replacing equality with $$\le$$ includes the interior ball. Similarly, $$x^2+y^2\le9$$ describes an infinite solid cylinder, while adding $$0\le z\le4$$ cuts out a finite cylinder with two flat ends.

<div class="theorem-box">

**Example.** A sphere has diameter endpoints $$A=(-1,2,0)$$ and $$B=(3,0,4)$$. Find its equation and describe its trace in the plane $$z=2$$.

The center is the midpoint, found by averaging corresponding coordinates:

$$
C=\left(\frac{-1+3}2,\frac{2+0}2,\frac{0+4}2\right)=(1,1,2).
$$

The diameter vector is $$\langle4,-2,4\rangle$$, whose length is $$6$$. The radius is therefore $$3$$, giving

$$
(x-1)^2+(y-1)^2+(z-2)^2=9.
$$

Set $$z=2$$ to obtain $$(x-1)^2+(y-1)^2=9$$. This is the largest circular cross section because the plane passes through the center. At $$z=4$$, the trace instead has radius $$\sqrt5$$; beyond $$z=5$$ there are no points on the sphere.

</div>

---

## Vectors

A vector describes a magnitude and direction, which you should already be familiar with from Precalculus and Calculus. One thing that vectors can model is displacement, or how far a point moved from another. The displacement from $$P$$ to $$Q$$ is defined as

$$
\overrightarrow{PQ}=\langle x_2-x_1,y_2-y_1,z_2-z_1\rangle.
$$

Unlike a point, a displacement vector can be moved without changing it. Its components tell us how much to move along each axis. For $$\mathbf u=\langle u_1,u_2,u_3\rangle$$ and $$\mathbf v=\langle v_1,v_2,v_3\rangle$$, we can add (and subtract) and scale the vectors component by component:

$$
\mathbf u+\mathbf v=\langle u_1+v_1,u_2+v_2,u_3+v_3\rangle,
\qquad
c\mathbf u=\langle cu_1,cu_2,cu_3\rangle.
$$

The standard basis vectors are $$\mathbf i=\langle1,0,0\rangle$$, $$\mathbf j=\langle0,1,0\rangle$$, and $$\mathbf k=\langle0,0,1\rangle$$. Thus $$\langle a,b,c\rangle=a\mathbf i+b\mathbf j+c\mathbf k$$.

The magnitude and a unit vector in the same direction are

$$
\lVert\mathbf v\rVert=\sqrt{v_1^2+v_2^2+v_3^2},
\qquad
\widehat{\mathbf v}=\frac{\mathbf v}{\lVert\mathbf v\rVert}
\quad (\mathbf v\ne\mathbf0).
$$

Two nonzero vectors are parallel exactly when one is a scalar multiple of the other. A negative multiple reverses direction. The zero vector has magnitude zero and no direction.

// add lots more introduction to vectors

### Direction and magnitude as separate steps

When a vector problem asks for a specified magnitude in a specified direction, handle the direction first. Subtract endpoint coordinates in the correct order, divide by the resulting magnitude, and only then multiply by the requested magnitude. A unit vector records direction without retaining the original displacement's length.

Adding vectors has a geometric interpretation too. Place the tail of the second displacement at the tip of the first. The sum runs from the original starting point to the final endpoint. This explains why displacement depends only on the endpoints even when the actual path changes direction many times.

<div class="theorem-box">

**Example.** A force of magnitude $$30$$ acts from $$P=(1,-2,2)$$ toward $$Q=(3,1,8)$$. Find its component form, then find the force needed to balance it together with $$\mathbf G=\langle4,0,-5\rangle$$.

The required direction is

$$
\overrightarrow{PQ}=\langle2,3,6\rangle,\qquad
\lVert\overrightarrow{PQ}\rVert=7.
$$

Thus the first force is

$$
\mathbf F=\frac{30}7\langle2,3,6\rangle
=\left\langle\frac{60}7,\frac{90}7,\frac{180}7\right\rangle.
$$

For equilibrium, the total force must be the zero vector. The balancing force is therefore

$$
\mathbf H=-(\mathbf F+\mathbf G)
=\left\langle-\frac{88}7,-\frac{90}7,-\frac{145}7\right\rangle.
$$

The minus sign reverses the entire resultant, not just its largest component. Adding all three forces componentwise gives zero, which is the quickest check.

</div>

---

## Dot Product; Projections

Suppose a force points partly along a displacement and partly across it. To measure how much of that force helps the motion, we need both its size and its alignment with the displacement. Multiplying the two magnitudes alone loses the direction information. A factor of $$\cos\theta$$ fixes that: it is one for matching directions, zero for perpendicular directions, and negative for opposing directions.

The dot product packages that geometric measurement into a calculation with components:

$$
\mathbf u\cdot\mathbf v=u_1v_1+u_2v_2+u_3v_3
=\lVert\mathbf u\rVert\lVert\mathbf v\rVert\cos\theta.
$$

The component formula and angle formula are two descriptions of the same operation. One is useful when coordinates are known; the other explains what the result means.

<div class="theorem-box">

**Proof (Dot product and angle).** Place nonzero vectors $$\mathbf u,\mathbf v$$ at a common starting point. The third side of their triangle is $$\mathbf u-\mathbf v$$. The law of cosines gives

$$
\lVert\mathbf u-\mathbf v\rVert^2
=\lVert\mathbf u\rVert^2+\lVert\mathbf v\rVert^2
-2\lVert\mathbf u\rVert\lVert\mathbf v\rVert\cos\theta.
$$

Expanding the squared coordinate differences gives the same first two terms, followed by $$-2(u_1v_1+u_2v_2+u_3v_3)$$. Equating the two expressions proves the identity. This also explains why a sum of component products can measure an angle even though no angle appears in that calculation.

</div>

For nonzero vectors, this gives the angle $$0\le\theta\le\pi$$. A positive dot product means an acute angle, a negative one means an obtuse angle, and zero means the vectors are perpendicular.

Imagine dropping a perpendicular from the tip of $$\mathbf u$$ onto the line in direction $$\mathbf v$$. The location of its foot gives the part of $$\mathbf u$$ that acts along that line. The signed distance to the foot is $$\lVert\mathbf u\rVert\cos\theta$$. By the dot-product identity, this equals $$\mathbf u\cdot\mathbf v/\lVert\mathbf v\rVert$$.

That distance is the scalar component. To turn it into a vector, multiply it by the unit direction $$\mathbf v/\lVert\mathbf v\rVert$$. This supplies the second factor of the magnitude in the denominator:

$$
\operatorname{comp}_{\mathbf v}\mathbf u
=\frac{\mathbf u\cdot\mathbf v}{\lVert\mathbf v\rVert},
\qquad
\operatorname{proj}_{\mathbf v}\mathbf u
=\frac{\mathbf u\cdot\mathbf v}{\lVert\mathbf v\rVert^2}\mathbf v.
$$

Subtracting the projection from $$\mathbf u$$ leaves a component perpendicular to $$\mathbf v$$. This splits a vector into parallel and perpendicular parts.

For a constant force $$\mathbf F$$ acting through displacement $$\mathbf d$$, work is $$W=\mathbf F\cdot\mathbf d$$. Only the force component along the displacement contributes.

<div class="theorem-box">

**Example.** For $$\mathbf u=\langle3,1,2\rangle$$ and $$\mathbf v=\langle1,1,0\rangle$$, find the projection of $$\mathbf u$$ onto $$\mathbf v$$ and the perpendicular remainder.

Since $$\mathbf u\cdot\mathbf v=4$$ and $$\lVert\mathbf v\rVert^2=2$$,

$$
\operatorname{proj}_{\mathbf v}\mathbf u=2\langle1,1,0\rangle=\langle2,2,0\rangle.
$$

The remainder is $$\langle1,-1,2\rangle$$. Its dot product with $$\mathbf v$$ is $$1-1=0$$, which checks that it is perpendicular.

</div>

### Where the projection formula comes from

Suppose the component of $$\mathbf u$$ parallel to $$\mathbf v$$ is $$c\mathbf v$$. The leftover vector must be perpendicular to $$\mathbf v$$, so

$$
(\mathbf u-c\mathbf v)\cdot\mathbf v=0.
$$

Expanding and solving gives $$c=(\mathbf u\cdot\mathbf v)/(\mathbf v\cdot\mathbf v)$$. This produces the vector projection formula without needing to find the angle first. It also explains why the denominator is the squared magnitude when the answer is a vector.

<div class="theorem-box">

**Example.** A point $$P=(2,1,3)$$ lies near the line $$\mathbf r(t)=\langle1,0,0\rangle+t\langle1,2,2\rangle$$. Find its nearest point on the line, the distance to the line, and the reflection of $$P$$ across the line.

The nearest point must be found along the whole line, rather than by choosing a coordinate that looks close. Write it as $$Q=\langle1+t,2t,2t\rangle$$. At a nearest point, the connecting displacement is perpendicular to the line direction. Otherwise we could move slightly along the line and shorten it.

Thus

$$
(P-Q)\cdot\langle1,2,2\rangle
=\langle1-t,1-2t,3-2t\rangle\cdot\langle1,2,2\rangle
=9-9t=0.
$$

This gives $$t=1$$ and $$Q=(2,2,2)$$. The distance is $$\lVert P-Q\rVert=\sqrt2$$.

The perpendicular foot is the midpoint between a point and its reflection across the line. Continuing the displacement from $$P$$ to $$Q$$ an equal distance gives

$$
P^*=2Q-P=(2,3,1).
$$

This reflection means a half-turn about the line in space. Its midpoint with $$P$$ lies on the line, and its distance to the line is again $$\sqrt2$$. Projection handles the nearest-point condition and the reflection in one calculation.

</div>

A scalar projection may be negative, but the length of the projected vector cannot be. Its length is the absolute value of the scalar projection. Keep this distinction when a question asks for a component, a projection vector, or a distance.

---

## Cross Product

The dot product tells us about alignment within a plane. Sometimes we need the plane's perpendicular direction instead, such as the normal to a triangular surface. Two independent vectors determine that plane, but there are two possible perpendicular directions. We choose one by the right-hand rule, curling from the first input toward the second.

We also want the result to record how much area the inputs span. Taking the first vector as a base, the perpendicular height supplied by the second is $$\lVert\mathbf v\rVert\sin\theta$$. The parallelogram area is therefore $$\lVert\mathbf u\rVert\lVert\mathbf v\rVert\sin\theta$$. Nearly parallel vectors span little area even if both are long.

The cross product is the vector with this area as its magnitude and the chosen normal as its direction. In components it is

$$
\mathbf u\times\mathbf v
=\langle u_2v_3-u_3v_2,\ u_3v_1-u_1v_3,\ u_1v_2-u_2v_1\rangle.
$$

You can remember this using a determinant:

$$
\mathbf u\times\mathbf v=
\begin{vmatrix}
\mathbf i&\mathbf j&\mathbf k\\
u_1&u_2&u_3\\
v_1&v_2&v_3
\end{vmatrix}.
$$

Its direction follows the right-hand rule from $$\mathbf u$$ toward $$\mathbf v$$. In particular, $$\mathbf i\times\mathbf j=\mathbf k$$, and reversing the order changes the sign:

$$
\mathbf v\times\mathbf u=-\mathbf u\times\mathbf v.
$$

Its magnitude measures the area of the parallelogram spanned by the vectors:

$$
\lVert\mathbf u\times\mathbf v\rVert
=\lVert\mathbf u\rVert\lVert\mathbf v\rVert\sin\theta.
$$

A triangle has half this area. The scalar triple product gives a signed volume, so the ordinary volume of a parallelepiped is

$$
V=\lvert\mathbf u\cdot(\mathbf v\times\mathbf w)\rvert.
$$

A zero triple product means the three vectors are coplanar. A zero cross product means the two vectors are linearly dependent.

<div class="theorem-box">

**Example.** A triangle has vertices $$A=(0,0,0)$$, $$B=(1,2,0)$$, and $$C=(0,1,3)$$. Find its area and a normal vector to its plane.

Use two edges from the same vertex:

$$
\overrightarrow{AB}\times\overrightarrow{AC}
=\langle1,2,0\rangle\times\langle0,1,3\rangle
=\langle6,-3,1\rangle.
$$

This is a normal vector, and the triangle's area is

$$
A=\frac12\sqrt{36+9+1}=\frac{\sqrt{46}}2.
$$

</div>

### Products answer different geometric questions

Use a dot product when the question concerns an angle, perpendicularity, or a component along a direction. Use a cross product when it concerns a normal direction or area. The dot product returns a scalar, while the cross product returns a vector; checking the type of the answer catches many setup errors.

Cross products distribute over addition, but they do not commute. They also do not generally associate, so keep parentheses in expressions involving three cross products. The determinant shortcut is safe when the component order is fixed and the middle cofactor receives its minus sign.

<div class="theorem-box">

**Example.** The edges of a parallelepiped are $$\mathbf u=\langle1,2,0\rangle$$, $$\mathbf v=\langle0,1,3\rangle$$, and $$\mathbf w=\langle2,0,1\rangle$$. Find its volume and its height above the base spanned by $$\mathbf u,\mathbf v$$.

The base normal is $$\mathbf u\times\mathbf v=\langle6,-3,1\rangle$$. The scalar triple product is

$$
\mathbf w\cdot(\mathbf u\times\mathbf v)=12+1=13.
$$

Thus the volume is $$13$$. The base area is $$\sqrt{46}$$, so the perpendicular height is

$$
h=\frac{V}{A}=\frac{13}{\sqrt{46}}.
$$

The height is smaller than the edge length $$\sqrt5$$ because that edge is tilted relative to the base normal. Interchanging the two base edges would reverse the normal and the signed triple product, but the volume would remain $$13$$.

</div>

---

## Parametric Equations of Lines

A point tells us where a line is, but it does not tell us which way the line runs. A direction vector supplies that missing information. Starting from $$\mathbf r_0$$, every move along the line must be a scalar multiple of the same direction: half a step, several steps, or a negative number of steps to move backward.

This is why one parameter is enough for a line in three-dimensional space. The coordinates vary together rather than independently:

$$
\mathbf r(t)=\mathbf r_0+t\mathbf v,\qquad -\infty<t<\infty.
$$

If $$\mathbf r_0=\langle x_0,y_0,z_0\rangle$$ and $$\mathbf v=\langle a,b,c\rangle$$, the component equations are $$x=x_0+at$$, $$y=y_0+bt$$, and $$z=z_0+ct$$. When all three direction components are nonzero, the symmetric form is

$$
\frac{x-x_0}{a}=\frac{y-y_0}{b}=\frac{z-z_0}{c}.
$$

If a component is zero, write that coordinate as constant instead of dividing by zero. A segment from $$P$$ to $$Q$$ uses $$\mathbf r(t)=P+t(Q-P)$$ with $$0\le t\le1$$.

To test whether two lines intersect, give them separate parameters and solve all three coordinate equations. Nonparallel lines in space can be **skew**: they do not intersect and are not in a common plane.

### Intersections require separate parameters

A parameter labels a point on one particular line. Two lines reaching the same spatial point need not do so at the same parameter value. Setting their parameter symbols equal imposes an extra condition that the geometry does not require. Instead, use one parameter for each line and solve for both.

<div class="theorem-box">

**Example.** Find the minimum distance between the lines $$L_1:\mathbf r(t)=\langle t,t,0\rangle$$ and $$L_2:\mathbf q(s)=\langle1+s,-s,1+s\rangle$$, and find the two points attaining it.

The lines have directions $$\mathbf u=\langle1,1,0\rangle$$ and $$\mathbf v=\langle1,-1,1\rangle$$. These are not parallel. At the closest pair, the connecting vector must be perpendicular to both directions; otherwise sliding one endpoint along its line would reduce the distance.

The connecting vector from $$\mathbf r(t)$$ to $$\mathbf q(s)$$ is

$$
\mathbf d=\langle1+s-t,-s-t,1+s\rangle.
$$

Imposing the two perpendicularity conditions gives

$$
\mathbf d\cdot\mathbf u=1-2t=0,
\qquad
\mathbf d\cdot\mathbf v=2+3s=0.
$$

Hence $$t=1/2$$ and $$s=-2/3$$. The closest points are

$$
A=\left(\frac12,\frac12,0\right),\qquad
B=\left(\frac13,\frac23,\frac13\right).
$$

Their displacement is $$\langle-1/6,1/6,1/3\rangle$$, with length $$1/\sqrt6$$. The positive minimum proves the lines are skew.

For an independent distance check, $$\mathbf u\times\mathbf v=\langle1,-1,-2\rangle$$. Project the initial connecting vector $$\mathbf q(0)-\mathbf r(0)=\langle1,0,1\rangle$$ onto that common normal:

$$
D=\frac{\lvert\langle1,0,1\rangle\cdot\langle1,-1,-2\rangle\rvert}{\sqrt6}
=\frac1{\sqrt6}.
$$

The projection gives the distance quickly, while the perpendicularity equations also locate the points. For nonparallel infinite lines, the connecting vector's common-normal component cannot change as either endpoint moves; finding a pair with no other component therefore establishes the global minimum.

</div>

For a line and a plane, substitution gives a single linear equation in the line parameter. One solution means the line crosses the plane once. An identity means every point of the line lies in the plane. A contradiction means the line is parallel to the plane and separate from it. These cases also follow from the dot product of the line direction with the plane normal: a nonzero dot product guarantees a unique intersection.

---

## Planes in 3-Space

A plane has two independent directions of motion within it. Instead of tracking both, we can describe the one direction that motion in the plane never follows: its normal. If $$P_0$$ is fixed in the plane and $$P$$ is another point in it, their displacement must have zero component along that normal.

Write $$P_0=(x_0,y_0,z_0)$$ and choose a nonzero normal $$\mathbf n=\langle a,b,c\rangle$$. Perpendicularity gives the plane equation directly:

$$
\mathbf n\cdot\langle x-x_0,y-y_0,z-z_0\rangle=0,
$$

or $$ax+by+cz=d$$. The normal is perpendicular to every displacement within the plane.

To find a plane through three noncollinear points, take the cross product of two edge vectors to obtain a normal. To find the line where two nonparallel planes intersect, cross their normals to get a direction and solve for one common point.

The distance from $$P=(x_1,y_1,z_1)$$ to $$ax+by+cz=d$$ is

$$
D=\frac{\lvert ax_1+by_1+cz_1-d\rvert}{\sqrt{a^2+b^2+c^2}}.
$$

This is the magnitude of the displacement's scalar projection onto the normal. Similarly, the distance from $$P$$ to the line through $$P_0$$ with direction $$\mathbf v$$ is $$\lVert\overrightarrow{P_0P}\times\mathbf v\rVert/\lVert\mathbf v\rVert$$.

<div class="theorem-box">

**Example.** Find both planes containing the line $$x+y=1$$, $$z=0$$ that are tangent to the sphere $$x^2+y^2+(z-2)^2=1$$.

A plane containing the given line must vanish whenever $$x+y-1=0$$ and $$z=0$$. Its equation can therefore be written

$$
A(x+y-1)+Bz=0.
$$

The case $$A=0$$ gives $$z=0$$, which is a distance $$2$$ from the sphere's center and is not tangent. For $$A\ne0$$, divide through and write $$x+y+kz=1$$.

Tangency means the perpendicular distance from the center $$C=(0,0,2)$$ to the plane equals the sphere's radius, one. Thus

$$
\frac{\lvert2k-1\rvert}{\sqrt{2+k^2}}=1.
$$

Squaring gives $$3k^2-4k-1=0$$, so

$$
k=\frac{2\pm\sqrt7}{3}.
$$

Both planes satisfy the original distance equation, so both are tangent. To see why this condition is enough, let $$H$$ be the center's perpendicular foot on either plane. Every point $$P$$ in the plane satisfies $$CP^2=CH^2+HP^2$$. Since $$CH=1$$, a point can also lie on the sphere only when $$HP=0$$. The plane and sphere meet at exactly $$H$$.

</div>

### Building a plane from points

Two independent directions within a plane are enough to determine its normal. Choose both directions from the same starting point so their geometric meaning is clear. The cross product may be multiplied by any nonzero constant without changing the plane; simplify its components before writing the equation.

<div class="theorem-box">

**Example.** Find the plane through $$A=(1,0,0)$$, $$B=(0,2,0)$$, and $$C=(0,0,3)$$. Then find the perpendicular foot from the origin to the plane.

The edge vectors are $$\overrightarrow{AB}=\langle-1,2,0\rangle$$ and $$\overrightarrow{AC}=\langle-1,0,3\rangle$$. Their cross product is $$\mathbf n=\langle6,3,2\rangle$$, so the plane is

$$
6(x-1)+3y+2z=0,
\qquad6x+3y+2z=6.
$$

A perpendicular line from the origin follows the normal: $$\mathbf r(t)=t\langle6,3,2\rangle$$. Substituting into the plane gives $$49t=6$$. Thus the perpendicular foot is

$$
H=\left(\frac{36}{49},\frac{18}{49},\frac{12}{49}\right).
$$

Its distance from the origin is $$\lVert H\rVert=6/7$$, agreeing with the point-to-plane distance formula. This construction finds the actual nearest point, not just the distance.

</div>

The acute angle between two planes is the acute angle between their normal lines. Use the absolute value of the normals' dot product in the cosine formula to select that acute angle. Parallel normals mean parallel or identical planes; perpendicular normals mean perpendicular planes.

### Angle between a line and a plane

A line direction is compared with the plane normal using a dot product, but that gives the angle to the normal rather than the angle to the plane itself. The acute angle to the plane is the complementary angle. If the line is parallel to the plane, its angle to the normal is a right angle and its angle to the plane is zero.

<div class="theorem-box">

**Example.** Find the acute angle between a line with direction $$\mathbf v=\langle1,0,1\rangle$$ and the plane $$z=2$$.

The plane has normal $$\mathbf n=\langle0,0,1\rangle$$. The cosine of the angle $$\beta$$ between direction and normal is

$$
\cos\beta=\frac{\lvert\mathbf v\cdot\mathbf n\rvert}{\lVert\mathbf v\rVert\lVert\mathbf n\rVert}
=\frac1{\sqrt2}.
$$

Thus $$\beta=\pi/4$$, and the angle to the plane is also $$\pi/4$$. In general, if $$\alpha$$ is the acute angle to a plane, use $$\sin\alpha=\lvert\mathbf v\cdot\mathbf n\rvert/(\lVert\mathbf v\rVert\lVert\mathbf n\rVert)$$. A direction perpendicular to the plane gives a ratio of one, as it should.

</div>

---

## Quadric Surfaces

A **trace** is the intersection of a surface with a plane. Setting one coordinate equal to a constant reduces a 3D problem to a familiar 2D curve. Use several traces before guessing a surface from its equation.

For positive $$a,b,c$$, these standard forms are centered at the origin:

| Surface | Standard equation | What to look for |
| --- | --- | --- |
| Ellipsoid | $$x^2/a^2+y^2/b^2+z^2/c^2=1$$ | All squared terms positive; bounded |
| Hyperboloid of one sheet | $$x^2/a^2+y^2/b^2-z^2/c^2=1$$ | One negative term; connected around its axis |
| Hyperboloid of two sheets | $$z^2/c^2-x^2/a^2-y^2/b^2=1$$ | One positive term; two separate pieces |
| Elliptic cone | $$z^2/c^2=x^2/a^2+y^2/b^2$$ | Two halves meeting at a vertex |
| Elliptic paraboloid | $$z=x^2/a^2+y^2/b^2$$ | Elliptical horizontal traces; one opening direction |
| Hyperbolic paraboloid | $$z=x^2/a^2-y^2/b^2$$ | Saddle; vertical traces open in opposite directions |

Changing which coordinate has the special sign changes the axis. Replacing $$x$$ by $$x-h$$ translates in the $$x$$-direction, and similarly for the other coordinates.

For example, $$z=x^2-y^2$$ has an upward parabola in $$y=0$$, a downward parabola in $$x=0$$, and two intersecting lines in $$z=0$$. These traces explain the saddle shape.

### Checking the shape with traces

A table of standard forms helps only after the equation has been normalized. Move the constant to one side, complete squares when necessary, and divide by the constant before comparing signs. A positive constant on the right and two positive squared terms describe a different surface from a negative constant with the same left side.

<div class="theorem-box">

**Example.** Identify $$4x^2+y^2-4z^2=-4$$ and describe where it exists relative to the $$z$$-axis.

Divide by $$-4$$ and rearrange:

$$
z^2-x^2-\frac{y^2}4=1.
$$

There is one positive squared term, so this is a hyperboloid of two sheets with axis along $$z$$. At $$z=k$$, its trace is

$$
x^2+\frac{y^2}4=k^2-1.
$$

When $$\lvert k\rvert<1$$, there is no trace because the left side cannot be negative. At $$k=\pm1$$, the trace is a single point. For $$\lvert k\rvert>1$$, the trace is an ellipse. The missing middle heights explain why there are two separate sheets.

</div>

Contrast this with $$x^2+y^2-z^2=1$$. Its horizontal trace has radius $$\sqrt{1+k^2}$$ for every height, so the surface stays connected through its narrowest circle. At a cone, that narrowest circle shrinks to a point instead. This trace-based reasoning is more reliable than memorizing the names from the signs alone.

---

## Cylindrical and Spherical Coordinates

Cylindrical coordinates use polar coordinates in the horizontal plane:

$$
x=r\cos\theta,\qquad y=r\sin\theta,\qquad z=z,
\qquad r=\sqrt{x^2+y^2}.
$$

Here $$r\ge0$$ and $$\theta$$ measures the angle from the positive $$x$$-axis in the $$xy$$-plane. Use the signs of $$x$$ and $$y$$ to select the quadrant; $$\tan\theta=y/x$$ alone loses that information.

Spherical coordinates locate a point by first choosing a ray from the origin and then traveling a distance $$\rho$$ along it. The polar angle $$\phi$$ tips the ray down from the positive $$z$$-axis; the azimuth $$\theta$$ turns its horizontal projection around the vertical axis.

There are two right triangles behind the conversion formulas. In the vertical triangle, the hypotenuse is $$\rho$$, the vertical leg is $$\rho\cos\phi$$, and the horizontal leg is $$r=\rho\sin\phi$$. In the horizontal triangle, split that leg into $$r\cos\theta$$ and $$r\sin\theta$$. Combining these steps gives

$$
x=\rho\sin\phi\cos\theta,\qquad
y=\rho\sin\phi\sin\theta,\qquad
z=\rho\cos\phi.
$$

We use $$\rho\ge0$$, $$0\le\phi\le\pi$$, and one full turn for $$\theta$$. Also,

$$
\rho^2=x^2+y^2+z^2,\qquad r=\rho\sin\phi.
$$

A constant $$\rho$$ gives a sphere, a constant $$r$$ gives a cylinder, and a constant $$\phi$$ strictly between $$0$$ and $$\pi/2$$ gives the upper half of a circular cone. Coordinates need not be unique on an axis or at the origin.

<div class="theorem-box">

**Example.** Convert $$(-1,\sqrt3,2)$$ to cylindrical and spherical coordinates.

The horizontal distance is $$r=2$$, and the point lies in quadrant II, so $$\theta=2\pi/3$$. Its distance from the origin is $$\rho=\sqrt8=2\sqrt2$$, and $$\cos\phi=2/(2\sqrt2)$$ gives $$\phi=\pi/4$$.

Thus one cylindrical representation is $$(2,2\pi/3,2)$$, and one spherical representation is $$(2\sqrt2,2\pi/3,\pi/4)$$.

</div>

### Converting surfaces instead of individual points

A coordinate system is useful when it simplifies a whole equation or region. Cylindrical coordinates preserve height and replace horizontal distance by $$r$$. Spherical coordinates measure distance from the origin directly, so spheres centered there have especially simple equations. Neither system is automatically better just because a problem is three-dimensional.

<div class="theorem-box">

**Example.** Rewrite the sphere $$x^2+y^2+z^2=4z$$ in cylindrical and spherical coordinates, and determine the spherical bounds for its interior.

In rectangular coordinates, completing the square gives $$x^2+y^2+(z-2)^2=4$$. The sphere has center $$(0,0,2)$$ and radius $$2$$, touching the origin from above.

Cylindrical substitution gives

$$
r^2+z^2=4z.
$$

Spherical substitution gives $$\rho^2=4\rho\cos\phi$$. Away from the origin, divide by $$\rho$$ to obtain $$\rho=4\cos\phi$$. The origin still belongs to the original surface and must be retained separately after this division.

For the interior, a ray from the origin travels from $$\rho=0$$ to $$\rho=4\cos\phi$$. Since the sphere is above the horizontal plane, use

$$
0\le\theta\le2\pi,\qquad0\le\phi\le\frac\pi2,
\qquad0\le\rho\le4\cos\phi.
$$

The radial upper bound depends on angle because this sphere is not centered at the origin. These same bounds will be useful for triple integrals in Chapter 4.

</div>

---

:::equations
| Idea | Equation or condition |
| --- | --- |
| Sphere | $$(x-a)^2+(y-b)^2+(z-c)^2=R^2$$ |
| Unit direction | $$\widehat{\mathbf v}=\mathbf v/\lVert\mathbf v\rVert,\quad\mathbf v\ne\mathbf0$$ |
| Dot product | $$\mathbf u\cdot\mathbf v=\lVert\mathbf u\rVert\lVert\mathbf v\rVert\cos\theta$$ |
| Projection | $$\operatorname{proj}_{\mathbf v}\mathbf u=(\mathbf u\cdot\mathbf v)\mathbf v/\lVert\mathbf v\rVert^2$$ |
| Cross product magnitude | $$\lVert\mathbf u\times\mathbf v\rVert=\lVert\mathbf u\rVert\lVert\mathbf v\rVert\sin\theta$$ |
| Parallelepiped volume | $$V=\lvert\mathbf u\cdot(\mathbf v\times\mathbf w)\rvert$$ |
| Nonparallel line distance | $$D=\lvert(\mathbf q_0-\mathbf r_0)\cdot(\mathbf u\times\mathbf v)\rvert/\lVert\mathbf u\times\mathbf v\rVert$$ |
| Line; plane | $$\mathbf r=\mathbf r_0+t\mathbf v;\quad\mathbf n\cdot(\mathbf r-\mathbf r_0)=0$$ |
| Acute line-plane angle | $$\sin\alpha=\lvert\mathbf v\cdot\mathbf n\rvert/(\lVert\mathbf v\rVert\lVert\mathbf n\rVert)$$ |
| Point-to-plane distance | $$D=\lvert ax_1+by_1+cz_1-d\rvert/\sqrt{a^2+b^2+c^2}$$ |
| Cylindrical | $$x=r\cos\theta,\ y=r\sin\theta,\ z=z$$ |
| Spherical | $$x=\rho\sin\phi\cos\theta,\ y=\rho\sin\phi\sin\theta,\ z=\rho\cos\phi$$ |
:::

## Reference

Topic and section order follows Anton, Bivens, and Davis, *Calculus: Early Transcendentals*, 12th edition, Chapter 11, renumbered as Chapter 1 here. Explanations and worked examples on this page are original study notes.
