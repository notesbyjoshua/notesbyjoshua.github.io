---
title: "Coordinate Geometry"
status: developing
progress: 68
sidebar:
  order: 4
description: "Competition geometry notes on coordinate choices, vectors, lines, circles, areas, and lattice points with worked problems and solving strategies."
---

## Choosing Coordinates

Coordinates replace geometric relations by equations. A good placement reduces the number of variables before the calculation begins.

Place a convenient vertex at the origin, a useful side on the horizontal axis, or a symmetry line on an axis. Use $$(0,0),(u,0),(v,w)$$ for a general triangle rather than assigning six unrelated coordinates. Normalize a length to one only when the requested result is unchanged by scaling, or restore the scale at the end.

<div class="theorem-box">

**Example.** A triangle has $$AB=6$$, $$AC=5$$, and $$BC=5$$. Find its altitude from $$C$$ to $$AB$$ using coordinates.

Place $$A=(-3,0)$$ and $$B=(3,0)$$. Equal distances to $$A,B$$ put $$C$$ on the vertical axis, so write $$C=(0,h)$$ with $$h>0$$. Then $$9+h^2=25$$, giving $$h=4$$.

</div>

---

## Distance, Midpoints, and Division Ratios

For $$A=(x_1,y_1)$$ and $$B=(x_2,y_2)$$,

$$
AB^2=(x_2-x_1)^2+(y_2-y_1)^2.
$$

The midpoint is the coordinate average. If $$P$$ divides $$AB$$ internally in the ratio $$AP:PB=m:n$$, then

$$
P=\frac{nA+mB}{m+n}.
$$

The larger weight is attached to the endpoint toward which $$P$$ moves. This vector formula applies to each coordinate separately.

<div class="theorem-box">

**Example.** Points $$A=(1,2)$$ and $$B=(7,5)$$ have an internal division point $$P$$ with $$AP:PB=2:1$$. Find $$P$$.

The point is two-thirds of the way from $$A$$ to $$B$$:

$$
P=\frac{A+2B}{3}=\left(5,4\right).
$$

</div>

---

## Lines, Slopes, and Vectors

A line can be written as $$ax+by=c$$ or parametrically as $$A+t\mathbf u$$, where $$\mathbf u$$ is a nonzero direction vector. The parametric form handles vertical lines without a special slope.

For finite slopes, parallel lines have equal slopes and perpendicular lines satisfy $$m_1m_2=-1$$. Vectors give a version that also handles vertical and horizontal lines:

$$
\mathbf u\perp\mathbf v\iff\mathbf u\cdot\mathbf v=0,
$$

where $$(u_1,u_2)\cdot(v_1,v_2)=u_1v_1+u_2v_2$$. The dot product also gives the angle through $$\mathbf u\cdot\mathbf v=\lVert\mathbf u\rVert\lVert\mathbf v\rVert\cos\theta$$.

<div class="theorem-box">

**Example.** Find the foot of the perpendicular from $$P=(4,3)$$ to the line through the origin with direction vector $$\mathbf u=(2,1)$$.

The foot has the form $$F=t\mathbf u$$. Perpendicularity requires $$(P-t\mathbf u)\cdot\mathbf u=0$$, so

$$
t=\frac{P\cdot\mathbf u}{\mathbf u\cdot\mathbf u}=\frac{11}{5}.
$$

Thus $$F=(22/5,11/5)$$.

</div>

More generally, the distance from $$(x_0,y_0)$$ to $$ax+by=c$$ is $$\lvert ax_0+by_0-c\rvert/\sqrt{a^2+b^2}$$ for $$(a,b)\ne(0,0)$$.

---

## Circles and Intersections

A circle with center $$(h,k)$$ and radius $$r$$ has equation $$(x-h)^2+(y-k)^2=r^2$$. Completing squares identifies its center from an expanded equation.

When two circle equations have the same quadratic terms, subtract them. The squared terms cancel, leaving the line containing their common points, if any.

<div class="theorem-box">

**Example.** Find the intersection points of $$x^2+y^2=25$$ and $$(x-6)^2+y^2=25$$.

Subtracting the first equation from the second gives $$-12x+36=0$$, so $$x=3$$. Substitution into the first circle gives $$y^2=16$$. The intersections are $$(3,4)$$ and $$(3,-4)$$.

</div>

The subtraction gives the radical axis, introduced in more detail on the [radical axes and inversion](/notes/math/geometry/radical-axes-and-inversion/) page.

---

## Coordinate Areas and Pick's Theorem

For vectors $$\mathbf u=(u_1,u_2)$$ and $$\mathbf v=(v_1,v_2)$$ from the same vertex, the triangle area is half the absolute determinant:

$$
K=\frac12\lvert u_1v_2-u_2v_1\rvert.
$$

For a simple polygon whose vertices $$(x_i,y_i)$$ are listed in boundary order, the **shoelace formula** is

$$
K=\frac12\left\lvert\sum_{i=1}^n(x_iy_{i+1}-y_ix_{i+1})\right\rvert,
$$

where the final vertex wraps back to the first. A scrambled vertex order does not trace the intended polygon.

For a simple polygon with integer-coordinate vertices, **Pick's theorem** gives $$K=I+B/2-1$$, where $$I$$ counts interior lattice points and $$B$$ counts boundary lattice points.

<div class="theorem-box">

**Example.** Find the number of lattice points strictly inside the triangle with vertices $$(0,0),(6,0),(0,4)$$.

Its area is $$12$$. A lattice segment with displacement $$(a,b)$$ has $$\gcd(\lvert a\rvert,\lvert b\rvert)+1$$ lattice points including endpoints. Summing the GCDs around the triangle counts each boundary point once, so

$$
B=\gcd(6,0)+\gcd(6,4)+\gcd(0,4)=6+2+4=12.
$$

Pick's theorem then gives $$I=12-12/2+1=7$$.

</div>

:::strategy
Use coordinates when perpendicularity, midpoints, or numerical distances dominate. Keep squared distances until a length is actually needed. Subtract circle equations before solving quadratics, and use vectors when slopes would introduce vertical-line exceptions.
:::

## Determinants and Parametric Intersections

For plane vectors, write $$\det(\mathbf u,\mathbf v)=u_1v_2-u_2v_1$$. The determinant is zero exactly when the vectors are parallel, and its absolute value is the parallelogram area they span.

Suppose two lines are $$A+t\mathbf u$$ and $$B+s\mathbf v$$. If $$\det(\mathbf u,\mathbf v)\ne0$$, take determinants of their intersection equation with each direction to get

$$
t=\frac{\det(B-A,\mathbf v)}{\det(\mathbf u,\mathbf v)},\qquad
s=\frac{\det(B-A,\mathbf u)}{\det(\mathbf u,\mathbf v)}.
$$

This avoids vertical-line exceptions. The parameter values also locate the intersection: $$0\le t\le1$$ means it lies on the segment from $$A$$ to $$A+\mathbf u$$, rather than merely on its supporting line.

<div class="theorem-box">

**Example.** Find the intersection of $$A+t(2,1)$$ with $$B+s(1,-1)$$, where $$A=(0,0)$$ and $$B=(0,3)$$.

The common denominator is $$\det((2,1),(1,-1))=-3$$. The numerator for $$t$$ is $$\det((0,3),(1,-1))=-3$$, so $$t=1$$. The intersection is $$(2,1)$$; substitution into the other line gives $$s=2$$.

Thus the point is an endpoint of the first unit-parameter segment but lies beyond the second segment's endpoint.

</div>

A zero determinant means the directions are parallel. Check one point to distinguish disjoint parallel lines from coincident lines rather than dividing by zero and treating the formula as meaningful.

---

## Constructing a Circle from Three Points

Write a circle in the form

$$
x^2+y^2+Dx+Ey+F=0.
$$

Three noncollinear points give three linear equations for $$D,E,F$$. The center is $$(-D/2,-E/2)$$ and the radius squared is $$(D^2+E^2)/4-F$$. This is usually simpler than introducing the center and radius as three nonlinear unknowns.

<div class="theorem-box">

**Example.** Find the circumcircle of the triangle with vertices $$(0,0),(6,0),(2,4)$$.

The first point gives $$F=0$$. The second gives $$36+6D=0$$, so $$D=-6$$. The third gives $$20-12+4E=0$$, so $$E=-2$$.

The circle is

$$
x^2+y^2-6x-2y=0,
$$

or $$(x-3)^2+(y-1)^2=10$$. Its center is $$(3,1)$$ and its radius is $$\sqrt{10}$$.

</div>

If the three points are collinear, no ordinary circle passes through them. The coefficient system then fails to determine a valid circle. Noncollinearity is the geometric condition behind the algebraic denominator.

---

## Circle–Line Intersections by Projection

A line at distance $$d$$ from a radius-$$R$$ circle's center cuts a chord of length $$2\sqrt{R^2-d^2}$$ when $$d<R$$. At $$d=R$$ it is tangent, and for $$d>R$$ there is no intersection.

This gives an efficient vector construction: find the perpendicular foot $$F$$ from the center to the line, take a unit direction $$\mathbf u$$ along the line, and write the intersections as

$$
F\pm\sqrt{R^2-d^2}\,\mathbf u.
$$

<div class="theorem-box">

**Example.** Find the intersections of $$x^2+y^2=25$$ and $$3x+4y=10$$.

The line's normal vector is $$(3,4)$$ with length five, so the center-to-line distance is two. The foot is $$F=(6/5,8/5)$$. A unit direction along the line is $$(4,-3)/5$$.

The half-chord length is $$\sqrt{21}$$. Thus the two points are

$$
\left(\frac{6+4\sqrt{21}}5,\frac{8-3\sqrt{21}}5\right),\qquad
\left(\frac{6-4\sqrt{21}}5,\frac{8+3\sqrt{21}}5\right).
$$

The projection approach keeps the symmetry of the two roots visible.

</div>

For a tangent line $$y=mx+b$$ to an origin-centered circle of radius $$R$$, the distance condition becomes $$b^2=R^2(1+m^2)$$. This is the same condition obtained by setting the substitution quadratic's discriminant to zero.

---

## Reflection and Shortest Broken Paths

Reflection can turn a path that bends at a line into one straight segment. If $$P$$ is reflected across $$\mathbf n\cdot X=c$$, then

$$
P'=P-2\frac{\mathbf n\cdot P-c}{\mathbf n\cdot\mathbf n}\mathbf n.
$$

The fraction gives the signed normal displacement to the line. Subtracting it twice crosses to the mirror image. The midpoint of $$PP'$$ lies on the mirror line and the joining segment is perpendicular to it.

<div class="theorem-box">

**Example.** Points $$A=(1,2)$$ and $$B=(7,4)$$ are above the horizontal axis. Find the point $$M$$ on that axis minimizing $$AM+MB$$.

Reflect $$B$$ to $$B'=(7,-4)$$. For every allowed $$M$$, $$MB=MB'$$, so the path length is at least $$AB'$$ by the triangle inequality.

The segment from $$A$$ to $$B'$$ crosses the axis one-third of the way along, at $$M=(3,0)$$. Equality is attained there, and the minimum is

$$
AB'=\sqrt{6^2+(-6)^2}=6\sqrt2.
$$

</div>

If $$M$$ were restricted to a finite segment of the axis, the crossing point would need to lie on that segment. Otherwise the minimum may occur at an endpoint. A reflection proves a lower bound, but attainability still depends on the allowed set.

---

## Affine Coordinates for Ratio Problems

A general affine transformation preserves collinearity, parallelism, ratios along one line, and ratios of areas. It does not generally preserve angles, lengths, or circles.

For a problem involving only those preserved quantities, any nondegenerate triangle can be mapped to $$A=(0,0),B=(1,0),C=(0,1)$$. This reduces arithmetic while keeping the desired conclusion intact. Do not use this normalization in a metric problem without accounting for the distortion.

<div class="theorem-box">

**Example.** Points $$P\in AB$$ and $$Q\in AC$$ satisfy $$AP:PB=2:1$$ and $$AQ:QC=1:2$$. Find $$[APQ]/[ABC]$$.

In the reference triangle, $$P=(2/3,0)$$ and $$Q=(0,1/3)$$. Determinants give

$$
\frac{[APQ]}{[ABC]}=\frac23\cdot\frac13=\frac29.
$$

Because an affine transformation multiplies both areas by the same factor, this ratio holds in every nondegenerate triangle.

</div>

The same method proves the midpoint quadrilateral theorem: the four side midpoints of any convex quadrilateral form a parallelogram. Its adjacent side vectors are half the original diagonals, so parallelism follows immediately. Expanding the determinant area shows its area is half the original quadrilateral's.

---

## General Lattice-Triangle Counts

For a segment joining lattice points with displacement $$(a,b)$$, its boundary count depends on $$\gcd(\lvert a\rvert,\lvert b\rvert)$$. The intermediate lattice points occur at equal fractions of the segment after reducing the direction vector to coprime coordinates.

A right triangle with vertices $$(0,0),(a,0),(0,b)$$, for positive integers $$a,b$$, has area $$ab/2$$ and boundary count $$a+b+\gcd(a,b)$$. Pick's theorem therefore gives

$$
I=\frac{ab-a-b-\gcd(a,b)+2}{2}.
$$

For a slanted lattice triangle, use the determinant for area and the three edge GCDs for boundary points. Counting endpoints separately on every side would count each vertex twice.

<div class="theorem-box">

**Example.** Find the number of interior lattice points in the triangle $$(0,0),(8,0),(3,6)$$.

The area is twenty-four. The boundary count is

$$
B=\gcd(8,0)+\gcd(5,6)+\gcd(3,6)=8+1+3=12.
$$

Thus $$I=24-12/2+1=19$$.

</div>

Pick's theorem requires a simple polygon with lattice vertices. A rational-coordinate polygon cannot be substituted directly without first changing the lattice and adjusting the area consistently.

:::strategy
Normalize only the features your target uses. For metric questions, keep Euclidean distances and angles intact. For ratio questions, affine coordinates may simplify the entire diagram. Before accepting an algebraic intersection, verify that it lies on the required segments or rays.
:::

---

## Explicit Coordinates for Two Triangle Centers

For $$A=(0,0),B=(c,0),C=(u,h)$$ with $$h\ne0$$, the circumcenter lies on $$x=c/2$$. Equating its squared distances to $$A,C$$ gives

$$
O=\left(\frac c2,\frac{u^2+h^2-cu}{2h}\right).
$$

The altitude from $$C$$ has equation $$x=u$$. The altitude from $$A$$ is perpendicular to vector $$(u-c,h)$$, so its points satisfy $$(u-c)x+hy=0$$. Therefore

$$
H=\left(u,\frac{u(c-u)}h\right).
$$

<div class="theorem-box">

**Example.** Find the circumcenter and orthocenter for $$A=(0,0),B=(10,0),C=(4,6)$$.

The formulas give $$O=(5,1)$$ and $$H=(4,4)$$. The centroid is $$G=(14/3,2)$$, and $$3G-2O=(4,4)=H$$ checks the Euler-line relation.

No inverse trigonometric functions are needed; perpendicular-bisector and altitude equations determine the centers directly.

</div>

---

## Minimizing a Sum of Squared Distances

Let $$G$$ be the average of fixed points $$A_1,\ldots,A_n$$. Expanding $$P-A_i=(P-G)+(G-A_i)$$ gives

$$
\sum_i\lVert P-A_i\rVert^2
=n\lVert P-G\rVert^2+\sum_i\lVert G-A_i\rVert^2,
$$

because the cross terms contain $$\sum_i(G-A_i)=0$$. The sum is minimized uniquely at $$P=G$$.

<div class="theorem-box">

**Example.** Find the minimum of the sum of squared distances from a point $$P$$ to $$(0,0),(6,0),(0,6)$$.

Their average is $$(2,2)$$. At that point the three squared distances are eight, twenty, twenty, totaling forty-eight. The identity shows every other point adds $$3\lVert P-(2,2)\rVert^2>0$$, so the minimum is forty-eight.

</div>

This minimizes squared distances, not ordinary distances. The point minimizing a sum of unsquared lengths can be different. Before importing a geometric “center,” check exactly which objective the problem specifies.

---

## Constrained Squared-Distance Optimization

The centroid identity also solves a constrained problem. If $$P$$ must lie on a line, the constant term in the squared-distance sum stays unchanged, so minimize $$PG^2$$ by projecting the centroid onto that line.

<div class="theorem-box">

**Example.** A point $$P$$ lies on $$3x+4y=10$$. Find the minimum sum of its squared distances to $$(0,0),(6,0),(0,6)$$.

The unconstrained centroid is $$G=(2,2)$$ and the unconstrained minimum is forty-eight. Its distance to the required line is $$\lvert14-10\rvert/5=4/5$$. Therefore the constrained minimum is

$$
48+3\left(\frac45\right)^2=\frac{1248}{25}.
$$

The attaining point is the perpendicular projection,

$$
P=(2,2)-\frac4{25}(3,4)=\left(\frac{38}{25},\frac{34}{25}\right).
$$

It satisfies the line equation, so the lower bound is attained within the allowed set.

</div>

The same identity describes a locus. A prescribed sum of squared distances equals a constant plus $$nPG^2$$. Above the minimum, the locus is a circle centered at the centroid; at the minimum it is a single point; below the minimum it is empty.

This converts a seemingly complicated sum involving many fixed points into one distance from their average. It is especially useful when the problem combines an area or line constraint with several squared distances.

---

## Key Equations

:::equations
| Tool | Formula |
| --- | --- |
| Squared distance | $$AB^2=(\Delta x)^2+(\Delta y)^2$$ |
| Internal division | $$P=(nA+mB)/(m+n)$$ for $$AP:PB=m:n$$ |
| Projection onto direction $$\mathbf u$$ | $$\operatorname{proj}_{\mathbf u}\mathbf v=\frac{\mathbf v\cdot\mathbf u}{\mathbf u\cdot\mathbf u}\mathbf u$$ |
| Point-to-line distance | $$d=\lvert ax_0+by_0-c\rvert/\sqrt{a^2+b^2}$$ |
| Triangle area | $$K=\tfrac12\lvert u_1v_2-u_2v_1\rvert$$ |
| Pick | $$K=I+B/2-1$$ for a simple lattice polygon |
| Parametric intersection | $$t=\det(B-A,\mathbf v)/\det(\mathbf u,\mathbf v)$$ for nonparallel directions |
| General circle | $$x^2+y^2+Dx+Ey+F=0$$; center $$(-D/2,-E/2)$$ |
| Circle–line endpoints | $$F\pm\sqrt{R^2-d^2}\,\mathbf u$$ for a unit line direction $$\mathbf u$$ |
| Reflection | $$P'=P-2(\mathbf n\cdot P-c)\mathbf n/(\mathbf n\cdot\mathbf n)$$ |
| Right lattice triangle | $$I=(ab-a-b-\gcd(a,b)+2)/2$$ |
| Coordinate circumcenter | $$O=(c/2,(u^2+h^2-cu)/(2h))$$ for $$A=(0,0),B=(c,0),C=(u,h)$$ |
| Coordinate orthocenter | $$H=(u,u(c-u)/h)$$ in the same placement |
| Squared-distance decomposition | $$\sum_i\lVert P-A_i\rVert^2=n\lVert P-G\rVert^2+\sum_i\lVert G-A_i\rVert^2$$ |
:::
