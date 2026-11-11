---
title: "Distributions and Lattice Paths"
status: developing
progress: 68
sidebar:
  order: 2
description: "Competition math notes on stars and bars, bounded distributions, repeated objects, lattice paths, and Catalan numbers with worked examples."
---

## Distributing Identical Objects

**Stars and bars** counts distributions of identical objects into distinct boxes. Equivalently, it counts integer solutions of

$$
x_1+\cdots+x_k=n,\qquad x_i\ge0.
$$

Write $$n$$ stars in a row and insert $$k-1$$ bars to separate the boxes. Adjacent bars mean an empty box. Choosing the positions of the bars among $$n+k-1$$ positions gives

$$
\binom{n+k-1}{k-1}.
$$

If the objects are distinct, assigning each object to a box instead gives $$k^n$$. If the boxes are indistinguishable, ordinary stars and bars does not apply.

<div class="theorem-box">

**Example.** Twelve identical candies are distributed to four named students, with empty shares allowed. How many distributions are possible?

A distribution is determined by the four nonnegative candy counts. Stars and bars gives

$$
\binom{12+4-1}{4-1}=\binom{15}3=455.
$$

</div>

---

## Lower and Upper Bounds

For lower bounds $$x_i\ge l_i$$, first give each box its required minimum. Setting $$y_i=x_i-l_i$$ leaves a nonnegative distribution of $$n-\sum l_i$$ objects. If that total is negative, there are no solutions.

<div class="theorem-box">

**Example.** Find the number of integer solutions to $$x+y+z=14$$ with $$x\ge2$$, $$y\ge3$$, and $$z\ge1$$.

Set $$u=x-2$$, $$v=y-3$$, and $$w=z-1$$. Then $$u,v,w\ge0$$ and $$u+v+w=8$$. Hence the count is

$$
\binom{10}2=45.
$$

</div>

Upper bounds need a different correction. Count all nonnegative solutions, then exclude the cases where a variable exceeds its bound. If two violations can occur together, inclusion–exclusion restores their overlap.

<div class="theorem-box">

**Example.** How many integer solutions satisfy $$x+y+z=8$$ and $$0\le x,y,z\le4$$?

There are $$\binom{10}2=45$$ unrestricted solutions. For a violation $$x\ge5$$, set $$x'=x-5$$; the remaining total is $$3$$, giving $$\binom52=10$$ solutions. The same count holds for $$y$$ and $$z$$.

Two violations would require a total of at least $$10$$, so none overlap. The answer is

$$
45-3(10)=15.
$$

</div>

For uniform upper bounds $$0\le x_i\le u$$, the general count is

$$
\sum_{j=0}^k(-1)^j\binom kj\binom{n-j(u+1)+k-1}{k-1},
$$

where a term is zero when $$n-j(u+1)<0$$. The shift is $$u+1$$ because that is the first forbidden value.

---

## Repeated Objects and Gaps

An arrangement with $$n_i$$ identical objects of type $$i$$ has $$n!/(\prod n_i!)$$ possibilities. For restrictions such as “no two adjacent,” arrange the other objects first and place the restricted objects in gaps.

<div class="theorem-box">

**Example.** How many arrangements of four identical A's and three identical B's have no two B's adjacent?

Place the A's first:

$$
\_\ A\ \_\ A\ \_\ A\ \_\ A\ \_.
$$

There are five gaps. Choose three different gaps for the B's, giving $$\binom53=10$$ arrangements. A gap receives at most one B, exactly enforcing the restriction. Because all B's are identical, no additional factor of $$3!$$ is needed.

</div>

---

## Lattice Paths and Waypoints

A path from $$(0,0)$$ to $$(a,b)$$ using only unit right and up steps has $$a+b$$ moves. Choose which $$b$$ moves are up steps:

$$
\#\text{paths}=\binom{a+b}b.
$$

To force a waypoint, count the path before it and after it separately. To forbid a waypoint, subtract the paths that pass through it.

<div class="theorem-box">

**Example.** How many right/up paths from $$(0,0)$$ to $$(5,4)$$ avoid $$(2,2)$$?

There are $$\binom94=126$$ paths in total. A path through $$(2,2)$$ has $$\binom42$$ choices before that point and $$\binom52$$ afterward. Thus the answer is

$$
126-\binom42\binom52=126-60=66.
$$

</div>

---

## Restricted Paths and Catalan Numbers

Paths from $$(0,0)$$ to $$(n,n)$$ that never go above $$y=x$$ are counted by the **Catalan number**

$$
C_n=\frac1{n+1}\binom{2n}n.
$$

To derive it, start with all $$\binom{2n}n$$ paths. For a bad path, reflect the initial segment up to its first arrival at $$y=x+1$$ by exchanging right and up moves. This transforms it into a path with $$n+1$$ right moves and $$n-1$$ up moves. The transformation is reversible by reflecting up to the first arrival at $$x=y+1$$. Thus there are $$\binom{2n}{n-1}$$ bad paths, and

$$
C_n=\binom{2n}n-\binom{2n}{n-1}=\frac1{n+1}\binom{2n}n.
$$

<div class="theorem-box">

**Example.** How many strings containing four opening and four closing parentheses are properly balanced?

Map an opening parenthesis to a right step and a closing parenthesis to an up step. A balanced prefix has at least as many opens as closes, so its path stays on or below $$y=x$$. This is a reversible correspondence, giving

$$
C_4=\frac15\binom84=14.
$$

</div>

:::strategy
Use stars and bars for unrestricted identical-object distributions, shifts for minimums, and inclusion–exclusion for maximums. For path restrictions, first try a waypoint decomposition or a reflection. Translate the restriction into the new model before applying its formula.
:::

## Generating Functions for Bounded Distributions

A generating function can record the allowed size of each box separately. If box $$i$$ may receive amounts in a set $$S_i$$, assign it the polynomial or series $$F_i(x)=\sum_{j\in S_i}x^j$$. Then

$$
[x^n]\prod_{i=1}^kF_i(x)
$$

counts distributions totaling $$n$$. Selecting one term from each factor selects the amount in each box, and multiplying adds those amounts through the exponent.

This method is particularly useful when the boxes have different restrictions, such as one receiving an even amount and another receiving at least two. The restrictions belong in the factors before any algebra is performed.

For an unrestricted nonnegative box, the factor is $$1/(1-x)$$. A box receiving at least $$l$$ contributes $$x^l/(1-x)$$, while a box receiving between zero and $$u$$ contributes $$(1-x^{u+1})/(1-x)$$. The numerator in the bounded case is exactly the algebraic form of excluding a first forbidden amount.

<div class="theorem-box">

**Example.** Three fair six-sided dice are rolled. Find the number of ordered outcomes whose sum is ten.

Each die contributes $$x+x^2+\cdots+x^6$$, so the desired count is

$$
[x^{10}]\left(\frac{x(1-x^6)}{1-x}\right)^3
=[x^7](1-3x^6+3x^{12}-x^{18})(1-x)^{-3}.
$$

Only the constant and $$x^6$$ numerator terms can contribute. Since $$[x^r](1-x)^{-3}=\binom{r+2}2$$, the answer is

$$
\binom92-3\binom32=36-9=27.
$$

The factors correspond to named dice, so outcomes with different orders are distinct. The method would need adjustment if only the multiset of face values were counted.

</div>

---

## Different Upper Bounds and Capacity Checks

For unequal upper bounds $$x_i\le u_i$$, declare the violation for box $$i$$ to be $$x_i\ge u_i+1$$. For a chosen set of violating boxes, subtract the corresponding quantities $$u_i+1$$ and count the residual nonnegative solutions. Intersections with negative residual total contribute zero.

Before computing a long sum, check capacity: if $$n>\sum_i u_i$$ there are no distributions. Likewise, lower bounds may already exceed the available total. These checks can collapse a problem before inclusion–exclusion begins.

<div class="theorem-box">

**Example.** Count solutions to $$x+y+z=10$$ with $$0\le x\le3$$, $$0\le y\le4$$, and $$z\ge2$$.

Set $$w=z-2$$, leaving $$x+y+w=8$$. The unrestricted count is $$\binom{10}2=45$$. A violation of the first bound shifts four units, giving $$\binom62=15$$ solutions. A violation of the second shifts five units, giving $$\binom52=10$$ solutions.

Both violations together require at least nine units, more than eight, so their intersection is empty. The answer is $$45-15-10=20$$.

</div>

An upper bound is not handled by simply replacing the total in stars and bars. It restricts individual coordinates, so the correction depends on which boxes violate it. The generating-function and inclusion–exclusion approaches are two descriptions of that same correction.

---

## Indistinguishable Boxes and Integer Partitions

Stars and bars assumes the boxes are labeled. If the boxes are indistinguishable, permuting their contents does not give a new distribution. Dividing a labeled count by $$k!$$ is generally invalid because repeated box sizes have smaller symmetry orbits.

An **integer partition** writes a positive integer as an unordered sum of positive parts. A distribution into exactly $$k$$ nonempty indistinguishable boxes corresponds to a partition into exactly $$k$$ parts. To list them without repetition, put the parts in nondecreasing order.

<div class="theorem-box">

**Example.** Eight identical objects are put into three nonempty indistinguishable boxes. Find the number of distributions.

Write the box sizes as $$a\le b\le c$$ with $$a+b+c=8$$. If $$a=1$$, the possibilities are $$(1,1,6),(1,2,5),(1,3,4)$$. If $$a=2$$, they are $$(2,2,4),(2,3,3)$$. Since $$a\le8/3$$, no larger smallest part is possible.

Thus there are five distributions. The ordered stars-and-bars count would be $$\binom72=21$$, and dividing by six would fail because the repeated-part patterns have different numbers of orderings.

</div>

Let $$p(n,k)$$ count partitions of $$n$$ into exactly $$k$$ positive parts. Separate partitions containing a part of size one from those whose parts are all at least two. Removing one part of size one gives $$p(n-1,k-1)$$. Subtracting one from each of the $$k$$ parts in the second case gives $$p(n-k,k)$$. Therefore

$$
p(n,k)=p(n-1,k-1)+p(n-k,k).
$$

The two cases are disjoint, and each construction is reversible. This recurrence is useful when a direct list becomes too long.

---

## Several Forbidden Waypoints

Paths through a sequence of waypoints can be counted by multiplying the counts between consecutive points, provided the coordinates never decrease. If a later waypoint lies left or below an earlier one, no right/up path can visit them in that order.

When avoiding several points, inclusion–exclusion is often more efficient than building a recurrence across the whole grid. The intersection terms are counts of paths visiting several waypoints, so ordering and compatibility matter.

<div class="theorem-box">

**Example.** How many right/up paths from $$(0,0)$$ to $$(6,6)$$ avoid both $$(2,2)$$ and $$(4,4)$$?

There are $$\binom{12}6=924$$ paths in total. Through either specified point there are

$$
\binom42\binom84=420
$$

paths. A path through both points splits into three $$2\times2$$ path segments, giving $$\binom42^3=216$$.

Inclusion–exclusion yields $$924-420-420+216=300$$. The last term restores paths that were excluded twice.

</div>

For obstacles covering edges rather than vertices, describe the forced step as well as the endpoints. A path using a specified edge splits into a path to its starting vertex, the edge itself, and a path from its ending vertex. This avoids accidentally subtracting every path through the vertex.

---

## Reflection and Ballot-Type Counts

The reflection principle works because it maps every bad path to one unrestricted path with a different endpoint. The reflecting point must be uniquely chosen, usually the first time a boundary is crossed. Choosing an arbitrary crossing makes the correspondence nonunique.

For paths from $$(0,0)$$ to $$(m,n)$$ with $$m\ge n$$ that never go above $$y=x$$, reflect the initial segment up to the first point with $$y=x+1$$. A bad path becomes a path with $$m+1$$ right steps and $$n-1$$ up steps. Therefore the good count is

$$
\binom{m+n}n-\binom{m+n}{n-1}
=\frac{m-n+1}{m+1}\binom{m+n}n.
$$

At $$m=n$$, this reduces to the Catalan formula. The numerator $$m-n+1$$ records the extra horizontal room available before the path violates the diagonal constraint.

<div class="theorem-box">

**Example.** A vote count contains six votes for A and four for B. In how many orders of the ten votes is A never behind B during the count?

Treat A as a right step and B as an up step. The prefix condition is exactly $$y\le x$$. The count is

$$
\binom{10}4-\binom{10}3=210-120=90.
$$

If A must be strictly ahead after every nonempty prefix, the boundary condition changes and this formula cannot be used unchanged.

</div>

---

## Catalan Decompositions and Their Generating Function

Catalan objects often split into two smaller objects at a distinguished first return or matching pair. For balanced parentheses, match the first opening parenthesis to its closing partner. The substring inside is a balanced string, and the substring after it is another balanced string.

If there are $$n$$ pairs in total and $$i$$ pairs inside, there are $$n-1-i$$ pairs after the partner. This gives

$$
C_n=\sum_{i=0}^{n-1}C_iC_{n-1-i},\qquad C_0=1.
$$

Let $$C(x)=\sum_{n\ge0}C_nx^n$$. The convolution becomes $$C(x)=1+xC(x)^2$$. Solving the quadratic gives

$$
C(x)=\frac{1-\sqrt{1-4x}}{2x}.
$$

The minus sign is selected because the series must have a finite constant term of one; the other branch has a negative power of $$x$$. This example shows how the same sequence can be understood through reflection, decomposition, and generating functions. Each viewpoint is useful for a different kind of modification to the problem.

:::strategy
Start by distinguishing identical objects from distinct ones and labeled boxes from unlabeled ones. Encode coordinate restrictions before calculating. For paths, decide whether the condition is local, such as an obstacle, or global, such as staying below a line; this usually determines whether decomposition, inclusion–exclusion, or reflection is the best first move.
:::

---

## Counting Missing Capacity Instead of Used Capacity

A distribution near full capacity can be easier to count through its deficits. For $$k$$ labeled boxes each with capacity $$u$$, put $$y_i=u-x_i$$. Then

$$
x_1+\cdots+x_k=n
\quad\Longleftrightarrow\quad
y_1+\cdots+y_k=ku-n,
$$

with the same bounds $$0\le y_i\le u$$. This is a reversible transformation, so the counts at totals $$n$$ and $$ku-n$$ are equal.

<div class="theorem-box">

**Example.** Thirty-one identical candies are distributed to five named students, each receiving at most seven. Count the distributions.

The total capacity is thirty-five, so the five deficits sum to four. Because their total is already less than seven, no individual deficit can exceed the allowed maximum. Ordinary stars and bars gives $$\binom84=70$$ distributions.

Directly applying inclusion–exclusion at total thirty-one would require several large alternating terms. The deficit model makes every upper bound automatic.

</div>

This complements the earlier lower-bound shift. Giving each box its minimum counts excess above a floor; subtracting each amount from capacity counts missing units below a ceiling.

---

## Key Equations

:::equations
| Model | Count |
| --- | --- |
| Nonnegative solutions | $$x_1+\cdots+x_k=n:\ \binom{n+k-1}{k-1}$$ |
| Positive solutions | $$x_i\ge1:\ \binom{n-1}{k-1}$$ for $$n\ge k$$ |
| Repeated objects | $$n!/(n_1!\cdots n_r!)$$ |
| Right/up lattice paths | $$(0,0)\to(a,b):\ \binom{a+b}a$$ |
| Catalan paths | $$C_n=\binom{2n}n/(n+1)$$ |
| Distribution generating function | $$[x^n]\prod_i\sum_{j\in S_i}x^j$$ for allowed box sizes $$S_i$$ |
| Partition recurrence | $$p(n,k)=p(n-1,k-1)+p(n-k,k)$$ |
| Weak ballot paths | $$\binom{m+n}n-\binom{m+n}{n-1}$$ for $$m\ge n$$ and $$y\le x$$ |
| Catalan generating function | $$C(x)=1+xC(x)^2=(1-\sqrt{1-4x})/(2x)$$ |
| Capacity symmetry | Totals $$n$$ and $$ku-n$$ have equal counts under uniform bounds $$0\le x_i\le u$$ |
:::
