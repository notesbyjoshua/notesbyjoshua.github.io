---
title: "Recursion"
description: "Math notes on recursive sequences, explicit formulas, recurrence relations, iteration, and pattern-based problem solving."
next: false
status: developing
progress: 72
sidebar:
  order: 6
---

<!--
Topic plan:
- Recursive sequences and explicit formulas
- Recursive counting
- Catalan numbers
- Linear recurrence relations
- Ordinary generating functions
- Coefficient extraction and the snake oil method
-->

## Introduction to Recurrence

Recursion uses earlier terms of a sequence to construct the next term. It appears in explicit recurrence problems on the AIME, USAMO, and USAJMO, as well as in counting and other combinatorics problems.

These notes are adapted in part from Jeffrey Chen's *Recursion in the AIME* handout and the generating-functions section of the summations notes.

A **recurrence relation** expresses a term of a sequence in terms of earlier terms. For example,

$$
a_n = 3a_{n-1}
$$

means that every term is three times the previous one. If $$a_1=1$$, then

$$
a_2=3,\qquad a_3=9,\qquad a_4=27,
$$

so the sequence begins

$$
1,3,9,27,81,\dots
$$

Because the relation holds for every valid $$n$$, we can repeatedly substitute backwards. For instance, if

$$
a_n=3a_{n-1}
\qquad\text{and}\qquad
a_{n-1}=3a_{n-2},
$$

then

$$
a_n=9a_{n-2}.
$$

In contest math, we often do not need a closed form.

:::strategy
- Define a sequence clearly.
- Find a recurrence.
- Compute initial values.
- Build a short table until you reach the term you want.
:::

## Explicit Formulas and Shifts

An **explicit formula** computes $$a_n$$ directly from $$n$$. Repeatedly applying $$a_n=ra_{n-1}$$ gives $$a_n=a_0r^n$$ when the indexing starts at zero. An arithmetic recurrence $$a_n=a_{n-1}+d$$ similarly gives $$a_n=a_0+nd$$. Check the starting index: with $$a_1$$ instead, the exponents and increments use $$n-1$$.

For an affine recurrence $$a_{n+1}=ra_n+c$$ with $$r\ne1$$, find a fixed value $$L=rL+c$$. Subtracting it gives $$a_{n+1}-L=r(a_n-L)$$, a geometric recurrence.

<div class="theorem-box">

**Example.** A sequence satisfies $$a_0=1$$ and $$a_{n+1}=3a_n+4$$. Find $$a_n$$.

The fixed value solves $$L=3L+4$$, so $$L=-2$$. Set $$b_n=a_n+2$$. Then $$b_{n+1}=3b_n$$ and $$b_0=3$$, giving

$$
a_n=b_n-2=3^{n+1}-2.
$$

At $$n=0$$ this gives one, and substitution reproduces the recurrence, verifying the formula.

</div>

### Characteristic Roots

For a homogeneous linear recurrence $$a_n=pa_{n-1}+qa_{n-2}$$, try a solution $$a_n=r^n$$. This gives the **characteristic equation** $$r^2-pr-q=0$$. If its roots $$r_1,r_2$$ are distinct, the general solution is $$A r_1^n+B r_2^n$$, with the constants determined by two initial values. Substitution verifies the recurrence, and the initial values determine every later term uniquely.

<div class="theorem-box">

**Example.** Find the sequence with $$a_0=0$$, $$a_1=1$$, and $$a_n=5a_{n-1}-6a_{n-2}$$ for $$n\ge2$$.

The characteristic equation is $$(r-2)(r-3)=0$$. Write $$a_n=A2^n+B3^n$$. The initial values give $$A+B=0$$ and $$2A+3B=1$$, hence $$A=-1,B=1$$. Thus

$$
a_n=3^n-2^n.
$$

</div>

For a nonzero repeated characteristic root $$r$$, use $$(A+Bn)r^n$$ instead. Nonhomogeneous recurrences need an additional particular solution; the fixed-value shift above is one simple example.

### Iteration Modulo an Integer

When only a remainder is requested, track residues rather than the entire sequence. For a first-order recurrence modulo $$m$$, there are only $$m$$ states, so some state eventually repeats. A deterministic transition then repeats forever from that point. For a second-order recurrence, the state must include the pair of consecutive residues.

<div class="theorem-box">

**Example.** Let $$a_0=0$$ and $$a_{n+1}=a_n^2+1$$. Find $$a_{100}\pmod5$$.

The residues are $$0,1,2,0,1,2,\ldots$$. The return to the full state zero proves a period of three. Since $$100\equiv1\pmod3$$, the requested remainder is $$1$$.

</div>

---

## Recursive Counting

Recursion becomes especially useful when direct counting is messy but a "last move" or "final case split" is easy to describe.

### Staircase Problem

<div class="theorem-box">

**Example.** Fred wants to climb a $$10$$-step staircase. He can climb either $$1$$ or $$2$$ steps at a time. In how many ways can he climb the staircase?

**Solution.** Instead of counting only the $$10$$-step case, define

$$
a_n = \text{the number of ways to climb } n \text{ stairs}.
$$

Now think about Fred's last move:

- If his last move is a single step, then before that he had climbed $$n-1$$ stairs.
- If his last move is a double step, then before that he had climbed $$n-2$$ stairs.

These are the only possibilities, so

$$
a_n = a_{n-1} + a_{n-2}.
$$

The initial values are

$$
a_1=1,\qquad a_2=2.
$$

So the sequence begins

$$
1,2,3,5,8,13,21,34,55,89.
$$

Therefore,

$$
a_{10}=89.
$$

This is the Fibonacci recurrence in disguise, which appears constantly in AMC and AIME counting problems.

</div>

### Spacy Subsets

<div class="theorem-box">

**Example.** (2007 AMC 12) Call a set of integers **spacy** if it contains no more than one out of any three consecutive integers. How many subsets of $$\{1,2,3,\dots,12\}$$, including the empty set, are spacy?

**Solution.** Let

$$
a_n = \text{the number of spacy subsets of } \{1,2,\dots,n\}.
$$

Now split into two cases:

- If a spacy subset contains $$n$$, then it cannot contain $$n-1$$ or $$n-2$$. So the rest of the set is a spacy subset of $$\{1,2,\dots,n-3\}$$, giving $$a_{n-3}$$ possibilities.
- If a spacy subset does not contain $$n$$, then it is just a spacy subset of $$\{1,2,\dots,n-1\}$$, giving $$a_{n-1}$$ possibilities.

Hence

$$
a_n=a_{n-1}+a_{n-3}.
$$

The initial values are

$$
a_1=2,\qquad a_2=3,\qquad a_3=4,
$$

since the spacy subsets are:

- for $$n=1$$: $$\varnothing,\{1\}$$,
- for $$n=2$$: $$\varnothing,\{1\},\{2\}$$,
- for $$n=3$$: $$\varnothing,\{1\},\{2\},\{3\}$$.

Now compute forward:

$$
\begin{aligned}
a_4&=6, & a_5&=9, & a_6&=13, \\
a_7&=19, & a_8&=28, & a_9&=41, \\
a_{10}&=60, & a_{11}&=88, & a_{12}&=129.
\end{aligned}
$$

So the answer is

$$
129.
$$

</div>

### Tower of Cubes

<div class="theorem-box">

**Example.** (AIME 2006) A collection of eight cubes consists of one cube with edge length $$k$$ for each integer $$k$$ from $$1$$ to $$8$$. A tower is built using all eight cubes, and the cube immediately on top of a cube with edge length $$k$$ must have edge length at most $$k+2$$. How many towers can be constructed?

**Solution.** Define

$$
a_n=\text{the number of valid towers using cubes }1,2,\dots,n.
$$

Look at the cube of edge length $$n$$. In a valid tower, it can be:

- at the bottom,
- directly above cube $$n-1$$,
- directly above cube $$n-2$$.

So for each valid tower on $$n-1$$ cubes, there are exactly three ways to insert cube $$n$$. Thus

$$
a_n=3a_{n-1}.
$$

We begin with

$$
a_2=2,
$$

since either the cube of side length $$1$$ is on the bottom and $$2$$ is on top, or vice versa.

Then

$$
a_8 = 3^6 \cdot a_2 = 3^6 \cdot 2 = 1458.
$$

This is a good reminder that some recurrences only become valid after the first few terms; here the relation is not meant to be applied at $$n=2$$ itself.

</div>

## Catalan Numbers

Catalan numbers arise in many recursive counting problems where a structure splits naturally into a left part and a right part.

<div class="theorem-box">

**Example.** How many paths are there from $$(0,0)$$ to $$(n,n)$$ using only right and up steps, such that the path never goes above the line $$y=x$$?

Let

$$
C_n=\text{the number of such paths from }(0,0)\text{ to }(n,n).
$$

To get a recurrence, look at the **first** point $$(i,i)$$ after $$(0,0)$$ where the path returns to the diagonal.

Then:

- the initial portion of the path contributes $$C_{i-1}$$ possibilities,
- the remaining portion contributes $$C_{n-i}$$ possibilities.

Summing over all possible first return points gives

$$
C_n = C_0C_{n-1}+C_1C_{n-2}+\cdots+C_{n-1}C_0
=\sum_{i=0}^{n-1} C_iC_{n-i-1}.
$$

For example, when $$n=3$$, there are $$5$$ such paths.

</div>

<div class="theorem-box">

**Theorem 4.2 (Catalan Numbers).** The $$n$$th Catalan number has explicit formula

$$
C_n=\frac{1}{n+1}\binom{2n}{n}.
$$

</div>

The reflection argument on the [distributions and lattice paths](/notes/math/combinatorics/distributions-and-lattice-paths/) page proves this closed form. Here the recurrence shows how it arises from splitting a path at its first return to the diagonal.

### Balanced Brackets

<div class="theorem-box">

**Example.** How many ways are there to arrange $$n$$ open brackets and $$n$$ closed brackets so that, reading from left to right, the number of closed brackets never exceeds the number of open brackets?

**Solution.** This is a Catalan-number problem.

Make the following bijection:

- each open bracket corresponds to a step to the right,
- each closed bracket corresponds to a step upward.

Then a bracket string with $$n$$ opens and $$n$$ closes becomes a path from $$(0,0)$$ to $$(n,n)$$. The condition that the number of closed brackets never exceeds the number of open brackets means the path never goes above the line $$y=x$$.

So the answer is simply

$$
C_n=\frac{1}{n+1}\binom{2n}{n}.
$$

</div>

## Generating Functions

Generating functions turn linear recurrences into algebraic equations and can also help evaluate sums. This section adapts the generating-functions material from the summations handout to recurrence problems. For a nonnegative integer upper index, use $$\binom nk=0$$ when $$k<0$$ or $$k>n$$; this convention lets us write coefficient sums without extra endpoint cases.

The basic idea is this: given a sequence $$a_n$$, package it into the formal power series

$$
A(x) = \sum_{n \ge 0} a_n x^n.
$$

Here $$[x^n]A(x)$$ denotes the coefficient of $$x^n$$, so $$[x^n]A(x)=a_n$$. We use formal power series: identities are compared coefficient by coefficient without assigning a numerical value to $$x$$. A rearrangement is valid in this setting when each coefficient receives only finitely many contributions. If we evaluate an infinite series at a numerical $$x$$, we must also check convergence.

Multiplying generating functions performs a convolution: $$[x^n](A(x)B(x))=\sum_{k=0}^n a_kb_{n-k}$$. This is why products describe structures built from two independent size contributions.

That lets us turn a whole sequence into one algebraic object. This is useful because:

- $$A(x)$$ may have a nice closed form.
- The coefficients of $$A(x)$$ encode the entire sequence.
- Recurrence relations often turn into algebraic equations in $$A(x)$$.
- Once you get a rational expression for $$A(x)$$, partial fractions can recover a closed form.

### Toy Applications

<div class="theorem-box">

**Example.** Show that

$$
\sum_{n \ge 0} \binom{1000}{n} = 2^{1000}.
$$

Let $$a_n=\binom{1000}{n}$$. Then

$$
A(x)=\sum_{n \ge 0} a_nx^n=\sum_{n \ge 0}\binom{1000}{n}x^n=(1+x)^{1000}.
$$

Plugging in $$x=1$$ gives the identity immediately.

</div>

<div class="theorem-box">

**Example.** Compute

$$
\sum_{n \ge 0} n\binom{1000}{n}.
$$

Differentiate the previous generating function:

$$
\sum_{n \ge 1} n\binom{1000}{n}x^{n-1} = 1000(1+x)^{999}.
$$

Now set $$x=1$$:

$$
\sum_{n \ge 0} n\binom{1000}{n}=1000\cdot 2^{999}.
$$

</div>

**Exercise 5.3.** Compute

$$
\sum_{n \ge 0} n^2\binom{1000}{n}.
$$

### Linear Recurrences

Consider the Lucas numbers $$L_n$$ defined by

$$
L_0=2,\qquad L_1=1,\qquad L_{n+2}=L_{n+1}+L_n.
$$

The first few terms are

$$
2,1,3,4,7,11,18,29,\dots
$$

<div class="theorem-box">

**Theorem 5.4 (Closed Form for Lucas Numbers).** Let

$$
\alpha=\frac{1+\sqrt5}{2},
\qquad
\beta=\frac{1-\sqrt5}{2}.
$$

Then

$$
L_n=\alpha^n+\beta^n.
$$

</div>

<div class="theorem-box">

**Proof (Lucas-number formula).** Consider the generating function

$$
L(x)=\sum_{n \ge 0} L_nx^n = 2+x+3x^2+4x^3+7x^4+\cdots.
$$

Now write shifted copies:

$$
xL(x)=2x+x^2+3x^3+4x^4+\cdots,
$$

$$
x^2L(x)=2x^2+x^3+3x^4+\cdots.
$$

Because $$L_{n+2}=L_{n+1}+L_n$$, subtracting gives

$$
L(x)-xL(x)-x^2L(x)=2-x.
$$

So

$$
(1-x-x^2)L(x)=2-x,
$$

hence

$$
L(x)=\frac{2-x}{1-x-x^2}.
$$

Factor the denominator:

$$
1-x-x^2=(1-\alpha x)(1-\beta x).
$$

Then partial fractions give

$$
L(x)=\frac{1}{1-\alpha x}+\frac{1}{1-\beta x}.
$$

Expand each as a geometric series:

$$
L(x)=\sum_{n \ge 0}(\alpha x)^n + \sum_{n \ge 0}(\beta x)^n
=\sum_{n \ge 0}(\alpha^n+\beta^n)x^n.
$$

Matching coefficients yields

$$
L_n=\alpha^n+\beta^n.
$$

</div>

**Exercise 5.5.** Derive Binet's formula for Fibonacci numbers:

$$
F_n=\frac{1}{\sqrt5}(\alpha^n-\beta^n).
$$

As an intermediate step, show that the Fibonacci generating function is

$$
\frac{x}{1-x-x^2}.
$$

### Common Generating Functions

We already know

$$
\frac{1}{1-x}=1+x+x^2+\cdots
$$

and

$$
(1+x)^n=\sum_{k \ge 0}\binom{n}{k}x^k.
$$

The next result gives many more useful expansions.

<div class="theorem-box">

**Theorem 5.6 (Generalized Binomial Theorem).** For any real number $$r$$, the following is a formal power-series identity. As a numerical series it converges to the stated function for $$\lvert x\rvert<1$$; if $$r$$ is a nonnegative integer, it is a finite polynomial identity valid for every $$x$$:

$$
(1+x)^r = \sum_{n \ge 0} \binom{r}{n}x^n,
$$

where $$\binom r0=1$$ and, for $$n\ge1$$,

$$
\binom{r}{n} = \frac{r(r-1)\cdots(r-n+1)}{n!}.
$$

</div>

<div class="theorem-box">

**Proof (Generalized binomial coefficients).** Write

$$
(1+x)^r = a_0+a_1x+a_2x^2+a_3x^3+\cdots
$$

and differentiate enough times to isolate the coefficient you want. For example, comparing constant terms after three derivatives gives

$$
a_3=\frac{r(r-1)(r-2)}{3!},\qquad
a_n=\frac{r(r-1)\cdots(r-n+1)}{n!}.
$$

</div>

Important consequences, interpreted formally or within their intervals of convergence:

- Setting $$r=-1$$ gives
  $$
  \frac{1}{1+x}=\sum_{n \ge 0}(-x)^n.
  $$
- More generally,
  $$
  \frac{1}{(1-x)^{m+1}}=\sum_{k \ge 0}\binom{k+m}{m}x^k.
  $$
- Also,
  $$
  \frac{x^m}{(1-x)^{m+1}}=\sum_{k \ge 0}\binom{k}{m}x^k.
  $$
- A very important identity is
  $$
  \frac{1}{\sqrt{1-4x}}=\sum_{k \ge 0}\binom{2k}{k}x^k.
  $$
- Integrating that identity gives the Catalan generating function:
  $$
  \frac{1-\sqrt{1-4x}}{2x}=\sum_{k \ge 0} C_kx^k,
  $$
  where
  $$
  C_k=\frac{1}{k+1}\binom{2k}{k}.
  $$
- The exponential series is
  $$
  e^x=\sum_{k \ge 0}\frac{x^k}{k!}.
  $$

For quick reference:

| Generating function | Sequence |
| --- | --- |
| $$ (1+x)^n $$ | $$ \displaystyle \sum_{k \ge 0}\binom{n}{k}x^k $$ |
| $$ \dfrac{1}{(1-x)^{m+1}} $$ | $$ \displaystyle \sum_{k \ge 0}\binom{k+m}{m}x^k $$ |
| $$ \dfrac{x^m}{(1-x)^{m+1}} $$ | $$ \displaystyle \sum_{k \ge 0}\binom{k}{m}x^k $$ |
| $$ \dfrac{1}{\sqrt{1-4x}} $$ | $$ \displaystyle \sum_{k \ge 0}\binom{2k}{k}x^k $$ |
| $$ \dfrac{1-\sqrt{1-4x}}{2x} $$ | $$ \displaystyle \sum_{k \ge 0} C_kx^k $$ |
| $$ e^x $$ | $$ \displaystyle \sum_{k \ge 0}\frac{x^k}{k!} $$ |

<div class="theorem-box">

**Example.** (HMMT 2007 Combinatorics #9) Let $$S$$ be the set of triples $$(i,j,k)$$ of positive integers satisfying $$i+j+k=17$$. Compute

$$
\sum_{(i,j,k)\in S} ijk.
$$

Consider

$$
F(x)=\left(\sum_{i \ge 0} ix^i\right)\left(\sum_{j \ge 0} jx^j\right)\left(\sum_{k \ge 0} kx^k\right).
$$

We want the coefficient of $$x^{17}$$. Since

$$
\sum_{n \ge 0} nx^n = \frac{x}{(1-x)^2},
$$

we get

$$
F(x)=\left(\frac{x}{(1-x)^2}\right)^3 = \frac{x^3}{(1-x)^6}.
$$

So we need the coefficient of $$x^{14}$$ in $$\frac{1}{(1-x)^6}$$, which is

$$
\binom{19}{5}.
$$

</div>

### Snake Oil Method

The "Snake Oil" method is a systematic way to evaluate a sum depending on a free variable. Suppose

$$
a_n=\sum_k F(k,n).
$$

:::strategy
- Instead of attacking $$a_n$$ directly, form the generating function $$A(x)=\sum_{n \ge 0} a_nx^n = \sum_{n \ge 0}\sum_k F(k,n)x^n$$.
- Switch the order of summation to get $$A(x)=\sum_k \sum_{n \ge 0} F(k,n)x^n$$.
- If the inner sums become recognizable generating functions, the problem becomes much easier.
:::

<div class="theorem-box">

**Example.** For $$n \ge 0$$, compute

$$
\sum_{k \ge 0}\binom{n+k}{2k}2^{n-k}.
$$

Let

$$
A(x)=\sum_{n \ge 0}\left[\sum_{k \ge 0}\binom{n+k}{2k}2^{n-k}\right]x^n.
$$

Then

$$
A(x)=\sum_{k \ge 0}\sum_{n \ge 0}\binom{n+k}{2k}2^{n-k}x^n.
$$

After shifting indices and using

$$
\sum_{a \ge 0}\binom{a+2k}{2k}(2x)^a = \frac{1}{(1-2x)^{2k+1}},
$$

we obtain

$$
A(x)=\sum_{k \ge 0} x^k\frac{1}{(1-2x)^{2k+1}}
= \frac{1}{1-2x}\sum_{k \ge 0}\left(\frac{x}{(1-2x)^2}\right)^k.
$$

This is geometric:

$$
A(x)=\frac{1}{1-2x}\cdot \frac{1}{1-\frac{x}{(1-2x)^2}}
= \frac{1-2x}{1-5x+4x^2}.
$$

Partial fractions give

$$
A(x)=\frac{1}{3}\cdot \frac{1}{1-x} + \frac{2}{3}\cdot \frac{1}{1-4x}.
$$

Therefore

$$
A(x)=\sum_{n \ge 0}\left(\frac13+\frac23\cdot 4^n\right)x^n,
$$

so

$$
\sum_{k \ge 0}\binom{n+k}{2k}2^{n-k}=\frac13+\frac23\cdot 4^n.
$$

</div>

<div class="theorem-box">

**Example.** For $$n \ge 0$$, compute

$$
\sum_{k \ge 0}\binom{k}{n-k}.
$$

Again,

$$
\sum_{n \ge 0}\left[\sum_{k \ge 0}\binom{k}{n-k}\right]x^n
= \sum_{k \ge 0}\sum_{n \ge 0}\binom{k}{n-k}x^n.
$$

Rewrite using $$x^k$$:

$$
= \sum_{k \ge 0} x^k \sum_{k \le n \le 2k}\binom{k}{n-k}x^{n-k}
= \sum_{k \ge 0} x^k(1+x)^k.
$$

Thus

$$
= \frac{1}{1-x(1+x)}
= \frac{1}{1-x-x^2}.
$$

This is the Fibonacci generating function, so the sum equals $$F_{n+1}$$.

If the free variable appears in many places at once, Snake Oil often works better after you first generalize the identity.

</div>

### Problems

**Problem 5.11.** Prove that for every integer $$n \ge 0$$,

$$
\sum_{a+b=n}\binom{2a}{a}\binom{2b}{b}=4^n.
$$

**Problem 5.12.** For integers $$m,n \ge 0$$, prove that

$$
\sum_{a+b=m}(-1)^a \binom{n}{a}\binom{n+b-1}{b}
=
\begin{cases}
1 & m=0, \\
0 & m>0.
\end{cases}
$$

**Problem 5.13.** Let $$m \le n$$ be positive integers. Compute

$$
\sum_{k=m}^{n}\binom{n}{k}\binom{k}{m}.
$$

**Problem 5.14.** For $$m,n \ge 1$$, compute

$$
\sum_{k \ge 0}\binom{n+k}{m+2k}\binom{2k}{k}\frac{(-1)^k}{k+1}.
$$

---

## Choosing States for Restricted Counting

A single count $$a_n$$ may not contain enough information to extend a structure by one step. Define several states that record exactly the feature affecting the next choice. Extra history that cannot influence later moves is unnecessary; missing relevant history leads to an incorrect recurrence.

For strings with forbidden runs, the length of the current trailing run is a natural state. For tilings, record the shape of the unfinished boundary. For a random walk, record the current position and any feature that changes the transition rule.

<div class="theorem-box">

**Example.** Find the number of binary strings of length eight containing no three consecutive ones, and derive a generating function for the counts.

Let $$a_n$$ count valid strings of length $$n$$, with $$a_0=1$$ for the empty string. A valid string ends with zero, with zero followed by one, or with zero followed by two ones, except for the short strings handled by initial values. For $$n\ge3$$ this gives

$$
a_n=a_{n-1}+a_{n-2}+a_{n-3},\qquad a_0=1,\ a_1=2,\ a_2=4.
$$

Equivalently, use states for trailing runs of zero, one, or two ones. Appending zero sends every state to the first; appending one advances the run length and is forbidden from the third state.

The counts are $$1,2,4,7,13,24,44,81,149$$, so the answer is $$149$$. Multiplying $$A(x)=\sum_{n\ge0}a_nx^n$$ by the recurrence denominator leaves only the initial corrections:

$$
(1-x-x^2-x^3)A(x)=1+x+x^2.
$$

Thus $$A(x)=(1+x+x^2)/(1-x-x^2-x^3)$$. The numerator records the initial conditions rather than being an arbitrary adjustment.

</div>

---

## Repeated Roots and Nonhomogeneous Terms

For a repeated nonzero characteristic root $$r$$, the two independent solutions are $$r^n$$ and $$nr^n$$. The extra factor of $$n$$ is necessary because two constant multiples of the same geometric sequence would supply only one free initial condition.

<div class="theorem-box">

**Example.** Solve $$a_n=6a_{n-1}-9a_{n-2}$$ with $$a_0=1,a_1=6$$.

The characteristic polynomial is $$(t-3)^2$$, so use $$a_n=(A+Bn)3^n$$. The first value gives $$A=1$$, and the second gives $$3(1+B)=6$$, hence $$B=1$$. Therefore

$$
a_n=(n+1)3^n.
$$

Substitution verifies the recurrence. Together with the two initial values, uniqueness of the recursively defined sequence proves the formula.

</div>

For a nonhomogeneous recurrence, first solve the homogeneous part and then find one particular solution. If the forcing term already resembles a homogeneous solution, multiply the trial by $$n$$, or by a higher power of $$n$$ when there is repeated overlap. This is the discrete counterpart of resonance in differential equations.

<div class="theorem-box">

**Example.** Solve $$a_{n+1}=2a_n+2^n$$ with $$a_0=0$$.

A trial $$C2^n$$ fails because the homogeneous recurrence already has that form. Instead, divide by the common geometric factor. Let $$b_n=a_n/2^n$$. Then

$$
b_{n+1}=b_n+\frac12.
$$

With $$b_0=0$$, we obtain $$b_n=n/2$$ and $$a_n=n2^{n-1}$$. This transformation also explains why the factor of $$n$$ appears.

</div>

---

## Nonlinear Recurrences That Become Linear

The apparent degree of a recurrence can be misleading. A reciprocal, shift, or ratio may reveal a linear relation. Choose the substitution by examining how the operation changes the denominator or the fixed points.

<div class="theorem-box">

**Example.** A sequence satisfies $$a_0=1/2$$ and $$a_{n+1}=a_n/(1+a_n)$$. Find $$a_n$$ and its limit.

All terms remain positive, so reciprocals are allowed. Set $$b_n=1/a_n$$. The recurrence becomes

$$
b_{n+1}=b_n+1,\qquad b_0=2.
$$

Hence $$b_n=n+2$$ and $$a_n=1/(n+2)$$. The terms tend to zero. Guessing the limit from the fixed-point equation alone would not have proved convergence; the explicit formula proves both the values and the limit.

</div>

For recurrences involving two coupled quantities, an invariant can be more useful than a closed form. Under the update

$$
x'=3x+4y,\qquad y'=2x+3y,
$$

direct expansion gives $$x'^2-2y'^2=x^2-2y^2$$. Starting from $$(3,2)$$ therefore produces integer solutions of $$x^2-2y^2=1$$ forever. When the question concerns divisibility or an equation satisfied by the terms, this invariant may answer it without diagonalizing the update.

---

## Ordinary and Exponential Generating Functions

Ordinary generating functions multiply by convolution because the coefficient records only the total size. For labeled objects, an **exponential generating function** uses $$a_nx^n/n!$$ instead. The factorial denominator makes multiplication insert the binomial coefficient choosing which labels belong to each component:

$$
n![x^n]\left(\sum_i\frac{a_ix^i}{i!}\right)
\left(\sum_j\frac{b_jx^j}{j!}\right)
=\sum_{i=0}^n\binom ni a_ib_{n-i}.
$$

Use the ordinary version for counts where sizes split without choosing labels, and the exponential version when distributing distinct labels among components. The two conventions encode different counting rules; switching between them without changing coefficients changes the problem.

For example, assigning $$n$$ distinct objects to three named nonempty boxes is counted by $$n![x^n](e^x-1)^3$$. Expanding the cube gives $$3^n-3\cdot2^n+3$$ for $$n\ge1$$, agreeing with inclusion–exclusion. This connection explains why generating functions can recover formulas first found by a completely different method.

:::tip
After deriving a recurrence or generating function, compare the first few coefficients with direct small cases. Include the empty object when it represents one valid construction, and keep track of whether the recurrence begins at zero, one, or a later index.
:::

---

## Key Equations

:::equations
| Tool | Formula and conditions |
| --- | --- |
| Geometric recurrence | $$a_n=a_0r^n$$ for $$a_n=ra_{n-1}$$ |
| Affine shift | $$a_n=L+(a_0-L)r^n$$, $$L=c/(1-r)$$, for $$a_{n+1}=ra_n+c$$ and $$r\ne1$$ |
| Second-order characteristic equation | $$r^2-pr-q=0$$ for $$a_n=pa_{n-1}+qa_{n-2}$$ |
| Catalan numbers | $$C_0=1$$, $$C_n=\sum_{i=0}^{n-1}C_iC_{n-1-i}=\binom{2n}n/(n+1)$$ |
| Ordinary generating function | $$A(x)=\sum_{n\ge0}a_nx^n$$, $$[x^n]A(x)=a_n$$ |
| Coefficient convolution | $$[x^n](AB)=\sum_{k=0}^n a_kb_{n-k}$$ |
| Fibonacci generating function | $$\sum_{n\ge0}F_nx^n=x/(1-x-x^2)$$, $$F_0=0,F_1=1$$ |
| Negative binomial series | $$(1-x)^{-m-1}=\sum_{k\ge0}\binom{k+m}m x^k$$, integer $$m\ge0$$; formal or $$\lvert x\rvert<1$$ |
| Run restriction | $$a_n=a_{n-1}+a_{n-2}+a_{n-3}$$ for binary strings avoiding three consecutive ones |
| Repeated characteristic root | $$a_n=(A+Bn)r^n$$ for a nonzero double root $$r$$ |
| Exponential generating function | $$A_{\mathrm{exp}}(x)=\sum_{n\ge0}a_nx^n/n!$$ |
| Coupled Pell invariant | $$(3x+4y)^2-2(2x+3y)^2=x^2-2y^2$$ |
:::

## Practice Problems

These are good recursion problems to revisit after you are comfortable with the examples above.

**Exercise 5.1.** How many ways are there to tile a $$10 \times 2$$ board with $$1 \times 2$$ dominoes?

**Exercise 5.2 (AMC 12 2019).** How many binary sequences of length $$19$$ begin with $$0$$, end with $$0$$, contain no two consecutive $$0$$'s, and contain no three consecutive $$1$$'s?

**Exercise 5.3 (AIME 2015).** There are $$2^{10}=1024$$ possible $$10$$-letter strings using only $$A$$ and $$B$$. How many do not contain more than three adjacent identical letters?

**Exercise 5.4.** Given a regular $$2n$$-gon, how many ways are there to pair vertices with nonintersecting chords?

**Exercise 5.5 (AIME 2001).** A mail carrier delivers mail to the nineteen houses on one side of Elm Street. No two adjacent houses receive mail on the same day, and there are never more than two consecutive houses that get no mail. How many delivery patterns are possible?
