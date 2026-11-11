---
title: "Principle of Inclusion–Exclusion"
status: developing
progress: 68
sidebar:
  order: 3
description: "Competition math notes on inclusion–exclusion, overlapping restrictions, derangements, and onto functions with worked counting examples."
---

## Counting Overlapping Sets

Adding two set sizes counts their intersection twice. The **principle of inclusion–exclusion** corrects this:

$$
\lvert A\cup B\rvert=\lvert A\rvert+\lvert B\rvert-\lvert A\cap B\rvert.
$$

For three sets,

$$
\begin{aligned}
\lvert A\cup B\cup C\rvert
={}&\lvert A\rvert+\lvert B\rvert+\lvert C\rvert\\
&-\lvert A\cap B\rvert-\lvert A\cap C\rvert-\lvert B\cap C\rvert\\
&+\lvert A\cap B\cap C\rvert.
\end{aligned}
$$

An object in all three sets is counted three times, subtracted three times, then added once. Its final contribution is one, as required.

<div class="theorem-box">

**Example.** How many integers from $$1$$ through $$100$$ are divisible by at least one of $$2,3,5$$?

A number divisible by both $$2$$ and $$3$$ is a multiple of $$6$$. Use the corresponding least common multiples for the other intersections:

$$
50+33+20-16-10-6+3=74.
$$

Thus $$74$$ integers satisfy at least one condition. Their complement contains $$100-74=26$$ integers.

</div>

---

## General Inclusion–Exclusion

For a finite universe $$U$$ and forbidden sets $$A_1,\ldots,A_m$$, the number avoiding every forbidden condition is

$$
\lvert U\rvert-\sum_i\lvert A_i\rvert
+\sum_{i<j}\lvert A_i\cap A_j\rvert-\cdots
+(-1)^m\lvert A_1\cap\cdots\cap A_m\rvert.
$$

To justify the alternating signs, take an object that belongs to exactly $$r>0$$ forbidden sets. Its contribution to the count of allowed objects is

$$
\sum_{j=0}^r(-1)^j\binom rj=(1-1)^r=0.
$$

An object belonging to no forbidden sets contributes one. This also explains why every intersection must be counted, even when it looks like it has already been removed.

If all $$j$$-fold intersections have the same size $$N_j$$, group them into $$\binom mjN_j$$. Otherwise, calculate their sizes separately.

<div class="theorem-box">

**Example.** How many length-five strings over $$\{A,B,C\}$$ contain all three letters?

There are $$3^5$$ strings in total. Define a forbidden event for each missing letter. A specified missing letter leaves $$2^5$$ strings, and two specified missing letters leave one string. No length-five string can miss all three letters. The result is

$$
3^5-\binom31 2^5+\binom32 1^5=243-96+3=150.
$$

</div>

---

## Onto Functions

A function from an $$n$$-element set to a labeled $$k$$-element set is **onto** if every target is used. There are $$k^n$$ unrestricted functions. Declare “target $$i$$ is missed” to be the $$i$$th bad event. Missing a specified collection of $$j$$ targets leaves $$(k-j)^n$$ functions, so for $$n\ge1$$,

$$
\#\text{onto functions}=\sum_{j=0}^k(-1)^j\binom kj(k-j)^n.
$$

This also counts assignments of $$n$$ distinct objects to $$k$$ distinct boxes with no empty box. It does not count distributions of identical objects.

<div class="theorem-box">

**Example.** Four distinct tasks are assigned to three named workers, with every worker receiving a task. Find the number of assignments.

Using the onto-function count,

$$
3^4-3\cdot2^4+3\cdot1^4=81-48+3=36.
$$

We can check by observing that the task counts must be $$2,1,1$$: choose the worker receiving two tasks in $$3$$ ways, choose their tasks in $$\binom42$$ ways, then assign the other two tasks in $$2!$$ ways. This also gives $$36$$.

</div>

---

## Derangements and Fixed Positions

A **derangement** is a permutation with no fixed points. Let $$A_i$$ be the permutations that leave object $$i$$ in its original position. Fixing a specified set of $$j$$ positions leaves $$(n-j)!$$ permutations, so

$$
D_n=\sum_{j=0}^n(-1)^j\binom nj(n-j)!
=n!\sum_{j=0}^n\frac{(-1)^j}{j!}.
$$

<div class="theorem-box">

**Example.** Five letters are placed into five addressed envelopes, one per envelope. In how many assignments does no letter reach its own envelope?

Every assignment is a permutation, and the restriction is exactly a derangement. Thus

$$
D_5=120-120+60-20+5-1=44.
$$

</div>

For **exactly $$r$$ fixed points**, first choose the fixed positions, then derange every remaining position. The count is $$\binom nrD_{n-r}$$. Merely arranging the remaining objects arbitrarily would allow additional fixed points and violate “exactly.”

---

## Restricted Arrangements

Some restrictions are easier to combine with blocks than with fixed positions. For example, in permutations of distinct objects, a specified adjacent pair can be treated as a block; intersections require checking whether several block conditions are compatible.

<div class="theorem-box">

**Example.** Six distinct people stand in a row. Two specified people, Alice and Bob, must not be adjacent, and two other specified people, Carol and Dan, must not be adjacent. Find the number of valid orders.

There are $$6!=720$$ unrestricted orders. Treating Alice and Bob as a block gives $$2\cdot5!=240$$ orders violating their restriction; Carol and Dan give the same count. When both pairs are adjacent, there are four units to arrange and two internal orders for each pair, giving $$2^2\cdot4!=96$$. Hence

$$
720-240-240+96=336
$$

orders satisfy both restrictions. The pairwise intersection must be added back because it was subtracted twice.

</div>

:::strategy
Define each bad event in a sentence before writing a formula. Work out one single event, one pairwise intersection, and one higher intersection. Group intersections by size only after confirming they have equal counts. Use a complement for “none,” and distinguish it carefully from “exactly one.”
:::

## Counting Exactly a Given Number of Conditions

The ordinary union formula counts objects satisfying at least one condition. To count exactly one, exactly two, or another fixed number, the intersection sizes need different weights.

Let $$S_j$$ be the sum of all $$j$$-fold intersection sizes, and let $$S_0=\lvert U\rvert$$. An object lying in exactly $$m$$ sets contributes $$\binom mj$$ to $$S_j$$. The number lying in exactly $$r$$ sets is

$$
N_r=\sum_{j=r}^k(-1)^{j-r}\binom jr S_j.
$$

To justify the formula, consider one object in $$m$$ sets. Its contribution is

$$
\sum_{j=r}^m(-1)^{j-r}\binom jr\binom mj
=\binom mr\sum_{h=0}^{m-r}(-1)^h\binom{m-r}h.
$$

This is one when $$m=r$$ and zero otherwise. The calculation explains why merely subtracting pairwise overlaps once does not count objects satisfying exactly one condition.

<div class="theorem-box">

**Example.** Among integers from one through one hundred, count those divisible by exactly one of two, three, and five.

The single-set total is $$S_1=50+33+20=103$$. The pairwise total is $$S_2=16+10+6=32$$, and the triple intersection has size $$S_3=3$$.

Therefore

$$
N_1=S_1-2S_2+3S_3=103-64+9=48.
$$

For comparison, exactly two conditions occur for $$S_2-3S_3=23$$ integers, and all three occur for three integers. These counts sum to seventy-four, the union count.

</div>

The coefficients two and three are not arbitrary corrections. An object in two bad sets was counted twice in $$S_1$$, while an object in three was counted three times and appears in three pairwise intersections. Track one hypothetical object to reconstruct the weights if you forget them.

---

## Forbidden Positions and Compatible Intersections

A restricted permutation can be represented by a board: rows are objects, columns are positions, and a forbidden cell records one disallowed assignment. A permutation selects exactly one cell in every row and every column.

When inclusion–exclusion chooses several forbidden cells, the corresponding events can occur together only if the cells lie in different rows and different columns. Compatible selections resemble nonattacking rooks on a chessboard.

Let $$r_j$$ count compatible selections of $$j$$ forbidden cells. Fixing those assignments leaves $$(n-j)!$$ ways to place the remaining objects. Hence the number of allowed permutations is

$$
\sum_{j=0}^n(-1)^j r_j(n-j)!.
$$

This is the rook-number form of inclusion–exclusion. It generalizes derangements, whose forbidden cells are exactly the diagonal and have $$r_j=\binom nj$$.

<div class="theorem-box">

**Example.** Four distinct tasks are assigned one each to four distinct students A, B, C, D. A cannot receive task one or two, and B cannot receive task one. Find the number of valid assignments.

There are three forbidden cells: $$(A,1),(A,2),(B,1)$$. Thus $$r_0=1,r_1=3$$. Only $$(A,2)$$ together with $$(B,1)$$ is a compatible pair; the other pairs share a row or column. Hence $$r_2=1$$, and no larger compatible selection exists.

The count is

$$
4!-3\cdot3!+1\cdot2!=24-18+2=8.
$$

As a direct check, A has two choices, then B has two allowed remaining choices, and the other students can be assigned in two ways. This also gives eight.

</div>

The board is useful because empty intersections become visible. Assuming all two-event intersections have the same size would fail here, even though the single-event sizes agree.

---

## Onto Functions and Unlabeled Set Partitions

Onto functions assign distinct objects to labeled nonempty boxes. An **unlabeled set partition** divides the objects into nonempty groups with no names on the groups. Each unlabeled partition into $$k$$ groups gives exactly $$k!$$ onto assignments after the groups are labeled, so

$$
S(n,k)=\frac1{k!}\sum_{j=0}^k(-1)^j\binom kj(k-j)^n
$$

for positive $$n,k$$. The numbers $$S(n,k)$$ are Stirling numbers of the second kind. They are different from integer partitions, which distribute identical objects.

<div class="theorem-box">

**Example.** In how many ways can six distinct students be split into three nonempty, unlabeled study groups?

First count assignments to three named groups:

$$
3^6-3\cdot2^6+3=540.
$$

Each unlabeled grouping appears exactly $$3!=6$$ times, because all three groups are nonempty and can be named in six ways. The answer is $$540/6=90$$.

</div>

These numbers also satisfy $$S(n,k)=kS(n-1,k)+S(n-1,k-1)$$. The last object either joins one of $$k$$ existing groups or forms a singleton group. The recurrence gives a useful independent check on an inclusion–exclusion computation.

The division by $$k!$$ works here because the objects are distinct and the groups are nonempty. If empty groups were allowed, changing the labels of empty boxes would not create all distinct assignments, and the uniform overcount argument would fail.

---

## Overlapping Word Patterns

Inclusion–exclusion applies to forbidden adjacent patterns, but intersections may merge into larger blocks. When patterns overlap, determine the resulting arrangement explicitly before counting its permutations.

<div class="theorem-box">

**Example.** How many permutations of the letters A, B, C, D, E contain neither the consecutive ordered pattern AB nor the consecutive ordered pattern BC?

There are $$5!=120$$ permutations. Those containing AB are counted by treating AB as one block, giving $$4!=24$$. The same holds for BC.

If both patterns occur, their shared B forces the single ordered block ABC. The remaining three units, ABC, D, E, can be ordered in $$3!=6$$ ways. Therefore the valid count is

$$
120-24-24+6=78.
$$

Treating AB and BC as disjoint blocks would use B twice and give an invalid intersection count.

</div>

For a repeated-letter string, an occurrence can be indexed by its starting position. Several starting positions may force some of the same letters. Check consistency of those forced letters; incompatible overlaps contribute zero. This is often the point where a recurrence becomes simpler than a large inclusion–exclusion expansion.

---

## Partial Inclusion–Exclusion and Bounds

A full formula may have too many terms to calculate, while the first few terms already prove the required bound. For a union of sets,

$$
S_1-S_2\le\left\lvert\bigcup_iA_i\right\rvert\le S_1.
$$

The upper bound is the union bound. The lower bound subtracts pairwise overlaps but ignores higher corrections. More generally, an odd-length truncation of the alternating union sum is an upper bound, and an even-length truncation is a lower bound. These are Bonferroni bounds.

They can be understood one object at a time. An object appearing in $$m$$ sets has a partial contribution determined by alternating binomial coefficients. Its error has a predictable sign, so summing over objects preserves the bound.

Suppose one hundred objects belong to three properties, each property holding for thirty objects, with every pairwise overlap containing at most five. The union has at least $$90-15=75$$ objects. The full triple intersection is unnecessary for this lower bound because its omitted contribution is nonnegative.

---

## Derangement Probability and Approximation

Dividing the derangement formula by $$n!$$ gives the probability that a random permutation has no fixed points:

$$
\frac{D_n}{n!}=\sum_{j=0}^n\frac{(-1)^j}{j!}.
$$

The infinite alternating series is $$e^{-1}$$. Its omitted terms decrease in magnitude, so the finite-sum error has magnitude less than $$1/(n+1)!$$. Multiplying back by $$n!$$ yields

$$
\left\lvert D_n-\frac{n!}{e}\right\rvert<\frac1{n+1}.
$$

For $$n\ge1$$, this identifies $$D_n$$ as the nearest integer to $$n!/e$$. The approximation comes with an error bound; it is not a substitute for an exact integer calculation when rounding could be uncertain.

It also shows that the no-fixed-point probability approaches approximately 0.368, even as the number of positions grows. The individual bad events become rarer, but their number grows at the same time. This is why multiplying independent-looking probabilities is tempting here and also why it needs care: fixed-point events are not independent.

:::strategy
For every intersection term, determine whether the selected restrictions are compatible and whether they all have equal counts. For “exactly,” use membership weights rather than the ordinary union formula. If only a bound is needed, consider a justified truncation before calculating the entire alternating sum.
:::

---

## An Exact Fixed-Point Probability

The derangement formula can be used inside a larger selection, but the remaining positions must have no extra fixed points.

<div class="theorem-box">

**Example.** A uniformly random permutation of seven objects is chosen. Find the probability that exactly two objects remain in their original positions.

Choose the two fixed positions in $$\binom72=21$$ ways. The other five objects must form a derangement, of which there are $$D_5=44$$. Thus the number of successful permutations is $$21\cdot44=924$$, and the probability is

$$
\frac{924}{7!}=\frac{11}{60}.
$$

Using $$5!$$ instead of $$D_5$$ would allow more fixed positions and would count permutations outside the requested event.

</div>

The selection and derangement steps describe one outcome uniquely: its actual fixed positions determine the chosen pair, and its restriction to the other positions determines the derangement. This is why no additional overcount correction is needed.

---

## Key Equations

:::equations
| Application | Formula |
| --- | --- |
| Two sets | $$\lvert A\cup B\rvert=\lvert A\rvert+\lvert B\rvert-\lvert A\cap B\rvert$$ |
| Onto functions, $$n\ge1$$ | $$\sum_{j=0}^k(-1)^j\binom kj(k-j)^n$$ |
| Derangements | $$D_n=n!\sum_{j=0}^n(-1)^j/j!$$, including $$D_0=1$$ |
| Exactly $$r$$ fixed points | $$\binom nrD_{n-r}$$ |
| Multiples in $$1,\ldots,N$$ | $$\lfloor N/d\rfloor$$ multiples of $$d$$; intersections use the LCM |
| Exactly $$r$$ conditions | $$N_r=\sum_{j=r}^k(-1)^{j-r}\binom jr S_j$$ |
| Forbidden permutation cells | $$\sum_j(-1)^jr_j(n-j)!$$, where $$r_j$$ counts compatible selections |
| Set partitions | $$k!S(n,k)=\sum_{j=0}^k(-1)^j\binom kj(k-j)^n$$ |
| Partition recurrence | $$S(n,k)=kS(n-1,k)+S(n-1,k-1)$$ |
| Union bounds | $$S_1-S_2\le\lvert\bigcup_iA_i\rvert\le S_1$$ |
| Derangement error | $$\lvert D_n-n!/e\rvert<1/(n+1)$$ for $$n\ge1$$ |
:::
