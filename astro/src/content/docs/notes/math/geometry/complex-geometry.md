---
title: "Complex Geometry"
status: developing
progress: 68
sidebar:
  order: 5
description: "Competition geometry notes on complex coordinates, rotations, unit-circle chords, tangents, and triangle centers with worked examples."
---

## Points as Complex Numbers

Identify a point $$(x,y)$$ with the complex number $$z=x+iy$$. Then $$b-a$$ is the vector from $$A$$ to $$B$$, $$\lvert b-a\rvert$$ is the distance $$AB$$, and the midpoint has coordinate $$(a+b)/2$$. Conjugation $$z\mapsto\overline z$$ reflects the plane across the real axis.

This method is especially useful when a configuration has rotations or many points on one circle. Review [complex numbers](/notes/math/algebra/complex-numbers/) before using the formulas here.

---

## Rotations and Similarities

Multiplication by $$u=r(\cos\theta+i\sin\theta)$$ scales distances by $$r$$ and rotates directions by $$\theta$$. To rotate about a point $$c$$ rather than the origin, first subtract $$c$$ and then add it back:

$$
z'=c+u(z-c).
$$

In particular, multiplication by $$i$$ gives a counterclockwise quarter-turn.

<div class="theorem-box">

**Example.** Point $$A$$ has coordinate $$2+i$$. Rotate it $$90^\circ$$ counterclockwise about $$C=1+i$$ and find the image.

The vector from $$C$$ to $$A$$ is $$1$$. After rotation it becomes $$i$$, so

$$
a'=1+i+i\bigl((2+i)-(1+i)\bigr)=1+2i.
$$

</div>

A direct similarity has the form $$z\mapsto uz+v$$ with $$u\ne0$$. Given two corresponding distinct point pairs, determine $$u$$ from the ratio of their difference vectors and then find $$v$$ from either point.

---

## Collinearity and Perpendicularity

For distinct $$a,b$$, the points $$a,b,z$$ are collinear exactly when

$$
\frac{z-a}{b-a}\in\mathbb R.
$$

The quotient compares two directions: a real value means the directions differ by zero or $$180^\circ$$. Similarly, two lines with nonzero direction vectors $$u,v$$ are perpendicular exactly when $$u/v$$ is purely imaginary.

These conditions can be tested by conjugating. A number $$w$$ is real iff $$w=\overline w$$, and purely imaginary iff $$w=-\overline w$$.

<div class="theorem-box">

**Example.** Segments $$AB$$ and $$CD$$ have endpoints $$a=1+i$$, $$b=3+3i$$, $$c=2$$, and $$d=4-2i$$. Prove their lines are perpendicular.

Their direction vectors are $$b-a=2+2i$$ and $$d-c=2-2i$$. The quotient is

$$
\frac{2+2i}{2-2i}=i,
$$

which is purely imaginary. Thus the lines are perpendicular.

</div>

---

## Normalizing a Circle

A translation and uniform scaling can make any given circle the **unit circle** centered at zero, provided we restore lengths if the question asks for an absolute measurement. Points on this circle satisfy

$$
\lvert z\rvert=1\quad\Longrightarrow\quad\overline z=\frac1z.
$$

This replaces conjugates by reciprocals and often turns geometric relations into manageable algebra.

For distinct unit-circle points $$a,b$$, their chord line has equation

$$
z+ab\overline z=a+b.
$$

It follows by taking the collinearity quotient, setting it equal to its conjugate, and using $$\overline a=1/a$$ and $$\overline b=1/b$$. This is one real line equation written in complex form.

<div class="theorem-box">

**Example.** Find a Cartesian equation for the chord joining $$a=1$$ and $$b=i$$.

The chord equation is $$z+i\overline z=1+i$$. Write $$z=x+iy$$. Then

$$
z+i\overline z=(x+y)+i(x+y),
$$

so the line is $$x+y=1$$.

</div>

To intersect two chord lines, solve their equations as a linear system in $$z$$ and $$\overline z$$. A zero determinant signals parallel or coincident lines and must be treated separately.

---

## Tangents to the Unit Circle

At a unit point $$a$$, the radius is perpendicular to the tangent. The tangent equation is

$$
z+a^2\overline z=2a.
$$

One derivation starts with $$\operatorname{Re}(z\overline a)=1$$, expressing that the projection of $$z$$ onto the unit radius equals one. Multiply $$z\overline a+\overline z a=2$$ by $$a$$.

For two distinct, non-antipodal unit points $$a,b$$, the two tangents meet at

$$
p=\frac{2ab}{a+b}.
$$

Subtracting their tangent equations first finds $$\overline p=2/(a+b)$$, and substitution gives the formula. Antipodal points have $$a+b=0$$ and parallel tangents.

<div class="theorem-box">

**Example.** Find the intersection of the tangents to the unit circle at $$a=3/5+4i/5$$ and $$b=3/5-4i/5$$.

Both points have modulus one, $$ab=1$$, and $$a+b=6/5$$. Therefore

$$
p=\frac2{6/5}=\frac53.
$$

The intersection is the point $$(5/3,0)$$ on the real axis.

</div>

---

## Triangle Centers on the Unit Circle

For distinct triangle vertices $$a,b,c$$ on the unit circle, the circumcenter is zero, the centroid is $$g=(a+b+c)/3$$, and the orthocenter is

$$
h=a+b+c.
$$

To check the orthocenter formula, compare the altitude vector $$h-a=b+c$$ with the opposite side vector $$b-c$$. If $$b+c\ne0$$, the quotient's conjugate is

$$
\overline{\left(\frac{b+c}{b-c}\right)}
=\frac{1/b+1/c}{1/b-1/c}=-\frac{b+c}{b-c},
$$

so it is purely imaginary. This proves the corresponding altitude condition. The same argument applies cyclically. If $$b+c=0$$, then $$BC$$ is a diameter and the triangle is right at $$A$$; the proposed $$h=a$$ is the orthocenter directly.

<div class="theorem-box">

**Example.** A triangle on the unit circle has vertices $$a=1$$, $$b=i$$, and $$c=-1$$. Find its centroid and orthocenter.

The sum is $$i$$, so $$g=i/3$$ and $$h=i$$. The orthocenter is vertex $$B$$, consistent with the right angle subtending diameter $$AC$$.

</div>

:::strategy
Use complex coordinates when one circle contains many key points or when rotations dominate. Normalize that circle first, replace conjugates of its points by reciprocals, and translate each target into a real or purely imaginary quotient. Check denominators before using a compact intersection formula.
:::

## Intersecting Two Unit-Circle Chords

For unit points $$a,b,c,d$$, the chord lines satisfy

$$
z+ab\overline z=a+b,\qquad z+cd\overline z=c+d.
$$

Subtract the equations to solve for $$\overline z$$, then substitute back. When $$ab\ne cd$$, their intersection is

$$
z=\frac{ab(c+d)-cd(a+b)}{ab-cd}.
$$

The formula is most manageable when sums or products of the endpoints simplify. If the denominator vanishes, inspect the geometry: the lines may be parallel or coincident. Four distinct unit endpoints cannot determine coincident chord lines, so in that case the zero denominator means parallel lines.

<div class="theorem-box">

**Example.** Let $$a,b,c,d$$ be distinct points on the unit circle with $$ab=cd$$. Prove chords $$AB$$ and $$CD$$ are parallel.

Their equations have the same left-hand linear part, $$z+ab\overline z$$. Since their endpoint pairs are distinct, they are distinct lines. Therefore they are parallel.

The product condition encodes a direction, while the sum determines the location of that parallel line.

</div>

This explains why products of unit points recur in chord formulas. Their arguments add, recording the average angular direction of the endpoints.

---

## Reflection and Orthogonal Projection

For distinct unit points $$a,b$$, reflection of a point $$z$$ across chord line $$AB$$ is

$$
z'=a+b-ab\overline z.
$$

To verify the formula, note that its fixed points satisfy the chord equation, it preserves distances because $$\lvert ab\rvert=1$$, and applying it twice returns $$z$$. An isometric involution fixing a line pointwise is reflection in that line.

The perpendicular foot is the midpoint of a point and its reflection:

$$
d=\frac{z+a+b-ab\overline z}{2}.
$$

<div class="theorem-box">

**Example.** Reflect the origin across the chord joining $$1$$ and $$i$$, and find its perpendicular foot.

The reflection is $$1+i$$. The foot is $$(1+i)/2$$, or $$(1/2,1/2)$$ in Cartesian coordinates. This agrees with perpendicular projection onto the line $$x+y=1$$.

</div>

The same formula gives a useful orthocenter fact. If $$h=a+b+c$$, then reflecting it across $$BC$$ gives

$$
h'=b+c-bc\overline h=-\frac{bc}{a}.
$$

Its modulus is one, so the reflected orthocenter lies on the circumcircle. This supplies an algebraic proof valid for acute and obtuse triangles alike.

---

## A Full Simson-Line Proof

The **Simson line** is the line containing the three perpendicular feet from a circumcircle point to the triangle's side lines. The claim is about supporting lines, so a foot may lie outside a side segment.

<div class="theorem-box">

**Example.** Let $$P$$ lie on the circumcircle of triangle $$ABC$$. Prove its perpendicular feet to $$BC,CA,AB$$ are collinear.

Normalize the circumcircle to the unit circle. If $$P$$ is a vertex, two feet coincide there and the collinearity claim follows directly. Otherwise use the foot formula and $$\overline p=1/p$$:

$$
d=\frac{p+b+c-bc/p}{2},\quad
e=\frac{p+c+a-ca/p}{2},\quad
f=\frac{p+a+b-ab/p}{2}.
$$

Subtract before expanding products:

$$
d-e=\frac{(b-a)(p-c)}{2p},\qquad
f-e=\frac{(b-c)(p-a)}{2p}.
$$

Thus

$$
\frac{d-e}{f-e}
=\frac{(b-a)(p-c)}{(b-c)(p-a)}.
$$

Conjugating the right side replaces each unit point by its reciprocal. The factors in the denominators cancel, leaving exactly the same expression. The quotient is therefore real, proving $$D,E,F$$ collinear.

</div>

The proof shows a useful workflow: normalize, write each construction once, subtract coordinates, then test a quotient. Expanding every coordinate into real and imaginary parts at the start would hide the factor cancellation.

---

## Cross Ratios and Cyclicity

For four distinct complex points, the expression

$$
\frac{(a-c)(b-d)}{(b-c)(a-d)}
$$

is real exactly when the four points are concyclic or collinear. To interpret it, compare the arguments of $$(a-c)/(b-c)$$ and $$(a-d)/(b-d)$$. Realness means these directed angles agree modulo $$180^\circ$$, the equal-angle criterion for a common circle or line.

The collinear exception matters. A real cross ratio alone does not distinguish an ordinary circle from a straight line. In a noncollinear configuration, it is an efficient cyclicity test.

When all four points already lie on the unit circle, conjugating the quotient proves realness immediately. This is the same mechanism used in the Simson proof; an algebraic quotient can carry a familiar angle theorem without drawing the angles separately.

For a proof involving two circles, choose which one to normalize based on the number of points that lie on it. Normalizing the more useful circle is often a greater simplification than any subsequent algebraic trick.

---

## Tangency Chords and Polars

Let $$p$$ be outside the unit circle, and let $$a,b$$ be its two tangency points. Since $$p$$ lies on the tangent at $$a$$,

$$
p\overline a+\overline p\,a=2.
$$

The same equation holds with $$b$$. Consequently the line through the tangency points is

$$
z\overline p+\overline z\,p=2.
$$

This line is the **polar** of $$p$$ with respect to the unit circle. Its normal direction is the vector $$p$$, and its distance from the origin is $$1/\lvert p\rvert$$. It is therefore perpendicular to the line joining the center to $$P$$.

<div class="theorem-box">

**Example.** Find the tangency points of the two tangents from $$P=(2,1)$$ to the unit circle.

With $$p=2+i$$ and $$z=x+iy$$, the polar equation becomes $$2x+y=1$$. Intersect it with $$x^2+y^2=1$$:

$$
x^2+(1-2x)^2=1
\quad\Longrightarrow\quad
x(5x-4)=0.
$$

The tangency points are $$(0,1)$$ and $$(4/5,-3/5)$$.

Both lie on the circle, and the radius at each is perpendicular to the corresponding line from $$P$$, checking the construction.

</div>

This approach avoids solving two separate tangent-line slopes. The tangency condition first produces the chord joining the unknown points, after which one circle–line intersection finds both.

---

## Constructing Equilateral Triangles and Rotated Vectors

For an ordered segment $$AB$$, the two possible equilateral third vertices are

$$
c=\frac{a+b}{2}\pm\frac{i\sqrt3}{2}(b-a).
$$

The midpoint term places the vertex over the base midpoint, while multiplication by $$i$$ rotates the base vector by a quarter-turn and the coefficient supplies the equilateral altitude. The sign chooses a side of the directed line.

Equivalently, $$c-a=e^{\pm i\pi/3}(b-a)$$. This version is convenient when several triangles are constructed with the same orientation.

For example, if $$a=1+2i$$ and $$b=5+2i$$, the third vertices are $$3+(2+2\sqrt3)i$$ and $$3+(2-2\sqrt3)i$$. They lie symmetrically above and below the horizontal base.

In a larger configuration, choose an orientation and use it consistently. Mixing clockwise and counterclockwise constructions changes signs and may describe a different diagram.

---

## Managing Algebra in a Long Complex Proof

Keep coordinates factored whenever possible. Expressions such as $$(a-b)(p-c)$$ reveal cancellations and directions, while an expanded polynomial can conceal both. Use $$a\overline a=1$$ immediately for unit points, but do not apply that identity to an arbitrary intersection point.

Before using a quotient as a collinearity or perpendicularity test, check that its denominator is nonzero. Degenerate cases often correspond to coincident feet, parallel chords, or an endpoint placed at a vertex. Handle those geometrically rather than discarding them silently.

Finally, translate the conclusion back to geometry. A quotient equal to its conjugate establishes realness; realness establishes collinearity. Writing that last implication makes the purpose of the calculation clear to a reader learning the method.

:::strategy
For a circle-heavy proof, normalize once and reuse chord, reflection, and tangent formulas. Subtract coordinates before expanding them. For the target, choose a single algebraic test—real quotient, imaginary quotient, modulus one, or polar equation—and organize the calculation around it.
:::

---

## Area in Complex Coordinates

Complex multiplication also expresses signed area. For triangle vertices $$a,b,c$$,

$$
[ABC]=\frac12\left\lvert\operatorname{Im}\bigl(\overline{(b-a)}(c-a)\bigr)\right\rvert.
$$

Multiplying the conjugate of one vector by the other has imaginary part equal to their determinant. Its sign records orientation, and its absolute value gives twice the area.

For a polygon in boundary order, the shoelace formula becomes

$$
K=\frac12\left\lvert\operatorname{Im}\sum_j\overline{z_j}z_{j+1}\right\rvert,
$$

with the last index returning to the first.

<div class="theorem-box">

**Example.** Find the area of the triangle whose vertices are the three cube roots of unity.

Use $$a=1,b=-1/2+i\sqrt3/2,c=-1/2-i\sqrt3/2$$. The imaginary part of $$\overline{(b-a)}(c-a)$$ is $$3\sqrt3/2$$, so the area is $$3\sqrt3/4$$.

The triangle is equilateral on the unit circle, which gives an independent geometric check.

</div>

For an area equality, retaining signed imaginary parts can avoid absolute-value cases until orientation is settled. For a numerical area, the final absolute value is necessary: reversing the vertex order changes the sign but not the geometric area.

---

## Key Equations

:::equations
| Tool | Formula and conditions |
| --- | --- |
| Rotation/dilation about $$c$$ | $$z'=c+u(z-c)$$ |
| Collinearity | $$(z-a)/(b-a)\in\mathbb R$$, $$a\ne b$$ |
| Perpendicular directions | $$u/v\in i\mathbb R$$ for nonzero $$u,v$$ |
| Unit-circle conjugation | $$\overline z=1/z$$ when $$\lvert z\rvert=1$$ |
| Chord line | $$z+ab\overline z=a+b$$ for distinct unit $$a,b$$ |
| Tangent | $$z+a^2\overline z=2a$$ for unit $$a$$ |
| Two tangents | $$p=2ab/(a+b)$$ for distinct non-antipodal unit $$a,b$$ |
| Unit-circle triangle centers | $$o=0,\ g=(a+b+c)/3,\ h=a+b+c$$ |
| Chord intersection | $$z=[ab(c+d)-cd(a+b)]/(ab-cd)$$, $$ab\ne cd$$ |
| Unit-chord reflection | $$z'=a+b-ab\overline z$$ |
| Perpendicular foot | $$d=(z+a+b-ab\overline z)/2$$ |
| Cyclicity test | $$[(a-c)(b-d)]/[(b-c)(a-d)]\in\mathbb R$$ implies concyclic or collinear |
| Polar of $$p$$ | $$z\overline p+\overline z p=2$$ for the unit circle |
| Equilateral vertex | $$c=(a+b)/2\pm i\sqrt3(b-a)/2$$ |
| Complex triangle area | $$K=\tfrac12\lvert\operatorname{Im}(\overline{(b-a)}(c-a))\rvert$$ |
| Complex polygon area | $$K=\tfrac12\lvert\operatorname{Im}\sum_j\overline{z_j}z_{j+1}\rvert$$ |
:::
