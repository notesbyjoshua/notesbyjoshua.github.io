---
title: "Polynomials"
status: developing
progress: 68
sidebar:
  order: 2
description: "Competition math notes on polynomial roots, remainders, Vieta's formulas, Newton sums, and identities, with worked problems and solving strategies."
---

## Division, Remainders, and Factors

A **polynomial** is an expression $$P(x)=a_nx^n+\cdots+a_0$$ with nonnegative integer exponents. If $$a_n\ne0$$, its degree is $$n$$. Polynomial division writes

$$
P(x)=D(x)Q(x)+R(x),\qquad \deg R<\deg D,
$$

where a zero remainder is also allowed. If $$D(x)=x-r$$, the remainder is constant. Substituting $$x=r$$ shows that the remainder is $$P(r)$$. Consequently, $$x-r$$ divides $$P(x)$$ exactly when $$P(r)=0$$.

<div class="theorem-box">

**Example.** A polynomial satisfies $$P(1)=4$$ and $$P(3)=10$$. Find the remainder when it is divided by $$(x-1)(x-3)$$.

The remainder has degree at most one, so write it as $$ax+b$$. Evaluating at the roots of the divisor gives

$$
a+b=4,\qquad3a+b=10.
$$

Thus $$a=3$$ and $$b=1$$, so the remainder is $$3x+1$$. We never needed the full polynomial.

</div>

:::strategy
To find a remainder, first use its degree bound to write a short general expression. Evaluate at roots of the divisor to determine its coefficients.
:::

---

## Computing with a Polynomial Remainder

A divisor gives an algebraic replacement rule. Modulo $$x^2+1$$, replace $$x^2$$ by negative one; modulo $$x^2-x-1$$, replace it by $$x+1$$. This is polynomial arithmetic, analogous to reducing integers modulo an integer.

Every multiplication can be followed by reduction to a smaller degree. This makes very high powers manageable and explains why remainder questions are often recurrence problems in disguise.

<div class="theorem-box">

**Example.** Find the remainder of $$x^{2026}+x^{2025}+1$$ upon division by $$x^2+1$$.

Because $$x^2\equiv-1$$ modulo the divisor, powers repeat with period four. The two exponents are respectively two and one modulo four, so

$$
x^{2026}+x^{2025}+1\equiv-1+x+1=x.
$$

The degree of $$x$$ is less than two, so it is already the unique remainder.

</div>

<div class="theorem-box">

**Example.** Prove that the remainder of $$x^n$$ modulo $$x^2-x-1$$ is $$F_nx+F_{n-1}$$ for $$n\ge1$$, where $$F_0=0,F_1=1$$ are Fibonacci numbers.

The formula holds at $$n=1$$ and $$n=2$$. If it holds at $$n$$, multiply by $$x$$ and reduce:

$$
x(F_nx+F_{n-1})\equiv F_n(x+1)+F_{n-1}x
=F_{n+1}x+F_n.
$$

This proves the next case and hence the formula by induction. A huge exponent has become a pair of recursively defined coefficients.

</div>

If a divisor has repeated roots, evaluating only at its distinct roots will not supply enough equations for the remainder. For division by $$(x-r)^2$$, the remainder $$A+B(x-r)$$ is determined by $$A=P(r)$$ and $$B=P'(r)$$. The derivative contributes the missing condition.

---

## Roots, Multiplicities, and Vieta's Formulas

A root $$r$$ has **multiplicity** $$m$$ when $$(x-r)^m$$ divides $$P(x)$$ but $$(x-r)^{m+1}$$ does not. Count roots with multiplicity when comparing a polynomial's factors to its degree. Over the complex numbers, a degree-$$n$$ polynomial has exactly $$n$$ roots with multiplicity.

For a monic cubic,

$$
P(x)=(x-a)(x-b)(x-c)=x^3-s_1x^2+s_2x-s_3,
$$

where

$$
s_1=a+b+c,\qquad s_2=ab+bc+ca,\qquad s_3=abc.
$$

These are **Vieta's formulas**. They let us calculate symmetric expressions without solving for the roots.

<div class="theorem-box">

**Example.** The roots of $$x^3-4x^2+2x+5$$ are $$a,b,c$$. Find $$a^2+b^2+c^2$$ and $$1/a+1/b+1/c$$.

Vieta gives $$s_1=4$$, $$s_2=2$$, and $$s_3=-5$$. Therefore,

$$
a^2+b^2+c^2=s_1^2-2s_2=12.
$$

The product is nonzero, so taking reciprocals is allowed:

$$
\frac1a+\frac1b+\frac1c=\frac{ab+bc+ca}{abc}=-\frac25.
$$

</div>

For rational roots of an integer-coefficient polynomial, the **rational root theorem** gives a useful candidate list: a reduced root $$p/q$$ must have $$p\mid a_0$$ and $$q\mid a_n$$. It does not guarantee that any candidate is a root.

---

## Repeated Roots and Derivatives

If $$P(x)=(x-r)^mQ(x)$$ with $$Q(r)\ne0$$, the exponent $$m$$ measures how strongly the polynomial vanishes at $$r$$. Differentiation reduces that multiplicity by one:

$$
P'(x)=m(x-r)^{m-1}Q(x)+(x-r)^mQ'(x).
$$

Consequently, $$r$$ is a repeated root exactly when $$P(r)=P'(r)=0$$. A root of multiplicity at least three also satisfies $$P''(r)=0$$. These tests replace repeated factoring when the coefficients contain unknown parameters.

For real polynomials, odd multiplicity means the sign changes across the root, while even multiplicity means it does not. The other factor stays nonzero and keeps a fixed sign sufficiently near the root. This explains why a double root can touch the horizontal axis without crossing it.

<div class="theorem-box">

**Example.** Find real numbers $$a,b$$ such that $$x=2$$ is a repeated root of $$P(x)=x^3+ax+b$$, and factor the resulting polynomial.

The root conditions give

$$
8+2a+b=0,\qquad P'(2)=12+a=0.
$$

Thus $$a=-12$$ and $$b=16$$. Dividing by $$(x-2)^2$$ gives

$$
P(x)=(x-2)^2(x+4).
$$

Since $$P''(2)=12\ne0$$, the root two has multiplicity exactly two. The remaining root is negative four.

</div>

The derivative test also helps find a polynomial's greatest common divisor with its derivative. A nonconstant common factor signals repeated roots. On a contest, it is often enough to exhibit one common root rather than perform a full polynomial Euclidean algorithm.

---

## Transforming Roots Without Solving for Them

Suppose a monic polynomial $$P$$ has roots $$r_1,\ldots,r_n$$. To find a polynomial with roots $$r_i+c$$, replace the input by $$x-c$$. To obtain roots $$kr_i$$ for $$k\ne0$$, use $$k^nP(x/k)$$. The multiplier keeps the resulting polynomial monic.

If none of the roots is zero, a polynomial with reciprocal roots is obtained from $$x^nP(1/x)$$, then normalized by its leading coefficient. This works because substituting $$x=1/r_i$$ makes its polynomial factor zero.

<div class="theorem-box">

**Example.** The roots of $$P(t)=t^3-2t^2-3t+1$$ are $$a,b,c$$. Find a monic polynomial with roots $$a+1,b+1,c+1$$.

Use $$P(x-1)$$ rather than finding the three roots:

$$
P(x-1)=(x-1)^3-2(x-1)^2-3(x-1)+1
=x^3-5x^2+4x+1.
$$

As a check, the new roots sum to $$a+b+c+3=5$$, matching the negative coefficient of $$x^2$$.

</div>

Products of paired roots can also be handled through Vieta. If $$abc\ne0$$, the three numbers $$ab,bc,ca$$ are $$abc$$ times the reciprocals of $$c,a,b$$. Their elementary symmetric quantities are

$$
ab+bc+ca=s_2,\quad
(ab)(bc)+(bc)(ca)+(ca)(ab)=s_1s_3,\quad
(ab)(bc)(ca)=s_3^2.
$$

Thus their monic polynomial is $$x^3-s_2x^2+s_1s_3x-s_3^2$$. Recognizing this transformation often saves a long symmetric expansion.

---

## Newton Sums

If the problem asks for high powers of roots, expanding symmetric identities repeatedly becomes awkward. Define $$p_k=a^k+b^k+c^k$$. For the monic cubic above,

$$
p_1=s_1,\qquad p_2=s_1p_1-2s_2,\qquad
p_3=s_1p_2-s_2p_1+3s_3.
$$

For $$k\ge4$$,

$$
p_k=s_1p_{k-1}-s_2p_{k-2}+s_3p_{k-3}.
$$

To see the recurrence, substitute a root $$a$$ into $$a^3-s_1a^2+s_2a-s_3=0$$, multiply by $$a^{k-3}$$, and sum over all three roots. At $$k=3$$ the last contribution is $$3s_3$$ because there are three roots, rather than just one constant term.

<div class="theorem-box">

**Example.** For the roots of $$x^3-4x^2+2x+5$$, find $$p_3$$ and $$p_4$$.

We already have $$p_1=4$$ and $$p_2=12$$. Using $$s_3=-5$$,

$$
p_3=4(12)-2(4)+3(-5)=25,
$$

$$
p_4=4(25)-2(12)-5(4)=56.
$$

The coefficients supply a recurrence for the desired sums even if the individual roots are unpleasant.

</div>

---

## Newton Sums in Arbitrary Degree

For a monic degree-$$n$$ polynomial $$P(x)=x^n+c_1x^{n-1}+\cdots+c_n$$, let $$s_k$$ be the sum of the $$k$$th powers of its roots, counted with multiplicity. The general Newton identities are

$$
s_k+c_1s_{k-1}+\cdots+c_{k-1}s_1+kc_k=0,\qquad1\le k\le n.
$$

For $$k>n$$, they become the recurrence

$$
s_k+c_1s_{k-1}+\cdots+c_ns_{k-n}=0.
$$

The special coefficient $$k$$ in the first formula is important. Replacing it by the degree at every stage gives the wrong initial power sums. Once all polynomial coefficients have entered, the later sums follow an ordinary linear recurrence.

<div class="theorem-box">

**Example.** The roots of $$x^4-2x^3+3x^2-4x+5$$ are $$a,b,c,d$$. Find their fifth-power sum and show the roots cannot all be real.

The first Newton sums are

$$
s_1=2,\qquad s_2=2s_1-6=-2,
$$

$$
s_3=2s_2-3s_1+12=2,\qquad
s_4=2s_3-3s_2+4s_1-20=-2.
$$

The recurrence then gives

$$
s_5=2s_4-3s_3+4s_2-5s_1=-28.
$$

If all roots were real, their squared values would be nonnegative and $$s_2$$ could not equal negative two. Thus at least one conjugate pair is nonreal.

</div>

The negative square sum is not an algebraic contradiction because the roots are complex. Conditions on the root domain can turn a computed symmetric value into an existence or impossibility argument.

---

## Polynomial Identities and Divisibility

A nonzero polynomial of degree $$d$$ has at most $$d$$ distinct roots. This gives an efficient way to prove identities: if two polynomials of degree at most $$d$$ agree at $$d+1$$ distinct inputs, their difference must be zero.

The degree bound matters. Checking a few numerical values proves nothing about an unrestricted function or a polynomial of unknown degree.

<div class="theorem-box">

**Example.** A polynomial $$P$$ has degree at most $$3$$ and satisfies $$P(0)=1$$, $$P(1)=2$$, $$P(2)=5$$, and $$P(3)=10$$. Find $$P(4)$$.

The values suggest $$P(x)=x^2+1$$. Define $$Q(x)=P(x)-(x^2+1)$$. It has degree at most $$3$$ and four distinct roots, namely $$0,1,2,3$$. Hence $$Q$$ is the zero polynomial, proving the guess. Therefore $$P(4)=17$$.

</div>

For integer-coefficient polynomials, another useful fact is

$$
a-b\mid P(a)-P(b)\qquad(a,b\in\mathbb Z,\ a\ne b).
$$

Each difference $$a^k-b^k$$ contains the factor $$a-b$$. This connects polynomial equations to divisibility problems.

:::tip
Before solving for roots, read the requested expression. Root sums, products, reciprocal sums, and power sums usually depend only on the coefficients.
:::

---

## Interpolation and Finite Differences

A polynomial of degree at most $$d$$ is determined by its values at any $$d+1$$ distinct inputs. One explicit construction is **Lagrange interpolation**:

$$
P(x)=\sum_{i=0}^d P(t_i)
\prod_{\substack{0\le j\le d\\j\ne i}}\frac{x-t_j}{t_i-t_j}.
$$

Each product equals one at its own input $$t_i$$ and zero at all the other listed inputs. The right side has the same values and degree bound as $$P$$, so the root-counting identity principle proves equality.

The formula is most useful when only one new value is requested. Substitute that input into the weights before expanding anything.

<div class="theorem-box">

**Example.** A polynomial of degree at most two satisfies $$P(1)=2,P(2)=3,P(3)=6$$. Find $$P(0)$$.

At zero, the three interpolation weights are

$$
\frac{(-2)(-3)}{(1-2)(1-3)}=3,\quad
\frac{(-1)(-3)}{(2-1)(2-3)}=-3,\quad
\frac{(-1)(-2)}{(3-1)(3-2)}=1.
$$

Therefore $$P(0)=3(2)-3(3)+6=3$$. No coefficient system is needed.

</div>

For equally spaced inputs, **finite differences** are often simpler. Define $$\Delta P(x)=P(x+1)-P(x)$$. A degree-$$d$$ polynomial has a difference of degree at most $$d-1$$ because its leading powers cancel. Repeating the operation $$d+1$$ times gives zero.

<div class="theorem-box">

**Example.** A polynomial of degree at most four satisfies $$P(k)=2^k$$ for $$k=0,1,2,3,4$$. Find $$P(5)$$.

The fifth difference vanishes, giving

$$
P(5)-5P(4)+10P(3)-10P(2)+5P(1)-P(0)=0.
$$

Substitute the known values:

$$
P(5)=5(16)-10(8)+10(4)-5(2)+1=31.
$$

The value is not thirty-two. Agreement with an exponential at five inputs does not make a degree-four polynomial equal that exponential everywhere.

</div>

---

## Integer Coefficients and Strong Root Counting

When a polynomial has integer coefficients, its values satisfy divisibility restrictions beyond its degree bound. The identity $$a-b\mid P(a)-P(b)$$ is one example. Division by a monic integer polynomial also preserves integer coefficients in the quotient and remainder.

<div class="theorem-box">

**Example.** An integer-coefficient polynomial satisfies $$P(0)=P(1)=1$$. Prove $$P(n)$$ is odd for every integer $$n$$.

The polynomial $$P(x)-1$$ has roots zero and one, so

$$
P(x)-1=x(x-1)Q(x)
$$

for an integer-coefficient polynomial $$Q$$. At an integer input, $$n(n-1)$$ is even. Thus $$P(n)-1$$ is even and $$P(n)$$ is odd.

The factorization uses both prescribed inputs simultaneously; applying divisibility to only one of them would give a weaker conclusion.

</div>

A useful olympiad pattern is to turn several possible function values into zeros of one polynomial. If a degree-at-most-$$d$$ polynomial takes values only from $$\{1,-1\}$$ at more than $$2d$$ distinct inputs, then $$P(x)^2-1$$ has too many roots and must vanish identically. Factoring it as $$(P-1)(P+1)$$ shows that $$P$$ is the constant one or negative one.

More generally, if $$P$$ takes values in a set of $$k$$ numbers at more than $$kd$$ distinct inputs, the product of $$P(x)$$ minus those values is identically zero. This is a useful bridge from a finite list of allowed outputs to a global polynomial identity.

:::strategy
Choose the representation that matches the question. Use values and interpolation for a value question, coefficients and Vieta for symmetric roots, and a low-degree remainder for high powers. When integer coefficients are given, look for divisibility before introducing approximate roots.
:::

---

## Prime Values from a Polynomial Factorization

A factorization can classify prime outputs without finding any roots.

<div class="theorem-box">

**Example.** Find all integers $$n$$ for which $$n^4+4$$ is prime.

Sophie Germain's identity gives

$$
n^4+4=(n^2-2n+2)(n^2+2n+2).
$$

Both factors are positive integers. If $$\lvert n\rvert\ge2$$, both exceed one, so the product is composite. At $$n=0$$ the value is four, also composite. At $$n=1$$ or negative one, the value is five, which is prime.

Therefore the complete list is $$n=\pm1$$.

</div>

The positivity check is essential when using a factorization to rule out primes: a factor equal to one does not establish compositeness. Boundary inputs often survive precisely because one algebraic factor becomes one.

---

## Bounding All Roots at Once

A monic polynomial with $$M=\max_i\lvert c_i\rvert$$ has every complex root in the disk $$\lvert z\rvert\le1+M$$. To prove this, suppose a root had modulus greater than $$1+M$$. The polynomial equation and triangle inequality would give

$$
\lvert z\rvert^n\le M(1+\lvert z\rvert+\cdots+\lvert z\rvert^{n-1})
=M\frac{\lvert z\rvert^n-1}{\lvert z\rvert-1}
<\lvert z\rvert^n,
$$

a contradiction.

This Cauchy root bound is rarely the sharpest numerical estimate, but it supplies a finite region containing every root without solving the polynomial. In an integer-root problem, combine it with the rational-root theorem to limit the candidate list.

For a real root, a sign change between two inputs proves existence in the interval by continuity. It does not prove uniqueness unless a monotonicity or root-count argument is added. Conversely, absence of a sign change does not rule out an even-multiplicity root. Keep existence, uniqueness, and multiplicity as separate questions when interpreting a graph or a numerical table.

---

## Key Equations

:::equations
| Tool | Formula |
| --- | --- |
| Remainder theorem | $$P(x)=(x-r)Q(x)+P(r)$$ |
| Cubic Vieta | $$a+b+c=s_1$$, $$ab+bc+ca=s_2$$, $$abc=s_3$$ for $$x^3-s_1x^2+s_2x-s_3$$ |
| Power sums | $$p_2=s_1^2-2s_2$$; $$p_3=s_1p_2-s_2p_1+3s_3$$ |
| Later cubic power sums | $$p_k=s_1p_{k-1}-s_2p_{k-2}+s_3p_{k-3}$$, $$k\ge4$$ |
| Integer evaluations | $$a-b\mid P(a)-P(b)$$ for integer-coefficient $$P$$ |
| Repeated root | $$P(r)=P'(r)=0$$ |
| Shifted roots | Roots of $$P(x-c)$$ are the roots of $$P$$ plus $$c$$ |
| Reciprocal roots | $$x^nP(1/x)$$, normalized, when $$P(0)\ne0$$ |
| Finite differences | $$\Delta P(x)=P(x+1)-P(x)$$; $$\Delta^{d+1}P=0$$ if $$\deg P\le d$$ |
| Repeated-factor remainder | $$P(x)\equiv P(r)+P'(r)(x-r)\pmod{(x-r)^2}$$ |
| General Newton identity | $$s_k+c_1s_{k-1}+\cdots+c_{k-1}s_1+kc_k=0$$ for $$k\le n$$ |
| Later power sums | $$s_k+c_1s_{k-1}+\cdots+c_ns_{k-n}=0$$ for $$k>n$$ |
| Cauchy root bound | $$\lvert z\rvert\le1+\max_i\lvert c_i\rvert$$ for monic $$P$$ |
:::
