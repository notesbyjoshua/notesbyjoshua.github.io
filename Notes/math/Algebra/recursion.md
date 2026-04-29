---
layout: default
title: "Recursion"
parent: Math
nav_order: 4
permalink: /notes/math/algebra/recursion/
---

# Recursion

The heart of recursion is to assume that you know previous elements of a sequence and then find a way to construct the next element in that sequence. Not only will explicit recursion problems appear of the AIME, USAMO, or USAJMO, often counting or combinatoric problems include them as well.

## Generating Functions

Generating functions are one of the cleanest ways to solve linear recurrences. They are also a powerful summation tool, so this section is adapted from the generating-functions part of the summations handout and placed here because it fits recursion especially well.

The basic idea is this: given a sequence $$a_n$$, package it into the formal power series

$$
A(x) = \sum_{n \ge 0} a_n x^n.
$$

That lets us turn a whole sequence into one algebraic object. This is useful because:

- $$A(x)$$ may have a nice closed form.
- The coefficients of $$A(x)$$ encode the entire sequence.
- Recurrence relations often turn into algebraic equations in $$A(x)$$.
- Once you get a rational expression for $$A(x)$$, partial fractions can recover a closed form.

### Toy Applications

**Example 5.1.** Show that

$$
\sum_{n \ge 0} \binom{1000}{n} = 2^{1000}.
$$

Let $$a_n=\binom{1000}{n}$$. Then

$$
A(x)=\sum_{n \ge 0} a_nx^n=\sum_{n \ge 0}\binom{1000}{n}x^n=(1+x)^{1000}.
$$

Plugging in $$x=1$$ gives the identity immediately.

**Example 5.2.** Compute

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

<div class="theorem-box" markdown="1">
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

**Proof.** Consider the generating function

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

<div class="theorem-box" markdown="1">
**Theorem 5.6 (Generalized Binomial Theorem).** For any real number $$r$$,

$$
(1+x)^r = \sum_{n \ge 0} \binom{r}{n}x^n,
$$

where

$$
\binom{r}{n} = \frac{r(r-1)\cdots(r-n+1)}{n!}.
$$
</div>

**Proof sketch.** Write

$$
(1+x)^r = a_0+a_1x+a_2x^2+a_3x^3+\cdots
$$

and differentiate enough times to isolate the coefficient you want. For example, comparing constant terms after three derivatives gives

$$
a_3=\frac{r(r-1)(r-2)}{3!}.
$$

Important consequences:

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

**Example 5.8 (HMMT 2007 Combinatorics #9).** Let $$S$$ be the set of triples $$(i,j,k)$$ of positive integers satisfying $$i+j+k=17$$. Compute

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

### Snake Oil Method

The "Snake Oil" method is a systematic way to evaluate a sum depending on a free variable. Suppose

$$
a_n=\sum_k F(k,n).
$$

Instead of attacking $$a_n$$ directly, form the generating function

$$
A(x)=\sum_{n \ge 0} a_nx^n
= \sum_{n \ge 0}\sum_k F(k,n)x^n.
$$

Now switch the order:

$$
A(x)=\sum_k \sum_{n \ge 0} F(k,n)x^n.
$$

If the inner sums become recognizable generating functions, the problem becomes much easier.

**Example 5.9.** For $$n \ge 0$$, compute

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

**Example 5.10.** For $$n \ge 0$$, compute

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
