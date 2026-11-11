---
title: "Modular Arithmetic"
status: developing
progress: 68
sidebar:
  order: 2
description: "Competition math notes on congruences, modular inverses, remainder cycles, CRT, and digit tests with worked number theory problems."
---

## Congruences and Remainders

For a positive integer $$m$$, write $$a\equiv b\pmod m$$ when $$m\mid(a-b)$$. The integers $$a,b$$ have the same remainder after division by $$m$$. Congruences let us discard information that is irrelevant to a divisibility or remainder question.

We can add, subtract, and multiply congruences with the same modulus. We can also raise them to nonnegative integer powers. Reducing intermediate results keeps calculations small.

<div class="theorem-box">

**Example.** Find the remainder when $$7^{2026}$$ is divided by $$10$$.

The last digits of successive powers of seven are $$7,9,3,1$$, then repeat because $$7^4\equiv1\pmod{10}$$. Since $$2026\equiv2\pmod4$$,

$$
7^{2026}\equiv7^2\equiv9\pmod{10}.
$$

</div>

A table suggests a cycle; an identity such as $$7^4\equiv1$$ proves the repetition. For longer exponents, repeated squaring is another efficient method.

---

## Inverses and Safe Cancellation

A **modular inverse** of $$a$$ modulo $$m$$ is an integer $$u$$ with $$au\equiv1\pmod m$$. It exists exactly when $$\gcd(a,m)=1$$, by Bézout's identity.

<div class="theorem-box">

**Example.** Solve $$7x\equiv5\pmod{26}$$.

The Euclidean algorithm gives $$1=3\cdot26-11\cdot7$$, so $$7^{-1}\equiv-11\equiv15\pmod{26}$$. Multiplying by the inverse,

$$
x\equiv15\cdot5\equiv23\pmod{26}.
$$

Check: $$7\cdot23=161\equiv5\pmod{26}$$.

</div>

If $$d=\gcd(a,m)$$, the congruence $$ax\equiv b\pmod m$$ has solutions exactly when $$d\mid b$$. In that case, divide the coefficients **and the modulus** by $$d$$, then solve the reduced congruence. There are $$d$$ solution classes modulo the original modulus.

<div class="theorem-box">

**Example.** Solve $$6x\equiv8\pmod{14}$$.

Divide all three numbers by two to get $$3x\equiv4\pmod7$$. Since $$3^{-1}\equiv5\pmod7$$, we have $$x\equiv6\pmod7$$. Modulo $$14$$ this gives $$x\equiv6$$ or $$13$$.

Canceling the six while keeping modulus $$14$$ would not be valid because six has no inverse modulo fourteen.

</div>

---

## Chinese Remainder Theorem

For coprime positive moduli $$m,n$$, any pair of congruences

$$
x\equiv a\pmod m,\qquad x\equiv b\pmod n
$$

has exactly one solution class modulo $$mn$$. A practical way to find it is to write $$x=a+mt$$ and substitute into the other congruence.

<div class="theorem-box">

**Example.** Find the smallest positive integer satisfying $$x\equiv2\pmod5$$ and $$x\equiv3\pmod7$$.

Write $$x=2+5t$$. The second congruence becomes $$5t\equiv1\pmod7$$, so $$t\equiv3\pmod7$$. Therefore $$x\equiv17\pmod{35}$$, and the smallest positive solution is $$17$$.

</div>

For noncoprime moduli, compatibility is required: $$a\equiv b\pmod{\gcd(m,n)}$$. Compatible systems have one class modulo $$\operatorname{lcm}(m,n)$$. For instance, $$x\equiv1\pmod4$$ and $$x\equiv2\pmod6$$ are incompatible because they force opposite parities.

---

## Bases, Digits, and Divisibility Tests

The base-$$b$$ numeral with digits $$d_k\cdots d_0$$ represents $$N=\sum_{i=0}^k d_ib^i$$, where $$0\le d_i<b$$. Modulo $$b-1$$, the base is one, so $$N$$ is congruent to its digit sum. Modulo $$b+1$$, the base is negative one, so $$N$$ is congruent to its alternating digit sum.

<div class="theorem-box">

**Example.** Find the digit $$d$$ for which the decimal number $$47d2$$ is divisible by $$9$$.

The digit sum is $$4+7+d+2=13+d$$. This must be divisible by nine. Since $$0\le d\le9$$, the only possibility is $$13+d=18$$, so $$d=5$$.

</div>

To specify the last two digits in base $$b$$, work modulo $$b^2$$. For decimal endings, that means modulo $$100$$, not modulo $$10$$.

---

## Ruling Out Integer Solutions

A congruence obstruction is enough to prove no integer solution exists. First list possible residues of the powers involved, then compare with the required residue.

<div class="theorem-box">

**Example.** Prove that $$x^2+y^2=4z+3$$ has no integer solutions.

An integer square is $$0$$ or $$1$$ modulo four. The sum of two squares can therefore be $$0,1,$$ or $$2$$, but never $$3$$ modulo four. The right side is always $$3$$ modulo four, giving a contradiction.

</div>

:::strategy
Choose a modulus that simplifies the expression: small powers of two for squares and parity, $$3$$ or $$9$$ for digit sums, and factors of the target divisor for CRT. Never divide a congruence without checking invertibility or reducing the modulus correctly.
:::

## Why Linear Congruences Have Several Solutions

Suppose $$ax\equiv b\pmod m$$ and $$d=\gcd(a,m)$$. The equivalent equation $$ax-b=mt$$ shows that $$d\mid b$$ is necessary. If it holds, divide by $$d$$ to obtain a congruence modulo $$m/d$$ with an invertible coefficient.

A single solution class modulo $$m/d$$ becomes $$d$$ classes modulo $$m$$, separated by $$m/d$$. This explains the solution count and the change of modulus at the same time.

<div class="theorem-box">

**Example.** Find all residue classes modulo sixty satisfying $$18x\equiv24\pmod{60}$$.

The GCD is six, which divides twenty-four. Divide to get $$3x\equiv4\pmod{10}$$. The inverse of three modulo ten is seven, so $$x\equiv8\pmod{10}$$.

The six classes modulo sixty are

$$
8,\ 18,\ 28,\ 38,\ 48,\ 58.
$$

Each differs from the next by ten, not sixty. Substituting the first gives $$18\cdot8-24=120$$, and adding ten to $$x$$ changes the left side by a multiple of sixty.

</div>

If the GCD did not divide the right side, there would be no solution at all. Checking this condition before finding an inverse avoids an impossible calculation.

---

## Constructing CRT Solutions

For pairwise coprime moduli $$m_1,\ldots,m_k$$, let $$M=\prod_i m_i$$ and $$M_i=M/m_i$$. Since $$M_i$$ is invertible modulo $$m_i$$, choose $$u_i$$ with $$M_i u_i\equiv1\pmod{m_i}$$. Then

$$
x=\sum_i a_iM_iu_i
$$

satisfies $$x\equiv a_i\pmod{m_i}$$ for every $$i$$. Each term is zero modulo all the other moduli and has the desired value modulo its own modulus.

Uniqueness modulo $$M$$ follows because the difference of two solutions is divisible by every coprime modulus and hence by their product. This proof explains both parts of CRT rather than treating it as a search rule.

<div class="theorem-box">

**Example.** Solve $$x\equiv1\pmod3$$, $$x\equiv2\pmod4$$, and $$x\equiv3\pmod5$$.

Here $$M=60$$. The complementary products are twenty, fifteen, and twelve, whose inverses modulo their respective moduli are two, three, and three. Therefore

$$
x\equiv1(20)(2)+2(15)(3)+3(12)(3)=238\equiv58\pmod{60}.
$$

The least nonnegative solution is fifty-eight. Direct substitution checks the three remainders.

</div>

For a system with noncoprime moduli, compare the required residues modulo their GCD first. Compatible systems can be merged two at a time, using the least common multiple as the new modulus. The product modulus is correct only in the coprime case.

---

## Large Powers with a Noninvertible Base

Euler's theorem cannot reduce an exponent when the base shares a factor with the modulus. A useful replacement is to split the modulus into coprime prime-power factors. On a factor dividing the base, a sufficiently large power becomes zero. On the remaining factors, ordinary order or Euler reduction is available.

<div class="theorem-box">

**Example.** Find the last three decimal digits of $$12^{100}$$.

Work modulo eight and one hundred twenty-five. The power is zero modulo eight because twelve contains two factors of two and the exponent is large enough.

Modulo $$125$$, the base is coprime and $$\varphi(125)=100$$. Euler gives $$12^{100}\equiv1\pmod{125}$$. Write $$x=1+125t$$. The condition modulo eight becomes $$1+5t\equiv0$$, giving $$t\equiv3\pmod8$$.

Thus $$x\equiv376\pmod{1000}$$, so the final three digits are 376.

</div>

This method avoids the tempting but invalid calculation of reducing the exponent modulo $$\varphi(1000)$$ before checking the base. CRT separates the part where the power dies from the part where it cycles.

---

## Square Roots Modulo Composite Numbers

Modulo a prime, a product is zero only if a factor is zero. Modulo a composite number, zero divisors invalidate that step. Thus $$x^2\equiv1\pmod m$$ need not imply $$x\equiv1$$ or $$-1\pmod m$$.

<div class="theorem-box">

**Example.** Find all solutions to $$x^2\equiv1\pmod{15}$$.

Modulo three, $$x$$ is one or negative one. Modulo five, it is also one or negative one. The four sign combinations are independent and give, by CRT,

$$
x\equiv1,\ 4,\ 11,\ 14\pmod{15}.
$$

For instance, $$4^2-1=15$$, even though neither $$4-1$$ nor $$4+1$$ is divisible by fifteen. The factors split the prime divisors between them.

</div>

For an odd squarefree modulus with $$r$$ distinct prime factors, this argument gives $$2^r$$ square roots of one. Prime powers and powers of two require separate analysis; the squarefree statement should not be extended without checking those cases.

For odd prime powers, the two factors $$x-1,x+1$$ have GCD dividing two. An odd prime cannot divide both, so its entire required power must lie in one factor. This explains why there are only two roots of one modulo an odd prime power.

---

## Numeral Bases and Division Pitfalls

Digit tests come from the base's residue, not from decimal notation itself. In base $$b$$, the value is congruent to the digit sum modulo $$b-1$$ and to the alternating digit sum modulo $$b+1$$. Also, the last $$k$$ digits determine the remainder modulo $$b^k$$.

<div class="theorem-box">

**Example.** The base-$$b$$ numeral with digits 3, 4, 5 is divisible by $$b-1$$. Find every possible base.

The digits require $$b\ge6$$. Since $$345_b=3b^2+4b+5\equiv12\pmod{b-1}$$, the integer $$b-1$$ must divide twelve and be at least five. It is therefore six or twelve, giving $$b=7$$ or $$13$$.

Both bases satisfy the digit restriction and the divisibility condition.

</div>

A repeated-digit number often has a quotient representation, such as $$R_n=(10^n-1)/9$$ for a string of $$n$$ decimal ones. Do not divide a congruence by nine modulo a multiple of three. The quotient is an integer, but nine does not have a modular inverse there.

For example, $$10^3-1$$ is divisible by twenty-seven, but $$R_3=111$$ is not. To prove $$m\mid R_n$$ by clearing this quotient, require $$9m\mid10^n-1$$, not merely $$m\mid10^n-1$$.

---

## Combining Moduli with Descent

A residue obstruction may become visible only after removing forced factors. If three squares sum to a multiple of four, each square must be zero modulo four: with only three terms, a sum of residues zero or one cannot otherwise be zero.

Thus every variable is even, and the equation can be divided by four. Repeating this step strips powers of four before testing modulo eight.

<div class="theorem-box">

**Example.** Prove that no integer of the form $$4^a(8b+7)$$, with $$a,b\ge0$$, can be a sum of three integer squares.

Suppose $$x^2+y^2+z^2=4^a(8b+7)$$. If $$a>0$$, the preceding modulo-four argument forces all variables even. Divide by four and repeat until the right side is $$8b+7$$.

A square modulo eight is zero, one, or four. Three such residues cannot sum to seven: with no four the sum is at most three; with one four the other two give residues zero, one, or two; with at least two fours the remaining residue gives zero, one, or four modulo eight. This is a contradiction.

</div>

The argument proves a necessary obstruction, not the full classification of sums of three squares. Keep that distinction when using a modular proof to infer existence.

:::strategy
For a composite modulus, decide whether CRT will separate incompatible algebraic behaviors. For a quotient, check invertibility before canceling. For a square congruence, list residues or split into prime powers. For an impossibility proof, remove forced common factors before choosing the final modulus.
:::

---

## Lifting a Square Root One Prime Power at a Time

Suppose $$x_0^2\equiv a\pmod p$$. Every lift of this residue modulo $$p^2$$ has the form $$x=x_0+pt$$. Expanding and dividing the known multiple of $$p$$ gives

$$
\frac{x_0^2-a}{p}+2x_0t\equiv0\pmod p.
$$

If $$p\nmid2x_0$$, this is a linear congruence with one solution for $$t$$ modulo $$p$$. Thus each nondegenerate root has a unique lift. This is an elementary instance of Hensel lifting, distinct from LTE's valuation formula.

<div class="theorem-box">

**Example.** Find all square roots of two modulo forty-nine.

Modulo seven, the roots are three and four. Lift three by writing $$x=3+7t$$. Then $$x^2-2=7+42t+49t^2$$, so $$1+6t\equiv0\pmod7$$. This gives $$t=1$$ and root ten.

The negative root is thirty-nine. Both original roots lift uniquely, so the complete list is ten and thirty-nine.

</div>

---

## Fractions in a Prime Modulus

A fraction modulo a prime means multiplication by an inverse. Its denominator must be nonzero modulo that prime. Record excluded values before clearing denominators.

<div class="theorem-box">

**Example.** Solve $$1/(x-1)+1/(x+1)\equiv1\pmod7$$.

Exclude $$x\equiv1,-1$$. Multiplying by the invertible denominator gives $$2x\equiv x^2-1$$, or $$(x-1)^2\equiv2$$. The square roots of two modulo seven are three and negative three, so $$x\equiv4$$ or five.

Neither is excluded, and substitution verifies both. At four, the inverses are five and three, whose sum is one modulo seven. The other candidate works the same way.

</div>

The polynomial obtained by clearing denominators may have a root at an excluded value in other problems. Solving it is only the candidate-generation step; the original modular domain must still be checked.

---

## Degenerate Roots Can Have Several Lifts

The coefficient $$2x_0$$ in a square-root lifting equation must be invertible for uniqueness. If it vanishes modulo the prime, there may be several lifts or none.

For example, $$x^2\equiv0\pmod{p^2}$$ is equivalent to $$p\mid x$$. Its solutions modulo $$p^2$$ are $$0,p,2p,\ldots,(p-1)p$$, giving $$p$$ different lifts of the single zero root modulo $$p$$.

Thus “every root lifts uniquely” requires the nondegeneracy hypothesis. The expansion proves which linear congruence must be solved and makes the exceptional case visible rather than hiding it in a memorized theorem.

---

## Key Equations

:::equations
| Tool | Formula or condition |
| --- | --- |
| Congruence | $$a\equiv b\pmod m\iff m\mid(a-b)$$ |
| Inverse | $$a^{-1}\pmod m$$ exists exactly when $$\gcd(a,m)=1$$ |
| Linear congruence | $$ax\equiv b\pmod m$$ is solvable exactly when $$\gcd(a,m)\mid b$$ |
| Coprime CRT | A pair of classes modulo $$m,n$$ gives one class modulo $$mn$$ |
| Base-$$b$$ digit sum | $$N\equiv\sum d_i\pmod{b-1}$$ |
| Alternating digit sum | $$N\equiv\sum(-1)^id_i\pmod{b+1}$$ |
| Linear solution count | $$\gcd(a,m)$$ classes modulo $$m$$ if $$\gcd(a,m)\mid b$$ |
| Constructive CRT | $$x\equiv\sum_i a_iM_i(M_i^{-1}\bmod m_i)\pmod M$$ for pairwise coprime moduli |
| Composite roots of one | $$2^r$$ roots for an odd squarefree modulus with $$r$$ prime factors |
| Repunit divisibility | $$m\mid(10^n-1)/9\iff9m\mid10^n-1$$ |
| Three-square obstruction | $$4^a(8b+7)$$ is not a sum of three integer squares |
| Root-lifting equation | $$(x_0^2-a)/p+2x_0t\equiv0\pmod p$$ for $$x=x_0+pt$$ |
:::
