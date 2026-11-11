---
title: "Circles and Cyclic Quadrilaterals"
status: developing
progress: 68
sidebar:
  order: 2
description: "Competition geometry notes on circle angles, tangents, power of a point, cyclic quadrilaterals, and Ptolemy's theorem with worked examples."
---

## Inscribed Angles and Cyclicity

An **inscribed angle** has its vertex on a circle and its sides along chords. It equals half the measure of the arc it intercepts, where the intercepted arc does not contain the vertex. A central angle subtending that same arc equals the full arc measure.

A quadrilateral is **cyclic** if all four vertices lie on one circle. In a convex cyclic quadrilateral, opposite angles sum to $$180^\circ$$. Conversely, a convex quadrilateral with supplementary opposite angles is cyclic.

<div class="theorem-box">

**Example.** Points $$A,B,C,D$$ occur in that order around a circle. If $$\angle ABC=112^\circ$$, find $$\angle ADC$$.

The angles are opposite angles of a convex cyclic quadrilateral, so

$$
\angle ADC=180^\circ-112^\circ=68^\circ.
$$

</div>

Angles subtending the same chord are equal when their vertices lie on the same side of that chord. If the vertices lie on opposite sides, the ordinary angles are supplementary. In longer proofs, directed angles modulo $$180^\circ$$ handle this orientation issue uniformly.

<div class="theorem-box">

**Example.** In an acute triangle $$ABC$$, let $$D$$ and $$E$$ be the feet of the altitudes from $$B$$ and $$C$$ onto $$AC$$ and $$AB$$. Prove $$B,C,D,E$$ are concyclic.

Both $$\angle BDC$$ and $$\angle BEC$$ are right angles. Thus $$D$$ and $$E$$ lie on the circle with diameter $$BC$$, so all four points are concyclic.

</div>

Finding a hidden cyclic quadrilateral often creates a new pair of equal angles, which can lead to similarity.

---

## Tangents and Tangent–Chord Angles

A tangent at $$T$$ is perpendicular to the radius $$OT$$. Tangent segments from the same external point have equal lengths because the right triangles formed with the center share a hypotenuse and a radius.

The angle between a tangent and a chord equals the inscribed angle subtending that chord in the corresponding opposite segment of the circle. Match the correct rays; supplementary angles can appear if a tangent ray is reversed.

<div class="theorem-box">

**Example.** The angle between a tangent ray at $$A$$ and chord $$AB$$ is $$42^\circ$$. A point $$C$$ on the circle lies in the alternate segment corresponding to that angle. Find $$\angle ACB$$.

The tangent–chord theorem gives $$\angle ACB=42^\circ$$. Equivalently, the intercepted arc has measure $$84^\circ$$, and the inscribed angle is half of it.

</div>

For a quadrilateral with an incircle tangent to all four sides, equal tangent lengths from each vertex imply that the sums of opposite side lengths are equal. This is Pitot's necessary condition; the side equality alone is not a universal test for a given quadrilateral to have an incircle.

---

## Power of a Point

For a circle with center $$O$$ and radius $$R$$, the **power** of a point $$P$$ is

$$
\operatorname{Pow}(P)=PO^2-R^2.
$$

It is positive outside, zero on, and negative inside the circle. If a secant from an external point meets the circle first at $$A$$ and then at $$B$$, then

$$
PA\cdot PB=\operatorname{Pow}(P).
$$

A tangent gives $$PT^2=\operatorname{Pow}(P)$$. Thus two secants from the same external point satisfy $$PA\cdot PB=PC\cdot PD$$. The farther distance is the full length from $$P$$, not merely the chord length.

<div class="theorem-box">

**Example.** A secant from external point $$P$$ meets a circle at $$A,B$$ in that order. If $$PA=4$$ and $$AB=5$$, find the tangent length $$PT$$.

The full secant length is $$PB=4+5=9$$. Therefore

$$
PT^2=PA\cdot PB=4\cdot9=36,
$$

so $$PT=6$$.

</div>

<img class="note-img note-img--w480" src="/assets/math/competition/power-secant.svg" alt="External point P, tangent PT of length six, and secant PAB with PA four and AB five" loading="lazy" decoding="async" />

For intersecting chords $$AB$$ and $$CD$$ meeting at an interior point $$P$$, ordinary positive lengths satisfy $$PA\cdot PB=PC\cdot PD$$. Both products equal $$R^2-PO^2$$, the negative of the signed power.

<div class="theorem-box">

**Example.** Two chords intersect inside a circle at $$P$$. If $$PA=3$$, $$PB=8$$, and $$PC=4$$, find $$PD$$.

The intersecting-chords relation gives $$3\cdot8=4\cdot PD$$, so $$PD=6$$.

</div>

---

## Ptolemy's Theorem

For a convex cyclic quadrilateral $$ABCD$$ with vertices in circular order,

$$
AC\cdot BD=AB\cdot CD+BC\cdot DA.
$$

The left side multiplies the diagonals, while the right side adds the products of opposite sides. Cyclicity is required for equality; an arbitrary quadrilateral instead satisfies Ptolemy's inequality.

<div class="theorem-box">

**Example.** A cyclic quadrilateral has side lengths $$AB=3$$, $$BC=4$$, $$CD=3$$, $$DA=4$$ and diagonal $$AC=5$$. Find $$BD$$.

Ptolemy gives

$$
5\cdot BD=3\cdot3+4\cdot4=25,
$$

so $$BD=5$$.

</div>

When only the four side lengths and the area are involved, **Brahmagupta's formula** gives

$$
K=\sqrt{(s-a)(s-b)(s-c)(s-d)},\qquad s=\frac{a+b+c+d}{2},
$$

for a convex cyclic quadrilateral. For sides $$4,5,6,7$$, the semiperimeter is eleven, so the area is $$\sqrt{7\cdot6\cdot5\cdot4}=2\sqrt{210}$$.

:::strategy
For angles, search for a shared chord or a hidden right-angle circle. For products of lengths through one point, try power of a point. For diagonals and four cyclic sides, try Ptolemy. Establish cyclicity before using a theorem that requires it.
:::

## Angles Made by Intersecting Chords and Secants

For two chords intersecting inside a circle, the angle between them is half the sum of the intercepted arcs of that angle and its vertical opposite. For two secants meeting outside, the angle is half the difference of the far and near intercepted arcs.

These formulas follow by introducing an auxiliary inscribed triangle and using either the exterior-angle theorem or the angle sum. The inside case adds two inscribed-angle contributions; the outside case subtracts one from the other. Drawing the intercepted arcs before substituting prevents a common sign error.

<div class="theorem-box">

**Example.** Two chords intersect inside a circle. The arcs intercepted by an angle and its vertical opposite have measures eighty and one hundred forty degrees. Find the angle.

Its measure is half their sum:

$$
\theta=\frac{80^\circ+140^\circ}{2}=110^\circ.
$$

The adjacent angle is seventy degrees. Using the outside-secant difference formula here would incorrectly give thirty degrees.

</div>

When tangents replace secants, treat the near and far endpoints as coinciding at the tangency point, or derive the angle through the perpendicular radii. In particular, the angle between two tangent rays from an external point is supplementary to the minor central angle between their tangency radii.

---

## Chords, Distances from the Center, and Arc Choice

A chord subtending an inscribed angle $$\theta$$ has length $$2R\sin\theta$$. The same chord is perpendicular to and bisected by the line joining its midpoint to the center. If the center-to-chord distance is $$d$$ and the chord length is $$\ell$$, then

$$
d^2+\left(\frac\ell2\right)^2=R^2.
$$

This converts a chord problem into a right triangle. It also proves that equal chords are equidistant from the center and that a longer chord lies closer to the center.

<div class="theorem-box">

**Example.** Parallel chords of lengths sixteen and twelve lie on opposite sides of the center of a circle of radius ten. Find their separation.

Their distances from the center are $$\sqrt{100-8^2}=6$$ and $$\sqrt{100-6^2}=8$$. Because they lie on opposite sides, their separation is $$6+8=14$$.

If they lay on the same side, the separation would instead be two. The length data alone do not determine which configuration is intended.

</div>

An angle can subtend either the minor or major arc, depending on its vertex. Keep track of which arc excludes that vertex. Equal sine values can correspond to supplementary inscribed angles, so a length equation alone may not identify the orientation.

---

## The Converse of Power of a Point

Power relations can prove cyclicity as well as calculate lengths. Suppose segments $$AB$$ and $$CD$$ intersect at an interior point $$P$$, with the two supporting lines distinct. If $$PA\cdot PB=PC\cdot PD$$, then the four endpoints are concyclic.

To see this, draw the circle through $$A,B,C$$ and let it meet ray $$PD$$ at $$E$$. The chord relation gives $$PC\cdot PE=PA\cdot PB=PC\cdot PD$$. Cancel the positive factor $$PC$$ to get $$PE=PD$$, hence $$E=D$$.

The location assumptions identify the correct second point. For external configurations, use signed distances or specify the endpoint order carefully.

<div class="theorem-box">

**Example.** Segments $$AB,CD$$ cross at $$P$$ with $$PA=2,PB=15,PC=5,PD=6$$. Prove their endpoints lie on a circle.

The two products are both thirty. The converse intersecting-chords theorem applies because $$P$$ lies inside both segments on distinct lines. Thus $$A,B,C,D$$ are concyclic.

Once cyclicity is established, angles subtending the same chord become available. A length product can therefore unlock an angle-chasing solution.

</div>

---

## A Similarity Proof of Ptolemy

The diagonal formula can be understood as splitting one diagonal into two pieces whose lengths are supplied by similar triangles.

<div class="theorem-box">

**Proof (Ptolemy's theorem).** Let $$ABCD$$ be a convex cyclic quadrilateral in that order. Choose $$E$$ on diagonal $$AC$$ so that $$\angle ABE=\angle DBC$$.

Angles subtending chord $$BC$$ give $$\angle BAE=\angle BDC$$. Thus $$\triangle ABE\sim\triangle DBC$$ and

$$
AE=\frac{AB\cdot CD}{BD}.
$$

Subtracting the equal angles at $$B$$ gives $$\angle EBC=\angle ABD$$. Also $$\angle ECB=\angle ADB$$ because both subtend chord $$AB$$. Hence $$\triangle EBC\sim\triangle ABD$$, giving

$$
EC=\frac{BC\cdot AD}{BD}.
$$

Add $$AE+EC=AC$$ and multiply by $$BD$$. The result is $$AC\cdot BD=AB\cdot CD+BC\cdot AD$$.

</div>

The constructed point is chosen to create two complementary similarities. In a difficult diagram, a useful auxiliary point often serves exactly this purpose: one part of a target segment accounts for one product, and the remainder accounts for the other.

<div class="theorem-box">

**Example.** Find the ratio of a diagonal to a side in a regular pentagon.

Let the side length be $$s$$ and diagonal length $$d$$. Four consecutive vertices form a cyclic quadrilateral with consecutive sides $$s,s,s,d$$ and both diagonals $$d$$. Ptolemy gives

$$
d^2=s^2+sd.
$$

Thus $$t=d/s>0$$ satisfies $$t^2=t+1$$. The positive root is $$(1+\sqrt5)/2$$, the golden ratio.

</div>

---

## Diagonals from Four Cyclic Sides

Let consecutive sides be $$a=AB,b=BC,c=CD,d=DA$$, and let $$e=AC$$. The cosine law in the two triangles sharing $$AC$$ gives

$$
e^2=a^2+b^2-2ab\cos B
=c^2+d^2+2cd\cos B,
$$

because the opposite angles are supplementary. Eliminating the cosine yields

$$
AC^2=\frac{(ac+bd)(ad+bc)}{ab+cd}.
$$

Rotating the side names gives

$$
BD^2=\frac{(ac+bd)(ab+cd)}{ad+bc}.
$$

Their product recovers Ptolemy, which is a useful algebraic check on the formulas.

<div class="theorem-box">

**Example.** A convex cyclic quadrilateral has consecutive side lengths two, three, four, five. Find the squares of its diagonals.

Substituting gives

$$
AC^2=\frac{23\cdot22}{26}=\frac{253}{13},\qquad
BD^2=\frac{23\cdot26}{22}=\frac{299}{11}.
$$

The product of the diagonal lengths is twenty-three, agreeing with $$2\cdot4+3\cdot5$$. The triangle inequalities for each diagonal are also satisfied, providing a geometric consistency check.

</div>

These formulas require the sides in circular order. Treating them as an unordered collection can attach the wrong products to the requested diagonal.

---

## The Arc Midpoint and the Incenter

If the internal angle bisector from $$A$$ meets the circumcircle again at $$D$$, then $$D$$ is the midpoint of the arc $$BC$$ not containing $$A$$. The equal angles $$BAD,DAC$$ subtend equal chords $$BD,DC$$.

A stronger relation is

$$
DB=DC=DI,
$$

where $$I$$ is the incenter. Since $$A,I,D$$ are collinear, $$\angle BID=90^\circ-C/2$$. Meanwhile $$\angle IBD=B/2+A/2=90^\circ-C/2$$. Thus $$DB=DI$$, and the equal-arc observation supplies $$DC=DB$$.

This lemma is useful when an incenter appears together with the circumcircle: it produces a new circle centered at an arc midpoint through two vertices and the incenter. The proof explains why the midpoint must be the arc not containing $$A$$; choosing the other arc changes the angle-bisector relation.

---

## Planning a Circle Configuration

Before calculating, identify which points are known to share each circle. A single right angle can identify a diameter circle; equal angles may suggest a cyclic quadrilateral; equal powers may identify a radical axis. These observations often turn a crowded diagram into a small sequence of standard steps.

For a numerical problem, decide whether the unknown is best controlled by an angle, a product, or a diagonal relation. For a proof, work backward from the desired conclusion: cyclicity suggests an angle or power criterion, tangency suggests a radius perpendicular or tangent–chord angle, and a length product suggests similarity or power of a point.

Keep positive lengths separate from signed powers. An interior chord product is positive even though the point's signed power is negative. Consistent signs prevent an otherwise valid algebraic relation from being used in the wrong configuration.

---

## Deriving Brahmagupta's Area Formula

Let consecutive sides of a convex cyclic quadrilateral be $$a,b,c,d$$. Splitting along the diagonal joining the vertices adjacent to angle $$B$$ gives

$$
K=\frac12ab\sin B+\frac12cd\sin D
=\frac12(ab+cd)\sin B,
$$

because $$B,D$$ are supplementary. The two cosine-law equations for the shared diagonal give

$$
\cos B=\frac{a^2+b^2-c^2-d^2}{2(ab+cd)}.
$$

Substituting $$\sin^2B=1-\cos^2B$$ yields

$$
16K^2=4(ab+cd)^2-(a^2+b^2-c^2-d^2)^2.
$$

Factoring this difference of squares produces $$16(s-a)(s-b)(s-c)(s-d)$$, proving Brahmagupta's formula.

For consecutive sides six, seven, eight, nine, the semiperimeter is fifteen and the area is $$\sqrt{9\cdot8\cdot7\cdot6}=12\sqrt{21}$$.

The supplementary-angle step is where cyclicity enters. Four side lengths alone do not determine an arbitrary quadrilateral's area, so the formula cannot be applied merely because all four sides are known. In a contest solution, establish the cyclic condition before using the side-only area expression.

---

## Key Equations

:::equations
| Tool | Formula and conditions |
| --- | --- |
| Inscribed angle | Half the intercepted arc not containing the vertex |
| Convex cyclic quadrilateral | $$\angle A+\angle C=180^\circ$$ |
| Signed power | $$\operatorname{Pow}(P)=PO^2-R^2$$ |
| External secant/tangent | $$PA\cdot PB=PT^2$$, with both secant distances measured from $$P$$ |
| Intersecting chords | $$PA\cdot PB=PC\cdot PD$$ for positive interior chord segments |
| Ptolemy | $$AC\cdot BD=AB\cdot CD+BC\cdot DA$$ |
| Brahmagupta | $$K^2=(s-a)(s-b)(s-c)(s-d)$$ for a convex cyclic quadrilateral |
| Intersecting-chord angle | Half the sum of the two intercepted arcs |
| External-secant angle | Half the difference of far and near intercepted arcs |
| Chord geometry | $$\ell=2R\sin\theta$$ and $$d^2+(\ell/2)^2=R^2$$ |
| Cyclic diagonals | $$AC^2=(ac+bd)(ad+bc)/(ab+cd)$$ for consecutive sides $$a,b,c,d$$ |
| Arc-midpoint lemma | $$DB=DC=DI$$ for the midpoint $$D$$ of arc $$BC$$ not containing $$A$$ |
:::
