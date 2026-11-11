---
title: "Quadratic Residues"
status: developing
progress: 68
sidebar:
  order: 6
description: "Competition math notes on quadratic residues, Euler's criterion, modular obstructions, and sums of two squares with worked examples."
---

## Which Remainders Can Be Squares?

An integer $$r$$ is a **quadratic residue modulo $$m$$** if $$x^2\equiv r\pmod m$$ has a solution. Some conventions reserve the term for nonzero residues, so we will explicitly say “nonzero quadratic residue” when needed.

Listing squares modulo a small integer is often enough to rule out an equation:

| Modulus | Possible square residues |
| --- | --- |
| $$3$$ | $$0,1$$ |
| $$4$$ | $$0,1$$ |
| $$5$$ | $$0,1,4$$ |
| $$8$$ | $$0,1,4$$ |
| $$16$$ | $$0,1,4,9$$ |

Because $$x^2\equiv(-x)^2$$, only about half the inputs need to be checked.

<div class="theorem-box">

**Example.** Prove that $$x^2=8y+3$$ has no integer solutions.

The right side is three modulo eight, but the possible square residues modulo eight are zero, one, and four. The equation is impossible.

</div>

---

## Squares Modulo an Odd Prime

For an odd prime $$p$$, exactly $$(p-1)/2$$ nonzero residue classes are squares. The nonzero inputs pair as $$x$$ and $$-x$$, and no other repetition occurs: if $$x^2\equiv y^2$$, then $$p\mid(x-y)(x+y)$$, so $$x\equiv y$$ or $$x\equiv-y$$.

**Euler's criterion** says that for $$p\nmid a$$,

$$
a^{(p-1)/2}\equiv
\begin{cases}
1\pmod p,&a\text{ is a quadratic residue},\\
-1\pmod p,&a\text{ is a nonresidue}.
\end{cases}
$$

It gives a test without searching for a square root. One justification is that every nonzero square satisfies the first equation by Fermat's theorem. There are already $$(p-1)/2$$ such roots, the maximum possible for that polynomial; every remaining input has value $$-1$$ because its value squared is one.

<div class="theorem-box">

**Example.** Determine whether $$5$$ is a square modulo $$13$$.

Compute by squaring:

$$
5^2\equiv-1\pmod{13},\qquad5^6\equiv(-1)^3\equiv-1\pmod{13}.
$$

Euler's criterion says that five is a nonresidue. Thus $$x^2\equiv5\pmod{13}$$ has no solution.

</div>

The test determines existence, not the square root itself. If a root is needed, a short residue table can still be the fastest method for a small prime.

---

## When Is Negative One a Square?

For an odd prime $$p$$, the number $$-1$$ is a quadratic residue exactly when $$p\equiv1\pmod4$$. Euler's criterion gives

$$
(-1)^{(p-1)/2}=1
$$

exactly in that case. Equivalently, a square root of negative one has multiplicative order four, forcing $$4\mid p-1$$.

<div class="theorem-box">

**Example.** An odd prime $$p$$ divides $$n^2+1$$. Prove that $$p\equiv1\pmod4$$.

Since $$n^2\equiv-1\pmod p$$, we have $$p\nmid n$$ and negative one is a square modulo $$p$$. The criterion above therefore gives $$p\equiv1\pmod4$$.

</div>

---

## Primes That Are Three Modulo Four

If $$q\equiv3\pmod4$$ is prime and $$q\mid a^2+b^2$$, then $$q$$ divides both $$a$$ and $$b$$. Otherwise, if $$q\nmid b$$, division by $$b^2$$ would give $$(ab^{-1})^2\equiv-1\pmod q$$, which is impossible. Thus $$q\mid b$$, and the original congruence then gives $$q\mid a$$.

Removing the resulting factor of $$q^2$$ and repeating shows that every prime congruent to three modulo four appears to an **even exponent** in a nonzero sum of two integer squares.

<div class="theorem-box">

**Example.** Decide whether $$2023$$ can be written as $$a^2+b^2$$ for integers $$a,b$$.

Factor $$2023=7\cdot17^2$$. The prime seven is three modulo four and has odd exponent one. The necessary condition fails, so no representation exists.

</div>

---

## Constructing Sums of Two Squares

The product identity

$$
(a^2+b^2)(c^2+d^2)=(ac-bd)^2+(ad+bc)^2
$$

lets us multiply representations. It is also the modulus identity for $$(a+bi)(c+di)$$.

**Fermat's two-square theorem**, also called Fermat's Christmas theorem, says that a prime $$p\equiv1\pmod4$$ is a sum of two integer squares. Together with $$2=1^2+1^2$$, the product identity, and the obstruction above, it gives the full criterion:

A positive integer is a sum of two integer squares, allowing zero, exactly when every prime divisor congruent to three modulo four has even exponent. The existence direction for primes is a deeper theorem; the small-modulus obstruction alone does not prove it.

<div class="theorem-box">

**Example.** Find two different representations of $$65$$ as a sum of two squares.

Use $$5=1^2+2^2$$ and $$13=2^2+3^2$$. The product identity gives

$$
65=(1\cdot2-2\cdot3)^2+(1\cdot3+2\cdot2)^2=4^2+7^2.
$$

Changing the sign of the second imaginary component gives another representation:

$$
65=(1\cdot2+2\cdot3)^2+(2\cdot2-1\cdot3)^2=8^2+1^2.
$$

</div>

:::strategy
Use small-modulus tables for a quick obstruction. For an odd prime modulus, Euler's criterion tests whether a nonzero residue is a square. For an integer sum of two squares, inspect the exponents of primes that are three modulo four before searching for a representation.
:::

## The Legendre Symbol

For an odd prime $$p$$, the **Legendre symbol** packages the quadratic-residue test:

$$
\left(\frac ap\right)=
\begin{cases}
0,&p\mid a,\\
1,&a\text{ is a nonzero square modulo }p,\\
-1,&a\text{ is a nonsquare modulo }p.
\end{cases}
$$

The notation is a symbol, not an ordinary fraction. Its numerator can be reduced modulo the denominator, and it is multiplicative:

$$
\left(\frac{ab}{p}\right)=\left(\frac ap\right)\left(\frac bp\right).
$$

For nonzero residues, this follows from Euler's criterion by multiplying the corresponding powers. Cases involving zero are immediate. Thus a product of two nonresidues is a residue, while multiplying a residue by a nonresidue produces a nonresidue.

<div class="theorem-box">

**Example.** Modulo seven, both three and five are nonresidues. Determine whether fifteen is a residue.

Multiplicativity gives $$(15/7)=(3/7)(5/7)=1$$. Since fifteen is one modulo seven, this agrees with the direct square $$1^2$$. The example illustrates that “nonsquare times nonsquare” behaves differently from ordinary positive integers.

</div>

---

## Quadratic Reciprocity and the Supplementary Laws

For distinct odd primes $$p,q$$, **quadratic reciprocity** states

$$
\left(\frac pq\right)\left(\frac qp\right)
=(-1)^{(p-1)(q-1)/4}.
$$

The sign changes exactly when both primes are three modulo four. Otherwise the two symbols are equal. The supplementary laws are

$$
\left(\frac{-1}{p}\right)=(-1)^{(p-1)/2},\qquad
\left(\frac2p\right)=(-1)^{(p^2-1)/8}.
$$

Thus two is a residue exactly when $$p\equiv1$$ or $$7\pmod8$$. These are deeper theorems; their role here is to reduce a residue calculation to smaller primes. They do not find an actual square root automatically.

<div class="theorem-box">

**Example.** Determine whether six is a square modulo one hundred one.

Factor the numerator: $$(6/101)=(2/101)(3/101)$$. Since $$101\equiv5\pmod8$$, the first symbol is negative one.

Because $$101\equiv1\pmod4$$, reciprocity gives $$(3/101)=(101/3)=(2/3)=-1$$. Their product is one, so six is a square modulo 101.

Indeed, $$39^2=1521\equiv6\pmod{101}$$, providing an explicit check.

</div>

<div class="theorem-box">

**Example.** Determine whether seven is a square modulo twenty-nine and find its roots if it is.

Reciprocity has no sign change because twenty-nine is one modulo four:

$$
\left(\frac7{29}\right)=\left(\frac{29}7\right)=\left(\frac17\right)=1.
$$

A short search gives $$6^2=36\equiv7\pmod{29}$$. The two roots are six and negative six, or residues six and twenty-three. A prime modulus gives at most two roots of a nonzero quadratic equation.

</div>

Do not apply these prime-denominator tests directly to an arbitrary composite modulus. Solve the congruence modulo its prime powers and combine compatible roots with CRT. A composite-symbol analogue can equal one without guaranteeing that a square root exists.

---

## Gaussian Integers and the Norm

A **Gaussian integer** is $$a+bi$$ with integers $$a,b$$. Its norm is

$$
N(a+bi)=a^2+b^2.
$$

The norm is multiplicative because complex moduli multiply. Thus finding a sum-of-two-squares representation is equivalent to finding a Gaussian integer with a prescribed norm.

Gaussian integers admit a Euclidean algorithm. Given $$z,w$$ with $$w\ne0$$, approximate the real and imaginary parts of $$z/w$$ by nearest integers to obtain a Gaussian integer $$q$$. Each coordinate error is at most one-half, so the remainder $$r=z-qw$$ satisfies $$N(r)\le N(w)/2<N(w)$$ unless it is zero.

This norm decrease proves termination just as the ordinary Euclidean algorithm does. It also supplies a Gaussian Bézout identity for the GCD. These facts explain why a square root of negative one modulo a prime can be converted into a sum of two squares.

<div class="theorem-box">

**Example.** Use the root $$5^2\equiv-1\pmod{13}$$ to construct a sum-of-two-squares representation of thirteen.

Compute a Gaussian GCD of thirteen and $$5+i$$. A convenient division is

$$
13=2(5+i)+(3-2i).
$$

The next division is exact:

$$
5+i=(1+i)(3-2i).
$$

Thus a Gaussian GCD is $$3-2i$$, whose norm is thirteen. Hence $$13=3^2+2^2$$.

The calculation turns the modular root into a Euclidean remainder with the required norm.

</div>

---

## Why a Prime That Is One Modulo Four Is a Sum of Squares

Let $$p\equiv1\pmod4$$ be prime, and choose $$t$$ with $$t^2\equiv-1\pmod p$$. Such a root exists by the negative-one criterion; Wilson's theorem also constructs one.

Take a Gaussian GCD $$\delta=\gcd(p,t+i)$$. Its norm divides $$p^2$$, because $$\delta$$ divides $$p$$, so the possible norms are $$1,p,p^2$$.

The norm cannot be one. Otherwise Gaussian Bézout gives a combination of $$p$$ and $$t+i$$ equal to one. Multiply it by $$t-i$$. Since $$(t+i)(t-i)=t^2+1$$ is divisible by $$p$$, this would force $$p$$ to divide $$t-i$$ as a Gaussian integer, which is impossible because its imaginary coefficient is negative one.

The norm cannot be $$p^2$$ either. In that case $$p/\delta$$ has norm one, making $$\delta$$ an associate of $$p$$. Then $$p$$ would divide $$t+i$$, again impossible from the imaginary coefficient.

Therefore $$N(\delta)=p$$. Writing $$\delta=a+bi$$ yields $$p=a^2+b^2$$. This proves the prime existence theorem using the Euclidean structure of Gaussian integers, rather than inferring existence from a modular test alone.

---

## Constructing Representations of Composite Numbers

Once the prime-factor criterion passes, multiply representations using the two-square identity. Prime factors congruent to three modulo four have even exponents and can be absorbed into a common integer square. Powers of two use $$2=1^2+1^2$$, while primes congruent to one modulo four use their individual representations.

<div class="theorem-box">

**Example.** Construct a representation of $$325$$ as a sum of two squares.

Since $$325=5^2\cdot13$$, use $$5=1^2+2^2$$ and $$13=2^2+3^2$$. One simple representation comes from multiplying the known representation of thirteen by the square twenty-five:

$$
325=10^2+15^2.
$$

Using a nontrivial representation $$25=3^2+4^2$$ instead, the product identity gives

$$
325=(3\cdot2-4\cdot3)^2+(3\cdot3+4\cdot2)^2=6^2+17^2.
$$

Changing the conjugate choice gives $$325=1^2+18^2$$. Different Gaussian factorizations can produce distinct integer representations.

</div>

The distinction between an existence criterion and a construction matters. Factoring the number proves that a representation exists, while multiplying explicit prime representations produces one. A numerical search may be quicker for small numbers, but the structural method scales and explains the result.

---

## Using Residues as a Filter Rather Than a Final Answer

A congruence solution is necessary for an integer equation, but generally not sufficient. Passing tests modulo three, five, and eight does not prove that a square or sum-of-squares representation exists. It merely eliminates some obstructions.

For instance, an integer can be a square modulo several small moduli and still lie strictly between consecutive integer squares. Combine residue information with bounds, factorization, or valuation arguments before declaring a classification complete.

Likewise, if a prime three modulo four divides a sum of squares, the forced common divisor may invite descent. Divide by its square and repeat until the valuation is exhausted. This proves the even-exponent condition and can turn an equation into an impossibility argument when primitivity is assumed.

:::strategy
Use small residues for quick exclusions, Legendre symbols for prime-modulus existence tests, and CRT for composite moduli. For sums of two squares, inspect prime exponents first, then construct representations with the product identity or a Gaussian GCD.
:::

---

## Primitive Representations and Forced Common Factors

A sum-of-two-squares representation is **primitive** when its two entries are coprime. The ordinary existence criterion allows square factors of primes three modulo four, but such a prime forces a common divisor in every representation.

<div class="theorem-box">

**Example.** Find all integer representations of forty-five as a sum of two squares and determine whether any is primitive.

Since three divides $$x^2+y^2=45$$ and is three modulo four, it divides both variables. Write $$x=3u,y=3v$$. The equation becomes $$u^2+v^2=5$$.

The only absolute-value pair is one and two. Thus all representations of forty-five have absolute values three and six, with independent signs and either order. There are eight ordered representations, and none is primitive because every pair has common divisor three.

</div>

The factorization criterion proves existence because $$45=3^2\cdot5$$ has an even exponent on three. The same prime exponent nevertheless prevents primitivity. These are different questions.

A factor of four also prevents a primitive representation: squares are zero or one modulo four, so a sum divisible by four forces both variables even. Hence a primitive sum of two squares contains no prime three modulo four and has at most one factor of two.

---

## Constructing a Right Triangle with Prime Hypotenuse

If a prime $$p=u^2+v^2$$, the product identity gives

$$
p^2=(u^2-v^2)^2+(2uv)^2.
$$

Thus a representation of the prime produces an integer right triangle with hypotenuse $$p$$. For an odd prime, the two entries are coprime and of opposite parity, so the resulting triangle is primitive.

For example, $$13=3^2+2^2$$ produces legs five and twelve. This connects the prime residue condition $$p\equiv1\pmod4$$ to the existence of primitive right triangles with that prime as hypotenuse.

A prime three modulo four cannot occur as the hypotenuse of a primitive integer right triangle: its square being a sum of two squares would force both legs divisible by that prime. This contradiction is another use of the same residue obstruction.

---

## Key Equations

:::equations
| Tool | Formula or condition |
| --- | --- |
| Euler's criterion | $$a^{(p-1)/2}\equiv1$$ or $$-1\pmod p$$ for a residue or nonresidue, with prime $$p\nmid a$$ |
| Negative one | $$-1$$ is a square modulo odd prime $$p$$ iff $$p\equiv1\pmod4$$ |
| Prime obstruction | $$q\mid a^2+b^2$$ and prime $$q\equiv3\pmod4$$ force $$q\mid a,b$$ |
| Product identity | $$(a^2+b^2)(c^2+d^2)=(ac-bd)^2+(ad+bc)^2$$ |
| Sum-of-two-squares criterion | Every prime $$q\equiv3\pmod4$$ has even exponent |
| Legendre multiplicativity | $$(ab/p)=(a/p)(b/p)$$ for odd prime $$p$$ |
| Reciprocity | $$(p/q)(q/p)=(-1)^{(p-1)(q-1)/4}$$ for distinct odd primes |
| Supplement for two | $$(2/p)=(-1)^{(p^2-1)/8}$$ |
| Gaussian norm | $$N(a+bi)=a^2+b^2$$ and $$N(zw)=N(z)N(w)$$ |
| Gaussian remainder | Choose nearest-coordinate quotient so $$N(r)\le N(w)/2$$ |
| Primitive obstruction | A prime $$q\equiv3\pmod4$$ dividing $$x^2+y^2$$ forces $$q\mid x,y$$ |
| Prime-to-triple construction | $$p=u^2+v^2\Longrightarrow p^2=(u^2-v^2)^2+(2uv)^2$$ |
:::
