---
title: "Homothety"
sidebar:
  order: 3
status: developing
progress: 68
description: "Competition geometry notes on homotheties, centers of similarity, tangent circles, and spiral similarity with worked ratio and construction problems."
---

## Dilations About a Center

A **homothety** with center $$S$$ and nonzero scale factor $$k$$ sends every point $$X$$ to $$X'$$ satisfying

$$
\overrightarrow{SX'}=k\overrightarrow{SX}.
$$

For $$k>0$$, the points lie on the same ray from $$S$$. For $$k<0$$, they lie on opposite rays. Distances scale by $$\lvert k\rvert$$, areas by $$k^2$$, and corresponding lines are parallel unless they pass through $$S$$, in which case the line is preserved.

A homothety therefore packages many similar triangles into one transformation. It is useful when lines joining corresponding points appear concurrent or several corresponding segments are parallel.

<div class="theorem-box">

**Example.** A homothety centered at $$S=(1,2)$$ has scale factor $$-2$$. Find the image of $$X=(4,3)$$.

Use the vector from the center:

$$
X'=S-2(X-S)=(1,2)-2(3,1)=(-5,0).
$$

The negative sign puts the image on the opposite ray, at twice the distance from $$S$$.

</div>

<img class="note-img note-img--w480" src="/assets/math/competition/signed-homothety.svg" alt="Images of X under positive and negative scale factors about center S" loading="lazy" decoding="async" />

---

## Parallel Sides and Corresponding Points

If $$D\in AB$$ and $$E\in AC$$ satisfy $$DE\parallel BC$$, the triangles $$ADE$$ and $$ABC$$ are related by a homothety centered at $$A$$. Its scale factor from the larger triangle to the smaller one is $$AD/AB=AE/AC$$.

<div class="theorem-box">

**Example.** In triangle $$ABC$$, $$D,E$$ are the midpoints of $$AB,AC$$. The median from $$A$$ meets $$BC$$ at $$M$$. Find where $$AM$$ meets $$DE$$ and the resulting ratio along $$AM$$.

The homothety with center $$A$$ and factor $$1/2$$ sends $$B,C$$ to $$D,E$$. It sends the midpoint $$M$$ of $$BC$$ to the midpoint $$N$$ of $$DE$$. Thus $$A,N,M$$ are collinear and $$AN=AM/2$$, so $$AN:NM=1:1$$.

</div>

To find a center in an unfamiliar diagram, join two pairs of corresponding points. Their lines meet at the candidate center. Then verify that the signed scale factors agree; concurrency alone is not enough.

---

## Centers of Similarity of Two Circles

A homothety sends a circle with center $$O_1$$ and radius $$r_1$$ to a circle with center $$O_2$$ and radius $$r_2$$ if its scale factor is $$k=r_2/r_1$$ or $$k=-r_2/r_1$$.

For distinct centers and unequal radii, the positive factor gives the **external center of similarity**, outside the segment $$O_1O_2$$. The negative factor gives the **internal center**, between the centers. In vector notation,

$$
S_{\mathrm{ext}}=\frac{r_1O_2-r_2O_1}{r_1-r_2},\qquad
S_{\mathrm{int}}=\frac{r_1O_2+r_2O_1}{r_1+r_2}.
$$

These follow by solving $$O_2=S+k(O_1-S)$$. For equal radii and distinct centers, the positive correspondence is a translation, with no finite external homothety center. The internal center is still their midpoint.

<div class="theorem-box">

**Example.** Two circles have centers $$O_1=(0,0)$$, $$O_2=(12,0)$$ and radii $$2,4$$. Find both centers of similarity.

The scale factors are $$2$$ and $$-2$$. The formulas give

$$
S_{\mathrm{ext}}=(-12,0),\qquad S_{\mathrm{int}}=(4,0).
$$

From $$S_{\mathrm{ext}}$$, the center distances are twelve and twenty-four on the same ray. From $$S_{\mathrm{int}}$$, they are four and eight on opposite rays. Both have the required radius ratio.

</div>

When common external tangents exist and are nonparallel, they meet at the external center. Common internal tangents, when they exist, meet at the internal center. This follows because a tangent line through a homothety center maps to itself.

---

## Tangent Circles

The tangency point of two tangent circles is a homothety center. For external tangency, it is the internal center and the scale factor is negative. For internal tangency of unequal circles, it is the external center and the scale factor is positive.

<div class="theorem-box">

**Example.** Two circles of radii two and five are externally tangent at $$T$$. A line through $$T$$ meets the smaller circle again at $$A$$ and the larger again at $$B$$. Find $$TA:TB$$.

The homothety centered at $$T$$ with scale factor $$-5/2$$ sends the smaller circle to the larger. It sends $$A$$ to $$B$$ along the same line but on the opposite ray. Thus

$$
TA:TB=2:5.
$$

</div>

The correspondence tells us which points to pair. It also gives parallel tangents at $$A,B$$, a conclusion that may be useful in a longer configuration.

---

## Spiral Similarity

A **spiral similarity** combines a rotation and a dilation about one center. In complex coordinates,

$$
z'=s+u(z-s),
$$

where $$\lvert u\rvert$$ is the scale and $$\arg u$$ is the rotation angle. A homothety is the case where $$u$$ is a nonzero real number.

To send an ordered segment $$AB$$ to $$CD$$, first determine $$u=(d-c)/(b-a)$$. If $$u\ne1$$, solve

$$
s=\frac{c-ua}{1-u}.
$$

If $$u=1$$, the map is a translation; a nontrivial translation has no finite center.

<div class="theorem-box">

**Example.** Find the direct similarity sending $$A=0$$ to $$C=1$$ and $$B=1$$ to $$D=1+i$$, and determine its center.

The difference ratio is $$u=i$$, so the transformation is $$z'=iz+1$$. Its center solves $$s=is+1$$:

$$
s=\frac1{1-i}=\frac{1+i}{2}.
$$

The map is a $$90^\circ$$ counterclockwise rotation with scale factor one about $$(1/2,1/2)$$.

</div>

---

## Auxiliary Constructions

If a desired ratio is hard to read, construct an image that carries it. A parallel through a known point can create homothetic triangles, while a rotation can turn an angle condition into a segment correspondence.

<div class="theorem-box">

**Example.** Points $$X,Y,Z$$ form a triangle, and $$P,Q,R$$ are their images under a homothety of factor three. If $$[XYZ]=7$$, find $$[PQR]$$ and explain why the lines $$XP,YQ,ZR$$ are concurrent unless a corresponding point is fixed at the center.

Areas scale by the square of the factor, so $$[PQR]=9\cdot7=63$$. Each point and its image lie on a line through the homothety center, so the three joining lines pass through that center. If one point is itself the center, its image coincides with it and its joining line is not uniquely defined.

</div>

:::strategy
Look for parallel corresponding segments and equal ratios from a candidate center. With two circles, compare radius ratios and determine whether the point correspondence uses the same ray or opposite rays. If a rotation is also needed, switch from homothety to spiral similarity.
:::

## Composing Homotheties

A homothety with center $$S$$ and factor $$k$$ can be written as $$H(X)=kX+(1-k)S$$. Applying $$H_1$$ first and $$H_2$$ second gives

$$
H_2(H_1(X))=k_1k_2X+k_2(1-k_1)S_1+(1-k_2)S_2.
$$

If $$k_1k_2\ne1$$, this is another homothety, whose center is

$$
S=\frac{k_2(1-k_1)S_1+(1-k_2)S_2}{1-k_1k_2}.
$$

The coefficients of the two centers sum to one, so the new center lies on their connecting line. It may lie outside their segment because the coefficients need not be positive.

If $$k_1k_2=1$$, the result is a translation or the identity. This exceptional case is not a failure of the calculation; it is a different type of similarity with no unique finite center.

<div class="theorem-box">

**Example.** A point is rotated one hundred eighty degrees about $$A=(0,0)$$ and then one hundred eighty degrees about $$B=(3,1)$$. Find the combined transformation.

A half-turn is a homothety with factor negative one. The first sends $$X$$ to $$-X$$ and the second sends that point to $$2B+X$$. Thus the composition is the translation

$$
X\longmapsto X+(6,2).
$$

Reversing the order produces the opposite translation. Homotheties with different centers need not commute.

</div>

---

## Monge's Theorem for Three Circles

For three circles with pairwise distinct radii, their three external centers of similarity are collinear. This is **Monge's theorem**.

Let $$H_{12}$$ be the positive homothety mapping circle one to circle two and $$H_{23}$$ the positive homothety mapping circle two to circle three. Their factors are $$r_2/r_1$$ and $$r_3/r_2$$, so the composition has factor $$r_3/r_1$$ and maps circle one to circle three.

Because the first and third radii differ, the composition is a homothety rather than a translation. Its center lies on the line joining the centers of $$H_{12},H_{23}$$ by the composition formula. But its center is also the external center of similarity of circles one and three. Hence all three external centers are collinear.

This proof does not require the circles to be disjoint or to have visible common tangents. Their similarity centers exist algebraically for distinct radii. When equal radii occur, an external center may move to infinity, and the theorem's ordinary finite-point statement must be adjusted.

<div class="theorem-box">

**Example.** Three circles have distinct radii, and each pair has two nonparallel common external tangents. Prove the three intersections of those tangent pairs are collinear.

Each tangent-pair intersection is the corresponding external similarity center. Monge's theorem therefore gives the desired collinearity. The tangent construction identifies the centers; the composition argument proves the relation among them.

</div>

---

## Incircle and Excircle as Homothetic Circles

The incircle and the $$A$$-excircle are tangent to the two side lines through $$A$$. Their centers lie on the same internal angle-bisector ray from $$A$$, so a positive homothety centered at $$A$$ maps the incircle to the excircle.

Using $$r=K/s$$ and $$r_a=K/(s-a)$$, the factor is

$$
k=\frac{r_a}{r}=\frac{s}{s-a}.
$$

It follows that $$AI_a/AI=s/(s-a)$$. The tangency length from $$A$$ to the incircle is $$s-a$$, while the corresponding tangent length to the excircle is $$s$$, agreeing with the same scale.

<div class="theorem-box">

**Example.** A triangle has side lengths thirteen, fourteen, fifteen, with $$A$$ opposite thirteen. Find $$AI_a/AI$$.

The semiperimeter is twenty-one and $$s-a=8$$. Therefore the ratio is $$21/8$$. The center locations are on the same angle-bisector ray, so the homothety factor is positive rather than negative.

</div>

A common tangency point gives a different homothety center for two tangent circles. Before using a radius ratio, decide whether the proposed center is the vertex of a shared angle or the actual circle tangency point; the sign and point correspondence may differ.

---

## Common Tangent Segment Lengths

For circles with center distance $$d$$ and radii $$r_1,r_2$$, the segment between tangency points of a common external tangent has length

$$
L_{\mathrm{ext}}=\sqrt{d^2-(r_1-r_2)^2}.
$$

The radii to the tangent are parallel, so their difference is the perpendicular leg of a right triangle whose hypotenuse joins the centers. For a common internal tangent, the radii point to opposite sides, giving

$$
L_{\mathrm{int}}=\sqrt{d^2-(r_1+r_2)^2}.
$$

The expression under the square root also tests existence. A negative value means the proposed tangent type does not exist.

<div class="theorem-box">

**Example.** Two circles of radii three and twelve are externally tangent. Find the length between the tangency points on a common external tangent.

Their center distance is fifteen. Hence

$$
L=\sqrt{15^2-9^2}=12.
$$

More generally, external circle tangency gives $$d=r_1+r_2$$, so the formula becomes $$L=2\sqrt{r_1r_2}$$.

</div>

The tangent lines themselves intersect at the external similarity center when the radii differ. Thus a numerical tangent problem may offer both a right-triangle calculation and a homothetic ratio calculation; use whichever directly controls the unknown.

---

## Parallel-Sided Triangles and a Converse

If two nondegenerate triangles have their three corresponding sides parallel, they are related by a homothety or a translation. One way to see this is to compare two side vectors from a vertex.

Suppose $$A'B'=k\,AB$$ and $$A'C'=\ell\,AC$$ as directed vectors. Parallelism of the third sides requires $$\ell AC-kAB$$ to be parallel to $$AC-AB$$. Since $$AB,AC$$ are independent, the coefficients must agree, so $$k=\ell$$.

Thus the same scale factor governs the whole triangle. If it is not one, the map has a finite homothety center; if it is one, the triangles differ by a translation.

This converse is useful when the diagram gives parallelism rather than explicit ratios. Establish the common factor first, then use vertex-joining lines to locate the center.

---

## Rotations Combined with Dilations

A spiral similarity sends every vector from its center through the same rotation and scale. Therefore it sends the segment joining any two points to the segment joining their images with that same rotation and length factor.

For example, if a sixty-degree rotation about $$O$$ sends $$A$$ to $$B$$ and $$C$$ to $$D$$, it also sends vector $$AC$$ to vector $$BD$$. Consequently $$AC=BD$$ and their directed angle is sixty degrees. A configuration of two equilateral triangles sharing $$O$$ can often be simplified through this observation.

The orientation matters. If one triangle is erected clockwise and the other counterclockwise, a single rotation no longer maps both pairs. Label the directed angle or use a complex multiplier before inferring the segment relation.

For two direct similarities $$z\mapsto u_1z+v_1$$ and $$z\mapsto u_2z+v_2$$, the composition multiplier is $$u_2u_1$$. Its modulus multiplies scales and its argument adds rotations. If the multiplier equals one, inspect the translation term; otherwise the center solves the fixed-point equation.

---

## Building an Auxiliary Image

When a problem asks for a ratio between segments that do not belong to one obvious triangle, construct the image of one endpoint under a candidate homothety. The new segment may become parallel to a known segment, creating a similarity or an area comparison.

A useful construction should have a reason before it is drawn. A ratio of radii suggests mapping one circle to another. A midpoint suggests factor one-half. Two opposite rays suggest a negative factor. A fixed angle together with a scale suggests spiral similarity.

After making the construction, verify both the center line and the scale. Collinearity of $$S,X,X'$$ alone does not identify an image: the signed distance relation is still required. Likewise, parallel corresponding sides alone may describe a translation rather than a finite-center homothety.

:::checklist
- Choose corresponding points in a fixed order.
- Determine the signed scale factor from one pair.
- Verify that the same factor maps the remaining data.
- Treat product-one compositions separately.
- Restore absolute lengths or areas after any normalization.
:::

---

## Key Equations

:::equations
| Tool | Formula and conditions |
| --- | --- |
| Homothety | $$X'=S+k(X-S)$$, $$k\ne0$$ |
| Scale changes | Length factor $$\lvert k\rvert$$; area factor $$k^2$$ |
| External circle center | $$S_{\mathrm{ext}}=(r_1O_2-r_2O_1)/(r_1-r_2)$$, $$r_1\ne r_2$$ |
| Internal circle center | $$S_{\mathrm{int}}=(r_1O_2+r_2O_1)/(r_1+r_2)$$ |
| Spiral similarity | $$z'=s+u(z-s)$$, $$u\ne0$$ |
| Similarity center | $$s=(c-ua)/(1-u)$$ when $$u=(d-c)/(b-a)\ne1$$ |
| Composition factor | $$k=k_1k_2$$ |
| Composition center | $$S=[k_2(1-k_1)S_1+(1-k_2)S_2]/(1-k_1k_2)$$, $$k_1k_2\ne1$$ |
| Incircle–excircle factor | $$AI_a/AI=r_a/r=s/(s-a)$$ |
| External tangent length | $$L^2=d^2-(r_1-r_2)^2$$ |
| Internal tangent length | $$L^2=d^2-(r_1+r_2)^2$$ |
:::
