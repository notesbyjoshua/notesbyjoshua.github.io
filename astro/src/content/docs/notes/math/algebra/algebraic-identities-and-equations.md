---
title: "Algebraic Identities and Equations"
status: developing
progress: 68
sidebar:
  order: 1
description: "Competition algebra notes on factoring, substitutions, symmetric expressions, systems, logarithms, and radical equations with worked examples."
---

## Factorizing Expressions

Often times, a nasty expression or equation requires factoring to simplify and solve.

### Basic factorizations

One of the most common factorizations are the difference of squares and cubes factorization:

$$
a^2-b^2=(a-b)(a+b),\qquad
a^3\pm b^3=(a\pm b)(a^2\mp ab+b^2).
$$

// add like a general form of a^n + b^n, as well as the fact that any polynomial can be factored up to quadratics

Another useful (lesser-known) factorization is **Sophie Germain's identity**:

$$
a^4+4b^4=(a^2-2ab+2b^2)(a^2+2ab+2b^2).
$$

It comes from adding and subtracting $$4a^2b^2$$ to create a difference of squares. This is a useful move when a sum has almost enough terms to be a perfect square, and can be manipulated for sums of fourth powers.

<div class="theorem-box">

**Example.** Without expanding four large factors, evaluate $$\sqrt{19\cdot20\cdot21\cdot22+1}$$.

Pair the outside numbers and the inside numbers:

$$
19\cdot22=418,\qquad20\cdot21=420.
$$

The product is therefore one below a square:

$$
418\cdot420+1=(419-1)(419+1)+1=419^2.
$$

The required square root is $$419$$.

</div>

// add an AMC/AIME problem as an example

// add a section on completing the square and stuff

### Simon's Favorite Factoring Trick

**Simon's Favorite Factoring Trick**, usually shortened to **SFFT**, completes a product in the same way that completing the square creates a square. If an equation contains a mixed term and two linear terms, compare it with

$$
(x+b)(y+a)=xy+ax+by+ab.
$$

Thus adding the missing constant turns $$xy+ax+by=c$$ into $$(x+b)(y+a)=c+ab$$. The coefficients cross over: the coefficient of $$x$$ becomes the constant added to $$y$$. Expanding the proposed product once is a good way to check the placement.

For a leading coefficient other than one, multiply first:

$$
Axy+Bx+Cy=D
\quad\Longrightarrow\quad
(Ax+C)(Ay+B)=AD+BC.
$$

The transformed factors carry extra restrictions. If the original variables are integers, the first factor must be $$C$$ modulo $$A$$ and the second must be $$B$$ modulo $$A$$. Listing every divisor pair without checking these restrictions can create false solutions.

<div class="theorem-box">

**Example.** Find every positive integer ordered pair satisfying $$xy-3x-2y=20$$.

The missing product constant is six:

$$
(x-2)(y-3)=26.
$$

The factors have the same sign. They cannot both be negative: positivity would force $$x-2=-1$$ and $$y-3\in\{-2,-1\}$$, whose product is at most two. Therefore both factors are positive. The ordered positive divisor pairs of twenty-six give

$$
(x,y)=(3,29),(4,16),(15,5),(28,4).
$$

These are all the possibilities because every original solution determines one of those factor pairs. Expanding the completed product verifies the reverse implication.

</div>

A particularly useful disguised version involves reciprocals. Clearing denominators in $$1/x+1/y=1/n$$ gives $$xy=n(x+y)$$, which becomes

$$
(x-n)(y-n)=n^2.
$$

If $$x,y,n$$ are positive, each of $$x,y$$ is greater than $$n$$: a reciprocal term already equal to or greater than $$1/n$$ leaves no room for the other positive term.

<div class="theorem-box">

**Example.** Find the number of positive integer ordered pairs satisfying $$1/x+1/y=1/12$$.

SFFT gives $$(x-12)(y-12)=144$$. Each positive divisor $$d$$ of $$144$$ gives exactly one pair

$$
x=12+d,\qquad y=12+\frac{144}{d}.
$$

Since $$144=2^4 3^2$$, it has $$(4+1)(2+1)=15$$ positive divisors, so there are fifteen ordered pairs. For unordered pairs there would be eight: seven reversed pairs and the single diagonal solution $$x=y=24$$.

</div>

:::strategy
When two variables appear only through their product and linear terms, try completing a product before applying the quadratic formula. For integer solutions, a product equation is especially valuable because divisors give a finite, complete search.
:::

---

## The Binomial Theorem and Coefficients

The **binomial theorem** expands a nonnegative integer power without multiplying the factors one at a time:

$$
(a+b)^n=\sum_{k=0}^n\binom nk a^{n-k}b^k.
$$

The term with $$b^k$$ occurs when exactly $$k$$ of the $$n$$ factors contribute their $$b$$. There are $$\binom nk$$ choices of those factors. This explains both the coefficient and the exponents. The coefficients in row $$n$$ are symmetric because choosing the $$b$$ factors also determines the remaining $$a$$ factors.

Use the general term to extract a requested coefficient. Expanding every term wastes time and makes exponent mistakes harder to find. In a product of two expansions, first determine which exponents can combine to produce the required total.

<div class="theorem-box">

**Example.** Find the constant term in $$(2x-x^{-2})^9$$.

If the second term is chosen $$k$$ times, the resulting term is

$$
\binom9k(2x)^{9-k}(-x^{-2})^k
=\binom9k2^{9-k}(-1)^k x^{9-3k}.
$$

A constant requires $$9-3k=0$$, so only $$k=3$$ contributes. The constant term is

$$
-\binom93 2^6=-5376.
$$

Notice that both the exponent equation and the sign are needed. The coefficient alone does not determine whether the contribution is positive.

</div>

The same argument extends to a sum of several terms. The coefficient of $$a^ib^jc^k$$ in $$(a+b+c)^n$$, with $$i+j+k=n$$, is $$n!/(i!j!k!)$$. Choose the positions of the first type, then the second; the remaining positions contain the third. This **multinomial theorem** is useful for coefficient problems and arrangements with repeated objects.

Substitution into the binomial theorem also evaluates sums of coefficients. Setting $$a=b=1$$ gives $$\sum_k\binom nk=2^n$$, while setting $$a=1,b=-1$$ gives $$\sum_k(-1)^k\binom nk=0$$ for $$n\ge1$$. Adding and subtracting these two equations separates the even-index and odd-index coefficients.

<div class="theorem-box">

**Example.** Evaluate $$\sum_{k=0}^{10}k\binom{10}{k}$$ without calculating eleven individual terms.

Differentiate $$(1+t)^{10}=\sum_k\binom{10}{k}t^k$$, then multiply by $$t$$:

$$
10t(1+t)^9=\sum_{k=0}^{10}k\binom{10}{k}t^k.
$$

At $$t=1$$, the required sum is $$10\cdot2^9=5120$$. Differentiating twice would produce the weight $$k(k-1)$$; to handle $$k^2$$, write it as $$k(k-1)+k$$.

</div>

---

## Substitution and Symmetric Expressions

A substitution should reduce the number of different expressions you need to track. For a reciprocal expression, let $$t=x+1/x$$ with $$x\ne0$$. Then

$$
x^2+\frac1{x^2}=t^2-2,\qquad
x^3+\frac1{x^3}=t^3-3t.
$$

Remember the possible values of the new variable. For real nonzero $$x$$, we have $$t\le-2$$ or $$t\ge2$$; if $$x>0$$, only $$t\ge2$$ is possible.

For expressions symmetric in two variables, use their sum $$s=x+y$$ and product $$p=xy$$:

$$
x^2+y^2=s^2-2p,\qquad x^3+y^3=s^3-3ps.
$$

The individual variables are roots of $$u^2-su+p=0$$, so real values require $$s^2\ge4p$$.

<div class="theorem-box">

**Example.** Positive real numbers $$x,y$$ satisfy $$x+y=7$$ and $$x^2+y^2=29$$. Find $$x^3+y^3$$.

Use the square of the sum to find the product:

$$
49=29+2xy\quad\Longrightarrow\quad xy=10.
$$

Then

$$
x^3+y^3=7^3-3(10)(7)=133.
$$

Solving separately for $$x$$ and $$y$$ would add work without helping us find the requested symmetric expression.

</div>

We can also solve these types of equations using Newton's Sums, which is explained in detail in the polynomials page.

---

## Symmetry in Three Variables

For three variables, introduce the elementary symmetric quantities

$$
s=x+y+z,\qquad q=xy+yz+zx,\qquad p=xyz.
$$

Then $$x^2+y^2+z^2=s^2-2q$$ and

$$
x^3+y^3+z^3=s^3-3sq+3p.
$$

A related factorization is

$$
x^3+y^3+z^3-3xyz
=(x+y+z)(x^2+y^2+z^2-xy-yz-zx).
$$

It is particularly strong when the sum is zero. Instead of finding the individual variables, the entire cubic expression collapses to a product. Also,

$$
x^2+y^2+z^2-xy-yz-zx
=\frac12\bigl((x-y)^2+(y-z)^2+(z-x)^2\bigr),
$$

so for real variables this factor is nonnegative and vanishes precisely when the three variables are equal. A factorization can therefore carry information about equality cases as well as numerical values.

<div class="theorem-box">

**Example.** Real numbers $$x,y,z$$ satisfy $$x+y+z=0$$ and $$xyz=18$$. Find $$x^3+y^3+z^3$$.

The first factor in the displayed identity is zero, so $$x^3+y^3+z^3=3xyz=54$$. The conditions do not identify one ordered triple, but they do identify the requested symmetric expression.

</div>

For two-variable symmetric systems, the discriminant can be more useful than solving the system. If $$x+y=s$$ and $$xy=p$$, the variables are roots of $$t^2-st+p=0$$. Real solutions require $$s^2-4p\ge0$$; positive solutions additionally require a positive sum and product.

<div class="theorem-box">

**Example.** Find every real value of $$k$$ for which real numbers $$x,y$$ satisfy $$x+y=k$$ and $$x^2+y^2=6$$.

The product is $$p=(k^2-6)/2$$. Hence the discriminant of the quadratic with roots $$x,y$$ is

$$
k^2-4p=12-k^2.
$$

It is nonnegative exactly when $$-\sqrt{12}\le k\le\sqrt{12}$$. Conversely, for any such $$k$$ the roots of that quadratic are real and have the required sum and square sum, proving sufficiency as well as necessity.

</div>

---

## Systems of Equations

Adding or subtracting equations can expose a factor that substitution would bury. If swapping $$x$$ and $$y$$ exchanges the two equations, subtracting them often produces a factor of $$x-y$$. Split into cases instead of dividing by that factor and losing solutions.

<div class="theorem-box">

**Example.** Find all real ordered pairs satisfying $$x^2+y=7$$ and $$y^2+x=7$$.

Subtracting gives

$$
x^2-y^2+y-x=(x-y)(x+y-1)=0.
$$

If $$x=y$$, then $$x^2+x-7=0$$, giving the pairs

$$
\left(\frac{-1+\sqrt{29}}2,\frac{-1+\sqrt{29}}2\right),\qquad
\left(\frac{-1-\sqrt{29}}2,\frac{-1-\sqrt{29}}2\right).
$$

If $$x+y=1$$, substitute $$y=1-x$$ into the first equation:

$$
x^2-x-6=0.
$$

This gives $$(x,y)=(3,-2)$$ or $$(-2,3)$$. Substitution verifies all four pairs in both original equations.

</div>

---

## Exponents and Logarithms

For exponential equations with a common base, replace the repeated power by one variable. For logarithms with different bases, change to a shared base:

$$
\log_a b=\frac{\ln b}{\ln a},\qquad a>0,\quad a\ne1,\quad b>0.
$$

In particular, reciprocals of logarithms often turn products in the base into sums.

<div class="theorem-box">

**Example.** Let $$x,y,z,w>1$$ satisfy $$\log_xw=12$$, $$\log_yw=18$$, and $$\log_{xyz}w=4$$. Find $$\log_zw$$.

Change the base to $$w$$. The given equations become

$$
\log_wx=\frac1{12},\qquad\log_wy=\frac1{18},\qquad
\log_w(xyz)=\frac14.
$$

Using the product rule,

$$
\log_wz=\frac14-\frac1{12}-\frac1{18}=\frac19.
$$

Thus $$\log_zw=9$$.

</div>

<div class="theorem-box">

**Example.** Find all real solutions of $$4^x-5\cdot2^x+4=0$$.

Let $$t=2^x>0$$. Since $$4^x=t^2$$, the equation becomes $$(t-1)(t-4)=0$$. Thus $$2^x=1$$ or $$2^x=4$$, giving $$x=0$$ or $$x=2$$. Both values satisfy the original equation.

</div>

---

## Radical Equations and Extraneous Solutions

Squaring can turn a false equality into a true one because $$a^2=b^2$$ allows both $$a=b$$ and $$a=-b$$. Isolate the radical first, record the sign condition, and check the candidates in the original equation.

<div class="theorem-box">

**Example.** Find all real solutions of $$\sqrt{x+6}=x$$.

The left side is nonnegative, so any solution has $$x\ge0$$. Squaring gives

$$
x+6=x^2\quad\Longrightarrow\quad(x-3)(x+2)=0.
$$

The candidate $$x=-2$$ violates $$x\ge0$$. Checking $$x=3$$ gives $$\sqrt9=3$$, so the only solution is $$3$$.

</div>

:::tip
Keep a short list of restrictions before manipulating an equation: nonzero denominators, positive logarithm arguments, and nonnegative square roots. Check those restrictions again after solving the simpler equation.
:::

---

## Conjugates and Nested Radicals

When an expression contains two similar radicals, multiplication by a conjugate can remove them:

$$
(\sqrt u+\sqrt v)(\sqrt u-\sqrt v)=u-v.
$$

For $$\sqrt{A+2\sqrt B}$$, try $$\sqrt m+\sqrt n$$ with $$m,n\ge0$$. Squaring shows that the required conditions are $$m+n=A$$ and $$mn=B$$. Thus the same sum-and-product method used for symmetric systems also simplifies radicals.

<div class="theorem-box">

**Example.** Simplify $$\sqrt{7+4\sqrt3}+\sqrt{7-4\sqrt3}$$.

We need $$m+n=7$$ and $$mn=12$$, giving $$m=4,n=3$$. Thus the first radical is $$2+\sqrt3$$. The second is $$\lvert2-\sqrt3\rvert=2-\sqrt3$$, because $$2>\sqrt3$$. Their sum is four.

The absolute value is essential: a principal square root is nonnegative, and $$\sqrt{a^2}=\lvert a\rvert$$ rather than automatically $$a$$.

</div>

When a substitution reduces a difficult equation, finish by recovering the original variable and checking its domain. A quadratic in $$x+1/x$$ might produce an inadmissible value between negative two and two. A factorization after squaring might produce a candidate with the wrong sign. Keeping these checks beside the algebra makes a long solution much easier to trust.

---

## Absolute Values and Parameter Cases

An absolute value is a distance, so its graph changes slope where the inside expression is zero. For an equation containing several absolute values, mark those breakpoints first. On each interval, replace every absolute value by the correct signed expression, solve, and check that the solution lies in that interval.

A geometric interpretation can reveal an entire parameter classification before the algebra. The sum of distances from a point on a line to two fixed endpoints is at least the distance between the endpoints. Equality holds at every point between them, not just at the midpoint.

<div class="theorem-box">

**Example.** For every real parameter $$c$$, determine the number of real solutions of $$\lvert x-2\rvert+\lvert x+1\rvert=c$$.

The endpoints are negative one and two, at distance three. For $$-1\le x\le2$$, the left side is $$(2-x)+(x+1)=3$$. Thus there are no solutions if $$c<3$$ and infinitely many, the entire interval, if $$c=3$$.

For $$c>3$$, a solution must lie outside that interval. On $$x>2$$, the equation is $$2x-1=c$$, giving $$x=(c+1)/2>2$$. On $$x<-1$$, it is $$1-2x=c$$, giving $$x=(1-c)/2<-1$$.

There are exactly two solutions when $$c>3$$. The boundary parameter creates a whole interval of solutions, which would be missed by squaring or by solving only the outside cases.

</div>

The same idea extends to sums of many distances. For fixed points on a line, the sum of distances is minimized at a median. Between consecutive listed points, count how many terms increase and decrease as $$x$$ moves; the slope is their difference. This gives a direct way to analyze a piecewise-linear expression without expanding every case independently.

---

## Floor Functions by Integer and Fractional Parts

For a floor equation, write $$x=n+t$$ with $$n\in\mathbb Z$$ and $$0\le t<1$$. Integer multiples of $$x$$ then separate into a known multiple of $$n$$ and a short list of possible floor values involving $$t$$.

<div class="theorem-box">

**Example.** Solve $$\lfloor x\rfloor+\lfloor2x\rfloor=7$$ over the reals.

With $$x=n+t$$, the equation becomes $$3n+\lfloor2t\rfloor=7$$. The last floor is either zero or one. Only $$n=2$$ and $$\lfloor2t\rfloor=1$$ work. Hence $$1/2\le t<1$$ and the solution set is $$[5/2,3)$$.

The right endpoint is excluded because at three the floor sum jumps to nine. The left endpoint is included because the floor of $$2t$$ becomes one exactly at $$t=1/2$$.

</div>

For inequalities involving floors, use the defining bounds $$\lfloor u\rfloor\le u<\lfloor u\rfloor+1$$. They can first bound the integer part and make a finite case split possible. Avoid replacing a floor by a nearby real number as an equality; that loses the discontinuity carrying the integer information.

---

## Key Equations

:::equations
| Tool | Identity or condition |
| --- | --- |
| Difference of squares | $$a^2-b^2=(a-b)(a+b)$$ |
| Symmetric squares | $$x^2+y^2=(x+y)^2-2xy$$ |
| Symmetric cubes | $$x^3+y^3=(x+y)^3-3xy(x+y)$$ |
| Reciprocal substitution | $$x^2+x^{-2}=(x+x^{-1})^2-2$$, for $$x\ne0$$ |
| Change of base | $$\log_a b=\ln b/\ln a$$, for $$a,b>0$$ and $$a\ne1$$ |
| SFFT | $$(x+b)(y+a)=xy+ax+by+ab$$ |
| General SFFT | $$(Ax+C)(Ay+B)=A(Axy+Bx+Cy)+BC$$ |
| Binomial theorem | $$(a+b)^n=\sum_{k=0}^n\binom nk a^{n-k}b^k$$, integer $$n\ge0$$ |
| Three-variable cubic | $$x^3+y^3+z^3-3xyz=(x+y+z)(x^2+y^2+z^2-xy-yz-zx)$$ |
| Quadratic feasibility | Roots with sum $$s$$ and product $$p$$ are real iff $$s^2-4p\ge0$$ |
| Radical conjugates | $$(\sqrt u+\sqrt v)(\sqrt u-\sqrt v)=u-v$$, $$u,v\ge0$$ |
| Floor decomposition | $$x=n+t$$ with $$n=\lfloor x\rfloor,\ 0\le t<1$$ |
| Two-point distance sum | $$\lvert x-a\rvert+\lvert x-b\rvert\ge\lvert a-b\rvert$$ |
:::
