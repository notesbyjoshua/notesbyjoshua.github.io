---
title: "Triangles"
status: developing
progress: 68
sidebar:
  order: 1
description: "Competition geometry notes on similarity, angle bisectors, area ratios, trigonometric laws, and triangle area formulas with worked examples."
---

## Angles, Congruence, and Similarity

For a triangle $$ABC$$, use $$a=BC$$, $$b=CA$$, and $$c=AB$$, with angles $$A,B,C$$ opposite those sides. Its angles sum to $$180^\circ$$, and an exterior angle equals the sum of the two nonadjacent interior angles.

In angle chasing, mark equal angles coming from parallel lines, isosceles triangles, or a shared angle. These equalities can establish **similarity**, which means corresponding angles are equal and corresponding sides have a common ratio. Two equal angles suffice for similarity. **Congruence** is stronger: corresponding sides and angles are equal, established for example by SSS, SAS, or ASA.

<div class="theorem-box">

**Example.** In triangle $$ABC$$, points $$D\in AB$$ and $$E\in AC$$ satisfy $$DE\parallel BC$$ and $$AD/AB=2/3$$. If $$BC=15$$ and $$[ABC]=54$$, find $$DE$$ and $$[ADE]$$.

Parallel lines give matching angles, so $$\triangle ADE\sim\triangle ABC$$ with scale factor $$2/3$$. Lengths scale by that factor and areas by its square:

$$
DE=\frac23(15)=10,\qquad[ADE]=\left(\frac23\right)^2(54)=24.
$$

Here $$[XYZ]$$ denotes the area of triangle $$XYZ$$.

</div>

<img class="note-img note-img--w480" src="/assets/math/competition/similar-triangles.svg" alt="Triangles ADE and ABC with DE parallel to BC and length scale two-thirds" loading="lazy" decoding="async" />

:::tip
Write corresponding vertices in matching order before using side ratios. A correct similarity with a reversed ratio can still give the wrong answer.
:::

---

## Special Right Triangles

An isosceles right triangle has side ratios $$1:1:\sqrt2$$. Cutting an equilateral triangle in half gives a $$30^\circ\! -60^\circ\! -90^\circ$$ triangle with ratios $$1:\sqrt3:2$$, listed opposite those angles.

<div class="theorem-box">

**Example.** An equilateral triangle has side length $$8$$. Find its altitude and area.

Its altitude bisects the base, creating a right triangle with hypotenuse eight and short leg four. The altitude is $$4\sqrt3$$, so the area is

$$
\frac12(8)(4\sqrt3)=16\sqrt3.
$$

</div>

When a diagram contains a perpendicular and a $$30^\circ$$ or $$45^\circ$$ angle, these ratios can avoid a longer trigonometric calculation.

---

## Angle Bisectors and Area Ratios

If the internal bisector of $$\angle A$$ meets $$BC$$ at $$D$$, the **angle bisector theorem** says

$$
\frac{BD}{DC}=\frac{AB}{AC}.
$$

To see why, compute $$[ABD]/[ACD]$$ in two ways. A shared altitude to line $$BC$$ gives $$BD/DC$$, while the sine area formula gives $$AB\sin\angle BAD/(AC\sin\angle DAC)=AB/AC$$.

More generally, triangles with the same altitude have areas proportional to their bases. If two sides of a smaller triangle lie along two sides of a larger triangle, the shared included angle gives an area ratio equal to the product of the two side ratios.

<div class="theorem-box">

**Example.** In triangle $$ABC$$, $$AB=9$$, $$AC=6$$, and $$BC=10$$. The internal angle bisector from $$A$$ meets $$BC$$ at $$D$$. Find $$BD$$ and $$[ABD]/[ACD]$$.

The side ratio is $$9:6=3:2$$, so $$BD=6$$ and $$DC=4$$. The two smaller triangles share the altitude from $$A$$, giving $$[ABD]/[ACD]=3/2$$.

</div>

---

## Laws of Sines and Cosines

The **Law of Sines** relates sides to opposite angles and the circumradius $$R$$:

$$
\frac a{\sin A}=\frac b{\sin B}=\frac c{\sin C}=2R.
$$

Use it when a side and its opposite angle are known. The **Law of Cosines** is useful for three sides or two sides and their included angle:

$$
a^2=b^2+c^2-2bc\cos A.
$$

At a right angle, it reduces to the Pythagorean theorem.

<div class="theorem-box">

**Example.** Two sides of a triangle have lengths $$5$$ and $$7$$, with included angle $$60^\circ$$. Find the third side and the area.

The Law of Cosines gives

$$
a^2=5^2+7^2-2(5)(7)\cos60^\circ=39,
$$

so the third side is $$\sqrt{39}$$. Using the same included angle,

$$
K=\frac12(5)(7)\sin60^\circ=\frac{35\sqrt3}{4}.
$$

</div>

If the Law of Sines gives $$\sin B=t$$, both $$B$$ and $$180^\circ-B$$ may have that sine. Check which angles fit the triangle rather than automatically taking only the acute angle.

---

## Area, Inradius, and Circumradius

Let $$K=[ABC]$$ and $$s=(a+b+c)/2$$. Useful area formulas are

$$
K=\frac12bc\sin A=\sqrt{s(s-a)(s-b)(s-c)}=rs=\frac{abc}{4R},
$$

where $$r$$ is the inradius. Heron's formula uses three side lengths. The relation $$K=rs$$ comes from splitting the triangle into three triangles with common height $$r$$ to the sides. The circumradius formula follows by substituting $$\sin A=a/(2R)$$ into the sine area formula.

<div class="theorem-box">

**Example.** A triangle has side lengths $$13,14,15$$. Find its area, inradius, and circumradius.

The semiperimeter is $$21$$, so Heron's formula gives

$$
K=\sqrt{21\cdot8\cdot7\cdot6}=84.
$$

Consequently,

$$
r=\frac{84}{21}=4,\qquad R=\frac{13\cdot14\cdot15}{4\cdot84}=\frac{65}{8}.
$$

</div>

---

## Cevians and Stewart's Theorem

A **cevian** joins a vertex to a point on the opposite side. If $$D\in BC$$, set $$BD=m$$, $$DC=n$$, and $$AD=d$$. **Stewart's theorem** states

$$
b^2m+c^2n=(m+n)(d^2+mn).
$$

It follows by applying the Law of Cosines to the two triangles at $$D$$; the cosine terms cancel because the two angles at $$D$$ are supplementary. This is useful when a cevian is neither perpendicular nor an angle bisector.

<div class="theorem-box">

**Example.** In a triangle, $$AB=13$$, $$AC=15$$, and $$BC=14$$. Find the length of the median from $$A$$.

A median has $$m=n=7$$. Stewart's theorem gives

$$
15^2(7)+13^2(7)=14(d^2+49).
$$

Thus $$d^2=148$$ and the median has length $$2\sqrt{37}$$.

</div>

:::strategy
For ratios, try similarity or shared-height areas. For an angle bisector, translate it into a side ratio. For numerical lengths, choose the Law of Cosines or Stewart before introducing coordinates. Compute the area once, then reuse it to find radii or altitudes.
:::

## Projections and a Derivation of Heron's Formula

An altitude need not land inside the opposite side. Using a signed projection avoids separate acute and obtuse cases. Place $$A=(0,0)$$, $$B=(c,0)$$, and $$C=(u,h)$$. The distance equations give

$$
u=\frac{b^2+c^2-a^2}{2c},\qquad h^2=b^2-u^2.
$$

The projection $$u$$ may be negative or exceed $$c$$, but the area formula $$K=c\lvert h\rvert/2$$ remains valid.

Squaring the area relation and substituting the projection gives

$$
16K^2=4b^2c^2-(b^2+c^2-a^2)^2.
$$

Factor the difference of squares:

$$
16K^2=(a+b+c)(-a+b+c)(a-b+c)(a+b-c).
$$

Replacing these factors by $$2s,2(s-a),2(s-b),2(s-c)$$ produces Heron's formula. This derivation also explains why the triangle inequalities are necessary: the semiperimeter differences must be positive for a nondegenerate triangle.

The method is useful when a side-length problem asks for both an altitude and a projection. Computing the signed projection once can supply both quantities without introducing an inverse trigonometric angle.

---

## Angle-Bisector Lengths and External Bisectors

The internal angle bisector from $$A$$ has length $$\ell_a$$ satisfying

$$
\ell_a^2=bc\left(1-\frac{a^2}{(b+c)^2}\right).
$$

To derive it, use the angle-bisector theorem to write $$BD=ac/(b+c)$$ and $$DC=ab/(b+c)$$. Substitute these two parts into Stewart's theorem and solve for $$AD^2$$. Another form is $$\ell_a=2bc\cos(A/2)/(b+c)$$.

The external angle bisector divides the opposite side line externally in the same ratio $$AB:AC$$. If the adjacent sides are equal, the external bisector is parallel to the opposite side and there is no finite intersection point. This is the geometric meaning of the zero denominator that would appear in an external-division formula.

<div class="theorem-box">

**Example.** A triangle has $$a=14,b=15,c=13$$. Find the internal angle-bisector length from $$A$$.

Here $$b+c=28$$, so

$$
\ell_a^2=195\left(1-\frac{196}{784}\right)=\frac{585}{4}.
$$

Thus $$\ell_a=3\sqrt{65}/2$$. The opposite-side division ratio is $$13:15$$, which is consistent with the side naming.

</div>

<div class="theorem-box">

**Example.** In triangle $$ABC$$, $$AB=10,AC=6,BC=8$$. The external angle bisector at $$A$$ meets $$BC$$ extended beyond $$C$$ at $$E$$. Find $$CE$$.

The external ratio gives $$BE/CE=10/6=5/3$$. Since $$BE=8+CE$$,

$$
\frac{8+CE}{CE}=\frac53,
$$

so $$CE=12$$ and $$BE=20$$. Using the internal relation $$BE+CE=BC$$ would contradict the diagram and the external location.

</div>

---

## Tangent Lengths and Half-Angle Formulas

If the incircle touches the sides, tangent segments from the same vertex are equal. Solving the three side-sum equations shows that the tangent length from $$A$$ is $$s-a$$, with cyclic versions at the other vertices.

The incenter and a tangency point form a right triangle, giving

$$
\tan\frac A2=\frac r{s-a}.
$$

Combining the cosine law with the half-angle identities also yields

$$
\sin\frac A2=\sqrt{\frac{(s-b)(s-c)}{bc}},\qquad
\cos\frac A2=\sqrt{\frac{s(s-a)}{bc}}.
$$

Take the positive square roots because a triangle's half-angles lie strictly between zero and ninety degrees.

<div class="theorem-box">

**Example.** A triangle has side lengths thirteen, fourteen, fifteen, and $$A$$ is opposite the side thirteen. Find $$\tan(A/2)$$.

Its area is eighty-four and semiperimeter twenty-one, giving inradius four. The tangent length from $$A$$ is $$s-a=8$$. Hence $$\tan(A/2)=4/8=1/2$$.

This uses the already known area and avoids solving for $$A$$ itself. Half-angle expressions can be simpler than the full angle.

</div>

These formulas are helpful when an angle bisector or incircle creates a half-angle that ordinary side-angle relations do not address directly.

---

## Excircles and Signed Areas

The $$A$$-excircle is tangent to side $$BC$$ and the extensions of the other two sides. Its center is the intersection of the internal angle bisector at $$A$$ with external bisectors at $$B,C$$. If its radius is $$r_a$$, signed area decomposition gives

$$
K=r_a(s-a).
$$

The positive area on one side is offset by the two triangle pieces on the extended sides. The resulting denominator is $$s-a$$ rather than $$s$$, which distinguishes an exradius from the inradius.

Thus

$$
r_a=\frac K{s-a},\qquad
\frac1{r_a}+\frac1{r_b}+\frac1{r_c}=\frac1r.
$$

The reciprocal identity follows because the three numerators $$s-a,s-b,s-c$$ sum to $$s$$. Heron's formula also gives $$r_ar_br_c=rs^2$$.

For sides thirteen, fourteen, fifteen, the three exradii are $$21/2,12,14$$, whereas the inradius is four. This provides a numerical check on the reciprocal identity.

---

## Radius and Area Inequalities

Triangle constraints often become easier through $$x=s-a,y=s-b,z=s-c$$. These are positive and satisfy $$a=y+z,b=z+x,c=x+y$$. In particular,

$$
abc=(x+y)(y+z)(z+x)\ge8xyz
$$

by applying two-variable AM–GM to the three factors. Since

$$
\frac Rr=\frac{abc}{4(s-a)(s-b)(s-c)},
$$

we obtain Euler's inequality $$R\ge2r$$, with equality exactly for an equilateral triangle.

<div class="theorem-box">

**Example.** Among triangles with fixed perimeter $$2s$$, find the largest possible area.

Heron's formula gives $$K^2=sxyz$$ with $$x+y+z=s$$. AM–GM gives $$xyz\le(s/3)^3$$, so

$$
K\le\frac{s^2}{3\sqrt3}.
$$

Equality requires $$x=y=z$$, equivalently equal side lengths. Such an equilateral triangle exists for every positive perimeter, so this is an attained maximum.

</div>

This is an optimization proof with both required parts: a universal bound and an admissible equality case. Merely guessing that symmetry makes the equilateral triangle largest would not establish the result.

---

## Choosing a Cevian or an Area Decomposition

A diagram can suggest many auxiliary lines, but a useful construction should create a relation the problem can exploit. Draw an altitude when products of a base and height appear, an angle bisector when ratios of adjacent sides appear, and a median when equal areas or midpoint coordinates matter.

If two triangles share a vertex and their opposite bases lie on the same line, compare their areas through the shared altitude. If they share an included angle instead, compare the products of the adjacent sides. These are different area comparisons and should not be interchanged.

For a point $$P$$ inside $$ABC$$, the three triangles $$PBC,PCA,PAB$$ partition the whole area. Their areas can serve as weights or coordinates. If the point approaches a side, one area tends to zero, which also explains how signed-area methods extend to exterior points.

A longer triangle problem often becomes short after computing the same area in two ways. Before expanding trigonometric expressions, list the available formulas for $$K$$ and check whether two of them connect exactly the quantities being asked for.

:::strategy
Keep the side naming consistent throughout a calculation. Use signed projections for obtuse configurations, tangent lengths for half-angles, Stewart for a general cevian, and semiperimeter substitutions for triangle inequalities. Whenever an extremum is claimed, verify that its equality configuration is a valid triangle.
:::

---

## Radius Identities for Trigonometric Expressions

Multiplying the three half-angle sine formulas gives

$$
\sin\frac A2\sin\frac B2\sin\frac C2
=\frac{(s-a)(s-b)(s-c)}{abc}=\frac r{4R}.
$$

The second equality follows from Heron's formula and $$abc=4RK$$. Thus $$r=4R\sin(A/2)\sin(B/2)\sin(C/2)$$.

Sum-to-product identities also give

$$
\cos A+\cos B+\cos C
=1+4\sin\frac A2\sin\frac B2\sin\frac C2
=1+\frac rR.
$$

For the thirteen-fourteen-fifteen triangle, $$r=4,R=65/8$$, so its three cosines sum to $$97/65$$. Finding each angle first would be unnecessary. Symmetric trigonometric expressions often have a simpler interpretation through radii.

---

## The Ambiguous SSA Case

Two sides and a nonincluded angle may determine two triangles. A sine equation provides two supplementary angle candidates, and both may fit the remaining angle sum.

<div class="theorem-box">

**Example.** A triangle has $$a=7,b=10,A=30^\circ$$. Find every possible length of side $$c$$.

Use the cosine law at $$A$$:

$$
49=100+c^2-10\sqrt3\,c.
$$

The quadratic has roots $$c=5\sqrt3\pm2\sqrt6$$. Both are positive, and both satisfy the triangle inequalities with seven and ten. They describe two distinct triangles.

Equivalently, the sine law gives $$\sin B=5/7$$. Both the acute and obtuse choices for $$B$$ leave a positive angle $$C$$, explaining the two algebraic roots geometrically.

</div>

A side-angle-side specification does not have this ambiguity because its included angle fixes the third side directly. The position of the supplied angle relative to the supplied sides is therefore essential, even when the same numerical data appear.

---

## The Sum of Squared Median Lengths

Setting the side divisions equal in Stewart's theorem gives

$$
m_a^2=\frac{2b^2+2c^2-a^2}{4}.
$$

Adding the three cyclic equations yields

$$
m_a^2+m_b^2+m_c^2=\frac34(a^2+b^2+c^2).
$$

For example, if a triangle's medians have lengths three, four, and five, the sum of its squared side lengths is $$4(9+16+25)/3=200/3$$.

This type of question asks for a symmetric quantity, so solving separately for all three sides would add work. The cyclic sum cancels the asymmetric terms automatically. The formula also provides a scale check: doubling every side doubles every median, so both squared sums must multiply by four.

---

## Key Equations

:::equations
| Tool | Formula |
| --- | --- |
| Similarity scale $$k$$ | Length ratio $$k$$; area ratio $$k^2$$ |
| Angle bisector | $$BD/DC=AB/AC$$ |
| Law of Sines | $$a/\sin A=b/\sin B=c/\sin C=2R$$ |
| Law of Cosines | $$a^2=b^2+c^2-2bc\cos A$$ |
| Areas | $$K=\tfrac12bc\sin A=\sqrt{s(s-a)(s-b)(s-c)}=rs=abc/(4R)$$ |
| Stewart | $$b^2m+c^2n=(m+n)(d^2+mn)$$ with $$m=BD,n=DC,d=AD$$ |
| Signed projection | $$u=(b^2+c^2-a^2)/(2c)$$ onto side $$AB=c$$ |
| Internal angle bisector | $$\ell_a^2=bc(1-a^2/(b+c)^2)$$ |
| Half-angle tangent | $$\tan(A/2)=r/(s-a)$$ |
| Half-angle sine | $$\sin(A/2)=\sqrt{(s-b)(s-c)/(bc)}$$ |
| Exradius | $$r_a=K/(s-a)$$; $$1/r=1/r_a+1/r_b+1/r_c$$ |
| Triangle bounds | $$R\ge2r$$ and $$K\le s^2/(3\sqrt3)$$ |
| Half-angle radius identity | $$r=4R\sin(A/2)\sin(B/2)\sin(C/2)$$ |
| Cosine sum | $$\cos A+\cos B+\cos C=1+r/R$$ |
| Median square sum | $$m_a^2+m_b^2+m_c^2=3(a^2+b^2+c^2)/4$$ |
:::
