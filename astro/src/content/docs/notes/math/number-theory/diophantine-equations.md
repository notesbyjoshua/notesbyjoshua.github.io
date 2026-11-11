---
title: "Diophantine Equations"
status: developing
progress: 68
sidebar:
  order: 3
description: "Competition math notes on integer equations, linear parametrization, factorization, modular restrictions, bounds, and Pythagorean triples."
---

## Integer Solutions and Linear Equations

A **Diophantine equation** asks for integer solutions. Integers are discrete, so factorization, divisibility, and bounds can be more useful than solving the equation over the reals.

The linear equation $$ax+by=c$$ has integer solutions exactly when $$d=\gcd(a,b)$$ divides $$c$$. If $$(x_0,y_0)$$ is one solution, all solutions are

$$
x=x_0+\frac bd t,\qquad y=y_0-\frac ad t,\qquad t\in\mathbb Z.
$$

Subtract two solutions to obtain $$a(x-x_0)=-b(y-y_0)$$; after dividing by the GCD, coprimality forces the stated multiples.

<div class="theorem-box">

**Example.** Find all nonnegative integer solutions of $$7x+11y=100$$.

Modulo seven, $$4y\equiv2$$, so $$y\equiv4\pmod7$$. Write $$y=4+7t$$. Substitution gives $$x=8-11t$$. Nonnegativity requires $$t\ge0$$ from $$y$$ and $$t\le0$$ from $$x$$. Thus the only solution is $$(x,y)=(8,4)$$.

</div>

---

## Factorization and Divisor Pairs

Rearranging an equation into a product converts infinitely many potential inputs into finitely many divisors. Adding a small constant can complete such a product.

<div class="theorem-box">

**Example.** Find all positive integer ordered pairs satisfying $$xy+x+y=23$$.

Add one to both sides:

$$
(x+1)(y+1)=24.
$$

Both factors are at least two. The ordered factor pairs are $$(2,12),(3,8),(4,6)$$ and their reverses. Subtracting one from each coordinate gives

$$
(1,11),(2,7),(3,5),(11,1),(7,2),(5,3).
$$

Every pair gives product $$24$$ after the shift and hence satisfies the original equation.

</div>

For a difference of squares, use $$(x-y)(x+y)=N$$. The two factors have the same parity; otherwise their half-sum and half-difference would not be integers.

<div class="theorem-box">

**Example.** Find positive integers $$x>y$$ satisfying $$x^2-y^2=45$$.

The positive factor pairs with the correct parity are $$(1,45),(3,15),(5,9)$$. For factors $$u=x-y$$ and $$v=x+y$$,

$$
x=\frac{u+v}{2},\qquad y=\frac{v-u}{2}.
$$

This gives $$(23,22),(9,6),(7,2)$$.

</div>

---

## Modular Restrictions and Bounds

Congruences eliminate impossible cases; inequalities can make the surviving casework finite. Neither tool alone must finish the problem.

<div class="theorem-box">

**Example.** Find all positive integer pairs satisfying $$x^2+y^2=25$$.

Positivity gives $$1\le x,y\le4$$. The possible positive squares are $$1,4,9,16$$. The only pair summing to $$25$$ is $$9+16$$, so $$(x,y)=(3,4)$$ or $$(4,3)$$.

A modular check supports the restriction: squares modulo four are zero or one, so exactly one variable is odd. The bound then finishes the search.

</div>

For symmetric equations, assume $$x\le y$$ only after explaining that swapping coordinates recovers the other solutions. For reciprocal equations, ordering variables often turns the equation into an upper bound on the smallest one.

---

## Pythagorean Triples

A positive triple satisfying $$a^2+b^2=c^2$$ is **primitive** if its entries have no common factor greater than one. Every primitive triple, after possibly swapping the legs, has the form

$$
a=m^2-n^2,\qquad b=2mn,\qquad c=m^2+n^2,
$$

where $$m>n\ge1$$, $$\gcd(m,n)=1$$, and $$m,n$$ have opposite parity. Nonprimitive triples are positive integer multiples of primitive ones.

To motivate the parametrization, a primitive triple has one odd and one even leg. Taking the odd leg to be $$a$$ gives

$$
\left(\frac b2\right)^2=\frac{c+a}{2}\cdot\frac{c-a}{2}.
$$

The two factors are coprime positive integers with a square product, so they are squares $$m^2,n^2$$. Adding and subtracting recovers the formulas.

<div class="theorem-box">

**Example.** Find all primitive Pythagorean triples whose hypotenuse is $$25$$.

We need $$m^2+n^2=25$$ with $$m>n>0$$. The only square pair is $$16+9$$, giving $$m=4,n=3$$. They are coprime and of opposite parity, so the triple is

$$
(7,24,25),
$$

with the two legs interchangeable. The triple $$(15,20,25)$$ also has hypotenuse $$25$$ but is not primitive.

</div>

---

## Nonnegative Combinations of Two Integers

For coprime positive integers $$a,b>1$$, the largest integer that cannot be written as $$ax+by$$ with $$x,y\ge0$$ is $$ab-a-b$$. This is the two-denomination **Frobenius** or **Chicken McNugget** theorem.

One way to prove representability above the bound is to choose $$y\in\{0,\ldots,a-1\}$$ so $$by\equiv N\pmod a$$. Such a choice exists because multiplication by $$b$$ permutes residues modulo $$a$$. If $$N>ab-a-b$$, then $$N-by>-a$$; being a multiple of $$a$$, it must be nonnegative. The bound itself is not representable: a representation of $$ab-a-b$$ would imply $$a(x+1)+b(y+1)=ab$$, forcing $$a\mid y+1$$ and making the left side exceed $$ab$$.

<div class="theorem-box">

**Example.** Stamps come in values $$4$$ and $$7$$. Find the largest nonnegative postage value that cannot be formed.

The values are coprime, so the largest gap is $$4\cdot7-4-7=17$$. As a direct check, $$18,19,20,21$$ are representable. Adding a four-cent stamp then proves every larger integer is representable as well, while $$17$$ cannot be formed.

</div>

:::strategy
Start with signs, parity, and an easy modulus. For a linear equation, find one solution and parametrize. For a product, list divisor pairs and retain parity restrictions. For a symmetric equation, order the variables to obtain bounds, then restore all permutations at the end.
:::

## Counting Nonnegative Linear Solutions

The general integer parametrization becomes a finite interval when the variables must be nonnegative. After finding one solution, write

$$
x=x_0+\frac bd t,\qquad y=y_0-\frac ad t,\qquad d=\gcd(a,b).
$$

For positive coefficients $$a,b$$, the first inequality gives a lower bound on $$t$$ and the second an upper bound. Count the integers in the resulting interval, rather than searching a large rectangle of possible $$x,y$$.

<div class="theorem-box">

**Example.** Find the number of nonnegative integer solutions of $$12x+18y=180$$.

Divide by six to get $$2x+3y=30$$. Modulo three, $$x\equiv0$$, so write $$x=3t$$. Then $$y=10-2t$$. Nonnegativity gives $$0\le t\le5$$, producing six solutions.

If positive rather than nonnegative variables were required, the endpoints would need to be checked again: here $$t=0$$ and $$t=5$$ each create a zero coordinate and would be excluded.

</div>

The count of integers in $$L\le t\le U$$ is $$\max(0,\lfloor U\rfloor-\lceil L\rceil+1)$$. The added one includes both endpoints; it is a common source of an off-by-one error in parameter counts.

---

## Ordering Variables in Reciprocal Equations

For a symmetric equation in positive variables, order them to obtain bounds on the smallest one. A reciprocal sum is especially effective because $$x\le y\le z$$ implies $$1/x\ge1/y\ge1/z$$.

<div class="theorem-box">

**Example.** Find all positive integer triples satisfying $$1/x+1/y+1/z=1$$.

First assume $$x\le y\le z$$. Since the sum is at most $$3/x$$, we have $$x\le3$$. The case $$x=1$$ is impossible because the other terms are positive.

If $$x=3$$, both remaining reciprocals are at most one-third and must sum to two-thirds. Hence $$y=z=3$$.

If $$x=2$$, the remaining equation is $$1/y+1/z=1/2$$. Completing a product gives

$$
(y-2)(z-2)=4.
$$

The positive factor pairs in increasing order are $$(1,4)$$ and $$(2,2)$$. They yield $$(y,z)=(3,6)$$ and $$(4,4)$$.

Thus the unordered triples are $$(2,3,6),(2,4,4),(3,3,3)$$. All permutations of these triples satisfy the equation, and the ordering argument proves there are no others.

</div>

The bound on the smallest variable is the step that makes the search finite. Beginning with arbitrary divisor pairs in three variables would obscure this reduction.

For larger reciprocal equations, repeat the idea after fixing the smallest variable. Each remaining sum has fewer unknowns and an updated upper bound on the next smallest denominator.

---

## Divisor Pairs and the Zero Boundary

Difference-of-squares equations require factor pairs of matching parity. If the right side is an odd square, every positive factor pair has matching parity, but the equal pair gives a zero value for the smaller variable.

<div class="theorem-box">

**Example.** Count positive integer pairs $$x>y$$ satisfying $$x^2-y^2=2025$$.

Factor $$2025=3^4 5^2$$, so it has fifteen positive divisors. There are seven unequal positive factor pairs and one equal pair, namely $$45\cdot45$$.

For each unequal pair $$u<v$$, set $$x=(u+v)/2$$ and $$y=(v-u)/2$$. Both are integers because the factors are odd, and $$y>0$$. The equal pair would give $$y=0$$ and is forbidden.

Therefore there are seven pairs.

</div>

This count separates ordering from positivity. If negative variables were allowed or if ordered factor pairs were counted directly, the multiplicities would change. State the required domain before turning a divisor count into a solution count.

---

## Integer-Valued Rational Expressions

When a polynomial quotient must be an integer, divide first. The polynomial part is automatically integral at integer inputs; only a small remainder can obstruct integrality.

<div class="theorem-box">

**Example.** Find every integer $$n\ne-1$$ such that $$(n^2+3n+5)/(n+1)$$ is an integer.

Polynomial division gives

$$
\frac{n^2+3n+5}{n+1}=n+2+\frac3{n+1}.
$$

Thus $$n+1$$ must be a nonzero divisor of three: $$1,-1,3,-3$$. The solutions are

$$
n=0,-2,2,-4.
$$

Every listed value satisfies the original domain restriction, and each makes the remaining fraction an integer.

</div>

For a general integer polynomial $$P$$ and integer $$a$$, division by $$n-a$$ leaves remainder $$P(a)$$. Thus $$n-a\mid P(n)$$ is equivalent to $$n-a\mid P(a)$$ when $$n\ne a$$. If $$P(a)\ne0$$, the resulting finite divisor list can completely solve the problem.

If the remainder is zero, the quotient condition may hold for every allowed integer instead. Check that case rather than assuming a finite search always results.

---

## Pythagorean Triples with a Fixed Perimeter

The primitive parametrization becomes more powerful when combined with a numerical constraint. Every positive Pythagorean triple, after interchanging the legs if necessary, has the form

$$
k(m^2-n^2),\quad 2kmn,\quad k(m^2+n^2),
$$

with $$m>n>0$$, coprime opposite-parity $$m,n$$, and $$k>0$$. Its perimeter is $$2km(m+n)$$.

<div class="theorem-box">

**Example.** Find all integer-sided right triangles with perimeter one hundred twenty.

The perimeter equation is $$km(m+n)=60$$. Since $$k\ge1$$ and $$n\ge1$$, we have $$m(m+1)\le60$$, so $$m\le7$$. The coprimality and parity conditions leave a short list.

For $$m=2,n=1$$, the product $$m(m+n)$$ is six, giving $$k=10$$ and sides $$(30,40,50)$$. For $$m=3,n=2$$ it is fifteen, giving $$k=4$$ and sides $$(20,48,52)$$. For $$m=4,n=1$$ it is twenty, giving $$k=3$$ and sides $$(24,45,51)$$.

The other admissible products not exceeding sixty are twenty-eight, thirty-five, forty-five, and forty-two; none divides sixty. At $$m=7$$, opposite parity forces $$n\ge2$$ and the product already exceeds sixty. Thus the three triangles listed are complete.

</div>

The conditions on $$m,n$$ prevent the same nonprimitive triangle from appearing through several parameter pairs. If those conditions are omitted, a search can still find examples but no longer has a clean uniqueness argument.

---

## Bounding Between Consecutive Powers

Sometimes an expression is close enough to a square that factorization is unnecessary. Locate it strictly between consecutive squares or cubes.

<div class="theorem-box">

**Example.** Prove that $$n^4+n^2+1$$ is not a perfect square for any positive integer $$n$$.

Compare it with the squares of $$n^2$$ and $$n^2+1$$:

$$
(n^2)^2<n^4+n^2+1<(n^2+1)^2.
$$

The second strict inequality follows from $$n^2+1<2n^2+1$$ for $$n>0$$. Since no integer square lies strictly between consecutive integer squares, the expression cannot be one.

</div>

A successful bound must use consecutive integer powers. Showing an expression lies between two distant squares leaves other squares available and proves nothing. Also check strictness at the smallest admissible input; a boundary value can be the only exceptional solution.

:::strategy
For a classification, make the search finite and explain why it is complete. Order symmetric variables to get bounds, divide rational expressions to get fixed remainders, and use a parametrization only with its parity and coprimality conditions. Finish by restoring permutations and checking the original domain.
:::

---

## Square Triangular Numbers and Pell Equations

A triangular number $$n(n+1)/2$$ is a square precisely when

$$
(2n+1)^2-8m^2=1.
$$

Completing the square converts the mixed product into a Pell equation. The variable change is reversible: a solution with odd positive $$x=2n+1$$ and nonnegative $$m$$ gives the original triangular-square solution.

The Pell classification for $$x^2-2y^2=1$$ applies with $$y=2m$$. Its generated solutions have odd $$x$$ and even $$y$$, so they produce all nonnegative triangular-square pairs. In the original variables, the update is

$$
n'=3n+4m+1,\qquad m'=2n+3m+1.
$$

Starting from $$(n,m)=(1,1)$$ gives $$(8,6),(49,35),(288,204)$$. Thus thirty-six and twelve hundred twenty-five are triangular squares, with indices eight and forty-nine.

The equation transformation alone constructs candidates. The completeness argument comes from the Pell descent, explained on the advanced Diophantine page. State that link when claiming an entire infinite family.

---

## Prime Differences of Cubes

A prime right side makes a factorization particularly restrictive, since its two positive factors must be one and the prime.

<div class="theorem-box">

**Example.** Find all positive integers $$x>y$$ satisfying $$x^3-y^3=61$$.

Factor:

$$
(x-y)(x^2+xy+y^2)=61.
$$

The second factor exceeds one, so primality forces $$x-y=1$$. Put $$x=y+1$$. Then $$3y^2+3y+1=61$$, giving $$y^2+y-20=0$$. The positive root is four, so $$(x,y)=(5,4)$$.

The other quadratic root is negative five and violates the specified domain. The positive pair verifies the original equation.

</div>

This method generalizes to differences of higher powers, but the remaining factor may be difficult to solve. The prime factorization reduces the problem; it does not automatically finish every exponent case. Retain the original positivity and ordering conditions throughout the reduction.

---

## Reduce to Primitive Variables First

A homogeneous equation often allows a common factor to be removed before any modular work.

<div class="theorem-box">

**Example.** Prove $$x^2+y^2=3xy$$ has no positive integer solutions.

Write $$x=du,y=dv$$ with $$\gcd(u,v)=1$$ and cancel $$d^2$$. The equation implies $$u\mid v^2$$, so coprimality forces $$u=1$$. Similarly $$v=1$$. Substitution would give $$2=3$$, a contradiction.

</div>

The primitive reduction turns divisibility of a square into a forced unit. This elementary argument is shorter than a descent or a quadratic-discriminant search; try removing the GCD before choosing a more advanced method.

---

## Key Equations

:::equations
| Method | Formula and conditions |
| --- | --- |
| Linear solvability | $$ax+by=c$$ has integer solutions iff $$\gcd(a,b)\mid c$$ |
| Linear parametrization | $$x=x_0+(b/d)t,\ y=y_0-(a/d)t$$, $$d=\gcd(a,b)$$ |
| Complete a product | $$xy+x+y+1=(x+1)(y+1)$$ |
| Difference of squares | $$x^2-y^2=(x-y)(x+y)$$; factors have the same parity |
| Primitive right triangles | $$(m^2-n^2,2mn,m^2+n^2)$$ with coprime opposite-parity $$m>n>0$$ |
| Two coprime denominations | Largest unattainable value is $$ab-a-b$$ for $$a,b>1$$ |
| Linear parameter interval | Number of integer parameters in $$[L,U]$$ is $$\max(0,\lfloor U\rfloor-\lceil L\rceil+1)$$ |
| Reciprocal pair | $$1/y+1/z=1/a\iff(y-a)(z-a)=a^2$$ for positive denominators |
| Pythagorean perimeter | $$P=2km(m+n)$$ with primitive parameter conditions |
| Polynomial remainder divisibility | $$n-a\mid P(n)\iff n-a\mid P(a)$$ for integer-coefficient $$P$$ and $$n\ne a$$ |
| Triangular square | $$n(n+1)/2=m^2\iff(2n+1)^2-8m^2=1$$ |
| Triangular-square update | $$(n,m)\mapsto(3n+4m+1,2n+3m+1)$$ |
:::
