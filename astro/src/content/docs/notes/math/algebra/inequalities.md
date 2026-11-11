---
title: "Inequalities"
status: developing
progress: 68
sidebar:
  order: 5
description: "Competition math notes on AM–GM, Cauchy–Schwarz, rearrangement, and substitutions, with equality cases and worked optimization problems."
---

## Bounds and Equality Cases

An inequality compares expressions over a stated domain. To prove a minimum, we need both a lower bound and an allowed input that attains it. A lower bound alone might be too weak, and an example alone does not rule out smaller values.

Before choosing a theorem, inspect the variables' signs and predict when equality should hold. If the expected equality case fails in one step of your proof, that step cannot produce the sharp bound you want.

<div class="theorem-box">

**Example.** For real $$x$$, find the minimum of $$x^2-6x+13$$.

Complete the square:

$$
x^2-6x+13=(x-3)^2+4\ge4.
$$

Equality occurs at $$x=3$$, which is allowed, so the minimum is $$4$$.

</div>

---

## Arithmetic Mean–Geometric Mean

For nonnegative real numbers $$a_1,\ldots,a_n$$, **AM–GM** states

$$
\frac{a_1+\cdots+a_n}{n}\ge\sqrt[n]{a_1\cdots a_n}.
$$

Equality holds exactly when all the inputs are equal. For two inputs, the inequality follows from $$(\sqrt a-\sqrt b)^2\ge0$$. Use it when a sum and product need to be connected.

<div class="theorem-box">

**Example.** For $$x>0$$, find the minimum of $$x+9/x$$.

Both terms are positive, and their product is $$9$$. Thus

$$
x+\frac9x\ge2\sqrt9=6.
$$

Equality requires $$x=9/x$$. With $$x>0$$ this gives $$x=3$$, so the minimum is $$6$$.

</div>

Sometimes the equality condition tells you how to split a term. To minimize $$x^2+2/x$$ for $$x>0$$, apply AM–GM to the three terms $$x^2,1/x,1/x$$. Their product is one, so the expression is at least $$3$$, attained at $$x=1$$.

:::warning
Do not apply AM–GM to arbitrary signed real numbers. Also check that every equality condition can hold at the same time under the problem's constraint.
:::

---

## Cauchy–Schwarz and Fractions

For real sequences $$a_i,b_i$$,

$$
\left(\sum a_i^2\right)\left(\sum b_i^2\right)\ge\left(\sum a_ib_i\right)^2.
$$

Equality means the two vectors are proportional, including the usual zero-vector cases. For positive $$b_i$$, replacing the two sequences by $$a_i/\sqrt{b_i}$$ and $$\sqrt{b_i}$$ gives the fraction form

$$
\sum_{i=1}^n\frac{a_i^2}{b_i}\ge\frac{(a_1+\cdots+a_n)^2}{b_1+\cdots+b_n}.
$$

This is especially useful when the denominators add to a familiar expression.

<div class="theorem-box">

**Example.** Positive numbers $$x,y,z$$ satisfy $$x+y+z=1$$. Find the minimum of $$1/x+1/y+1/z$$.

Apply the fraction form with numerators all equal to one:

$$
\frac1x+\frac1y+\frac1z\ge\frac{(1+1+1)^2}{x+y+z}=9.
$$

Equality requires $$1/x=1/y=1/z$$, so $$x=y=z=1/3$$. These values satisfy the constraint, and the minimum is $$9$$.

</div>

For nonnegative $$a_i$$ and positive $$b_i$$, the equality condition in the fraction form is that $$a_i/b_i$$ is constant. With signed numerators, use the same proportionality condition rather than assuming all terms are positive.

---

## Rearrangement

If $$a_1\le\cdots\le a_n$$ and $$b_1\le\cdots\le b_n$$, pairing them in the same order maximizes the sum of products; pairing them in reverse order minimizes it:

$$
\sum_{i=1}^n a_ib_{n+1-i}\le\sum_{i=1}^n a_ib_{\sigma(i)}\le\sum_{i=1}^n a_ib_i.
$$

Here $$\sigma$$ is any permutation. For two pairs, the reason is

$$
(a_jb_j+a_ib_i)-(a_jb_i+a_ib_j)=(a_j-a_i)(b_j-b_i)\ge0.
$$

Successively removing out-of-order pairings proves the general statement.

<div class="theorem-box">

**Example.** The numbers $$a,b,c$$ are a rearrangement of $$1,3,5$$. Find the largest and smallest values of $$2a+4b+7c$$.

The weights are increasing, so the maximum pairs them with $$1,3,5$$ in that order:

$$
2(1)+4(3)+7(5)=49.
$$

The reverse pairing gives the minimum:

$$
2(5)+4(3)+7(1)=29.
$$

</div>

---

## Homogenization and Useful Substitutions

An expression is **homogeneous of degree $$d$$** if scaling every variable by $$t$$ scales the expression by $$t^d$$. A constraint such as $$a+b+c=1$$ lets you replace constants by powers of $$a+b+c$$ so that both sides have the same degree. A homogeneous inequality may also allow a convenient normalization, provided the normalizing quantity is positive.

<div class="theorem-box">

**Example.** Nonnegative numbers $$a,b,c$$ satisfy $$a+b+c=1$$. Prove that $$ab+bc+ca\le1/3$$.

Use the constraint to rewrite the desired constant bound as

$$
3(ab+bc+ca)\le(a+b+c)^2.
$$

After expanding, the difference is

$$
a^2+b^2+c^2-ab-bc-ca
=\frac12\bigl((a-b)^2+(b-c)^2+(c-a)^2\bigr)\ge0.
$$

Equality occurs when $$a=b=c=1/3$$.

</div>

For triangle sides, **Ravi substitution** writes $$a=u+v$$, $$b=v+w$$, $$c=w+u$$ with positive $$u,v,w$$. Such values exist because, for example, $$u=(a+c-b)/2>0$$ by the triangle inequality. This changes triangle constraints into positivity conditions.

<div class="theorem-box">

**Example.** Prove that the side lengths of any nondegenerate triangle satisfy $$(a+b-c)(b+c-a)(c+a-b)\le abc$$.

Use Ravi substitution $$a=u+v$$, $$b=v+w$$, $$c=w+u$$ with positive $$u,v,w$$. The left side becomes $$8uvw$$, while AM–GM gives

$$
(u+v)(v+w)(w+u)\ge(2\sqrt{uv})(2\sqrt{vw})(2\sqrt{wu})=8uvw.
$$

Thus the desired inequality holds. Equality requires $$u=v=w$$, equivalently an equilateral triangle.

</div>

:::strategy
Try completing squares for a polynomial in one variable, AM–GM for sums with a fixed product, Cauchy–Schwarz for fractions, and rearrangement when only a pairing changes. Test equality before doing a long chain of estimates. Multiplying by a denominator requires knowing its sign.
:::

## Weighted AM–GM and Choosing the Right Terms

The ordinary AM–GM inequality gives equal weight to each input. Repeating an input produces rational weights, and the general weighted form is

$$
\lambda_1a_1+\cdots+\lambda_na_n
\ge a_1^{\lambda_1}\cdots a_n^{\lambda_n},
\qquad \lambda_i>0,\quad \sum_i\lambda_i=1,\quad a_i>0.
$$

Equality requires all the inputs with positive weights to be equal. The choice of inputs matters: using the visible terms exactly as written may give an equality condition that cannot occur. Splitting a coefficient into repeated terms often repairs this.

<div class="theorem-box">

**Example.** Find the minimum of $$2x^3+3/x^2$$ for $$x>0$$.

Write the expression as five positive terms:

$$
x^3+x^3+x^{-2}+x^{-2}+x^{-2}.
$$

Their product is one, so AM–GM gives a lower bound of five. Equality requires $$x^3=x^{-2}$$, which gives $$x=1$$. The expression equals five there, so five is the minimum.

The exponents suggest the split: two copies of exponent three cancel three copies of exponent negative two. This is more systematic than trying arbitrary groupings.

</div>

For a fixed sum, AM–GM supplies an upper bound on a product. For a fixed product, it supplies a lower bound on a sum. The direction is determined by which quantity is controlled; changing the question changes how the same inequality should be used.

---

## Cauchy–Schwarz in Several Stages

A useful inequality proof often has two distinct jobs: simplify the expression and then use the constraint. Cauchy–Schwarz can combine fractions, after which a square-sum identity or AM–GM finishes the bound. Check equality in both stages.

<div class="theorem-box">

**Example.** For positive $$a,b,c$$, prove Nesbitt's inequality

$$
\frac a{b+c}+\frac b{c+a}+\frac c{a+b}\ge\frac32.
$$

Let $$s=a+b+c$$. Since $$a/(b+c)=s/(b+c)-1$$, the left side is

$$
s\left(\frac1{b+c}+\frac1{c+a}+\frac1{a+b}\right)-3.
$$

Cauchy–Schwarz bounds the reciprocal sum below by $$9/(2s)$$. Hence the expression is at least $$9/2-3=3/2$$. Equality requires $$b+c=c+a=a+b$$, equivalently $$a=b=c$$.

</div>

The form $$a^2/(b+c)$$ suggests applying the fraction form directly. The form $$a/(b+c)$$ may require rewriting the numerator or inserting square roots. Both are legitimate, but the better choice is the one whose equality condition and denominator sum are easy to control.

**Hölder's inequality** extends this idea. A useful positive-variable form is

$$
\left(\sum_i\frac{a_i^3}{b_i^2}\right)\left(\sum_i b_i\right)^2
\ge\left(\sum_i a_i\right)^3,\qquad a_i\ge0,\ b_i>0.
$$

It follows by applying the three-factor Hölder inequality to $$a_i/b_i^{2/3}$$, $$b_i^{1/3}$$, and $$b_i^{1/3}$$. Equality occurs when $$a_i/b_i$$ is constant. Think of this as the cubic analogue of combining quadratic fractions with Cauchy–Schwarz.

<div class="theorem-box">

**Example.** Positive $$x,y,z$$ satisfy $$x+y+z=1$$. Find the minimum of $$1/x^2+1/y^2+1/z^2$$.

Set every $$a_i$$ equal to one and use $$b_i=x,y,z$$. Hölder gives

$$
\left(\frac1{x^2}+\frac1{y^2}+\frac1{z^2}\right)(x+y+z)^2\ge27.
$$

The minimum is twenty-seven, achieved at $$x=y=z=1/3$$. A direct AM–GM argument would also work here, but the Hölder form adapts to unequal numerators.

</div>

---

## Schur's Inequality and Symmetric Cubics

For nonnegative $$a,b,c$$, **Schur's inequality of degree three** states

$$
a^3+b^3+c^3+3abc
\ge a^2b+a^2c+b^2a+b^2c+c^2a+c^2b.
$$

Unlike AM–GM applied separately to arbitrary terms, Schur keeps the mixed cubic structure together. In terms of $$s=a+b+c$$, $$q=ab+bc+ca$$, and $$p=abc$$, it is equivalent to

$$
s^3+9p\ge4sq.
$$

<div class="theorem-box">

**Proof (Schur's inequality).** Because the expression is symmetric, order the variables as $$a\ge b\ge c\ge0$$. The difference of the two sides is

$$
a(a-b)(a-c)+b(b-c)(b-a)+c(c-a)(c-b).
$$

Combine the first two terms and simplify:

$$
(a-b)^2(a+b-c)+c(a-c)(b-c)\ge0.
$$

Every displayed factor is nonnegative under the ordering. Equality occurs when all three variables are equal, or when the smallest is zero and the other two are equal.

</div>

A symmetric proof may assume an ordering because relabeling does not change the expression. A cyclic expression generally does not allow arbitrary relabeling; check that distinction before writing “without loss of generality.”

---

## Convexity and Jensen's Inequality

A function is **convex** on an interval if the graph lies below each chord joining two of its points. Equivalently,

$$
f(\lambda x+(1-\lambda)y)\le\lambda f(x)+(1-\lambda)f(y)
$$

for $$0\le\lambda\le1$$. A twice-differentiable function with $$f''\ge0$$ is convex. A concave function has the opposite inequality.

**Jensen's inequality** extends the definition to several inputs:

$$
f\left(\sum_i\lambda_i x_i\right)\le\sum_i\lambda_i f(x_i)
$$

for nonnegative weights totaling one, with all inputs in a convexity interval. If the function is strictly convex and all weights are positive, equality forces the inputs to be equal.

<div class="theorem-box">

**Example.** Nonnegative $$a,b,c$$ satisfy $$a+b+c=3$$. Find the maximum of $$a/(1+a)+b/(1+b)+c/(1+c)$$.

The function $$g(t)=t/(1+t)$$ satisfies $$g''(t)=-2/(1+t)^3<0$$ for $$t\ge0$$, so it is strictly concave. Jensen, with its inequality reversed for concavity, gives

$$
g(a)+g(b)+g(c)\le3g(1)=\frac32.
$$

Equality holds at $$a=b=c=1$$, proving the maximum. Applying convex Jensen in the wrong direction would produce a false lower bound.

</div>

Jensen requires a function of separate variables. It does not directly handle a denominator mixing several unrelated inputs. Often a substitution or a fixed-sum rewrite is needed before the expression fits its form.

---

## Tangent Bounds Without Calculus

A differentiable convex function lies above each of its tangent lines. This gives the estimate $$f(x)\ge f(t)+f'(t)(x-t)$$. In an inequality with a fixed sum, linear terms can then cancel when added over the variables.

You can frequently prove the required tangent bound by factoring its difference, avoiding calculus in the final solution. The equality point tells you where the tangent should touch.

<div class="theorem-box">

**Example.** Prove $$a^3+b^3+c^3\ge3$$ when $$a,b,c\ge0$$ and $$a+b+c=3$$, using a linear bound.

The expected equality point is one. The needed bound is

$$
x^3\ge3x-2,
$$

because $$x^3-3x+2=(x-1)^2(x+2)\ge0$$ for $$x\ge0$$. Apply it to each variable and add:

$$
a^3+b^3+c^3\ge3(a+b+c)-6=3.
$$

Equality requires every variable to be one.

</div>

The useful part of this approach is its adaptability. For a less familiar rational function, guess a line through the expected equality point, clear a denominator of known sign, and try to factor the resulting polynomial. Do not assume a tangent is a global bound outside the interval where convexity is known.

---

## Sharpness, Boundary Cases, and Proof Planning

Symmetry suggests testing equal variables, but it does not guarantee the extremum occurs there. Also test one variable approaching zero and, for scale-invariant expressions, one variable becoming much larger than the others. These experiments help predict whether a bound is attained or only approached.

For positive variables with a fixed sum, the boundary is not included. An expression may have an infimum that occurs only when one variable tends to zero; calling it a minimum would then be incorrect. State both the bound and the nature of its equality or limiting case.

A productive proof plan begins with the target equality case. Work backward to identify an inequality that is sharp there, then check whether its output matches the given constraint. If one step forces two variables equal and another forces a contradictory ratio, the chain cannot establish the exact optimum. It may still prove a weaker inequality, but it needs a different purpose.

---

## Product-One Constraints and Scale

If positive variables satisfy $$abc=1$$, they can be represented as ratios $$a=x/y,b=y/z,c=z/x$$ of positive quantities. For instance, take $$z=1,y=b,x=ab$$. This substitution removes the product constraint, but it may introduce fractions, so use it only when the resulting cyclic expression simplifies.

Alternatively, exploit the product directly. Both $$a,b,c$$ and $$ab,bc,ca$$ have product one, so AM–GM gives sums at least three. Expanding then proves $$(1+a)(1+b)(1+c)\ge8$$, with equality at $$a=b=c=1$$.

For a homogeneous expression, scaling can normalize a sum instead. The degree must match on both sides before setting that sum to one. A nonhomogeneous constant cannot be normalized away without changing the problem.

---

## A Valid Bound Need Not Be the Exact Optimum

A chain of inequalities may prove the requested statement without locating the sharp minimum. Make the distinction explicit when using several separate constraints.

<div class="theorem-box">

**Example.** Nonnegative $$a,b,c$$ satisfy $$a+b+c=3$$ and $$ab+bc+ca\ge5/2$$. Prove $$abc\ge1/3$$.

With $$s=3,q=ab+bc+ca,p=abc$$, Schur gives

$$
27+9p\ge12q\ge30.
$$

Therefore $$p\ge1/3$$, as required.

This argument establishes the stated lower bound. It does not claim that one-third is attained: equality would require equality in Schur and in the separate bound on $$q$$ simultaneously. Those conditions do not match here.

</div>

When the question asks only to prove an inequality, a convenient nonsharp estimate may be enough. When it asks for the minimum, the equality analysis is indispensable. Working out that distinction before optimizing can save a long search for an equality case that the chosen bound cannot have.

---

## Unequal Quadratic Weights

Cauchy–Schwarz can locate a nonsymmetric equality point when the coefficients are unequal.

<div class="theorem-box">

**Example.** Real numbers satisfy $$x+y+z=1$$. Find the minimum of $$x^2+2y^2+3z^2$$.

Apply Cauchy–Schwarz to $$(x,\sqrt2y,\sqrt3z)$$ and $$(1,1/\sqrt2,1/\sqrt3)$$:

$$
(x^2+2y^2+3z^2)\left(1+\frac12+\frac13\right)\ge1.
$$

The lower bound is $$6/11$$. Equality requires $$x:y:z=1:1/2:1/3$$, so the constraint gives $$(x,y,z)=(6/11,3/11,2/11)$$. These values attain the bound.

</div>

Unequal weights shift the minimizing point away from equal variables. The proportionality condition identifies the correct point directly, which is more reliable than guessing from symmetry that the expression does not possess.

---

## Key Equations

:::equations
| Tool | Formula and conditions |
| --- | --- |
| AM–GM | $$\sum a_i\ge n\sqrt[n]{\prod a_i}$$, $$a_i\ge0$$ |
| Cauchy–Schwarz | $$(\sum a_i^2)(\sum b_i^2)\ge(\sum a_ib_i)^2$$ |
| Fraction form | $$\sum a_i^2/b_i\ge(\sum a_i)^2/\sum b_i$$, $$b_i>0$$ |
| Three-variable squares | $$a^2+b^2+c^2-ab-bc-ca=\tfrac12\sum_{\mathrm{cyc}}(a-b)^2$$ |
| Ravi substitution | $$a=u+v,\ b=v+w,\ c=w+u$$, $$u,v,w>0$$ for a nondegenerate triangle |
| Weighted AM–GM | $$\sum\lambda_i a_i\ge\prod a_i^{\lambda_i}$$, $$a_i>0,\lambda_i>0,\sum\lambda_i=1$$ |
| Cubic fraction bound | $$(\sum a_i^3/b_i^2)(\sum b_i)^2\ge(\sum a_i)^3$$, $$a_i\ge0,b_i>0$$ |
| Schur | $$s^3+9p\ge4sq$$ for nonnegative variables, $$s=a+b+c,q=ab+bc+ca,p=abc$$ |
| Jensen | $$f(\sum\lambda_i x_i)\le\sum\lambda_i f(x_i)$$ for convex $$f$$ and weights totaling one |
| Convex tangent bound | $$f(x)\ge f(t)+f'(t)(x-t)$$ within a convexity interval |
:::
