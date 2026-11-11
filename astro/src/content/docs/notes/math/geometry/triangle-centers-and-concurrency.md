---
title: "Triangle Centers and Concurrency"
status: developing
progress: 68
sidebar:
  order: 3
description: "Competition geometry notes on triangle centers, Ceva, trigonometric Ceva, Menelaus, the Euler line, and the nine-point circle with examples."
---

## Four Triangle Centers

Several different constructions produce a triangle's “center.” Match each center to the relation it controls:

| Center | Construction | Useful property |
| --- | --- | --- |
| Centroid $$G$$ | Intersection of medians | Divides each median in the ratio $$2:1$$ from the vertex |
| Incenter $$I$$ | Intersection of internal angle bisectors | Equal perpendicular distances to the three side lines |
| Circumcenter $$O$$ | Intersection of perpendicular bisectors | Equal distances to the three vertices |
| Orthocenter $$H$$ | Intersection of altitudes | Each vertex-to-center line is perpendicular to the opposite side |

The incenter and centroid lie inside a nondegenerate triangle. The circumcenter and orthocenter can lie outside an obtuse triangle. In a right triangle, the circumcenter is the hypotenuse midpoint and the orthocenter is the right-angle vertex.

<div class="theorem-box">

**Example.** A right triangle has vertices $$A=(0,0)$$, $$B=(6,0)$$, and $$C=(0,8)$$. Find its four centers.

The centroid is the coordinate average, $$G=(2,8/3)$$. The hypotenuse midpoint is $$O=(3,4)$$, and the right-angle vertex gives $$H=(0,0)$$.

The hypotenuse has length ten, the area is twenty-four, and the semiperimeter is twelve. Thus the inradius is $$r=24/12=2$$. The incenter is two units from each coordinate axis, giving $$I=(2,2)$$.

</div>

---

## Ceva's Theorem

Three lines are **concurrent** if they pass through one point. For points $$D,E,F$$ in the interiors of $$BC,CA,AB$$, respectively, **Ceva's theorem** states that $$AD,BE,CF$$ are concurrent exactly when

$$
\frac{BD}{DC}\cdot\frac{CE}{EA}\cdot\frac{AF}{FB}=1.
$$

Ratios travel around the triangle in a consistent cycle. For external points, directed ratios are needed; the positive-length version here assumes the points are on the side segments.

If the three lines meet at $$P$$ inside the triangle, shared-altitude area ratios give

$$
\frac{BD}{DC}=\frac{[ABP]}{[ACP]},\quad
\frac{CE}{EA}=\frac{[BCP]}{[ABP]},\quad
\frac{AF}{FB}=\frac{[ACP]}{[BCP]}.
$$

Their product is one. The converse follows by intersecting two cevians and observing that the required ratio determines a unique point on the third side.

<div class="theorem-box">

**Example.** Points $$D,E,F$$ lie on the three side segments of triangle $$ABC$$. If $$BD/DC=2/3$$ and $$CE/EA=5/4$$, find the ratio $$AF/FB$$ that makes the cevians concurrent.

Ceva requires

$$
\frac23\cdot\frac54\cdot\frac{AF}{FB}=1,
$$

so $$AF/FB=6/5$$.

</div>

For the medians, all three ratios are one, so Ceva proves concurrency. For internal angle bisectors, the angle bisector theorem makes the product telescope to one, proving the existence of the incenter.

---

## Trigonometric Ceva

When the data are angles instead of lengths, convert the side ratios using the sine area formula. For internal cevians,

$$
\frac{BD}{DC}=\frac{AB\sin\angle BAD}{AC\sin\angle DAC}.
$$

The side-length factors cancel when the three ratios are multiplied, giving **trigonometric Ceva**:

$$
\frac{\sin\angle BAD}{\sin\angle DAC}
\frac{\sin\angle CBE}{\sin\angle EBA}
\frac{\sin\angle ACF}{\sin\angle FCB}=1.
$$

<div class="theorem-box">

**Example.** Three internal cevians have the first two sine ratios in the displayed formula equal to $$2$$ and $$1/3$$. What must the third ratio be for concurrency?

Their product must be one, so the third ratio is $$3/2$$. This establishes concurrency by trigonometric Ceva without finding the side division points.

</div>

---

## Menelaus and Collinearity

Three points are **collinear** if they lie on one line. **Menelaus's theorem** converts that conclusion into side ratios.

For $$D\in BC$$ and $$E\in CA$$ on the interiors of those segments, and $$F$$ on line $$AB$$ outside the segment, the points are collinear exactly when the positive lengths satisfy

$$
\frac{BD}{DC}\cdot\frac{CE}{EA}\cdot\frac{AF}{FB}=1.
$$

The same-looking formula has different geometric assumptions from Ceva. In a fully directed form, the product for Menelaus is $$-1$$ when the directed ratios are taken cyclically. Do not mix a directed factor with positive-length factors.

<div class="theorem-box">

**Example.** In triangle $$ABC$$, $$AB=6$$. Points $$D\in BC$$ and $$E\in CA$$ satisfy $$BD/DC=1/2$$ and $$CE/EA=1$$. Their line meets $$AB$$ extended beyond $$B$$ at $$F$$. Find $$BF$$.

Menelaus gives $$AF/FB=2$$. Since $$F$$ is beyond $$B$$, $$AF=AB+BF=6+BF$$. Therefore

$$
\frac{6+BF}{BF}=2\quad\Longrightarrow\quad BF=6.
$$

</div>

---

## Euler Line and Nine-Point Circle

In a non-equilateral triangle, $$O,G,H$$ lie on the **Euler line**, with the centroid between the other two and $$OG:GH=1:2$$. In vector coordinates,

$$
H=3G-2O.
$$

An equilateral triangle has $$O=G=H$$, so those coincident points do not determine a unique line.

The **nine-point circle** passes through the three side midpoints, the three altitude feet, and the three midpoints between $$H$$ and the vertices. Its center is the midpoint of $$OH$$ and its radius is $$R/2$$, where $$R$$ is the circumradius. These facts are useful when a midpoint configuration seems to have its own hidden circle.

<div class="theorem-box">

**Example.** For the right triangle with vertices $$(0,0),(6,0),(0,8)$$, find the nine-point center and radius, and check the Euler-line relation.

We found $$O=(3,4)$$, $$G=(2,8/3)$$, and $$H=(0,0)$$. Indeed,

$$
3G-2O=(6,8)-(6,8)=(0,0)=H.
$$

The circumradius is half the hypotenuse, so $$R=5$$. The nine-point center is $$(3/2,2)$$ and its radius is $$5/2$$.

</div>

:::strategy
For concurrence, try Ceva if side ratios are given and trigonometric Ceva if angles are given. For collinearity across the side lines, try Menelaus. For centers, use their defining equal distances or perpendicularities before introducing a formula.
:::

## Mass Points and Barycentric Coordinates

A point inside a triangle can be written as

$$
P=\frac{\alpha A+\beta B+\gamma C}{\alpha+\beta+\gamma},
\qquad \alpha,\beta,\gamma>0.
$$

The triple $$\alpha:\beta:\gamma$$ gives its **barycentric coordinates**. Scaling all three weights leaves the point unchanged. The same weights are proportional to the areas $$[PBC],[PCA],[PAB]$$, so the coordinate system has both an algebraic and geometric interpretation.

If $$AP$$ meets $$BC$$ at $$D$$, then

$$
\frac{BD}{DC}=\frac{\gamma}{\beta},\qquad
\frac{AP}{PD}=\frac{\beta+\gamma}{\alpha}.
$$

The weights on the side endpoints are inverse to the distances from the division point, just as in balancing a lever. This is the basis of the **mass-points** method.

<div class="theorem-box">

**Example.** Cevians $$AD,BE$$ meet at $$P$$ inside triangle $$ABC$$. Suppose $$BD/DC=2/3$$ and $$CE/EA=3/4$$. Find $$AP/PD$$ and $$[PBC]/[ABC]$$.

The first ratio requires $$\gamma/\beta=2/3$$. The second requires $$\alpha/\gamma=3/4$$. Compatible weights are $$\alpha:\beta:\gamma=3:6:4$$.

Therefore

$$
\frac{AP}{PD}=\frac{6+4}{3}=\frac{10}{3},\qquad
\frac{[PBC]}{[ABC]}=\frac3{13}.
$$

The weights must be chosen consistently across both side ratios. Assigning unrelated masses on the two sides would not describe one intersection point.

</div>

For exterior points, signed weights are allowed when their sum is nonzero. Positive-area intuition no longer applies unchanged, so start with the vector formula or directed areas. A zero weight means the point lies on the opposite side line.

---

## Coordinates of the Incenter

The incenter's perpendicular distances to the three sides all equal $$r$$. Thus its three subtriangle areas are $$ar/2,br/2,cr/2$$, proving

$$
I=\frac{aA+bB+cC}{a+b+c}.
$$

The barycentric coordinates are $$a:b:c$$, with each side length attached to its opposite vertex. This is a useful formula when coordinates of the vertices are available but solving two angle-bisector equations would be cumbersome.

The centroid has weights $$1:1:1$$ because its three subtriangle areas are equal. An excenter uses one negative side weight; the signs reflect which subtriangle lies outside. These signed formulas should be derived from the intended exterior region rather than recalled without checking the vertex labels.

<div class="theorem-box">

**Example.** Find the incenter of the triangle with vertices $$A=(0,0),B=(6,0),C=(0,8)$$ using side weights.

The opposite side lengths are $$a=10,b=8,c=6$$. Hence

$$
I=\frac{10(0,0)+8(6,0)+6(0,8)}{24}=(2,2).
$$

This agrees with the radius-two circle tangent to the coordinate axes and the hypotenuse.

</div>

---

## A Vector Proof of the Euler Line

Place the circumcenter at the origin and represent the vertices by vectors $$\mathbf a,\mathbf b,\mathbf c$$ of equal length $$R$$. Let $$\mathbf h=\mathbf a+\mathbf b+\mathbf c$$. Then

$$
(\mathbf h-\mathbf a)\cdot(\mathbf b-\mathbf c)
=(\mathbf b+\mathbf c)\cdot(\mathbf b-\mathbf c)
=\lVert\mathbf b\rVert^2-\lVert\mathbf c\rVert^2=0.
$$

Thus the point $$H$$ lies on the altitude from $$A$$. The cyclic equations show it lies on all three altitudes, so it is the orthocenter.

The centroid vector is $$\mathbf g=(\mathbf a+\mathbf b+\mathbf c)/3$$, hence $$\mathbf h=3\mathbf g$$. Restoring an arbitrary origin gives $$H=3G-2O$$. Therefore $$G$$ divides $$OH$$ with ratio $$OG:GH=1:2$$.

This proof simultaneously establishes altitude concurrency and the Euler-line relation. It also works for obtuse triangles, where a drawing that assumes the orthocenter is inside would be misleading.

---

## Why the Nine-Point Circle Has Half the Radius

The homothety centered at $$H$$ with factor one-half sends the circumcircle to a circle with center $$(H+O)/2$$ and radius $$R/2$$. It sends the three vertices to the midpoints of $$HA,HB,HC$$, proving those three midpoint claims.

It also contains the side midpoints. With $$O=0$$ and $$H=A+B+C$$, the antipode of $$A$$ on the circumcircle is $$-A$$. Its image under the same homothety is

$$
\frac{H-A}{2}=\frac{B+C}{2},
$$

the midpoint of $$BC$$. The other two follow cyclically.

For an altitude foot $$D$$ on $$BC$$, reflect $$H$$ across $$BC$$ to $$H'$$. The reflected point lies on the circumcircle: in an acute triangle, the supplementary angle relation follows from $$\angle BHC=180^\circ-A$$, and directed angles extend the argument to other configurations. Since $$D$$ is the midpoint of $$HH'$$, it is also in the homothetic image.

This proves all nine incidences and identifies the center and radius in one construction. It is often more efficient than finding the circle separately from three coordinate points.

---

## Contact Triangles and Gergonne Concurrency

Let the incircle touch $$BC,CA,AB$$ at $$D,E,F$$. Tangent lengths from a common vertex give

$$
BD=s-b,\quad DC=s-c,\quad
CE=s-c,\quad EA=s-a,\quad
AF=s-a,\quad FB=s-b.
$$

Their Ceva product is one, so $$AD,BE,CF$$ concur at the **Gergonne point**. The proof is short because the tangent-length expressions cancel cyclically.

For the touchpoints of the three respective excircles on the side segments, the side divisions reverse: on $$BC$$, the $$A$$-excircle gives $$BD=s-c,DC=s-b$$. The analogous Ceva product again equals one. The three vertex-to-extouch cevians concur at the **Nagel point**.

These are different centers. The contact points come from one incircle in the first construction and three different excircles in the second. Keeping the source circle attached to each point avoids mixing the two concurrency statements.

---

## Isogonal Cevians and Symmedians

Two lines through a vertex are **isogonal** if they are reflections of one another across the angle bisector. For internal cevians, reflecting exchanges the two angles adjacent to the bisector, so it inverts the sine ratio appearing in trigonometric Ceva.

If three internal cevians are concurrent, their three sine ratios have product one. Reflect all three in the corresponding angle bisectors; the new product is the reciprocal, still one. Trigonometric Ceva therefore proves that the reflected cevians are concurrent as well.

<div class="theorem-box">

**Example.** Reflect the three medians of a triangle across their respective angle bisectors. Prove the reflected lines are concurrent and find their barycentric intersection.

The reflected medians are called **symmedians**. Median concurrency and the isogonal argument establish their concurrency.

For a cevian through $$A$$, the sine-area relation is

$$
\frac{BD}{DC}=\frac cb\frac{\sin\angle BAD}{\sin\angle DAC}.
$$

Reflection inverts the sine ratio. Thus if the original side ratio is $$t$$, the reflected ratio is $$(c/b)^2/t$$. A median has $$t=1$$, so its symmedian divides $$BC$$ in ratio $$c^2:b^2$$.

The barycentric point $$a^2:b^2:c^2$$ has exactly these cyclic side ratios, hence is the common intersection.

</div>

This example combines a geometric transformation with an algebraic concurrency test. It is useful when a diagram has angle reflections but the side ratios are not initially visible.

---

## A Concurrency Proof Should Have a Target

Before choosing Ceva, identify the three side-intersection points and write their ratios in the same cyclic order. Before choosing trigonometric Ceva, identify the two angles at each vertex and keep the numerator orientation consistent.

For a configuration involving centers, first use their defining properties to obtain ratios or angles. Equal perpendicular distances suggest an incenter; equal vertex distances suggest a circumcenter; perpendicular vertex-side relations suggest an orthocenter. A center name is useful only after the needed relation has been extracted.

If two cevians already meet at a known point, a third-line claim can often be proved by calculating the side ratio of the line through that point. Mass points, areas, and Ceva are compatible ways to do this; choose whichever uses the supplied data with the fewest new quantities.

---

## A Coordinate Explanation of Menelaus' Sign

A line in barycentric coordinates has a homogeneous equation $$u\alpha+v\beta+w\gamma=0$$. Suppose its intersections with the side lines are finite and no coefficient vanishes.

On $$BC$$, the coordinate $$\alpha$$ is zero, so the directed side ratio is $$BD/DC=\gamma/\beta=-v/w$$. On $$CA$$ and $$AB$$, the corresponding ratios are $$-w/u$$ and $$-u/v$$. Their product is negative one.

This derives the directed Menelaus condition and explains why an external division must appear. Three interior side points have positive ratios and cannot be collinear. A line passing through two side interiors must meet the third supporting line externally unless it is parallel to that side.

For example, the line $$2\alpha+3\beta-\gamma=0$$ gives side ratios $$3,1/2,-2/3$$, whose product is negative one. The negative ratio marks the external intersection. Replacing it by its absolute value is legitimate only when switching explicitly to the positive-length version with the correct external-point assumptions.

If an intersection has coordinate sum zero, it is not a finite point in ordinary affine coordinates; geometrically the line is parallel to the corresponding side. Such a case should be handled separately rather than substituted into a division formula with a zero denominator.

The coordinate derivation also connects Ceva and Menelaus: Ceva tests concurrency of vertex lines, while Menelaus tests collinearity of side points. Their ratio products look similar, but their objects and sign conventions differ.

---

## Key Equations

:::equations
| Tool | Formula and conditions |
| --- | --- |
| Centroid | $$G=(A+B+C)/3$$; median ratio $$2:1$$ |
| Internal Ceva | $$(BD/DC)(CE/EA)(AF/FB)=1$$ |
| Trigonometric Ceva | $$\frac{\sin BAD}{\sin DAC}\frac{\sin CBE}{\sin EBA}\frac{\sin ACF}{\sin FCB}=1$$ for internal cevians |
| Menelaus | Same positive-length ratio product for two internal side points and one external side point |
| Euler line | $$H=3G-2O$$ |
| Nine-point circle | $$N=(O+H)/2$$ and radius $$R/2$$ |
| Barycentric point | $$P=(\alpha A+\beta B+\gamma C)/(\alpha+\beta+\gamma)$$ |
| Barycentric side ratio | $$BD/DC=\gamma/\beta$$ for $$D=AP\cap BC$$ |
| Incenter | $$I=(aA+bB+cC)/(a+b+c)$$ |
| Orthocenter vector | $$H=A+B+C-2O$$ |
| Symmedian point | Barycentric coordinates $$a^2:b^2:c^2$$ |
| Isogonal ratio | $$t\mapsto(c/b)^2/t$$ for a cevian from $$A$$ |
:::
