---
title: "Divisibility and Prime Factorization"
status: developing
progress: 68
sidebar:
  order: 1
description: "Competition math notes on prime factorization, GCD, LCM, Bézout's identity, divisors, and perfect powers with worked number theory examples."
---

## Divisibility and Prime Factorization

For integers $$a\ne0$$ and $$b$$, the notation $$a\mid b$$ means $$b=ak$$ for some integer $$k$$. If $$a$$ divides both $$b$$ and $$c$$, it divides every integer combination $$ub+vc$$. This lets us replace large expressions by smaller differences.

Every integer greater than one has a unique factorization into primes, apart from the order of the factors. Divisibility can therefore be checked one prime at a time: $$a\mid b$$ for positive integers exactly when every prime exponent in $$a$$ is at most the corresponding exponent in $$b$$.

<div class="theorem-box">

**Example.** A positive integer $$n$$ satisfies $$n\mid3n+14$$. Find all possible $$n$$.

Because $$n\mid3n$$, subtracting gives $$n\mid14$$. Thus $$n\in\{1,2,7,14\}$$. Conversely, every positive divisor of $$14$$ divides $$3n+14$$, so all four values work.

</div>

---

## GCD, LCM, and the Euclidean Algorithm

The **greatest common divisor** $$\gcd(a,b)$$ takes the smaller exponent of each prime in positive $$a,b$$. The **least common multiple** $$\operatorname{lcm}(a,b)$$ takes the larger. Thus

$$
\gcd(a,b)\operatorname{lcm}(a,b)=ab.
$$

Factoring is not always the fastest way to find a GCD. The Euclidean algorithm repeatedly uses

$$
\gcd(a,b)=\gcd(b,a-qb).
$$

The common divisors stay the same when a multiple of one number is subtracted from the other.

<div class="theorem-box">

**Example.** Find $$\gcd(252,198)$$ and express it as an integer combination of the two numbers.

The divisions are

$$
252=198+54,\quad198=3\cdot54+36,\quad54=36+18.
$$

The last nonzero remainder is $$18$$. Substituting backward,

$$
18=54-36=4\cdot54-198=4\cdot252-5\cdot198.
$$

Thus the GCD is $$18$$, with the displayed integer combination.

</div>

**Bézout's identity** says that such a combination always exists:

$$
au+bv=\gcd(a,b)
$$

for some integers $$u,v$$. In particular, if $$\gcd(a,b)=1$$ and $$a\mid bc$$, then $$a\mid c$$: multiply a Bézout combination of $$a,b$$ by $$c$$. This is the correct cancellation rule for divisibility.

---

## Counting and Summing Divisors

If $$n=p_1^{e_1}\cdots p_r^{e_r}$$, each positive divisor chooses its exponent of $$p_i$$ independently from $$0,1,\ldots,e_i$$. Therefore

$$
\tau(n)=\prod_{i=1}^r(e_i+1).
$$

Multiplying the possible prime-power contributions instead of just counting them gives the divisor sum:

$$
\sigma(n)=\prod_{i=1}^r(1+p_i+\cdots+p_i^{e_i})
=\prod_{i=1}^r\frac{p_i^{e_i+1}-1}{p_i-1}.
$$

<div class="theorem-box">

**Example.** Find the number and sum of the positive divisors of $$360$$.

Factor $$360=2^3\cdot3^2\cdot5$$. Thus

$$
\tau(360)=(3+1)(2+1)(1+1)=24,
$$

$$
\sigma(360)=(1+2+4+8)(1+3+9)(1+5)=15\cdot13\cdot6=1170.
$$

</div>

Divisors also pair as $$d$$ and $$n/d$$. A positive integer has an odd number of divisors exactly when it is a square, because only a square has a divisor paired with itself.

---

## Perfect Powers and Coprimality

A positive integer is a perfect $$k$$th power exactly when all its prime exponents are divisible by $$k$$. This turns questions about squares and cubes into remainder calculations on exponents.

<div class="theorem-box">

**Example.** Find the smallest positive integer $$m$$ for which $$360m$$ is a square.

The exponents in $$360=2^3\cdot3^2\cdot5$$ must all become even. Add one factor of $$2$$ and one factor of $$5$$, giving $$m=10$$ and $$360m=3600=60^2$$. Any successful $$m$$ must contain both of those factors, so $$10$$ is smallest.

</div>

If coprime positive integers $$a,b$$ have a square product, each is a square: no prime is shared, so an odd exponent in one cannot be repaired by the other. The same statement holds for any perfect $$k$$th power.

<div class="theorem-box">

**Example.** Find all positive integers $$n$$ for which $$n(n+1)$$ is a square.

Consecutive integers are coprime, so both $$n=a^2$$ and $$n+1=b^2$$ would have to be squares. Then

$$
(b-a)(b+a)=1.
$$

The only nonnegative square solution is $$a=0,b=1$$, which gives $$n=0$$ and violates positivity. Thus no positive $$n$$ works.

</div>

:::strategy
For divisibility, subtract multiples to reduce the expression. For a product that is a perfect power, check the GCD of its factors before separating them. For a smallest-number problem, fill only the missing prime exponents and justify why each is forced.
:::

## GCDs of Algebraic Expressions

The Euclidean algorithm applies to expressions as well as numerical inputs. The useful move is still subtracting an integer multiple, chosen so that the largest terms cancel. A complicated GCD can collapse to a small constant or a familiar expression.

For positive $$m,n$$ and integer $$a>1$$,

$$
\gcd(a^m-1,a^n-1)=a^{\gcd(m,n)}-1.
$$

If $$m>n$$, subtract $$a^{m-n}(a^n-1)$$ from $$a^m-1$$ to replace the first exponent by $$m-n$$. The common divisors are unchanged. Repeating the subtraction follows the Euclidean algorithm on the exponents, ending at their GCD.

<div class="theorem-box">

**Example.** Find $$\gcd(2^{84}-1,2^{60}-1)$$ without evaluating either large number.

The exponent GCD is twelve, so the expression equals $$2^{12}-1=4095$$. The exponent identity is the reason reducing the problem this way is valid; simply taking the GCD of exponents inside an arbitrary expression would not be justified.

</div>

A smaller algebraic GCD often controls how prime powers can split across factors. For instance,

$$
\gcd(n-1,n+1)=\gcd(n-1,2).
$$

Thus the two factors of $$n^2-1$$ are coprime when $$n$$ is even and share only a factor of two when $$n$$ is odd. This is often the decisive observation in perfect-power equations.

---

## Divisors with Additional Restrictions

The divisor-count formula comes from choosing prime exponents independently. Additional conditions simply alter the allowed exponent choices.

If $$N=\prod p_i^{e_i}$$, the number of square divisors is $$\prod_i(\lfloor e_i/2\rfloor+1)$$, since only even exponents are permitted. More generally, perfect $$k$$th-power divisors use exponents $$0,k,2k,\ldots$$. For divisors divisible by $$M=\prod p_i^{f_i}$$ with $$M\mid N$$, the available exponent range is $$f_i,\ldots,e_i$$, giving $$\prod_i(e_i-f_i+1)$$.

<div class="theorem-box">

**Example.** Find the number of positive divisors of $$360$$ that are squares, and the number divisible by twelve.

Use $$360=2^3 3^2 5$$. A square divisor chooses the exponent of two from $$\{0,2\}$$, of three from $$\{0,2\}$$, and of five only as zero. There are four square divisors.

For a divisor divisible by $$12=2^2 3$$, the exponents have respectively two, two, and two choices. Hence there are eight such divisors.

</div>

For coprime factor pairs $$ab=N$$, every prime power of $$N$$ must go entirely into one factor or the other. If $$N$$ has $$r$$ distinct prime divisors, there are $$2^r$$ ordered coprime factorizations. Allowing a prime power to split between the two factors would violate coprimality.

---

## Least Common Multiples of Long Lists

To make an integer divisible by every number in a list, retain the largest required exponent of each prime. In particular,

$$
\operatorname{lcm}(1,2,\ldots,n)=\prod_{p\le n}p^{e_p},
$$

where $$p^{e_p}$$ is the largest power of $$p$$ not exceeding $$n$$. This is different from $$n!$$, which contains many repeated factors that are unnecessary for the divisibility requirement.

If a power of an unknown number must satisfy the divisibility, divide the required exponents by that power and round up.

<div class="theorem-box">

**Example.** Find the smallest positive integer $$m$$ such that $$m^2$$ is divisible by every integer from one through twelve.

The required least common multiple is $$2^3 3^2 5\cdot7\cdot11$$. Therefore $$m$$ needs prime exponents at least $$\lceil3/2\rceil,\lceil2/2\rceil,1,1,1$$. The smallest possibility is

$$
m=2^2\cdot3\cdot5\cdot7\cdot11=4620.
$$

Each required exponent is forced, so omitting any factor would fail. Adding any other prime would only increase the number.

</div>

This “required exponent, then round up” method also handles a smallest multiplier making a number a cube or a smallest denominator clearing several rational expressions.

---

## The Smallest Number with a Given Divisor Count

Suppose $$N$$ has exactly $$d$$ positive divisors. Its exponents satisfy $$\prod_i(e_i+1)=d$$. To minimize $$N$$, use the smallest available primes and place the largest exponents on the smallest primes.

The ordering follows from an exchange: if $$p<q$$ and $$a>b$$, then $$p^aq^b<p^bq^a$$. Thus a minimizing factorization has nonincreasing exponents attached to increasing primes.

<div class="theorem-box">

**Example.** Find the smallest positive integer with exactly twenty-four divisors.

List the unordered factorizations of twenty-four into integers greater than one. They give exponent patterns

$$
(23),\ (11,1),\ (7,2),\ (5,3),\ (5,1,1),\ (3,2,1),\ (2,1,1,1).
$$

Using the smallest primes in decreasing exponent order gives, respectively,

$$
2^{23},\ 6144,\ 1152,\ 864,\ 480,\ 360,\ 420.
$$

The smallest is $$360=2^3 3^2 5$$. Its divisor count is $$4\cdot3\cdot2=24$$. The complete factorization list and exchange argument prove that a smaller integer cannot work.

</div>

The divisor-count equation is multiplicative, so treating twenty-four as a sum of exponent contributions would be incorrect. Each new prime adds a new factor to the divisor count.

---

## Divisor Sums and Perfect Numbers

A positive integer is **perfect** when the sum of its proper positive divisors equals the number itself. Equivalently, $$\sigma(N)=2N$$. The divisor-sum formula lets us verify such conditions without listing every divisor.

If $$2^p-1$$ is prime, then

$$
N=2^{p-1}(2^p-1)
$$

is perfect. The two displayed factors are coprime, so their divisor sums multiply:

$$
\sigma(N)=(1+2+\cdots+2^{p-1})(1+(2^p-1))
=(2^p-1)2^p=2N.
$$

For $$p=3$$ this gives twenty-eight, and for $$p=5$$ it gives four hundred ninety-six. The prime condition matters; a composite second factor has additional divisors and changes the sum.

This is a construction of perfect numbers, not a proof that every number of the displayed shape works. A formula containing a primality hypothesis must keep that hypothesis when used in examples.

---

## Factorials, Coprimality, and New Prime Divisors

For $$n\ge2$$, no prime at most $$n$$ divides $$n!+1$$, because it divides $$n!$$ and cannot also divide the difference one. Therefore every prime divisor of $$n!+1$$ exceeds $$n$$. This proves there are arbitrarily large primes, but does not prove $$n!+1$$ itself is prime.

<div class="theorem-box">

**Example.** Prove that $$n!+1$$ and $$(n+1)!+1$$ are coprime for every positive integer $$n$$.

Subtract $$(n+1)$$ times the first expression from the second. Their common divisors must divide $$-n$$, so

$$
\gcd(n!+1,(n+1)!+1)=\gcd(n!+1,n).
$$

Since $$n$$ divides $$n!$$, any common divisor of $$n!+1$$ and $$n$$ divides one. The GCD is therefore one.

</div>

The proof combines algebraic subtraction with a simple divisibility fact. This is often more effective than trying to factor expressions involving factorials.

:::strategy
For a GCD, subtract expressions before factoring large numbers. For constrained divisors, translate every condition into allowed prime exponents. For a least-number problem, justify both which primes occur and how their exponents are ordered. Keep construction arguments separate from classification claims.
:::

---

## Coprimality of a Sum and a Product

If positive integers $$a,b$$ are coprime, then $$a+b$$ is coprime to $$ab$$. A prime dividing both would divide one of $$a,b$$ and then, from the sum, the other, contradicting coprimality.

This lets us cancel an entire product in a divisibility condition even when the numbers themselves are unknown.

<div class="theorem-box">

**Example.** Coprime positive integers $$a,b$$ satisfy $$a+b\mid a^2+b^2$$. Find all possible pairs.

Subtract the divisible expression $$(a+b)^2$$ to obtain $$a+b\mid2ab$$. Since $$\gcd(a+b,ab)=1$$, the sum divides two. Positivity gives $$a+b\ge2$$, so the sum is exactly two and $$a=b=1$$.

The pair satisfies both the coprimality and divisibility requirements. Without coprimality, many scaled examples would remain, so that hypothesis is doing essential work.

</div>

---

## Fibonacci GCDs by the Euclidean Algorithm

The Fibonacci numbers satisfy

$$
\gcd(F_m,F_n)=F_{\gcd(m,n)}.
$$

The proof combines two simple recurrence facts. First, consecutive Fibonacci numbers are coprime, since applying the recurrence repeatedly reduces their GCD to $$\gcd(F_1,F_0)=1$$.

Second, the addition identity

$$
F_{n+r}=F_{n+1}F_r+F_nF_{r-1}
$$

follows by induction on $$r\ge1$$. Reducing it modulo $$F_n$$ and using the coprimality of $$F_{n+1},F_n$$ gives

$$
\gcd(F_{n+r},F_n)=\gcd(F_r,F_n).
$$

Thus the Euclidean algorithm on the indices is mirrored by a Euclidean algorithm on the Fibonacci values. The endpoint with equal indices or a zero index supplies the claimed formula.

For example, $$\gcd(F_{84},F_{60})=F_{12}=144$$. The two original Fibonacci numbers can be very large, but their common divisor is controlled by the much smaller index calculation.

This is a useful general contest habit: when a sequence has an addition identity, check whether it reduces a GCD just as exponent subtraction did for $$a^n-1$$. The recurrence may provide a divisibility structure that is invisible from the first few numerical terms.

---

## Reconstructing Numbers from Their GCD and LCM

If positive integers have GCD $$g$$, write them as $$a=gx,b=gy$$ with $$\gcd(x,y)=1$$. Their LCM is then $$gxy$$. Thus prescribing LCM $$L$$ reduces the problem to coprime factor pairs $$xy=L/g$$.

This requires $$g\mid L$$. When it holds, each full prime power of $$L/g$$ must be assigned entirely to one of $$x,y$$. The condition is stronger than simply asking for any factor pair.

<div class="theorem-box">

**Example.** Positive integers $$a,b$$ have GCD twelve and LCM four hundred twenty. Find the smallest possible value of $$a+b$$.

Write $$a=12x,b=12y$$. Then $$xy=35$$ and $$x,y$$ are coprime. Up to order, the possibilities are $$(1,35)$$ and $$(5,7)$$. Their corresponding sums are $$432$$ and $$144$$.

The minimum is therefore 144, attained by sixty and eighty-four. Checking gives GCD twelve and LCM four hundred twenty, so the candidate meets both requirements.

</div>

A fixed product generally favors factors near its square root when minimizing a sum, but the coprimality condition restricts which near factors are admissible. Listing the coprime factor pairs supplies the necessary completeness argument instead of relying only on a continuous AM–GM bound.

---

## Key Equations

:::equations
| Tool | Formula |
| --- | --- |
| Euclidean algorithm | $$\gcd(a,b)=\gcd(b,a-qb)$$ |
| Bézout | $$au+bv=\gcd(a,b)$$ for some integers $$u,v$$ |
| GCD–LCM | $$\gcd(a,b)\operatorname{lcm}(a,b)=ab$$ for $$a,b>0$$ |
| Divisor count | $$\tau(n)=\prod(e_i+1)$$ |
| Divisor sum | $$\sigma(n)=\prod(1+p_i+\cdots+p_i^{e_i})$$ |
| Perfect $$k$$th power | Each exponent $$e_i$$ is divisible by $$k$$ |
| Exponential GCD | $$\gcd(a^m-1,a^n-1)=a^{\gcd(m,n)}-1$$ for $$a>1,m,n>0$$ |
| Perfect-power divisors | $$\prod_i(\lfloor e_i/k\rfloor+1)$$ perfect $$k$$th-power divisors of $$\prod p_i^{e_i}$$ |
| Divisors containing $$M$$ | $$\prod_i(e_i-f_i+1)$$ if $$M=\prod p_i^{f_i}\mid N=\prod p_i^{e_i}$$ |
| Coprime ordered factor pairs | $$2^{\omega(N)}$$, with $$\omega(N)$$ the number of distinct prime divisors |
| Perfect-number test | $$\sigma(N)=2N$$ |
| Coprime sum and product | $$\gcd(a,b)=1\Longrightarrow\gcd(a+b,ab)=1$$ |
| Fibonacci GCD | $$\gcd(F_m,F_n)=F_{\gcd(m,n)}$$ |
| GCD–LCM reconstruction | $$a=gx,b=gy,\ \gcd(x,y)=1,\ xy=L/g$$ |
:::
