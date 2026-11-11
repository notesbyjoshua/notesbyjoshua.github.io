---
title: "Pigeonhole Principle"
status: developing
progress: 68
sidebar:
  order: 5
description: "Competition math notes on the pigeonhole principle, remainder and partial-sum arguments, geometric boxes, and sharp bounds with worked examples."
---

## Objects, Boxes, and Guarantees

The **pigeonhole principle** says that placing more than $$k$$ objects into $$k$$ boxes forces some box to contain at least two objects. More generally, placing $$N$$ objects into $$k$$ boxes forces a box with at least

$$
\left\lceil\frac Nk\right\rceil
$$

objects. If every box had fewer, their total capacity would be too small.

The work in a contest problem is usually choosing what the objects and boxes represent. A box can be a remainder class, an interval, a pair, a region, or a possible value of an expression.

<div class="theorem-box">

**Example.** What is the smallest number of people needed to guarantee that at least four have birthdays in the same month?

Twelve months can each hold three people without meeting the target, for a total of $$36$$. The next person forces a fourth birthday in one month. Thus $$37$$ people are necessary and sufficient for the guarantee.

</div>

To prove a threshold is smallest, give both the guarantee and an example below the threshold that avoids it.

---

## Pairing Boxes

Sometimes each box should hold a carefully chosen group rather than a single possible value. Choose the groups so that sharing a box gives the desired relation immediately.

<div class="theorem-box">

**Example.** Prove that any six distinct numbers chosen from $$\{1,2,\ldots,10\}$$ include two whose sum is $$11$$.

Partition the set into five boxes:

$$
\{1,10\},\quad\{2,9\},\quad\{3,8\},\quad\{4,7\},\quad\{5,6\}.
$$

Six choices force two into the same box, and those two sum to $$11$$. Five choices do not guarantee this: $$\{1,2,3,4,5\}$$ contains no such pair.

</div>

---

## Remainders and Partial Sums

Modulo $$m$$, there are only $$m$$ possible remainders. If two integers have the same remainder, their difference is divisible by $$m$$.

<div class="theorem-box">

**Example.** Prove that among any eight integers, two have a difference divisible by $$7$$.

Place each integer into its remainder class modulo $$7$$. There are seven classes and eight integers, so two share a remainder. Their difference is a multiple of $$7$$.

</div>

For a consecutive block of terms, use partial sums so that a difference corresponds to the block's sum.

<div class="theorem-box">

**Example.** Prove that any sequence of $$n$$ integers has a nonempty consecutive block whose sum is divisible by $$n$$.

Define $$S_0=0$$ and $$S_j=a_1+\cdots+a_j$$ for $$1\le j\le n$$. These are $$n+1$$ integers but only $$n$$ remainder classes modulo $$n$$. Thus $$S_i\equiv S_j\pmod n$$ for some $$0\le i<j\le n$$. Their difference is

$$
S_j-S_i=a_{i+1}+\cdots+a_j\equiv0\pmod n.
$$

Because $$j>i$$, this block is nonempty.

</div>

Including $$S_0$$ avoids a separate case for a partial sum that is itself divisible by $$n$$.

---

## Geometric Boxes

Partition a region into smaller pieces whose diameter is controlled. Two points in one piece must then be close. Specify boundary assignments so every point belongs to exactly one piece.

<div class="theorem-box">

**Example.** Five points lie in a unit square. Prove that two are at distance at most $$\sqrt2/2$$.

Divide the square into four squares of side $$1/2$$, assigning points on dividing lines to one adjacent square consistently. Two points share a small square. Its diagonal is

$$
\sqrt{(1/2)^2+(1/2)^2}=\frac{\sqrt2}{2},
$$

which bounds the distance between those points.

</div>

For numbers in an interval, dividing the interval into equal subintervals gives an analogous closeness argument. Endpoints matter if the desired conclusion uses a strict inequality.

---

## Choosing an Extremal Object

An **extremal argument** starts with a largest or smallest object, which forces additional structure. Combining that choice with pigeonhole can reveal boxes that were not obvious at first.

<div class="theorem-box">

**Example.** Prove that among any $$n+1$$ distinct numbers chosen from $$\{1,2,\ldots,2n\}$$, one divides another.

Write each chosen number uniquely as $$2^ku$$, where $$u$$ is odd. Use its odd part $$u$$ as its box label. There are only $$n$$ possible odd parts in the range, namely $$1,3,\ldots,2n-1$$.

Two selected numbers therefore share an odd part: $$2^au$$ and $$2^bu$$. Their exponents are different because the numbers are distinct. If $$a<b$$, then $$2^au$$ divides $$2^bu$$.

</div>

The useful representation here comes from repeatedly removing powers of two until the number is odd. Grouping by ordinary remainders would not directly give divisibility.

:::strategy
First describe what it would mean for every box to avoid the desired event. This gives a capacity bound and often reveals the correct boxes. For consecutive sums, use partial sums; for divisibility, try remainders or a canonical factorization; for distance, partition the region into small-diameter pieces.
:::

## Proving a Bound Is Sharp

A guarantee and a best possible guarantee are different claims. To prove a threshold is sharp, first show that crossing it forces the desired configuration, then construct an example at the threshold that avoids it. A construction is not an optional illustration; it is half of a sharp-bound solution.

For example, choosing $$n+1$$ numbers from $$1,\ldots,2n$$ forces a divisible pair by the odd-part argument. The threshold cannot be reduced to $$n$$ because the set $$\{n+1,\ldots,2n\}$$ has no divisible pair: twice any member already exceeds $$2n$$.

The counterexample often suggests the right boxes. If the extremal construction takes exactly one object from each group, those groups may be the boxes needed for the proof. Try to understand why one more choice creates a conflict.

<div class="theorem-box">

**Example.** Prove that choosing $$n+1$$ distinct numbers from $$1,\ldots,2n$$ forces a coprime pair.

Use the boxes $$\{1,2\},\{3,4\},\ldots,\{2n-1,2n\}$$. Two chosen numbers occupy the same box and are consecutive. A common divisor of consecutive integers divides their difference one, so they are coprime.

The example of all even numbers gives $$n$$ choices with no coprime pair when $$n\ge2$$, so the guarantee is sharp in that range.

</div>

The same number of objects can require very different boxes depending on the conclusion. Odd parts reveal divisibility; consecutive pairs reveal coprimality. Choosing boxes by habit rather than by the target relation is a common reason a pigeonhole attempt stalls.

---

## Subset-Sum Collisions

Sometimes the objects should be subsets rather than the original numbers. If many subsets have only a small range of possible sums, two must share a sum. Removing their common elements can turn an equality between overlapping subsets into an equality between disjoint collections.

<div class="theorem-box">

**Example.** Ten positive integers are each at most one hundred. Prove that two disjoint nonempty collections of their positions have equal sums.

There are $$2^{10}=1024$$ subsets of the ten positions, including the empty subset. Every subset sum is an integer between zero and one thousand, giving at most $$1001$$ boxes. Two different subsets therefore have equal sums.

Remove every position common to both subsets. The remaining collections are disjoint and still have equal sums. Neither can be empty: if one were empty and the other nonempty, positivity would make their sums different. Thus both are nonempty.

</div>

The positivity assumption is used only at the last step, but it is essential there. With arbitrary signed integers, a nonempty zero-sum subset could collide with the empty subset. That might still prove a useful statement, but it is a different conclusion.

The general counting principle is that $$2^n$$ subset objects exceed the number of possible sum values. Estimate the range first; if it is too large, try fixed-size subsets, residues, or a different statistic rather than assuming the collision is automatic.

---

## Fractional Parts and Rational Approximation

For a real number $$x$$, write $$\{x\}=x-\lfloor x\rfloor$$ for its fractional part in $$[0,1)$$. Two nearby fractional parts imply that the corresponding original values differ by nearly an integer.

This turns geometric interval boxes into an approximation theorem. Divide $$[0,1)$$ into $$N$$ half-open intervals of length $$1/N$$ and consider

$$
\{0\alpha\},\{\alpha\},\{2\alpha\},\ldots,\{N\alpha\}.
$$

Two of these $$N+1$$ values share an interval. Their indices differ by some $$q$$ with $$1\le q\le N$$, and their difference shows that for an integer $$p$$,

$$
\lvert q\alpha-p\rvert<\frac1N.
$$

Equivalently, $$\lvert\alpha-p/q\rvert<1/(qN)$$. This is a basic form of Dirichlet approximation. The denominator bound comes directly from the index difference.

<div class="theorem-box">

**Example.** Prove that some integer $$q$$ between one and ten satisfies $$\lvert q\sqrt2-p\rvert<1/10$$ for an integer $$p$$, and exhibit one such pair.

Apply the fractional-part argument with $$N=10$$. It guarantees a pair without locating it. For a concrete choice, take $$q=5,p=7$$:

$$
5\sqrt2-7=\frac{50-49}{5\sqrt2+7}=\frac1{5\sqrt2+7}<\frac1{10}.
$$

The pigeonhole proof gives existence, while rationalization verifies the chosen witness exactly.

</div>

---

## Increasing and Decreasing Subsequences

A **subsequence** keeps the original order but may skip entries. For distinct real numbers, a long enough sequence must have a long increasing or decreasing subsequence.

Suppose a sequence has $$(r-1)(s-1)+1$$ distinct entries. For entry $$a_i$$, let $$I_i$$ be the length of the longest increasing subsequence ending there and $$D_i$$ the analogous decreasing length. If no increasing subsequence has length $$r$$ and no decreasing one has length $$s$$, every pair $$(I_i,D_i)$$ lies in

$$
\{1,\ldots,r-1\}\times\{1,\ldots,s-1\}.
$$

There are only $$(r-1)(s-1)$$ boxes. Two entries cannot have the same pair: if $$i<j$$ and $$a_i<a_j$$, then $$I_j\ge I_i+1$$; if $$a_i>a_j$$, then $$D_j\ge D_i+1$$. Pigeonhole therefore gives a contradiction. This proves the Erdős–Szekeres subsequence theorem.

<div class="theorem-box">

**Example.** Show that seventeen distinct real numbers in a row contain an increasing or decreasing subsequence of length five, and show that sixteen do not suffice.

Use $$r=s=5$$, since $$(5-1)^2+1=17$$. For sharpness, consider

$$
4,3,2,1,\ 8,7,6,5,\ 12,11,10,9,\ 16,15,14,13.
$$

An increasing subsequence uses at most one number from each block, so has length at most four. A decreasing subsequence cannot cross from an earlier block to a later block because every later value is larger; it also has length at most four.

</div>

This argument illustrates a powerful trick: attach a structured label to each object. The boxes do not need to be simple remainders; a pair of extremal statistics can be the right encoding.

---

## A Small Zero-Sum Selection

Pigeonhole can sometimes force a sum involving a prescribed number of terms. The residue counts matter, not merely the existence of two equal residues.

<div class="theorem-box">

**Example.** Prove that among any five integers, three have a sum divisible by three.

Sort the integers into their three residue classes. If a class contains at least three integers, choose those three; their sum is zero modulo three.

Otherwise every class has at most two integers. Since there are five integers altogether, all three classes must be nonempty. Choose one from each class; their residues sum to $$0+1+2=3$$, again giving a multiple of three.

</div>

The case split handles both ways the objects can be distributed. This is stronger than simply observing that some residue class contains two integers, which does not yet supply a three-term sum.

---

## Pigeonhole with Impossible Extreme Boxes

A nominal list of possible values may contain values that cannot occur together. Removing that incompatibility can reduce the number of boxes by one and make the principle work.

<div class="theorem-box">

**Example.** In any group of $$n\ge2$$ people, acquaintance is mutual. Prove two people have the same number of acquaintances within the group.

Each count is between zero and $$n-1$$. However, a person knowing nobody and a person knowing everybody cannot both exist: the latter would know the former. Thus either zero or $$n-1$$ is absent, leaving at most $$n-1$$ possible counts for $$n$$ people. Two counts agree.

</div>

:::strategy
If the obvious boxes are one too numerous, look for an impossible combination of extremes. If the original objects are too few, build new objects such as partial sums or subsets. If the conclusion concerns order, try labels that measure the best structure ending at each position.
:::

---

## Sector Boxes in a Disk

Geometric boxes need not be rectangles. If the region is circular, angular sectors can give a stronger distance bound.

<div class="theorem-box">

**Example.** Seven points lie in a disk of radius one. Prove two have distance at most one.

Split the disk into six sectors of angle sixty degrees, assigning boundary points consistently. Two points share a sector. Let their distances from the center be $$r,s\in[0,1]$$ and their angular separation be $$\theta\le60^\circ$$.

Their squared distance is $$r^2+s^2-2rs\cos\theta\le r^2+s^2-rs$$. This quadratic reaches its maximum on the square $$0\le r,s\le1$$ at a corner: fixing either variable makes it convex in the other. The four corner values are zero, one, one, one.

Thus the squared distance is at most one, proving the claim.

</div>

The diameter of each chosen box is the property that matters. A sector's arc length is not its diameter, and the arc length alone would not justify the bound. Establish the geometric size of a box before applying pigeonhole.

---

## Key Bounds

:::equations
| Situation | Guarantee |
| --- | --- |
| General pigeonhole | Some box contains at least $$\lceil N/k\rceil$$ objects |
| Force $$r$$ in one of $$k$$ boxes | $$k(r-1)+1$$ objects suffice |
| Matching remainders | $$a\equiv b\pmod m\Longrightarrow m\mid(a-b)$$ |
| Consecutive block | $$S_j-S_i=a_{i+1}+\cdots+a_j$$ |
| Square of side $$s$$ | Any two points in it have distance at most $$s\sqrt2$$ |
| Fractional part | $$\{x\}=x-\lfloor x\rfloor\in[0,1)$$ |
| Approximation guarantee | Some $$1\le q\le N$$ and integer $$p$$ satisfy $$\lvert q\alpha-p\rvert<1/N$$ |
| Monotone subsequences | $$(r-1)(s-1)+1$$ distinct entries force an increasing $$r$$-term or decreasing $$s$$-term subsequence |
| Subset-sum collision | $$2^n>\sum_i a_i+1$$ suffices for two equal subset sums of positive integers |
:::
