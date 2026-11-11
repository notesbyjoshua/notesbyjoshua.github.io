---
title: "Radical Axes and Inversion"
status: developing
progress: 68
sidebar:
  order: 8
description: "Competition geometry notes on radical axes, radical centers, circle inversion, orthogonality, and tangency with worked examples and strategy."
---

## Radical Axes: Equal Powers

For a circle with center $$O$$ and radius $$r$$, the power of $$P$$ is $$PO^2-r^2$$. The **radical axis** of two nonconcentric circles is the set of points with equal power to them. It is a line perpendicular to their line of centers.

In coordinates, subtracting the two power expressions cancels $$x^2+y^2$$ and leaves a linear equation. If the circles intersect at two points, their radical axis is the line through those points, the common chord line. It still exists when the circles do not intersect.

<div class="theorem-box">

**Example.** Find the radical axis of circles $$x^2+y^2=9$$ and $$(x-4)^2+y^2=1$$.

Equal powers give

$$
x^2+y^2-9=(x-4)^2+y^2-1.
$$

Canceling gives $$8x=24$$, so the radical axis is $$x=3$$. The circles are externally tangent at $$(3,0)$$, and this line is their common tangent there.

</div>

Concentric circles of different radii have no points of equal power, since their powers differ by a nonzero constant. Identical circles have equal power everywhere. These are exceptions to the ordinary line statement.

---

## Radical Center Theorem

If the radical axes of circles $$\omega_1,\omega_2$$ and $$\omega_2,\omega_3$$ intersect at $$P$$, then

$$
\operatorname{Pow}_{\omega_1}(P)=\operatorname{Pow}_{\omega_2}(P)
=\operatorname{Pow}_{\omega_3}(P).
$$

Thus $$P$$ also lies on the third radical axis. When the three ordinary axes are distinct, they are either concurrent or parallel. In configurations, this is a way to prove that three common-chord lines meet without finding the intersection point.

<div class="theorem-box">

**Example.** Three circles intersect pairwise in point pairs $$A,B$$; $$C,D$$; and $$E,F$$. Lines $$AB$$ and $$CD$$ meet at $$P$$. Prove $$P,E,F$$ are collinear.

Each common-chord line is a radical axis. The point $$P$$ therefore has equal power to the first and second circles and to the second and third circles. It has equal power to the first and third, so it lies on their common-chord line $$EF$$.

</div>

---

## Inversion of Points

An **inversion** with center $$O$$ and radius $$R>0$$ sends a point $$P\ne O$$ to the point $$P'$$ on the same ray satisfying

$$
OP\cdot OP'=R^2.
$$

Points inside the inversion circle move outside, points outside move inside, and points on the circle remain fixed. Applying the inversion twice returns the original point. The center itself has no finite image.

For an origin-centered inversion, the vector formula is

$$
\mathbf p'=\frac{R^2}{\lVert\mathbf p\rVert^2}\mathbf p.
$$

Unlike a homothety, inversion has a scale factor that depends on the point's distance from the center. It does not preserve ordinary length ratios.

<div class="theorem-box">

**Example.** Under inversion centered at the origin with radius two, find the image of $$P=(3,4)$$.

Since $$OP=5$$, the image distance is $$4/5$$. Scale the vector by $$R^2/OP^2=4/25$$:

$$
P'=\left(\frac{12}{25},\frac{16}{25}\right).
$$

</div>

<img class="note-img note-img--w480" src="/assets/math/competition/inversion-points.svg" alt="Inversion with radius two exchanges distances five and four-fifths from the center" loading="lazy" decoding="async" />

---

## Images of Lines and Circles

Inversion transforms circles and lines as follows, omitting the inversion center wherever needed:

| Original object | Image |
| --- | --- |
| Line through $$O$$ | The same line |
| Line not through $$O$$ | A circle through $$O$$ |
| Circle through $$O$$ | A line not through $$O$$ |
| Circle not through $$O$$ | Another circle not through $$O$$ |

The circle-to-line rule is a main reason to use inversion: a configuration of many circles through one point can become a configuration of lines.

<div class="theorem-box">

**Example.** Under unit inversion centered at the origin, find the image of the circle $$(x-1)^2+y^2=1$$.

The circle passes through the origin. Rewrite its equation as $$x^2+y^2=2x$$. Let the image coordinates be $$(X,Y)$$. Inversion is its own inverse, so

$$
x=\frac{X}{X^2+Y^2},\qquad y=\frac{Y}{X^2+Y^2}.
$$

Substituting gives $$1/(X^2+Y^2)=2X/(X^2+Y^2)$$, hence the image is the line $$X=1/2$$.

</div>

For a circle with center vector $$\mathbf c$$ and radius $$r$$, not passing through the inversion center, set $$\Delta=\lVert\mathbf c\rVert^2-r^2\ne0$$. Its image has center $$R^2\mathbf c/\Delta$$ and radius $$R^2r/\lvert\Delta\rvert$$. The signed denominator matters for the center's direction.

---

## Orthogonal Circles

Two circles are **orthogonal** if their tangents at an intersection are perpendicular. Their radii to that point are then perpendicular too, so if their center distance is $$d$$,

$$
d^2=R^2+r^2.
$$

A circle orthogonal to the inversion circle is preserved as a set by that inversion. This does not mean every point is fixed; only points on the inversion circle are fixed individually.

<div class="theorem-box">

**Example.** A unit inversion is centered at the origin. Show that the circle with center $$(\sqrt2,0)$$ and radius one maps to itself.

Its center distance satisfies $$d^2=2=1^2+1^2$$, so the circles are orthogonal. We can also check the image formula: $$\Delta=2-1=1$$, so both the center and radius remain unchanged.

</div>

---

## Tangency and Choosing the Inversion

Away from the inversion center, inversion preserves angle magnitudes between curves and preserves tangency. It reverses orientation, so directed-angle signs need care. Tangency at the center is a special case because that point has no finite image.

<div class="theorem-box">

**Example.** Two circles are tangent at $$O$$. Explain why inversion centered at $$O$$ sends them to parallel lines.

Both circles pass through $$O$$, so both images are lines. To identify their directions, place $$O$$ at the origin. A circle through the origin with center vector $$\mathbf c$$ has equation $$\lVert\mathbf x\rVert^2=2\mathbf c\cdot\mathbf x$$. Its image under radius-$$R$$ inversion is the line

$$
2\mathbf c\cdot\mathbf X=R^2.
$$

The two original centers and their tangency point are collinear, so the two center vectors are parallel. They are normals to the image lines, which must therefore be parallel. Distinct original circles give distinct lines.

</div>

:::strategy
For a collinearity or concurrency involving several circles, try radical axes first. Use inversion when many circles pass through one point or tangencies might become parallel lines. Choose the center to simplify the largest part of the diagram, and choose the radius to fix a useful point or exchange a useful pair.
:::

## Deriving the Circle-Image Formula

Place the inversion center at the origin. A circle with center vector $$\mathbf c$$ and radius $$r$$ has equation

$$
\lVert\mathbf x\rVert^2-2\mathbf c\cdot\mathbf x+\Delta=0,\qquad
\Delta=\lVert\mathbf c\rVert^2-r^2.
$$

Substitute $$\mathbf x=R^2\mathbf X/\lVert\mathbf X\rVert^2$$ and multiply by $$\lVert\mathbf X\rVert^2$$. The image equation is

$$
\Delta\lVert\mathbf X\rVert^2-2R^2\mathbf c\cdot\mathbf X+R^4=0.
$$

If $$\Delta\ne0$$, completing the square gives center $$R^2\mathbf c/\Delta$$ and radius $$R^2r/\lvert\Delta\rvert$$. If $$\Delta=0$$, the quadratic term disappears and the image is a line.

The sign of $$\Delta$$ is the power of the inversion center with respect to the original circle. A negative sign sends the image circle's center to the opposite ray. This is why the center formula has a signed denominator while the radius formula uses an absolute value.

Do not invert the old circle's center and assume it becomes the new center. Point inversion would give $$R^2\mathbf c/\lVert\mathbf c\rVert^2$$, which is generally different. Inversion is nonlinear, so it does not preserve midpoints or centers.

---

## Distances under Inversion

For two noncentral points $$P,Q$$ and their images,

$$
P'Q'=\frac{R^2PQ}{OP\cdot OQ}.
$$

The angle between the rays from $$O$$ remains the same. Applying the cosine law to the image triangle and using $$OP'=R^2/OP$$ and $$OQ'=R^2/OQ$$ proves the formula after factoring.

<div class="theorem-box">

**Example.** Under inversion of radius three, points satisfy $$OP=2,OQ=6,PQ=5$$. Find $$P'Q'$$.

The image distance is

$$
P'Q'=\frac{9\cdot5}{2\cdot6}=\frac{15}{4}.
$$

This is not obtained by multiplying every original length by one common scale. The factor depends on both endpoint distances to the inversion center.

</div>

The distance formula is especially useful when an inverted diagram simplifies incidence but the original question asks for a length. Keep track of the endpoint distances so the final result can be translated back.

---

## Ptolemy's Inequality from Inversion

For any four distinct points in the plane, Ptolemy's inequality is

$$
AC\cdot BD\le AB\cdot CD+AD\cdot BC.
$$

Inversion turns this four-point product relation into an ordinary triangle inequality.

<div class="theorem-box">

**Proof (Ptolemy's inequality by inversion).** Invert about $$A$$ with radius one. The triangle inequality for the other three images gives

$$
B'D'\le B'C'+C'D'.
$$

Using the image-distance formula,

$$
\frac{BD}{AB\cdot AD}
\le
\frac{BC}{AB\cdot AC}+\frac{CD}{AC\cdot AD}.
$$

Multiply by the positive product $$AB\cdot AC\cdot AD$$ to obtain the desired inequality.

If $$A,B,C,D$$ lie on a circle in convex circular order, the inversion sends the circle through $$A$$ to a line, with $$C'$$ between $$B',D'$$. The triangle inequality becomes equality, recovering Ptolemy's theorem.

</div>

This proof explains both the inequality and its cyclic equality case through one transformation. It is a good example of choosing an inversion center to turn a target algebraic expression into a simpler geometric statement.

---

## Choosing an Inversion That Fixes a Circle

A circle is preserved as a set when it is orthogonal to the inversion circle. If the desired fixed circle has center $$C$$ and radius $$r$$, choose an inversion center $$O$$ outside it and set

$$
R^2=OC^2-r^2.
$$

The orthogonality condition is then satisfied automatically. The right side must be positive because an ordinary inversion radius is real and nonzero.

If two circles have equal positive power at $$O$$, the same choice of $$R$$ fixes both. Thus points on their radical axis can serve as centers of inversions preserving both circles, provided those points lie outside both.

This links two topics that initially look unrelated: radical axes select centers with equal powers, while orthogonality turns that common power into an inversion radius.

<div class="theorem-box">

**Example.** A point $$O$$ has power nine to each of two circles. Find an inversion centered at $$O$$ preserving both circles.

Choose radius three. For each circle, the center-distance squared minus its radius squared equals nine, so it is orthogonal to the inversion circle. Both are preserved as sets.

Individual points generally move; preserving a circle does not mean fixing each of its points.

</div>

---

## A Tangent-Circle Problem Reduced to a Strip

When two circles are tangent at the inversion center, their images are parallel lines. A third circle tangent to both becomes a circle tangent to both lines, so its radius is determined by the strip width.

<div class="theorem-box">

**Example.** Two unit circles have centers $$(-1,0)$$ and $$(1,0)$$. A third circle lies above the horizontal axis, is externally tangent to both, and passes through $$(0,2)$$. Find its center and radius.

The equal tangency distances force its center onto the vertical axis. Invert about the origin with radius one. The two unit circles, each passing through the origin, become the lines $$X=-1/2$$ and $$X=1/2$$.

The third circle does not contain the origin and maps to a circle inside the strip, tangent to both lines. Its radius is one-half and its center is $$(0,t)$$. The point $$(0,2)$$ maps to $$(0,1/2)$$, so $$t=0$$ or $$1$$.

The value zero would make the image circle contain the origin, contrary to the original circle's exterior relation to the inversion center. Therefore the image center is $$(0,1)$$.

Its power at the origin is $$1-1/4=3/4$$. Invert its center and radius using the circle-image formula to obtain original center $$(0,4/3)$$ and radius $$2/3$$.

The center distance to either unit-circle center is $$\sqrt{1+16/9}=5/3=1+2/3$$, confirming external tangency. The top point is indeed $$(0,2)$$.

</div>

The strip construction determines the radius immediately. The remaining point condition determines the center, and the inverse formula restores the original circle. Each datum has a separate role.

---

## Coaxal Circle Families

A collection of circles with the same radical axis is called coaxal. If two circle equations have normalized quadratic part $$x^2+y^2$$, a linear combination whose coefficients sum to one has that same quadratic part. Wherever it represents a real circle, it belongs to the family through the original common points.

For example,

$$
F_1=x^2+y^2-4x,\qquad F_2=x^2+y^2-6y
$$

have radical axis $$2x=3y$$. Every equation $$(1-t)F_1+tF_2=0$$ passes through their common points. Subtracting any two distinct members again gives the same radical axis.

A useful consequence is that one known equal-power point can replace a long coordinate intersection. If a point lies on the common radical axis, its power agrees across the entire family. This can prove an unexpected tangency length or locate a radical center.

Be careful with arbitrary linear combinations: the quadratic coefficient can vanish, producing a line, or the completed-square radius can fail to be positive. Normalize and check the resulting object rather than assuming every combination is an ordinary circle.

---

## Choosing the Center and Radius Strategically

Choose the center based on incidence first. A common point of many circles converts them to lines. A common tangency point creates parallel lines. A point with equal positive powers can preserve selected circles. These choices simplify different features and should not be interchanged automatically.

Choose the radius second. It can fix a useful point, exchange two points with known distance product, or preserve an orthogonal circle. Often unit radius simplifies algebra, but another radius can make several important image distances integral.

Finally, record the missing point. A circle through the inversion center becomes a line with that central point omitted; a line image is completed geometrically by the point at infinity only in an extended-plane interpretation. For ordinary contest solutions, it is enough to state that the center has no finite image and handle tangency there separately.

:::strategy
Identify which circles pass through the proposed center, which lie outside it, and which tangencies occur at it. Use the image-distance formula to return to lengths, equal powers to select invariant circles, and a final substitution to verify that an inverted candidate matches the original configuration.
:::

---

## Key Equations

:::equations
| Tool | Formula and conditions |
| --- | --- |
| Power | $$\operatorname{Pow}(P)=PO^2-r^2$$ |
| Radical axis | $$\operatorname{Pow}_1(P)=\operatorname{Pow}_2(P)$$ |
| Point inversion | $$OP\cdot OP'=R^2$$, $$P\ne O$$ |
| Vector inversion | $$\mathbf p'=R^2\mathbf p/\lVert\mathbf p\rVert^2$$ |
| Circle image | Center $$R^2\mathbf c/\Delta$$, radius $$R^2r/\lvert\Delta\rvert$$, $$\Delta=\lVert\mathbf c\rVert^2-r^2\ne0$$ |
| Orthogonality | $$d^2=R^2+r^2$$ |
| Inverted distance | $$P'Q'=R^2PQ/(OP\cdot OQ)$$ |
| Ptolemy inequality | $$AC\cdot BD\le AB\cdot CD+AD\cdot BC$$ |
| Fixed-circle inversion | $$R^2=OC^2-r^2>0$$ |
| Coaxal pencil | $$(1-t)F_1+tF_2=0$$ for normalized circle equations, where it defines a real circle |
:::
