---
layout: default
title: "Unit 10: Infinite Sums and Series (BC-only)"
parent: "AP Calculus AB/BC"
nav_order: 10
permalink: /notes/math/infsumseries/
---

# Unit 10: Infinite Sums and Series (BC-only)

This BC-only unit is about representing functions and numbers through infinitely many terms, and then deciding when those infinite processes make sense.

---

## Sequences

A sequence is a function whose domain is the positive integers:

$$
a_1, a_2, a_3, \dots
$$

We write

$$
\lim_{n \to \infty} a_n = L
$$

if the terms approach $$L$$.

If $$\sum a_n$$ converges, then necessarily $$a_n \to 0$$. The converse is false.

---

## Infinite series

A series is the sum

$$
\sum_{n=1}^{\infty} a_n.
$$

Its convergence is defined by the sequence of partial sums:

$$
S_N = \sum_{n=1}^{N} a_n.
$$

---

## Geometric series

$$
\sum_{n=0}^{\infty} ar^n
$$

converges when $$|r| < 1$$ and then

$$
\sum_{n=0}^{\infty} ar^n = \frac{a}{1-r}.
$$

---

## Harmonic and p-series

The harmonic series

$$
\sum_{n=1}^{\infty} \frac{1}{n}
$$

diverges.

The p-series

$$
\sum_{n=1}^{\infty} \frac{1}{n^p}
$$

converges if and only if $$p>1$$.

---

## Integral Test

If $$f(x)$$ is positive, continuous, and decreasing for large $$x$$ with $$f(n)=a_n$$, then

$$
\sum a_n
$$

and

$$
\int f(x)\,dx
$$

either both converge or both diverge.

---

## Comparison tests

Direct comparison:

- if $$0 \le a_n \le b_n$$ and $$\sum b_n$$ converges, then $$\sum a_n$$ converges,
- if $$0 \le b_n \le a_n$$ and $$\sum b_n$$ diverges, then $$\sum a_n$$ diverges.

Limit comparison:

If

$$
\lim_{n \to \infty} \frac{a_n}{b_n} = c
$$

with $$0<c<\infty$$, then $$\sum a_n$$ and $$\sum b_n$$ behave the same.

---

## Alternating series

An alternating series often has the form

$$
\sum_{n=1}^{\infty} (-1)^n b_n
$$

or

$$
\sum_{n=1}^{\infty} (-1)^{n+1} b_n
$$

with $$b_n > 0$$.

The Alternating Series Test says the series converges if:

- $$b_n$$ decreases eventually,
- $$b_n \to 0$$.

---

## Absolute vs conditional convergence

If

$$
\sum |a_n|
$$

converges, then $$\sum a_n$$ converges absolutely.

If $$\sum a_n$$ converges but $$\sum |a_n|$$ diverges, the convergence is conditional.

---

## Ratio and root tests

Ratio Test:

$$
L = \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right|
$$

Root Test:

$$
L = \lim_{n \to \infty} \sqrt[n]{|a_n|}
$$

In either test:

- if $$L<1$$, converge absolutely,
- if $$L>1$$ or infinite, diverge,
- if $$L=1$$, inconclusive.

---

## nth-term test for divergence

If

$$
\lim_{n \to \infty} a_n \ne 0
$$

or the limit does not exist, then

$$
\sum a_n
$$

diverges.

---

## Power series

A power series centered at $$c$$ has form

$$
\sum_{n=0}^{\infty} a_n(x-c)^n.
$$

There is a radius of convergence $$R$$:

- converges for $$|x-c|<R$$,
- diverges for $$|x-c|>R$$,
- endpoints must be checked separately.

> [Image Placeholder: number line showing center, radius, and endpoint testing]

---

## Taylor and Maclaurin series

The Taylor series of $$f$$ centered at $$c$$ is

$$
\sum_{n=0}^{\infty} \frac{f^{(n)}(c)}{n!}(x-c)^n.
$$

Maclaurin series is the special case $$c=0$$.

Core series to memorize:

$$
\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n, \qquad |x|<1
$$

$$
e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}
$$

$$
\sin x = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!}
$$

$$
\cos x = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!}
$$

---

## Taylor polynomial and error

The $$n$$th Taylor polynomial is the finite truncation:

$$
T_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(c)}{k!}(x-c)^k.
$$

For alternating Maclaurin series with decreasing term magnitudes, the truncation error is at most the first omitted term in absolute value.

---

## Common mistakes

- Forgetting that $$a_n \to 0$$ is necessary but not sufficient.
- Using a convergence test whose hypotheses do not apply.
- Stopping after finding the radius of convergence without testing endpoints.
- Mixing up absolute and conditional convergence.
