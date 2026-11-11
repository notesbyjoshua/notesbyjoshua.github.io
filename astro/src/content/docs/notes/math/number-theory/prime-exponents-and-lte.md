---
title: "Prime Exponents and LTE"
status: developing
progress: 68
sidebar:
  order: 5
description: "Competition math notes on prime valuations, factorial exponents, trailing zeros, binomial coefficients, and LTE with conditions and worked examples."
---

## Prime Valuations

For a prime $$p$$ and a nonzero integer $$n$$, the **valuation** $$v_p(n)$$ is the exponent of $$p$$ in the prime factorization of $$\lvert n\rvert$$. For example, $$72=2^3\cdot3^2$$, so $$v_2(72)=3$$ and $$v_3(72)=2$$. Set $$v_p(0)=\infty$$ when needed.

Products and powers become addition and multiplication of exponents:

$$
v_p(ab)=v_p(a)+v_p(b),\qquad v_p(a^k)=kv_p(a).
$$

For nonzero rationals, define $$v_p(a/b)=v_p(a)-v_p(b)$$. For sums, we only have

$$
v_p(a+b)\ge\min(v_p(a),v_p(b)),
$$

with equality if the two valuations differ. Equal valuations can allow extra cancellation, so valuations do not distribute over addition.

<div class="theorem-box">

**Example.** Find the largest power of two dividing $$24\cdot40^3$$.

Since $$v_2(24)=3$$ and $$v_2(40)=3$$,

$$
v_2(24\cdot40^3)=3+3\cdot3=12.
$$

The largest power is $$2^{12}$$, meaning $$2^{12}$$ divides the number but $$2^{13}$$ does not.

</div>

---

## Factorials and Legendre's Formula

In $$n!$$, every multiple of $$p$$ contributes a factor of $$p$$, every multiple of $$p^2$$ contributes another, and so on. This gives **Legendre's formula**:

$$
v_p(n!)=\sum_{j\ge1}\left\lfloor\frac n{p^j}\right\rfloor.
$$

The sum is finite because the terms become zero once $$p^j>n$$.

<div class="theorem-box">

**Example.** Find the number of trailing decimal zeros in $$100!$$.

A zero needs a factor of ten, so its count is $$\min(v_2(100!),v_5(100!))$$. There are more factors of two than five, and

$$
v_5(100!)=\left\lfloor\frac{100}5\right\rfloor+\left\lfloor\frac{100}{25}\right\rfloor=20+4=24.
$$

Thus $$100!$$ ends in exactly $$24$$ zeros.

</div>

For base $$b=\prod p_i^{e_i}$$, the number of trailing base-$$b$$ zeros is $$\min_i\lfloor v_{p_i}(N)/e_i\rfloor$$. Dividing by the base exponents is essential for bases such as twelve or one hundred.

---

## Binomial Coefficients

Use the factorial definition to subtract valuations:

$$
v_p\left(\binom nk\right)=v_p(n!)-v_p(k!)-v_p((n-k)!).
$$

This determines prime divisibility without calculating the binomial coefficient itself.

<div class="theorem-box">

**Example.** Find the exponent of two in $$\binom{20}{10}$$.

Legendre gives $$v_2(20!)=10+5+2+1=18$$ and $$v_2(10!)=5+2+1=8$$. Therefore

$$
v_2\left(\binom{20}{10}\right)=18-2(8)=2.
$$

The binomial coefficient is divisible by four but not eight.

</div>

---

## LTE for Odd Primes

The **lifting-the-exponent lemma**, or **LTE**, finds the exact valuation of certain differences of powers. If $$p$$ is an odd prime, $$p\mid a-b$$, $$p\nmid ab$$, and $$n\ge1$$, then

$$
v_p(a^n-b^n)=v_p(a-b)+v_p(n).
$$

Assume the difference is nonzero when asking for a finite exponent. The lemma says that once $$a,b$$ agree modulo $$p$$ and neither contains a factor of $$p$$, raising to the $$n$$th power adds exactly the exponent of $$p$$ in $$n$$.

For odd $$n$$, replacing $$b$$ by $$-b$$ gives the sum version:

$$
v_p(a^n+b^n)=v_p(a+b)+v_p(n),
$$

provided $$p\mid a+b$$ and $$p\nmid ab$$. The oddness of $$n$$ is required for this rewrite.

<div class="theorem-box">

**Example.** Find the largest exponent $$e$$ such that $$3^e\mid10^{54}-1$$.

The prime three is odd, $$3\mid10-1$$, and $$3\nmid10\cdot1$$. Thus LTE applies:

$$
e=v_3(10^{54}-1)=v_3(9)+v_3(54)=2+3=5.
$$

</div>

<div class="theorem-box">

**Example.** Find $$v_3(2^{81}+1)$$.

Here $$81$$ is odd, $$3\mid2+1$$, and $$3\nmid2$$. The sum version gives

$$
v_3(2^{81}+1)=v_3(3)+v_3(81)=1+4=5.
$$

</div>

---

## The Prime Two

For odd integers $$a,b$$, the two-adic formulas depend on the exponent's parity. If $$n$$ is odd,

$$
v_2(a^n-b^n)=v_2(a-b).
$$

If $$n$$ is even,

$$
v_2(a^n-b^n)=v_2(a-b)+v_2(a+b)+v_2(n)-1.
$$

For odd $$n$$, we also have $$v_2(a^n+b^n)=v_2(a+b)$$. For even $$n$$ and odd $$a,b$$, each even power is one modulo eight, so $$v_2(a^n+b^n)=1$$.

<div class="theorem-box">

**Example.** Find $$v_2(3^{20}-1)$$.

Both bases are odd and the exponent is even, so

$$
v_2(3^{20}-1)=v_2(2)+v_2(4)+v_2(20)-1=1+2+2-1=4.
$$

Using the odd-prime formula would incorrectly give three.

</div>

:::strategy
Use valuations whenever the question asks for a largest prime power, a perfect power, or trailing zeros. Before LTE, write down the prime, the base difference or sum, the coprimality condition, and the parity of the exponent. If $$p\nmid a-b$$, first look for a suitable power or order that creates the required congruence.
:::

## Why Valuation Rules Work

Write $$a=p^ru$$ and $$b=p^sv$$ with $$p\nmid uv$$. If $$r<s$$, then

$$
a+b=p^r(u+p^{s-r}v),
$$

and the factor in parentheses is not divisible by $$p$$. Therefore $$v_p(a+b)=r$$. If $$r=s$$, the unit terms may cancel modulo $$p$$ and create extra powers. This proves the unequal-valuation rule and explains why equal valuations need more information.

The same argument applies to a difference. It is useful before LTE: sometimes the two terms already have unequal valuations, so the answer is immediate and lifting is unnecessary.

<div class="theorem-box">

**Example.** Find $$v_3(6^{20}-9^{20})$$.

The two valuations are twenty and forty. Because they differ, the difference has valuation twenty. Equivalently,

$$
6^{20}-9^{20}=3^{20}(2^{20}-3^{20}),
$$

and the parenthetical factor is not divisible by three.

</div>

---

## Legendre's Formula and Base Digits

Let $$s_p(n)$$ be the sum of the base-$$p$$ digits of $$n$$. Legendre's formula can be rewritten as

$$
v_p(n!)=\frac{n-s_p(n)}{p-1}.
$$

To derive it, write $$n=\sum_jd_jp^j$$. The floor sum counts a digit $$d_j$$ with total weight $$1+p+\cdots+p^{j-1}=(p^j-1)/(p-1)$$. Summing the contributions gives the formula.

The digit version is especially useful for powers of the base or for differences of factorial valuations, where the large linear terms cancel.

<div class="theorem-box">

**Example.** Find the exponent of two in $$\binom{100}{50}$$.

The binary digit sums are $$s_2(100)=3$$ and $$s_2(50)=3$$. Therefore

$$
v_2\binom{100}{50}
=(100-3)-2(50-3)=3.
$$

The coefficient is divisible by eight but not sixteen. No factorial or binomial coefficient needs to be evaluated.

</div>

For base $$p$$, the general binomial valuation becomes

$$
v_p\binom nk=\frac{s_p(k)+s_p(n-k)-s_p(n)}{p-1}.
$$

Every carry in adding $$k$$ and $$n-k$$ reduces the combined digit sum by $$p-1$$, including carries propagated through several positions. Thus this valuation equals the number of carries. This is **Kummer's theorem**, with the carry interpretation derived directly from Legendre.

---

## A Catalan Parity Classification

The factorial form of a Catalan number is $$C_n=(2n)!/[n!(n+1)!]$$. Applying the binary digit formula and using $$s_2(2n)=s_2(n)$$ gives

$$
v_2(C_n)=s_2(n+1)-1.
$$

A positive integer has binary digit sum one exactly when it is a power of two. Consequently, $$C_n$$ is odd exactly when $$n=2^r-1$$ for some $$r\ge0$$.

<div class="theorem-box">

**Example.** Determine whether $$C_{31}$$ and $$C_{32}$$ are odd, and find their exact powers of two.

For $$n=31$$, the number $$n+1=32$$ has one binary one, so $$v_2(C_{31})=0$$ and the Catalan number is odd.

For $$n=32$$, the number $$n+1=33$$ has two binary ones, so $$v_2(C_{32})=1$$. It is even but not divisible by four.

</div>

This is a useful example of a structural answer replacing a large calculation. The numerical values of the Catalan numbers are irrelevant to their parity.

---

## A Proof of Odd-Prime LTE

Assume $$p$$ is odd, $$p\mid a-b$$, and $$p\nmid ab$$. First suppose the exponent $$m$$ is not divisible by $$p$$. Factoring a difference of powers gives

$$
\frac{a^m-b^m}{a-b}=a^{m-1}+a^{m-2}b+\cdots+b^{m-1}
\equiv mb^{m-1}\not\equiv0\pmod p.
$$

Thus raising to an exponent prime to $$p$$ adds no new valuation.

Next consider exponent $$p$$. Write $$a=b+h$$ with $$v_p(h)=r\ge1$$. In the binomial expansion of $$(b+h)^p-b^p$$, the first term $$pb^{p-1}h$$ has valuation $$r+1$$. Every other term has valuation at least $$r+2$$: the intermediate binomial coefficients contain $$p$$, and the final term $$h^p$$ has valuation $$pr\ge r+2$$.

The unequal-valuation principle therefore gives

$$
v_p(a^p-b^p)=r+1.
$$

Finally write $$n=p^tm$$ with $$p\nmid m$$. The first step preserves the original valuation, and each of the $$t$$ exponent-$$p$$ steps adds one. Hence $$v_p(a^n-b^n)=v_p(a-b)+t$$.

The proof also explains the exceptional behavior at two: the final binomial term may tie the first term's valuation rather than lying strictly above it, permitting additional cancellation.

---

## Preparing an Expression Before LTE

If $$p\nmid a-b$$, the lemma's difference form does not apply. An order calculation or a parity condition may let us group powers so that the new bases do agree modulo $$p$$.

If both bases contain $$p$$, remove the common prime-power factor first. LTE concerns unit bases, not arbitrary multiples of the prime.

<div class="theorem-box">

**Example.** Find $$v_3(6^{20}-12^{20})$$.

Factor the common term:

$$
6^{20}-12^{20}=6^{20}(1-2^{20}).
$$

The first factor has valuation twenty. For the second, write $$2^{20}-1=4^{10}-1$$. Now three divides $$4-1$$ and divides neither base, so LTE gives

$$
v_3(4^{10}-1)=v_3(3)+v_3(10)=1.
$$

The total valuation is twenty-one. Applying LTE directly to bases six and twelve would violate the coprimality hypothesis.

</div>

---

## A Least-Exponent Problem Combining Several Primes

When a target divisor contains several prime powers, translate each into a valuation inequality. The least exponent must satisfy all resulting divisibility conditions simultaneously.

<div class="theorem-box">

**Example.** Find the smallest positive $$n$$ such that $$3^7 11^2\mid10^n-1$$.

For three, LTE applies directly:

$$
v_3(10^n-1)=2+v_3(n).
$$

Thus $$3^5\mid n$$.

Modulo eleven, ten is negative one, so $$n$$ must be even. Write $$n=2t$$ and apply LTE to $$100^t-1$$:

$$
v_{11}(100^t-1)=v_{11}(99)+v_{11}(t)=1+v_{11}(t).
$$

Therefore eleven divides $$t$$, equivalently twenty-two divides $$n$$. Combining the conditions gives

$$
n_{\min}=\operatorname{lcm}(3^5,22)=5346.
$$

Both valuation inequalities hold at this value, so the necessary conditions are also sufficient.

</div>

A single prime condition may force a preliminary rewrite before another theorem becomes usable. Here parity determined the exponent form before the eleven-adic calculation. Establish that information in the solution rather than applying a formula with an unresolved parity parameter.

---

## When Valuations Prove an Impossibility

If an equation asserts that an expression is a perfect $$k$$th power, every finite prime valuation must be a multiple of $$k$$. Finding one prime whose valuation is forced into the wrong residue class rules out the equation.

For example, for positive odd $$n$$, the formula $$v_3(2^n+1)=1+v_3(n)$$ immediately rules out a square whenever $$v_3(n)$$ is even. This is a conditional obstruction, not a full classification: if the valuation is even, other primes may still prevent a square.

:::strategy
Strip common prime factors, determine the relevant order or parity, and only then lift the exponent. For factorials, choose between floor sums and digit sums. For a perfect-power equation, compare the resulting valuation with the required multiple before calculating the whole integer.
:::

---

## Square Roots of One Modulo Powers of Two

For $$k\ge3$$, the congruence $$x^2\equiv1\pmod{2^k}$$ has four solutions:

$$
x\equiv1,-1,1+2^{k-1},-1+2^{k-1}\pmod{2^k}.
$$

To prove completeness, $$x$$ must be odd. The factors $$x-1,x+1$$ are consecutive even numbers, so one has valuation exactly one and the other has valuation at least two. Their product has valuation at least $$k$$ only if the second factor has valuation at least $$k-1$$.

Thus $$x\equiv1$$ or negative one modulo $$2^{k-1}$$, giving the four classes above modulo $$2^k$$. Squaring each class verifies that it works.

For modulus sixty-four, the solutions are one, thirty-one, thirty-three, sixty-three. This differs from an odd prime power, which has only the two sign roots. The exceptional two-adic LTE formula reflects the same split between the valuations of $$x-1$$ and $$x+1$$.

---

## Inverting Legendre's Formula

Sometimes the question asks for the smallest factorial containing a required prime power. The valuation is nondecreasing in $$n$$ but may jump by more than one at a multiple of a high prime power.

<div class="theorem-box">

**Example.** Find the smallest $$n$$ such that $$3^{20}\mid n!$$.

Legendre gives

$$
v_3(44!)=14+4+1=19,\qquad
v_3(45!)=15+5+1=21.
$$

The valuation is nondecreasing, so every earlier factorial has valuation below twenty, while forty-five factorial has enough. The smallest $$n$$ is forty-five.

There is no factorial valuation equal to twenty at this transition. Searching for equality rather than the inequality would miss the correct threshold.

</div>

For larger targets, a monotone search can bracket the smallest $$n$$. The approximation $$v_p(n!)<n/(p-1)$$ supplies a quick necessary lower bound, while the exact floor sum settles the final neighboring values.

---

## A Unique Least Valuation Cannot Cancel

For several nonzero terms, if exactly one term has the smallest $$p$$-valuation, their sum has that same valuation. Factor out the common smallest power; one remaining term is a unit modulo $$p$$ and all others are divisible by $$p$$.

This gives an impossibility test for rational sums. A rational number is an integer only if all its prime valuations are nonnegative.

<div class="theorem-box">

**Example.** Prove that $$2^{-a}+3^{-b}+5^{-c}$$ is not an integer when $$a,b,c$$ are positive integers.

At the prime two, the valuations of the three summands are $$-a,0,0$$. The smallest valuation is unique, so the sum has valuation $$-a<0$$. Therefore it cannot be an integer.

</div>

This proof avoids a large common denominator and identifies exactly which prime obstructs integrality. If two least valuations tied, cancellation could occur and a further argument would be needed.

---

## Trailing Zeros in a Composite Base

A base-zero count compares each available prime exponent with the number required for one copy of the base. The scarcest raw prime exponent need not be the bottleneck after this division.

For $$100!$$, Legendre gives $$v_2=97$$ and $$v_3=48$$. In base $$72=2^3 3^2$$, the trailing-zero count is

$$
\min\left(\left\lfloor\frac{97}{3}\right\rfloor,
\left\lfloor\frac{48}{2}\right\rfloor\right)=24.
$$

Each zero consumes three twos and two threes. Counting only factors of the largest prime, as in ordinary decimal factorial problems, would not be justified for an arbitrary base.

---

## Prime Binomial Coefficients and Congruences

For a prime $$p$$ and $$1\le k\le p-1$$, the numerator of $$\binom pk=p!/[k!(p-k)!]$$ contains exactly one factor of $$p$$ and neither denominator factorial contains one. Hence $$v_p\binom pk=1$$.

Applying the binomial theorem gives

$$
(a+b)^p\equiv a^p+b^p\pmod p
$$

for integers $$a,b$$. Every middle coefficient vanishes modulo the prime. This congruence does not generally hold modulo $$p^2$$, because those coefficients have valuation exactly one rather than at least two.

The valuation calculation therefore explains both the useful congruence and its limitation at the next prime power.

---

## Key Equations

:::equations
| Tool | Formula and conditions |
| --- | --- |
| Products | $$v_p(ab)=v_p(a)+v_p(b)$$ |
| Factorials | $$v_p(n!)=\sum_{j\ge1}\lfloor n/p^j\rfloor$$ |
| Binomial coefficients | $$v_p\binom nk=v_p(n!)-v_p(k!)-v_p((n-k)!)$$ |
| Odd-prime LTE | $$v_p(a^n-b^n)=v_p(a-b)+v_p(n)$$ if $$p\mid a-b$$ and $$p\nmid ab$$ |
| Two-adic LTE, even $$n$$ | $$v_2(a^n-b^n)=v_2(a-b)+v_2(a+b)+v_2(n)-1$$ for odd $$a,b$$ |
| Base-$$b$$ trailing zeros | $$\min_i\lfloor v_{p_i}(N)/e_i\rfloor$$ for $$b=\prod p_i^{e_i}$$ |
| Digit form of Legendre | $$v_p(n!)=(n-s_p(n))/(p-1)$$ |
| Kummer | $$v_p\binom nk$$ equals the number of carries in base-$$p$$ addition of $$k,n-k$$ |
| Catalan parity | $$v_2(C_n)=s_2(n+1)-1$$; odd iff $$n=2^r-1$$ |
| Unequal valuations | $$v_p(a\pm b)=\min(v_p(a),v_p(b))$$ when the two valuations differ |
| Two-power square roots | $$x^2\equiv1\pmod{2^k}$$ has classes $$\pm1,2^{k-1}\pm1$$ for $$k\ge3$$ |
| Unique least valuation | If one summand has strictly least valuation, the sum has that valuation |
| Prime binomial valuation | $$v_p\binom pk=1$$ for $$1\le k\le p-1$$ |
| Binomial congruence | $$(a+b)^p\equiv a^p+b^p\pmod p$$ |
:::
