---
title: "Fermat's Little Theorem and Orders"
status: developing
progress: 68
sidebar:
  order: 4
description: "Competition math notes on Fermat's little theorem, Euler's theorem, totients, multiplicative orders, and Wilson's theorem with worked examples."
---

## Fermat's Little Theorem

Remainder cycles become more predictable when the base is coprime to the modulus. For a prime $$p$$ and an integer $$a$$ not divisible by $$p$$, **Fermat's little theorem** states

$$
a^{p-1}\equiv1\pmod p.
$$

Multiplication by $$a$$ permutes the nonzero residues modulo $$p$$. Multiplying all those residues gives $$a^{p-1}(p-1)!\equiv(p-1)!$$; the factorial is invertible modulo $$p$$, so it cancels.

The equivalent statement $$a^p\equiv a\pmod p$$ holds for every integer $$a$$, including multiples of $$p$$.

<div class="theorem-box">

**Example.** Find the remainder when $$3^{100}$$ is divided by $$7$$.

Since $$3^6\equiv1\pmod7$$ and $$100=6\cdot16+4$$,

$$
3^{100}\equiv3^4=81\equiv4\pmod7.
$$

</div>

Do not replace $$p-1$$ by $$m-1$$ for an arbitrary composite modulus. A different exponent is needed.

---

## Euler's Totient Function and Theorem

The **totient** $$\varphi(m)$$ counts integers in $$\{1,\ldots,m\}$$ coprime to $$m$$. If the distinct prime divisors of $$m$$ are $$p$$, inclusion–exclusion gives

$$
\varphi(m)=m\prod_{p\mid m}\left(1-\frac1p\right).
$$

For $$\gcd(a,m)=1$$, the same residue-permutation proof gives **Euler's theorem**:

$$
a^{\varphi(m)}\equiv1\pmod m.
$$

<div class="theorem-box">

**Example.** Find the last two decimal digits of $$7^{222}$$.

Since $$100=2^2\cdot5^2$$, we have $$\varphi(100)=100(1-1/2)(1-1/5)=40$$. Euler's theorem permits reduction of the exponent modulo forty. In this case a shorter cycle is visible: $$7^4=2401\equiv1\pmod{100}$$. Therefore

$$
7^{222}\equiv7^2\equiv49\pmod{100}.
$$

The last two digits are $$49$$.

</div>

If the base shares a factor with the modulus, exponent reduction can fail. For example, $$1\equiv5\pmod{\varphi(8)}$$, but $$2^1\equiv2\pmod8$$ while $$2^5\equiv0\pmod8$$. Always check coprimality before using Euler's theorem.

---

## Multiplicative Order

For $$\gcd(a,m)=1$$, the **order** $$\operatorname{ord}_m(a)$$ is the smallest positive integer $$d$$ with $$a^d\equiv1\pmod m$$. Every exponent giving one is a multiple of $$d$$.

To prove the last statement, divide an exponent $$k$$ by $$d$$: $$k=qd+r$$ with $$0\le r<d$$. If $$a^k\equiv1$$, then $$a^r\equiv1$$, so minimality forces $$r=0$$. In particular,

$$
\operatorname{ord}_m(a)\mid\varphi(m).
$$

<div class="theorem-box">

**Example.** Find all positive integers $$n$$ for which $$7\mid2^n-1$$.

The first three powers of two modulo seven are $$2,4,1$$, so $$\operatorname{ord}_7(2)=3$$. Hence $$2^n\equiv1\pmod7$$ exactly when $$3\mid n$$. The solutions are all positive multiples of three.

</div>

To find an order, test divisors of $$\varphi(m)$$ rather than every exponent. For a prime modulus $$p$$, a number with order $$p-1$$ is called a **primitive root**. For instance, two has order ten modulo eleven because $$2^5\equiv-1$$, $$2^2\not\equiv1$$, and $$2\not\equiv1$$; these exclude all proper divisors of ten.

---

## Restricting Prime Divisors

If a prime $$p$$ divides an expression like $$a^n-1$$, the order of $$a$$ modulo $$p$$ links the exponent $$n$$ to $$p-1$$. For $$a^n+1$$, use $$a^{2n}\equiv1$$ while keeping $$a^n\equiv-1$$.

<div class="theorem-box">

**Example.** Let an odd prime $$p$$ divide $$2^{16}+1$$. Prove $$p\equiv1\pmod{32}$$.

We have $$2^{16}\equiv-1\pmod p$$ and $$2^{32}\equiv1\pmod p$$. The order divides $$32$$ but does not divide $$16$$. Every proper divisor of $$32$$ divides $$16$$, so the order is exactly $$32$$. Fermat's theorem gives $$32\mid p-1$$.

</div>

The power-of-two exponent makes the order exact. For a general $$a^n+1$$, the order need not equal $$2n$$, so prove it rather than assuming it.

---

## Wilson's Theorem

For a prime $$p$$,

$$
(p-1)!\equiv-1\pmod p.
$$

For odd $$p$$, pair each nonzero residue with its multiplicative inverse. Only $$1$$ and $$-1$$ are their own inverses, because $$x^2\equiv1$$ implies $$(x-1)(x+1)\equiv0$$ modulo a prime. All other pairs multiply to one, leaving product $$-1$$. The prime $$2$$ can be checked directly.

<div class="theorem-box">

**Example.** Find the remainder of $$9!$$ modulo $$11$$.

Wilson gives $$10!\equiv-1\pmod{11}$$. Since $$10\equiv-1$$,

$$
-9!\equiv-1\pmod{11}\quad\Longrightarrow\quad9!\equiv1\pmod{11}.
$$

</div>

:::strategy
For one large power, use repeated squaring or Fermat/Euler. For “find all exponents,” determine the order. For a prime divisor of an exponential expression, use its order to constrain the prime. For a factorial near a prime, try Wilson and cancel only invertible factors.
:::

## Finding an Order Efficiently

Once Euler or Fermat supplies an exponent $$M$$ with $$a^M\equiv1\pmod m$$, the actual order divides $$M$$. Factor $$M$$ and repeatedly test whether the exponent can be divided by one of its prime factors.

If $$a^{M/q}\equiv1$$, replace $$M$$ by $$M/q$$ and continue. If the test fails, the order requires that remaining prime-power contribution. This is faster than checking all exponents and makes the minimality argument explicit.

<div class="theorem-box">

**Example.** Show that three has order sixteen modulo seventeen.

Fermat gives an order dividing sixteen. Compute

$$
3^2\equiv9,\qquad3^4\equiv13,\qquad3^8\equiv16\equiv-1\pmod{17}.
$$

The order does not divide eight. Every proper divisor of sixteen does divide eight, so the order must be sixteen.

</div>

When the candidate exponent has several prime factors, failing only one reduced-exponent test may not establish the full order. To prove order twelve, for example, check that the twelfth power is one while the sixth and fourth powers are not. Every proper divisor of twelve divides at least one of six or four.

---

## Combining Orders by CRT

For coprime moduli $$u,v$$ and a base coprime to both,

$$
\operatorname{ord}_{uv}(a)
=\operatorname{lcm}(\operatorname{ord}_u(a),\operatorname{ord}_v(a)).
$$

An exponent produces one modulo the product exactly when it produces one modulo both factors. The two order divisibility requirements are therefore equivalent to being a multiple of their least common multiple.

<div class="theorem-box">

**Example.** Find the smallest positive $$n$$ for which $$63\mid2^n-1$$.

Factor $$63=7\cdot9$$. The order of two modulo seven is three. Modulo nine, $$2^3\equiv-1$$ and $$2^2\not\equiv1$$, so the order is six.

Their least common multiple is six, and $$2^6-1=63$$ confirms the answer.

</div>

This method also handles a simultaneous system of exponential divisibility conditions. First identify the order required by each modulus; only then combine the exponent conditions. Adding the orders or multiplying them indiscriminately can give a nonminimal answer.

---

## Nested Exponents

For a power tower, reduce the outer exponent modulo the order of the outer base. The relevant modulus for the exponent is an order, not necessarily the original numerical modulus.

<div class="theorem-box">

**Example.** Find the last two digits of $$7^{7^7}$$.

Modulo one hundred, the order of seven is four: $$7^4\equiv1$$ while $$7^2\equiv49\ne1$$. Thus only $$7^7\bmod4$$ is needed.

Since $$7\equiv-1\pmod4$$ and seven is odd, $$7^7\equiv3\pmod4$$. Therefore

$$
7^{7^7}\equiv7^3\equiv43\pmod{100}.
$$

The final two digits are 43. Reducing the exponent modulo one hundred would not be the principle that justifies this calculation.

</div>

For a noncoprime base, a tower requires separate prime-power analysis. One part of the modulus may force a sufficiently high power to vanish, while another part cycles. Check this before building an exponent-reduction chain.

---

## Orders Modulo Prime Powers

An order modulo $$p$$ does not automatically stay the same modulo $$p^2$$. Let $$p$$ be odd, $$p\nmid a$$, and $$d=\operatorname{ord}_p(a)$$. Write $$c=v_p(a^d-1)$$. For $$k\ge1$$,

$$
\operatorname{ord}_{p^k}(a)=d\,p^{\max(0,k-c)}.
$$

To derive the formula, any successful exponent is $$dt$$ because reduction modulo $$p$$ already forces that multiple. LTE gives

$$
v_p(a^{dt}-1)=v_p(a^d-1)+v_p(t)=c+v_p(t).
$$

Divisibility by $$p^k$$ therefore requires exactly the extra power $$p^{\max(0,k-c)}$$ in $$t$$. This links order, divisibility, and valuation in one calculation.

<div class="theorem-box">

**Example.** Find the orders of two modulo forty-nine and three hundred forty-three.

Modulo seven, two has order three, and $$2^3-1=7$$ has valuation one. The formula gives

$$
\operatorname{ord}_{49}(2)=3\cdot7=21,\qquad
\operatorname{ord}_{343}(2)=3\cdot7^2=147.
$$

The prime-power formula used the odd-prime LTE hypotheses. Powers of two have different lifting behavior and must be handled separately.

</div>

---

## Primitive Roots and Exponential Equations

A primitive root modulo an odd prime generates every nonzero residue by its powers. If $$g$$ has order $$p-1$$, the equality $$g^u\equiv g^v\pmod p$$ is equivalent to $$u\equiv v\pmod{p-1}$$.

Thus an equation between powers of the same primitive root becomes a linear congruence in the exponents. If the base has smaller order, use that smaller order instead.

<div class="theorem-box">

**Example.** Find all positive integers $$n$$ satisfying $$3^{3n+2}\equiv-1\pmod{17}$$.

We proved three has order sixteen. Since $$3^8\equiv-1$$, the condition is

$$
3n+2\equiv8\pmod{16}.
$$

The inverse of three modulo sixteen is eleven, giving $$n\equiv2\pmod{16}$$. All positive integers in this class work, and order sixteen proves no other classes do.

</div>

An odd prime admits primitive roots, but finding a convenient one is a separate task. For many contest problems, determining the order of the specific given base is enough; constructing a generator for the whole residue group would add unnecessary work.

---

## Why Fermat's Converse Fails

If $$p$$ is prime, every base coprime to it satisfies $$a^{p-1}\equiv1$$. The converse is false. Some composite numbers satisfy the same congruence for every coprime base; these are Carmichael numbers.

For example, $$561=3\cdot11\cdot17$$. If $$a$$ is coprime to 561, Fermat applied to the three prime factors gives exponents two, ten, and sixteen. Each divides 560, so $$a^{560}\equiv1$$ modulo each factor, and CRT gives

$$
a^{560}\equiv1\pmod{561}.
$$

Thus passing a Fermat congruence does not establish primality. The argument does not require testing hundreds of bases; the prime-factor structure explains every coprime base at once.

Wilson's theorem has a genuine converse for integers greater than one, but computing the factorial may be impractical. Distinguish a theorem's logical strength from the efficiency of using it in a numerical problem.

---

## Decimal Periods and a Wilson Construction

If $$\gcd(m,10)=1$$, the repeating decimal period of $$1/m$$ is $$\operatorname{ord}_m(10)$$. Long division returns to its initial remainder precisely when $$10^d\equiv1\pmod m$$. For denominator seven, the order is six, explaining the six-digit repeating block.

When the denominator contains powers of two or five, those factors produce an initial nonrepeating portion. The period afterward is controlled by the remaining factor coprime to ten.

Wilson also constructs a square root of negative one modulo a prime $$p\equiv1\pmod4$$. Set $$h=(p-1)/2$$ and pair the factorial terms:

$$
(p-1)!\equiv(-1)^h(h!)^2\pmod p.
$$

Here $$h$$ is even, so Wilson gives $$(h!)^2\equiv-1\pmod p$$. For $$p=13$$, $$6!\equiv5$$ and $$5^2\equiv-1$$. This provides an explicit root and connects factorial identities with quadratic residues.

:::strategy
For a smallest exponent, prove the order rather than merely finding a working exponent. For a product modulus, combine component orders by an LCM. For a prime power, inspect the valuation of the first return to one. Keep primality tests and consequences of primality logically separate.
:::

---

## Fermat Numbers and New Prime Factors

Define $$F_n=2^{2^n}+1$$. Repeated difference-of-squares factorization gives

$$
F_0F_1\cdots F_{n-1}=F_n-2.
$$

One proof is induction: multiplying $$2^{2^n}-1$$ by $$2^{2^n}+1$$ produces $$2^{2^{n+1}}-1$$, the next required product.

Any common divisor of $$F_n$$ and an earlier $$F_i$$ therefore divides two. All Fermat numbers are odd, so they are pairwise coprime. Choosing a prime divisor from each gives infinitely many distinct primes.

If an odd prime $$p$$ divides $$F_n$$, then $$2^{2^n}\equiv-1\pmod p$$. Its order is exactly $$2^{n+1}$$, since every proper divisor of that power of two divides $$2^n$$. Therefore $$p\equiv1\pmod{2^{n+1}}$$.

The numbers themselves need not be prime. For example, 641 divides $$F_5=2^{32}+1$$. To verify this without long division, use

$$
641=5\cdot2^7+1=5^4+2^4.
$$

The first identity gives $$5^4 2^{28}\equiv1$$ modulo 641, while the second gives $$5^4\equiv-2^4$$. Hence $$-2^{32}\equiv1$$, proving the divisibility.

Pairwise coprimality guarantees new prime factors, not primality of every term. That distinction is the point of the construction.

---

## Counting Roots through a Primitive Root

If $$g$$ is primitive modulo an odd prime $$p$$, every nonzero residue is uniquely $$g^t$$ with $$t$$ taken modulo $$p-1$$. Thus $$x^k\equiv1\pmod p$$ becomes $$kt\equiv0\pmod{p-1}$$ and has exactly $$\gcd(k,p-1)$$ solutions.

<div class="theorem-box">

**Example.** Find every solution of $$x^4\equiv1\pmod{17}$$.

There are exactly four solutions because $$\gcd(4,16)=4$$. Using primitive root three, the allowed exponents are $$t=0,4,8,12$$, giving

$$
x\equiv1,13,16,4\pmod{17}.
$$

The factorization $$(x^2-1)(x^2+1)$$ provides a second route: the roots of one are positive and negative one, and the roots of negative one are four and thirteen.

</div>

The count follows from a linear congruence in exponents, while the polynomial degree confirms there cannot be more than four roots over the prime field.

---

## Wilson's Converse

For an integer $$n>1$$, if $$(n-1)!\equiv-1\pmod n$$, then $$n$$ is prime. If it were composite, it would have a divisor $$d$$ with $$1<d<n$$. That divisor occurs in the factorial, so reducing the congruence modulo $$d$$ would say zero is negative one, a contradiction.

Thus Wilson provides an if-and-only-if primality criterion, unlike Fermat. Its drawback is computational rather than logical: a factorial near a large candidate can be costly to evaluate. In contest problems, Wilson is most effective when almost all factors cancel or pair with inverses.

---

## The Order of a Power

If $$a$$ has order $$d$$ modulo $$m$$, then

$$
\operatorname{ord}_m(a^k)=\frac d{\gcd(d,k)}
$$

for positive $$k$$. Indeed, $$(a^k)^t$$ equals one precisely when $$d\mid kt$$, whose least positive solution is the displayed quotient.

For example, three has order sixteen modulo seventeen. Its square nine has order eight, while its cube twenty-seven still has order sixteen because three is coprime to sixteen.

This rule is useful when several bases in a problem are powers of one known element. It avoids recalculating a full remainder cycle for each base and explains exactly when taking a power shortens that cycle.

---

## Key Equations

:::equations
| Tool | Formula and conditions |
| --- | --- |
| Fermat | $$a^{p-1}\equiv1\pmod p$$, prime $$p\nmid a$$ |
| Totient | $$\varphi(m)=m\prod_{p\mid m}(1-1/p)$$ |
| Euler | $$a^{\varphi(m)}\equiv1\pmod m$$, $$\gcd(a,m)=1$$ |
| Order | $$a^k\equiv1\pmod m\iff\operatorname{ord}_m(a)\mid k$$ |
| Order bound | $$\operatorname{ord}_m(a)\mid\varphi(m)$$ |
| Wilson | $$(p-1)!\equiv-1\pmod p$$ for prime $$p$$ |
| CRT order | $$\operatorname{ord}_{uv}(a)=\operatorname{lcm}(\operatorname{ord}_u(a),\operatorname{ord}_v(a))$$ for coprime $$u,v$$ |
| Prime-power order | $$\operatorname{ord}_{p^k}(a)=d\,p^{\max(0,k-c)}$$, odd $$p$$, $$d=\operatorname{ord}_p(a),c=v_p(a^d-1)$$ |
| Same-base powers | $$a^u\equiv a^v\pmod m\iff u\equiv v\pmod{\operatorname{ord}_m(a)}$$ |
| Decimal period | Period of $$1/m$$ is $$\operatorname{ord}_m(10)$$ when $$\gcd(m,10)=1$$ |
| Wilson square root | $$[((p-1)/2)!]^2\equiv-1\pmod p$$ for prime $$p\equiv1\pmod4$$ |
| Fermat-number product | $$\prod_{i=0}^{n-1}(2^{2^i}+1)=2^{2^n}-1$$ |
| Roots over a prime field | $$x^k\equiv1\pmod p$$ has $$\gcd(k,p-1)$$ nonzero solutions |
| Order of a power | $$\operatorname{ord}_m(a^k)=d/\gcd(d,k)$$, $$d=\operatorname{ord}_m(a)$$ |
:::
