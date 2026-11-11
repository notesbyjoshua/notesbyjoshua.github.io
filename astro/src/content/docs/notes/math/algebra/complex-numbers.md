---
title: "Complex Numbers"
status: developing
progress: 68
sidebar:
  order: 4
description: "Competition math notes on complex arithmetic, polar form, De Moivre's theorem, and roots of unity, with worked examples and filtering techniques."
---

## Arithmetic and Conjugates

A complex number has the form $$z=a+bi$$, where $$a,b$$ are real and $$i^2=-1$$. Add real and imaginary parts separately; multiply by expanding and replacing $$i^2$$ by $$-1$$.

The **conjugate** is $$\overline z=a-bi$$. Multiplying a number by its conjugate produces a real number:

$$
z\overline z=a^2+b^2=\lvert z\rvert^2.
$$

Here $$\lvert z\rvert=\sqrt{a^2+b^2}$$ is the **modulus**, or distance from the origin. Conjugation preserves sums and products, so it is useful for both division and equations involving real coefficients.

<div class="theorem-box">

**Example.** Write $$\dfrac{3+4i}{1-2i}$$ in the form $$a+bi$$.

Multiply the numerator and denominator by the denominator's conjugate:

$$
\frac{3+4i}{1-2i}=\frac{(3+4i)(1+2i)}{(1-2i)(1+2i)}
=\frac{-5+10i}{5}=-1+2i.
$$

The denominator becomes real because it is a modulus squared.

</div>

If a polynomial has real coefficients and $$z$$ is a root, then $$\overline z$$ is also a root: conjugating $$P(z)=0$$ gives $$P(\overline z)=0$$.

---

## Polar Form and De Moivre's Theorem

For a nonzero complex number, write

$$
z=r(\cos\theta+i\sin\theta),\qquad r=\lvert z\rvert>0.
$$

The angle $$\theta$$ is an **argument** of $$z$$ and is determined up to multiples of $$2\pi$$. Multiplication multiplies moduli and adds arguments, so multiplying by a unit complex number rotates the plane.

Repeated multiplication gives **De Moivre's theorem**:

$$
\bigl(r(\cos\theta+i\sin\theta)\bigr)^n
=r^n(\cos n\theta+i\sin n\theta)
$$

for integers $$n$$, with $$z\ne0$$ required if $$n<0$$.

<div class="theorem-box">

**Example.** Evaluate $$(1+i)^{12}$$.

The modulus of $$1+i$$ is $$\sqrt2$$ and its argument is $$\pi/4$$. Thus

$$
(1+i)^{12}=(\sqrt2)^{12}\left(\cos3\pi+i\sin3\pi\right)=-64.
$$

Expanding twelve factors would hide the periodicity of the angle.

</div>

For roots, reverse the process. The $$n$$th roots of $$r(\cos\theta+i\sin\theta)$$ are

$$
r^{1/n}\left(\cos\frac{\theta+2\pi k}{n}+i\sin\frac{\theta+2\pi k}{n}\right),
\qquad k=0,1,\ldots,n-1.
$$

They are equally spaced around a circle. For instance, the cube roots of $$8$$ are $$2$$, $$-1+i\sqrt3$$, and $$-1-i\sqrt3$$.

---

## Roots of Unity

The **$$n$$th roots of unity** solve $$z^n=1$$. Let

$$
\omega=\cos\frac{2\pi}{n}+i\sin\frac{2\pi}{n}.
$$

The roots are $$1,\omega,\ldots,\omega^{n-1}$$. For $$n>1$$, their sum is zero by the finite geometric-series formula. More generally,

$$
\sum_{j=0}^{n-1}\omega^{jk}=
\begin{cases}
n,&n\mid k,\\
0,&n\nmid k.
\end{cases}
$$

If $$n\nmid k$$, then $$\omega^k\ne1$$ and the geometric numerator is $$1-(\omega^k)^n=0$$. If $$n\mid k$$, every term is one.

<div class="theorem-box">

**Example.** Let $$\omega$$ be a primitive fifth root of unity. Evaluate $$1+\omega^7+\omega^{14}+\omega^{21}+\omega^{28}$$.

Reduce each exponent modulo $$5$$. The exponents become $$0,2,4,1,3$$, so the expression contains each fifth root once. Its value is $$0$$.

</div>

Products can be found from a polynomial as well. Since

$$
\frac{x^n-1}{x-1}=\prod_{j=1}^{n-1}(x-\omega^j),
$$

evaluating at $$x=1$$ gives $$\prod_{j=1}^{n-1}(1-\omega^j)=n$$.

---

## Filtering Coefficients by Their Exponents

A roots-of-unity filter keeps only terms whose exponent has a chosen remainder. If $$F(x)=\sum_k a_kx^k$$ is a polynomial, then

$$
\sum_{k\equiv r\pmod n}a_k
=\frac1n\sum_{j=0}^{n-1}\omega^{-rj}F(\omega^j).
$$

To understand the filter, expand the right side. The coefficient $$a_k$$ is multiplied by $$\frac1n\sum_j\omega^{j(k-r)}$$, which is one for the wanted exponents and zero for the others.

<div class="theorem-box">

**Example.** Evaluate $$\displaystyle\sum_{k\equiv0\pmod3}\binom6k$$, where $$0\le k\le6$$.

Use $$F(x)=(1+x)^6$$ and a primitive cube root $$\omega$$. Because $$1+\omega+\omega^2=0$$,

$$
1+\omega=-\omega^2,\qquad1+\omega^2=-\omega.
$$

Both have sixth power one. The filter gives

$$
\frac{F(1)+F(\omega)+F(\omega^2)}3=\frac{64+1+1}{3}=22.
$$

This agrees with $$\binom60+\binom63+\binom66=1+20+1$$.

</div>

:::strategy
Use rectangular form for addition, conjugation for division, and polar form for powers and roots. If a sum selects every second, third, or fourth coefficient, try a roots-of-unity filter. The parity case uses only $$F(1)$$ and $$F(-1)$$.
:::

## Equations Involving Conjugates

Conjugation gives an algebraic way to separate real and imaginary parts:

$$
\operatorname{Re}z=\frac{z+\overline z}{2},\qquad
\operatorname{Im}z=\frac{z-\overline z}{2i}.
$$

If an equation involves both $$z$$ and $$\overline z$$ linearly, conjugate the entire equation to obtain a second relation. Solve the resulting system rather than guessing the real and imaginary parts separately. Remember that conjugation also changes every occurrence of $$i$$ to $$-i$$.

<div class="theorem-box">

**Example.** Find all complex numbers satisfying $$2z+\overline z=6+4i$$.

Write $$z=x+iy$$. Then $$2z+\overline z=3x+iy$$, so $$3x=6$$ and $$y=4$$. Thus $$z=2+4i$$. Alternatively, conjugate the equation to obtain $$z+2\overline z=6-4i$$ and eliminate one variable.

</div>

For nonlinear equations, use $$z\overline z=\lvert z\rvert^2$$ to replace a product by a nonnegative real quantity. This supplies a useful sign restriction that is easy to miss if the symbols are treated as unrelated variables.

A polynomial with real coefficients has conjugate pairs of nonreal roots. Consequently, if $$2+3i$$ is a root, then $$(x-(2+3i))(x-(2-3i))=x^2-4x+13$$ is a real quadratic factor. This can reduce a seemingly complex factorization to ordinary real polynomial division.

---

## Modulus, Loci, and Geometry

The quantity $$\lvert z-a\rvert$$ is the distance from the point $$z$$ to the point $$a$$. An equation such as $$\lvert z-a\rvert=r$$ describes a circle, while $$\lvert z-a\rvert=\lvert z-b\rvert$$ describes the perpendicular bisector of the segment joining $$a,b$$.

The triangle inequality,

$$
\lvert z+w\rvert\le\lvert z\rvert+\lvert w\rvert,
$$

is the ordinary triangle inequality for the two vectors. Equality holds when the two nonzero vectors point in the same direction; a zero vector also permits equality. The reverse triangle inequality follows by applying this bound to $$z=(z-w)+w$$:

$$
\bigl\lvert\lvert z\rvert-\lvert w\rvert\bigr\rvert\le\lvert z-w\rvert.
$$

<div class="theorem-box">

**Example.** A complex number satisfies $$\lvert z-1\rvert=2\lvert z+1\rvert$$. Describe all possible points $$z$$.

Set $$z=x+iy$$ and square the nonnegative distances:

$$
(x-1)^2+y^2=4((x+1)^2+y^2).
$$

After collecting terms and completing the square,

$$
\left(x+\frac53\right)^2+y^2=\frac{16}{9}.
$$

Thus the locus is a circle centered at $$(-5/3,0)$$ with radius $$4/3$$. This is an example of an Apollonius circle: a fixed ratio of distances to two points.

</div>

A locus translation is especially helpful in optimization. If $$\lvert z\rvert=3$$, then the smallest and largest values of $$\lvert z-5\rvert$$ are two and eight, attained along the real axis. The geometry proves attainability as well as the bounds; an inequality alone should still be accompanied by the points achieving equality.

---

## Recovering Trigonometric Sums

Polar notation can be compressed using $$e^{i\theta}=\cos\theta+i\sin\theta$$. This is shorthand for a unit complex number and makes multiplication rules easy to read. A finite sum of equally spaced angles is a geometric series:

$$
1+e^{i\theta}+\cdots+e^{i(n-1)\theta}
=\frac{1-e^{in\theta}}{1-e^{i\theta}}.
$$

Taking real or imaginary parts produces cosine or sine sums. The denominator is nonzero unless $$\theta$$ is a multiple of $$2\pi$$; in that exceptional case every summand equals one.

A symmetric rewrite factors a half-angle from the numerator and denominator and yields

$$
\sum_{k=0}^{n-1}\cos(k\theta)
=\frac{\sin(n\theta/2)\cos((n-1)\theta/2)}{\sin(\theta/2)}.
$$

Do not memorize this formula independently of its origin. The geometric series usually adapts more easily when the sum starts at a different index or has alternating signs.

<div class="theorem-box">

**Example.** Evaluate $$\cos(2\pi/7)+\cos(4\pi/7)+\cos(6\pi/7)$$ exactly.

Let $$\zeta=e^{2\pi i/7}$$. The sum of all seven roots is zero. Pairing conjugate terms and taking real parts gives

$$
1+2\left(\cos\frac{2\pi}7+\cos\frac{4\pi}7+\cos\frac{6\pi}7\right)=0.
$$

The desired value is negative one-half, even though none of the individual cosine values has a simple familiar-angle expression.

</div>

---

## Products over Roots of Unity

For primitive $$n$$th root $$\zeta$$,

$$
x^n-1=(x-1)\prod_{k=1}^{n-1}(x-\zeta^k).
$$

Evaluating this factorization is often much easier than multiplying its complex factors. It also handles products that appear as distances: take moduli after evaluating the algebraic product.

<div class="theorem-box">

**Example.** Let $$\zeta$$ be a primitive seventh root of unity. Evaluate $$\prod_{k=1}^{6}(2-\zeta^k)$$.

Evaluate the quotient polynomial at two:

$$
\prod_{k=1}^{6}(2-\zeta^k)=\frac{2^7-1}{2-1}=127.
$$

The product is real because the factors occur in conjugate pairs. The factorization supplies its exact value without any approximate trigonometry.

</div>

For a regular $$n$$-gon on the unit circle, the distances from the vertex one to all other vertices have product $$n$$, since $$\prod_{k=1}^{n-1}(1-\zeta^k)=n$$. On a circle of radius $$R$$, every distance scales by $$R$$, giving product $$nR^{n-1}$$. Keep the number of factors in mind when restoring the geometric scale.

---

## Reciprocal Sums by Differentiating a Product

Suppose $$P(x)=\prod_j(x-r_j)$$ and $$P(t)\ne0$$. Differentiate the product and divide by it:

$$
\frac{P'(t)}{P(t)}=\sum_j\frac1{t-r_j}.
$$

This is the **logarithmic derivative** identity; no choice of a complex logarithm is needed because it follows directly from the product rule. A second derivative gives

$$
\sum_j\frac1{(t-r_j)^2}
=\left(\frac{P'(t)}{P(t)}\right)^2-\frac{P''(t)}{P(t)}.
$$

These formulas turn reciprocal expressions in roots into values of a polynomial and its derivatives.

<div class="theorem-box">

**Example.** For primitive $$n$$th root $$\zeta$$ with $$n>1$$, evaluate $$\sum_{k=1}^{n-1}1/(1-\zeta^k)$$.

Use $$P(x)=1+x+\cdots+x^{n-1}$$. At one,

$$
P(1)=n,\qquad P'(1)=1+2+\cdots+(n-1)=\frac{n(n-1)}2.
$$

The logarithmic derivative therefore gives the sum $$(n-1)/2$$. Pairing $$\zeta^k$$ with its reciprocal gives another explanation: the corresponding two reciprocal terms sum to one.

</div>

For a harder distance sum, the second derivative gives

$$
S_2=\sum_{k=1}^{n-1}\frac1{(1-\zeta^k)^2}
=\frac{(n-1)(5-n)}{12}.
$$

Indeed, $$P''(1)=n(n-1)(n-2)/3$$, obtained by summing $$j(j-1)$$. Although some terms of this complex sum can have negative real parts, the geometric squared-distance sum is positive. Since $$\overline{\zeta^k}=\zeta^{-k}$$,

$$
\frac1{\lvert1-\zeta^k\rvert^2}
=-\frac{\zeta^k}{(1-\zeta^k)^2}
=\frac1{1-\zeta^k}-\frac1{(1-\zeta^k)^2}.
$$

Summing gives $$\sum_{k=1}^{n-1}\lvert1-\zeta^k\rvert^{-2}=(n^2-1)/12$$. This example combines conjugation, roots of unity, and polynomial differentiation; each tool removes one difficult feature of the original expression.

---

## A Filter That Selects a Nonzero Remainder

For a polynomial $$F(x)=\sum_k a_kx^k$$, filtering exponents congruent to $$r$$ requires the weight $$\zeta^{-rj}$$. Without that weight, the filter selects only exponents divisible by $$n$$. Work out the contribution of one monomial if you are unsure which sign to use.

<div class="theorem-box">

**Example.** How many subsets of a twelve-element set have size congruent to one modulo three?

Use $$F(x)=(1+x)^{12}$$ and a primitive cube root $$\omega$$. The required count is

$$
\frac{F(1)+\omega^{-1}F(\omega)+\omega^{-2}F(\omega^2)}3.
$$

Both $$F(\omega)$$ and $$F(\omega^2)$$ are one, because $$1+\omega=-\omega^2$$ and twelve is a multiple of six. The weighted terms sum to $$\omega+\omega^2=-1$$. Thus the count is $$(4096-1)/3=1365$$.

</div>

:::strategy
When roots appear in a product or reciprocal sum, build the polynomial having those roots. When distances appear, translate them to moduli and use conjugation. When angles advance by a fixed amount, try a geometric series. These choices usually shorten the calculation more than expanding in real and imaginary parts immediately.
:::

---

## Algebraic Equations for Trigonometric Values

Roots of unity can produce a low-degree polynomial for a trigonometric expression even when its individual radicals are inconvenient. Pair opposite exponents and use $$t=z+z^{-1}$$. The identities for $$z^2+z^{-2}$$ and $$z^3+z^{-3}$$ then turn a complex equation into a real polynomial.

<div class="theorem-box">

**Example.** Find a cubic whose roots are $$\cos(2\pi/7),\cos(4\pi/7),\cos(6\pi/7)$$, and evaluate their product.

For a nontrivial seventh root $$z$$, divide $$1+z+\cdots+z^6=0$$ by $$z^3$$:

$$
1+(z+z^{-1})+(z^2+z^{-2})+(z^3+z^{-3})=0.
$$

Setting $$t=z+z^{-1}$$ gives $$t^3+t^2-2t-1=0$$. With $$t=2u$$, the cosine values satisfy

$$
8u^3+4u^2-4u-1=0.
$$

The three specified cosine values are distinct and supply all three roots. Vieta therefore gives their product as one-eighth and their sum as negative one-half.

The distinctness and degree check complete the argument: merely showing that each value satisfies a cubic would not identify its full root list if repeated values were possible.

</div>

This method is useful for symmetric expressions in several related angles. Once the polynomial is known, Vieta or Newton sums can evaluate those expressions without ever solving the cubic.

---

## Simultaneous Root Conditions

When a complex number satisfies several power equations, reduce the exponents using one equation before listing roots. Two large root sets may have a much smaller intersection.

<div class="theorem-box">

**Example.** Find all complex numbers satisfying $$z^{12}=1$$ and $$z^{18}=-1$$.

The first equation implies $$z\ne0$$ and $$z^{18}=z^6$$. Thus the two conditions are equivalent to $$z^6=-1$$: this equation implies $$z^{12}=1$$ automatically.

The complete list is

$$
z=\cos\frac{(2k+1)\pi}{6}+i\sin\frac{(2k+1)\pi}{6},
\qquad k=0,1,\ldots,5.
$$

There are six solutions. Their sum is zero and their product is one by the polynomial $$z^6+1$$. Counting twelve roots and eighteen roots separately would not determine the intersection.

</div>

For two equations $$z^m=z^n=1$$, the solutions are exactly the $$\gcd(m,n)$$th roots of unity. Bézout's identity applied to the exponents proves one direction using negative powers, which are allowed because $$z\ne0$$. The reverse direction follows because the exponent GCD divides both original exponents.

---

## Numerical Substitution into Infinite Series

A roots-of-unity filter for a polynomial has no convergence issue. For an infinite generating series, substituting $$z=1,\omega,\omega^2$$ requires convergence at those points. A formal power-series identity does not by itself authorize evaluating at a nonzero number.

One safe approach is to filter a finite partial sum first and then justify the limit by absolute convergence. Another is to apply the filter inside a disk where the series converges absolutely. The algebraic selector still works, but exchanging its finite average with an infinite sum requires that analytic step.

This distinction becomes useful when a contest expression mixes exponential series, factorial denominators, and congruence classes of indices. The factorial series converges absolutely everywhere, whereas a geometric generating function may fail at a unit root. Check the actual series before carrying a polynomial trick into an infinite setting.

---

## A Distance Condition That Determines Powers

For a unit complex number,

$$
\lvert1+z\rvert^2=2+z+\overline z=2+2\operatorname{Re}z.
$$

Thus a distance can determine the real part and force a short root-of-unity period.

<div class="theorem-box">

**Example.** Suppose $$\lvert z\rvert=1$$ and $$\lvert1+z\rvert=\sqrt3$$. Find $$z^{2026}+z^{-2026}$$.

The distance identity gives $$\operatorname{Re}z=1/2$$. The unit-circle condition then gives $$z=1/2\pm i\sqrt3/2$$. Hence $$z^6=1$$ and $$z^3=-1$$.

Reduce 2026 modulo six to four. The requested expression is $$z^4+z^{-4}=2\cos(4\pi/3)=-1$$, independent of the conjugate choice.

</div>

This combines a geometric modulus condition with an algebraic periodicity argument. Keeping both conjugate candidates avoids choosing an angle sign that the original data did not specify.

---

## Key Equations

:::equations
| Tool | Formula |
| --- | --- |
| Conjugate and modulus | $$z\overline z=\lvert z\rvert^2$$ |
| Polar powers | $$[r(\cos\theta+i\sin\theta)]^n=r^n(\cos n\theta+i\sin n\theta)$$ |
| Root sum | $$\sum_{j=0}^{n-1}\omega^{jk}=n$$ if $$n\mid k$$, and $$0$$ otherwise |
| Root product | $$\prod_{j=1}^{n-1}(1-\omega^j)=n$$ |
| Coefficient filter | $$\sum_{k\equiv r\pmod n}a_k=\frac1n\sum_{j=0}^{n-1}\omega^{-rj}F(\omega^j)$$ |
| Real and imaginary parts | $$\operatorname{Re}z=(z+\overline z)/2$$, $$\operatorname{Im}z=(z-\overline z)/(2i)$$ |
| Triangle inequality | $$\lvert z+w\rvert\le\lvert z\rvert+\lvert w\rvert$$ |
| Logarithmic derivative | $$P'(t)/P(t)=\sum_j(t-r_j)^{-1}$$, $$P(t)\ne0$$ |
| Unit-root reciprocal sum | $$\sum_{k=1}^{n-1}(1-\zeta^k)^{-1}=(n-1)/2$$ |
| Regular-polygon distance sum | $$\sum_{k=1}^{n-1}\lvert1-\zeta^k\rvert^{-2}=(n^2-1)/12$$ |
| Common roots of unity | $$z^m=z^n=1\iff z^{\gcd(m,n)}=1$$ |
| Seventh-root cosine cubic | $$8u^3+4u^2-4u-1=0$$ for $$u=\cos(2k\pi/7)$$, $$k=1,2,3$$ |
:::
