---
title: "Counting Fundamentals"
status: developing
progress: 68
sidebar:
  order: 1
description: "Competition math notes on permutations, combinations, casework, bijections, double counting, and binomial identities with worked examples."
---

## Sum and Product Rules

Counting starts by describing one outcome precisely. A team is an unordered set of people; a ranking is an ordered list. They require different counts even when they use the same people.

The **sum rule** adds counts for disjoint cases. The **product rule** multiplies counts for successive choices when every partial outcome has the stated number of extensions. The choices need not be probabilistically independent; what matters is that the number of available extensions is correct at every stage.

<div class="theorem-box">

**Example.** How many three-digit positive integers have distinct digits?

The hundreds digit has $$9$$ choices because zero is forbidden. The tens digit has $$9$$ choices, including zero but excluding the hundreds digit. The units digit has $$8$$ choices. Thus there are

$$
9\cdot9\cdot8=648
$$

such integers.

</div>

If a later number of choices depends on an earlier decision, separate those earlier decisions into cases or count extensions individually. Multiplying an average-looking number of choices can silently overcount.

---

## Permutations and Combinations

There are $$n!$$ orderings of $$n$$ distinct objects. Choosing an ordered list of $$k$$ different objects gives

$$
n(n-1)\cdots(n-k+1)=\frac{n!}{(n-k)!}.
$$

For an unordered $$k$$-element selection, each set appears $$k!$$ times in the ordered count, so

$$
\binom nk=\frac{n!}{k!(n-k)!}.
$$

<div class="theorem-box">

**Example.** From eight students, choose a three-person committee with one designated chair. How many choices are possible?

Choose the committee, then its chair:

$$
\binom83\cdot3=56\cdot3=168.
$$

Alternatively, choose the chair first and then two ordinary members: $$8\binom72=168$$. The chair is distinguished, while the two ordinary members are not ordered.

</div>

For repeated objects, divide by permutations among indistinguishable copies. The number of arrangements with multiplicities $$n_1,\ldots,n_r$$ totaling $$n$$ is $$n!/(n_1!\cdots n_r!)$$. For example, BANANA has $$6!/(3!2!)=60$$ distinct letter arrangements.

---

## Casework and Complementary Counting

Good casework has no overlap and covers every valid outcome. Useful case labels include the smallest chosen element, the number of selected objects of one type, or whether a particular object is present.

When the forbidden outcomes are easier to describe, count everything and subtract them.

<div class="theorem-box">

**Example.** A committee of four is chosen from six seniors and five juniors. How many committees contain at least one student from each group?

There are $$\binom{11}4$$ committees in total. The invalid ones contain only seniors or only juniors; these two cases are disjoint. Therefore the answer is

$$
\binom{11}4-\binom64-\binom54=330-15-5=310.
$$

</div>

Words such as “at least one” often suggest a complement. “Exactly two” usually suggests choosing the two directly and then choosing the remaining objects from the other group.

---

## Overcounting and Circular Arrangements

Dividing an overcount is valid only if every wanted outcome has the same number of representations in your count.

For $$n$$ distinct people around a circular table, with rotations considered identical and reflections different, fix one person as a reference. Arrange the others relative to that person to get $$(n-1)!$$. If seats are labeled, rotations are different and the count is $$n!$$ instead.

<div class="theorem-box">

**Example.** Six distinct people sit around a circular table. Two particular people must sit next to each other. With rotations considered identical, how many arrangements are possible?

Treat the pair as one block. There are now five distinct units around the circle, giving $$4!$$ arrangements. The two people can switch places inside the block, so the answer is

$$
2\cdot4!=48.
$$

</div>

For necklaces with repeated colors, different patterns may have different rotational symmetries. Dividing the number of linear strings by the number of rotations is not automatically valid.

---

## Bijections and Double Counting

A **bijection** pairs each object in one set with exactly one object in another set, with a reversible rule. It converts a difficult count into an easier count without changing the answer.

**Double counting** counts the same collection of objects in two ways. It is especially useful for identities involving binomial coefficients.

<div class="theorem-box">

**Example.** Prove $$k\binom nk=n\binom{n-1}{k-1}$$ for $$1\le k\le n$$.

Count committees of size $$k$$ with one designated captain. Choosing the committee first gives $$\binom nk$$ choices and then $$k$$ captain choices. Choosing the captain first gives $$n$$ choices and then $$\binom{n-1}{k-1}$$ choices for the other members. Both counts describe exactly the same objects, proving the identity.

</div>

To explain **Pascal's identity**, distinguish one particular person. A size-$$k$$ committee either excludes that person or includes them, giving

$$
\binom nk=\binom{n-1}k+\binom{n-1}{k-1}.
$$

The **binomial theorem** is another counting statement:

$$
(x+y)^n=\sum_{k=0}^n\binom nkx^{n-k}y^k.
$$

Each product term arises by choosing which $$k$$ of the $$n$$ factors supply a $$y$$. Setting $$x=y=1$$ gives $$\sum_k\binom nk=2^n$$, the number of all subsets of an $$n$$-element set.

:::strategy
Before calculating, state whether order matters, repetitions are allowed, and rotations or reflections are identified. Then choose one way to construct each outcome. If you divide afterward, explain exactly why every outcome was counted the same number of times.
:::

## Constructing a Bijection Carefully

A counting correspondence must work in both directions. Describe how to encode an object, explain how to recover the original object, and check that the restriction translates correctly. An encoding that forgets information can identify different objects, while an encoding that allows impossible patterns can introduce extras.

For instance, choosing a subset of an ordered list can be encoded by a binary string, with one indicating a chosen element. If adjacent elements may not both be chosen, the condition becomes a forbidden pattern in the string. This translation makes gaps or recurrence relations available.

<div class="theorem-box">

**Example.** How many five-element subsets of $$\{1,2,\ldots,15\}$$ contain no consecutive integers?

Write the chosen elements as $$a_1<a_2<\cdots<a_5$$, with $$a_{i+1}\ge a_i+2$$. Set $$b_i=a_i-(i-1)$$. Then

$$
1\le b_1<b_2<\cdots<b_5\le11.
$$

Conversely, any increasing five-element selection from one through eleven gives a valid original selection by $$a_i=b_i+i-1$$. This is a bijection, so the count is $$\binom{11}{5}=462$$.

The subtraction removes the mandatory gaps. The inverse adds them back, proving that no valid subset was lost and no invalid one was introduced.

</div>

More generally, selecting $$k$$ elements from $$1,\ldots,n$$ with gaps at least $$d$$ gives $$\binom{n-(d-1)(k-1)}k$$ when enough room exists. Deriving the shift is safer than recalling the formula without checking whether the required gap counts unchosen elements or differences of chosen values.

---

## Blocks, Gaps, and Multiple Restrictions

A block forces objects to stay together; gaps force them apart. The two constructions solve opposite kinds of restrictions and can be combined when different groups have different requirements.

When using gaps, first arrange the unrestricted objects. They create one more gap than their number, including both end gaps. If several distinct restricted objects occupy different gaps, choose the gaps and then arrange the objects. If the restricted objects are identical, the second ordering factor disappears.

<div class="theorem-box">

**Example.** Five distinct boys and four distinct girls stand in a row, with no two girls adjacent. Find the number of orders.

Arrange the boys in $$5!$$ ways. The five boys create six gaps. Choose four of them for the girls, then assign the four distinct girls to those gaps:

$$
5!\binom64 4!=43200.
$$

Every valid order determines its boys' order, its occupied gaps, and its girls' assignment uniquely, so the construction counts each order exactly once.

</div>

If the condition says every boy and girl must alternate, the endpoints are no longer optional: with five boys and four girls, all four internal gaps are used and the order must begin and end with a boy. The answer becomes $$5!4!$$. A small change in the wording can remove an entire binomial factor.

For overlapping adjacency conditions, blocks need care. Requiring A next to B and B next to C does not produce two independent blocks, since B belongs to both. Instead, analyze the compatible local arrangements first. In this case the three people must form ABC or CBA, a single three-person block with two internal orders.

---

## More Double-Counting Identities

Binomial identities are often easier to understand by counting a concrete object. The goal is to identify what the summation index records: a chosen captain, the number chosen from one group, or the largest selected element.

**Vandermonde's identity** is

$$
\sum_k\binom mk\binom n{r-k}=\binom{m+n}r.
$$

Choose an $$r$$-person committee from groups of sizes $$m,n$$. The term with index $$k$$ counts those with exactly $$k$$ members from the first group. These cases are disjoint and exhaustive. Use the convention that a binomial coefficient is zero when its lower index is outside the allowed range.

<div class="theorem-box">

**Example.** Evaluate $$\sum_{k=0}^6\binom8k\binom9{6-k}$$.

The sum counts six-element subsets of a seventeen-element set split into groups of eight and nine. Therefore it equals $$\binom{17}6=12376$$.

The product inside each term records two independent selections; the sum combines the possible first-group sizes. This interpretation also confirms the bounds without expanding the coefficients.

</div>

The **hockey-stick identity**

$$
\sum_{j=k}^n\binom jk=\binom{n+1}{k+1}
$$

counts $$(k+1)$$-element subsets by their largest element. If the largest is $$j+1$$, the remaining $$k$$ elements come from the first $$j$$ positions. A weighted variant can often be derived by adding a distinguished object to this same model.

For example, $$\sum_k k\binom nk=n2^{n-1}$$ counts a subset with one distinguished member. Choose the member first, then independently choose any subset of the other $$n-1$$ elements. The method explains the weight $$k$$, rather than treating it as an obstacle to algebraic simplification.

---

## Permutations as Disjoint Cycles

A permutation can be viewed as a collection of directed cycles. A cycle $$a\mapsto b\mapsto c\mapsto a$$ has three written rotations but represents one cycle, so $$m$$ specified elements form $$(m-1)!$$ cycles. Reversing a cycle generally changes the permutation.

This model is useful when a problem describes repeated application of a rearrangement, fixed points, or the number of cycles. A fixed point is a cycle of length one.

<div class="theorem-box">

**Example.** How many permutations of five distinct elements have exactly two cycles?

The cycle sizes must be $$1+4$$ or $$2+3$$. In the first case, choose the fixed element in five ways and arrange the other four into one cycle in $$3!$$ ways, giving thirty.

In the second case, choose the two-element cycle's members in $$\binom52$$ ways. They form one cycle, while the remaining three form $$2!$$ cycles. This gives twenty. The total is fifty.

The cases do not need division by two because the two cycle sizes are different and identify the roles uniquely.

</div>

Let $$c(n,k)$$ count permutations of $$n$$ elements with $$k$$ cycles. The new element either forms its own cycle or is inserted immediately after one of the existing $$n-1$$ elements. Thus

$$
c(n,k)=c(n-1,k-1)+(n-1)c(n-1,k).
$$

This recurrence is another example of counting by an insertion rule. The same idea can solve problems where constructing the final object directly is awkward.

---

## Symmetry and Burnside's Lemma

For arrangements identified under rotations, division by the number of rotations works only when every arrangement has a full orbit. Repeated-color patterns can return to themselves after a smaller rotation, so their orbits have different sizes.

**Burnside's lemma** repairs this. For a finite collection acted on by a finite symmetry group $$G$$,

$$
\#\text{distinct arrangements}
=\frac1{\lvert G\rvert}\sum_{g\in G}\#\text{arrangements fixed by }g.
$$

To understand the average, count pairs consisting of an arrangement and a symmetry fixing it. An orbit of size $$s$$ has $$\lvert G\rvert/s$$ symmetries fixing each member, so the whole orbit contributes exactly $$\lvert G\rvert$$ pairs. Dividing the total pair count by $$\lvert G\rvert$$ therefore counts the orbits once each.

<div class="theorem-box">

**Example.** Five beads form a circular necklace, each colored with one of three colors. Rotations are identified, but reflected necklaces remain different. Find the number of necklaces.

The identity rotation fixes all $$3^5$$ colorings. Since five is prime, every nonidentity rotation cycles through all five positions. A fixed coloring must therefore be monochromatic, giving three choices for each of those four rotations.

Burnside gives

$$
\frac{3^5+4\cdot3}{5}=51.
$$

Simply dividing $$3^5$$ by five would not even give an integer. The monochromatic necklaces are exactly the patterns with unusually small rotational orbits.

</div>

For a rotation by $$r$$ positions of an $$n$$-bead necklace, the positions split into $$\gcd(n,r)$$ cycles. A fixed coloring is constant on each cycle, so with $$q$$ colors there are $$q^{\gcd(n,r)}$$ fixed colorings. This gives a general necklace formula by averaging over the rotations. If reflections are also identified, the symmetry group is larger and its reflections require their own fixed-coloring counts.

:::strategy
Use a direct construction when outcomes have a natural order of choices, a bijection when a restriction can be removed by encoding, and double counting when a sum has a meaningful index. Use symmetry averaging only after stating precisely which transformations identify two outcomes.
:::

---

## Key Equations

:::equations
| Count | Formula and conditions |
| --- | --- |
| Ordered selection without replacement | $$n!/(n-k)!$$ |
| Unordered selection | $$\binom nk=n!/[k!(n-k)!]$$ |
| Repeated objects | $$n!/(n_1!\cdots n_r!)$$ |
| Circular arrangements | $$(n-1)!$$ for distinct objects, with rotations identified |
| Pascal | $$\binom nk=\binom{n-1}k+\binom{n-1}{k-1}$$ |
| Binomial theorem | $$(x+y)^n=\sum_{k=0}^n\binom nkx^{n-k}y^k$$ |
| Spaced subsets | $$\binom{n-(d-1)(k-1)}k$$ for $$k$$ increasing choices with differences at least $$d$$ |
| Vandermonde | $$\sum_k\binom mk\binom n{r-k}=\binom{m+n}r$$ |
| Hockey stick | $$\sum_{j=k}^n\binom jk=\binom{n+1}{k+1}$$ |
| Cycle recurrence | $$c(n,k)=c(n-1,k-1)+(n-1)c(n-1,k)$$ |
| Burnside | Number of orbits equals $$\lvert G\rvert^{-1}\sum_{g\in G}\lvert\operatorname{Fix}(g)\rvert$$ |
:::
