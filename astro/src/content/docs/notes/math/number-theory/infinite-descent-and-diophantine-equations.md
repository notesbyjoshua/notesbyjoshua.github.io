---
title: "Advanced Diophantine Equations"
status: developing
progress: 68
sidebar:
  order: 7
description: "Competition math notes on infinite descent, minimal solutions, Vieta jumping, and Pell-type constructions with complete worked arguments."
---

## Minimal Solutions and Infinite Descent

**Infinite descent** proves that a certain positive integer solution cannot exist by showing that any such solution produces a smaller one. Choose a size measure that is a positive integer, such as the largest variable or the sum of the variables. The existence of a smallest solution then contradicts the construction of a smaller one.

A descent needs three checks: the transformed values are integers, they remain in the required domain, and the chosen measure strictly decreases. An algebraic transformation without those checks does not establish a contradiction.

<div class="theorem-box">

**Example.** Prove that $$x^2=2y^2$$ has no solution in positive integers.

Assume a solution exists and choose one with $$y$$ as small as possible. The equation makes $$x^2$$ even, hence $$x$$ even. Write $$x=2u$$; then $$y^2=2u^2$$, so $$y=2v$$ is even as well.

Substitution gives $$u^2=2v^2$$. This is another positive integer solution, but $$v=y/2<y$$. It contradicts the minimal choice of $$y$$, so there is no positive solution.

</div>

---

## Congruences That Force a Common Factor

A modular obstruction may not rule out a solution immediately. Instead, it may force every variable to contain the same prime factor, which gives a descent after division.

<div class="theorem-box">

**Example.** Find all integer solutions of $$x^2+y^2=3z^2$$.

Modulo three, squares are zero or one. The only way for $$x^2+y^2$$ to be zero is for both squares to be zero, so $$3\mid x$$ and $$3\mid y$$. Write $$x=3u$$, $$y=3v$$. Then

$$
3(u^2+v^2)=z^2,
$$

so $$3\mid z$$ as well. Writing $$z=3w$$ recovers

$$
u^2+v^2=3w^2.
$$

If a nonzero solution existed, choose one minimizing the positive integer $$\lvert x\rvert+\lvert y\rvert+\lvert z\rvert$$. Dividing all three variables by three produces a nonzero solution with a smaller measure, a contradiction. Therefore the only solution is $$(0,0,0)$$.

</div>

This combines congruences with scaling. The modulus identifies a forced common factor; homogeneity ensures that dividing it out preserves the equation.

---

## Vieta Jumping

Suppose an integer equation is quadratic in one variable:

$$
y^2-B(x)y+C(x)=0.
$$

If $$y$$ is an integer root and $$B(x)$$ is integer, the other root

$$
y'=B(x)-y
$$

is also integer. Vieta's product formula also gives $$yy'=C(x)$$, which can help prove positivity or a size bound. Replacing $$y$$ by $$y'$$ is called **Vieta jumping**.

<div class="theorem-box">

**Example.** Show that every positive integer solution of $$x^2+y^2+1=3xy$$ can be reduced to $$(1,1)$$ by swaps and Vieta jumps.

The equation is symmetric, so order the variables as $$x\le y$$. If $$x=y$$, then $$x^2=1$$, giving $$(1,1)$$. If $$x=1$$, the equation factors as

$$
y^2-3y+2=(y-1)(y-2)=0.
$$

The only additional pair is $$(1,2)$$, which jumps to $$(1,1)$$.

Now suppose $$2\le x<y$$. Viewed as a quadratic in $$y$$, the equation has other root

$$
y'=3x-y=\frac{x^2+1}{y}.
$$

The first expression proves integrality, and the second proves positivity. Because $$y\ge x+1$$,

$$
y'\le\frac{x^2+1}{x+1}<x
$$

for $$x>1$$. Thus $$(y',x)$$ is a positive integer solution whose largest coordinate is smaller than $$y$$. Repeating must terminate, and only the base case $$(1,1)$$ remains.

</div>

The positivity proof matters: the other root of an integer quadratic need not be positive in a different problem.

---

## Reversing a Descent to Find All Solutions

When the transformation is reversible, descent can classify solutions as well as prove impossibility. For the preceding equation, the forward step is

$$
(x,y)\longmapsto(y,3y-x).
$$

Starting from $$(1,1)$$ gives

$$
(1,1),\ (1,2),\ (2,5),\ (5,13),\ (13,34),\ldots.
$$

The new pair satisfies the equation by the same quadratic-root relation. The descent proves that there are no other positive solutions apart from swapping coordinates: every ordered pair with $$x<y$$ reduces to a unique smaller ordered pair, and reversing those steps returns to this chain.

<div class="theorem-box">

**Example.** Find all positive solutions of $$x^2+y^2+1=3xy$$ with $$\max(x,y)\le20$$.

The chain gives $$(1,1),(1,2),(2,5),(5,13)$$ before the next pair has largest coordinate $$34$$. Include the reverses of the unequal pairs:

$$
(1,1),(1,2),(2,1),(2,5),(5,2),(5,13),(13,5).
$$

The reduction argument proves this list is complete.

</div>

---

## Pell-Type Constructions

A **Pell equation** has the form $$x^2-Dy^2=1$$ for a positive nonsquare integer $$D$$. Multiplication of expressions $$x+y\sqrt D$$ preserves the relation because their product with the conjugate is one.

<div class="theorem-box">

**Example.** Construct infinitely many positive integer solutions to $$x^2-2y^2=1$$.

Begin with $$3^2-2\cdot2^2=1$$. If $$(x,y)$$ is a positive solution, multiply by $$3+2\sqrt2$$:

$$
(x+y\sqrt2)(3+2\sqrt2)=(3x+4y)+(2x+3y)\sqrt2.
$$

Thus $$(3x+4y,2x+3y)$$ is another positive integer solution. Both coordinates increase, so the repeated construction produces infinitely many distinct solutions, beginning $$(3,2),(17,12),(99,70)$$.

This proves an infinite family exists. Classifying every solution would require an additional completeness argument.

</div>

:::strategy
Try congruences and factorization before descent. If every variable gains a common factor, divide and measure the decrease. If the equation is quadratic in one variable, inspect the other root and prove it stays positive. For a “find all” problem, reverse the descent and verify every generated family.
:::

## A Descent Involving Triangle Area

A useful descent does not always produce smaller values of the original variables directly. It may reinterpret a solution as another mathematical object whose size can decrease. Integer right triangles provide a classical example.

<div class="theorem-box">

**Example.** Prove that no integer-sided right triangle has area equal to a positive integer square.

Assume such a triangle exists and choose one with smallest hypotenuse. It must be primitive: dividing a common factor from all sides divides the area by its square, preserving the square-area property and decreasing the hypotenuse.

Write its legs as $$m^2-n^2$$ and $$2mn$$, with coprime opposite-parity $$m>n>0$$. The area condition says

$$
mn(m+n)(m-n)
$$

is a square. The four positive factors are pairwise coprime. For example, $$\gcd(m+n,m-n)$$ divides two and both factors are odd, so their GCD is one. Hence each factor is a square. Write

$$
m=u^2,\quad n=v^2,\quad m+n=w^2,\quad m-n=t^2.
$$

The integers $$w,t$$ are odd. Thus $$w^2-t^2=2v^2$$ is divisible by eight, forcing $$v$$ even. Set

$$
r=\frac{w+t}{2},\qquad s=\frac{w-t}{2}.
$$

These are positive integers, and

$$
r^2+s^2=\frac{w^2+t^2}{2}=m=u^2.
$$

They form a new integer right triangle with area

$$
\frac{rs}{2}=\frac{w^2-t^2}{8}=\frac{v^2}{4},
$$

again a positive integer square. Its hypotenuse is $$u=\sqrt m$$, strictly smaller than the original $$m^2+n^2$$. This contradicts minimality.

</div>

Notice the separate roles of the hypotheses. Primitivity makes the factors coprime, the square-product condition makes each a square, parity makes the new coordinates integral, and the hypotenuse comparison completes the descent. Removing any one of those checks would leave a gap.

---

## A Harder Vieta-Jumping Classification

Some quotient problems hide a quadratic equation after introducing an integer parameter. Fix the quotient, preserve it under the jump, and descend among solutions with that same value.

<div class="theorem-box">

**Example.** Positive integers $$a,b$$ satisfy $$ab+1\mid a^2+b^2$$. Prove that the quotient is a perfect square.

Let $$k=(a^2+b^2)/(ab+1)$$. Suppose a nonsquare value occurs, and choose a solution with minimal $$a+b$$ for that fixed $$k$$. By symmetry assume $$a\ge b$$.

The value $$k=1$$ is already square. If $$k=2$$, the equation becomes $$(a-b)^2=2$$, impossible. Hence a nonsquare candidate has $$k\ge3$$.

Viewed as a quadratic in $$a$$, the equation is

$$
a^2-kba+(b^2-k)=0.
$$

The other root is the integer $$a'=kb-a$$, and $$aa'=b^2-k$$.

First prove $$a'\ge0$$. If $$a'\le-1$$, then $$a\ge kb+1$$. But the original equation gives

$$
a(a-kb)=k-b^2\le k-1,
$$

while the left side is at least $$a\ge kb+1\ge k+1$$, a contradiction.

If $$a'=0$$, the product relation gives $$k=b^2$$, contrary to the nonsquare assumption. Thus $$a'>0$$. Also,

$$
a'=\frac{b^2-k}{a}<b,
$$

since $$a\ge b$$ and $$k>0$$.

The pair $$(b,a')$$ is therefore a positive integer solution with the same quotient $$k$$ and smaller sum than $$(a,b)$$. This contradicts the minimal choice. Every possible quotient must be a square.

</div>

The positivity argument is the difficult part. Integrality follows immediately from Vieta, but a negative other root would not be an admissible smaller solution. In many olympiad problems, most of the real work lies in proving that the jump stays inside the domain.

---

## Classifying All Solutions of a Pell Equation

Multiplying by $$3+2\sqrt2$$ constructs solutions of $$x^2-2y^2=1$$. To prove it constructs every positive solution, reverse the multiplication and show it decreases a coordinate.

For a solution with $$y>2$$, define

$$
x'=3x-4y,\qquad y'=3y-2x.
$$

The norm identity preserves $$x'^2-2y'^2=1$$. Since $$x^2/y^2=2+1/y^2$$, we have

$$
\frac43<\sqrt2<\frac xy<\frac32.
$$

Hence both new coordinates are positive. Also $$x>y$$ gives $$y'=3y-2x<y$$. Thus the positive integer $$y$$ decreases.

There is no solution with $$y=1$$, and $$y=2$$ gives $$x=3$$. That solution reverses to $$(1,0)$$. Repeating the descent proves that every nonnegative solution with $$x>0$$ is reached by reversing these steps:

$$
x+y\sqrt2=(3+2\sqrt2)^n,\qquad n\ge0.
$$

The classification now has both directions: powers of the fundamental unit produce solutions, and descent proves every solution belongs to that family.

<div class="theorem-box">

**Example.** Find all positive solutions to $$x^2-2y^2=1$$ with $$y<100$$.

The classified sequence begins

$$
(3,2),\ (17,12),\ (99,70),\ (577,408).
$$

The update increases both positive coordinates, so once the second coordinate reaches 408 it can never return below one hundred. The complete list is the first three pairs.

</div>

For a different nonsquare $$D$$, the smallest positive Pell solution may be much larger than expected. Do not assume a short search has found the fundamental one; a completeness method such as continued fractions is needed in general.

---

## Rational Parametrization as an Alternative to Descent

Not every infinite family needs a descent. An equation with a known rational point may admit a rational parametrization by lines through that point.

For the unit circle $$x^2+y^2=1$$, draw a line of rational slope $$t$$ through $$(-1,0)$$:

$$
y=t(x+1).
$$

Substitute into the circle equation. One intersection is the known point. Factoring that root gives the other as

$$
x=\frac{1-t^2}{1+t^2},\qquad y=\frac{2t}{1+t^2}.
$$

Every rational $$t$$ gives a rational point, and every rational point other than $$(-1,0)$$ has the rational slope $$t=y/(x+1)$$. The excluded point must be listed separately to make the classification complete.

Taking $$t=n/m$$ and clearing denominators produces the Pythagorean expressions $$m^2-n^2,2mn,m^2+n^2$$. The usual parity and coprimality conditions then identify primitive integer triples.

This connects geometric parametrization with number theory. The construction explains why a formula has its particular shape rather than presenting it as a pattern to memorize.

---

## Choosing the Right Descent Measure

A transformed solution can decrease one coordinate while increasing another. Therefore “the numbers get smaller” is not a valid measure unless the proof specifies which quantity is controlled.

Possible measures include the largest coordinate, the sum, the hypotenuse of an associated triangle, or a lexicographically ordered pair. The measure must belong to a set with no infinite strictly decreasing chain, such as positive integers or nonnegative integer pairs in a justified lexicographic order.

When a boundary case gives a known solution instead of a contradiction, stop there and reverse the transformations. This is how a descent becomes a classification. When no boundary case is admissible, the same mechanism proves impossibility.

:::checklist
- Fix any parameter that the transformation must preserve.
- Prove the new coordinates are integers.
- Check positivity, parity, coprimality, and nonzero denominators where required.
- Verify the original equation for the transformed solution.
- Identify one strictly decreasing integer measure.
- Handle the terminal cases and reverse the construction when classifying solutions.
:::

The best descent is often suggested by the equation itself: a quadratic supplies its other root, a homogeneous equation supplies a common factor to remove, and a norm equation supplies multiplication by an inverse unit. Use the structure to choose the transformation, then let the domain restrictions determine whether it works.

---

## Rational Consequences of an Integer Descent

An integer impossibility theorem can sometimes rule out rational objects by clearing denominators. Choose a common positive denominator for every rational length; multiplying all lengths by it produces an integer object with the same shape.

If a rational right triangle had area equal to a nonzero rational square $$q^2$$, clearing denominators by a factor $$d$$ would produce an integer right triangle of area $$(dq)^2$$. This area is an integer square: a rational number whose square is an integer must itself be an integer, as prime exponents in a reduced fraction show.

The square-area descent therefore rules out such rational triangles as well.

<div class="theorem-box">

**Example.** Prove $$x^4+4y^4=z^2$$ has no solution in positive integers.

A solution would give a right triangle with legs $$x^2$$ and $$2y^2$$ and hypotenuse $$z$$. Its area would be $$x^2y^2=(xy)^2$$, a positive square, contradicting the square-area theorem proved above.

The same argument rules out positive rational solutions after clearing denominators.

</div>

Clearing denominators is essential before using a smallest-integer measure. Positive rational numbers can decrease forever, so choosing a “smallest positive rational solution” is not justified. The integer model supplies the well-ordering needed for descent.

---

## Key Relations

:::equations
| Method | Relation or condition |
| --- | --- |
| Descent measure | $$M\in\mathbb Z_{>0}$$ and $$0<M'<M$$ |
| Other quadratic root | $$y'=B-y$$ and $$yy'=C$$ for $$y^2-By+C=0$$ |
| Vieta example | $$y'=3x-y=(x^2+1)/y$$ for $$x^2+y^2+1=3xy$$ |
| Reverse jump | $$(x,y)\mapsto(y,3y-x)$$ |
| Pell multiplication | $$(x+y\sqrt D)(u+v\sqrt D)=(xu+D yv)+(xv+yu)\sqrt D$$ |
| Square-quotient jump | $$a'=kb-a=(b^2-k)/a$$ for $$a^2+b^2=k(ab+1)$$ |
| Pell inverse step | $$(x,y)\mapsto(3x-4y,3y-2x)$$ preserves $$x^2-2y^2$$ |
| Pell classification for $$D=2$$ | $$x+y\sqrt2=(3+2\sqrt2)^n$$ for $$x>0,y\ge0$$ |
| Unit-circle parametrization | $$x=(1-t^2)/(1+t^2),\ y=2t/(1+t^2)$$ plus $$(-1,0)$$ |
:::
