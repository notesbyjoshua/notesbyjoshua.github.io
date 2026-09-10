---
title: "Unit 1: Limits and Continuity"
description: "AP Calculus notes on limits, continuity, asymptotes, the squeeze theorem, intermediate value theorem, and limit techniques."
sidebar:
  order: 1
---

## Definition of a Limit

<div class="theorem-box">

**Definition.** A limit is defined as

$$
\lim_{x \to a} f(x) = L
$$

if we can make $$f(x)$$ as close to $$L$$ as we want by taking $$x$$ sufficiently close to $$a$$, with $$x \ne a$$.

</div>

This is about nearby behavior, not direct substitution. It is possible for:

- the limit to exist while $$f(a)$$ is undefined,
- the limit to exist while $$f(a) \ne L$$,
- the limit to fail even though $$f(a)$$ exists.

A quick check is direct substitution. If substituting $$x = a$$ gives a finite number and the expression is defined there, the limit is usually that number.
 
<div class="theorem-box">

**Example.** Evaluate $$\displaystyle\lim_{x\to 2}\bigl(3x^2-1\bigr).$$

This function is a polynomial, and doesn't have any weird jumps or other features. Thus,

$$
3(2)^2-1 = 11.
$$

So the limit is $$11$$.

</div>

### One-sided and two-sided limits

A one-sided limit describes the value approached from one direction only.

- Left-hand limit: $$\lim_{x \to a^-} f(x)$$
- Right-hand limit: $$\lim_{x \to a^+} f(x)$$

A two-sided limit exists exactly when both one-sided limits exist and agree:

$$
\lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = L.
$$

If the left-hand and right-hand limits disagree, then the two-sided limit does not exist.

<div class="theorem-box">

**Example.** Evaluate $$\displaystyle\lim_{x\to2} f(x)$$ for

$$
f(x)=
\begin{cases}
x+1, & x<2,\\
5, & x=2,\\
3x-3, & x>2.
\end{cases}
$$

The left-hand limit uses the branch $$x+1$$:

$$
\lim_{x\to2^-}f(x)=2+1=3.
$$

The right-hand limit uses the branch $$3x-3$$:

$$
\lim_{x\to2^+}f(x)=3(2)-3=3.
$$

Since the one-sided limits agree,

$$
\lim_{x\to2}f(x)=3.
$$

Notice that $$f(2)=5$$, but that does not change the limit. The limit depends on nearby values, not the value directly at $$x=2$$.

</div>

<div class="theorem-box">

**Example.** The graph of $$f$$ is shown below. Evaluate $$\lim_{x\to0} f(1-x^2).$$

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle,
  xmin=-3.2, xmax=3.2,
  ymin=-0.4, ymax=6.8,
  xtick={-3,-2,-1,0,1,2,3},
  ytick={1,2,3,4,5,6},
  grid=both,
  grid style={gray!22},
  width=8cm,
  height=6.4cm,
  xlabel=$x$,
  ylabel=$y$,
  tick label style={font=\small},
  label style={font=\small},
]
\addplot[black, thick, domain=-2.2:1, samples=120] {(x)^2+2};
\addplot[black, thick, domain=1:2.35, samples=120] {(x-1)^2+4};
\addplot[only marks, mark=o, mark size=2.3pt, black, thick] coordinates {(1,3) (1,4)};
\addplot[only marks, mark=*, mark size=2.6pt, black] coordinates {(1,2)};
\end{axis}
\end{tikzpicture}
```

As $$x\to0$$, the inside expression satisfies

$$
1-x^2\to1.
$$

However, $$1-x^2$$ is always less than or equal to $$1$$ near $$x=0$$. For $$x\ne0$$, it approaches $$1$$ from the left:

$$
1-x^2\to1^-.
$$

So the limit depends on the left-hand behavior of $$f$$ at $$x=1$$. From the graph,

$$
\lim_{u\to1^-} f(u)=3.
$$

Therefore,

$$
\lim_{x\to0} f(1-x^2)=3.
$$

</div>

### Limits from table of values

When you do not have a formula or graph, use a table to estimate what the outputs approach from each side.

A table does not prove a limit by itself, but it gives strong evidence. It is especially useful for reading calculator-generated data, numerical models, or functions that are hard to simplify by hand.

When using a table, check two things:

- values of $$x$$ slightly less than $$a$$,
- values of $$x$$ slightly greater than $$a$$.

If the outputs approach the same number from both sides, the two-sided limit likely equals that number. If the outputs approach different numbers, the two-sided limit does not exist.

<div class="theorem-box">

**Example.** Use the table to estimate $$\displaystyle\lim_{x\to2}f(x)$$.

$$
\begin{array}{c|cccccc}
x & 1.9 & 1.99 & 1.999 & 2.001 & 2.01 & 2.1 \\\hline
f(x) & 4.71 & 4.9701 & 4.997001 & 5.003001 & 5.0301 & 5.31
\end{array}
$$

From the left, the function values approach $$5$$:

$$
\lim_{x\to2^-}f(x)=5.
$$

From the right, the function values also approach $$5$$:

$$
\lim_{x\to2^+}f(x)=5.
$$

Since the one-sided limits agree,

$$
\lim_{x\to2}f(x)=5.
$$

</div>

<div class="theorem-box">

**Example.** Use the table to estimate $$\displaystyle\lim_{x\to0}g(x)$$.

$$
\begin{array}{c|cccccc}
x & -0.1 & -0.01 & -0.001 & 0.001 & 0.01 & 0.1 \\\hline
g(x) & -1.9 & -1.99 & -1.999 & 2.001 & 2.01 & 2.1
\end{array}
$$

From the left, the outputs approach $$-2$$:

$$
\lim_{x\to0^-}g(x)=-2.
$$

From the right, the outputs approach $$2$$:

$$
\lim_{x\to0^+}g(x)=2.
$$

Since the one-sided limits do not agree,

$$
\lim_{x\to0}g(x)
$$

does not exist.

</div>

---

## Limit laws and direct substitution

If $$\lim_{x \to a} f(x) = L$$ and $$\lim_{x \to a} g(x) = M$$, then:

$$
\lim_{x \to a} (f(x) \pm g(x)) = L \pm M,
$$

$$
\lim_{x \to a} (f(x)g(x)) = LM,
$$

$$
\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{L}{M}, \qquad M \ne 0,
$$

$$
\lim_{x \to a} [f(x)]^n = L^n.
$$

For polynomials and rational functions, direct substitution works whenever the denominator is nonzero. If substitution gives a finite number, the limit is usually that number.

<div class="theorem-box">

**Proof (Limit Laws).** A limit statement means the function values can be forced arbitrarily close to a target value. If $$f(x)$$ is close to $$L$$ and $$g(x)$$ is close to $$M$$, then their sum is close to $$L + M$$, their product is close to $$LM$$, and their quotient is close to $$L/M$$ as long as $$M \ne 0$$.

A key idea is that the limit might not be exactly at the input value, but the function values can get arbitrarily close to the target. In AP Calculus, we often think of the small error as $$\varepsilon$$, which becomes negligible when the limit exists.

</div>

<div class="theorem-box">

**Example.** Suppose $$\lim_{x\to 2}f(x)=3$$ and $$\lim_{x\to 2}g(x)=-1$$. Find

$$
\lim_{x\to2}\frac{2f(x)-g(x)}{[f(x)]^2}.
$$

Using limit laws, substitute the known limits:

$$
\frac{2\cdot 3-(-1)}{3^2} = \frac{7}{9}.
$$

Therefore the limit equals $$\frac{7}{9}$$.

</div>

<div class="theorem-box">

**Example.** Suppose

$$
\lim_{x\to1}f(x)=4,
\qquad
\lim_{x\to1}g(x)=0,
\qquad
\lim_{x\to1}h(x)=-2.
$$

Find

$$
\lim_{x\to1}\frac{\sqrt{f(x)+5}-3h(x)}{f(x)-h(x)g(x)+1}.
$$

Use the limit laws inside the expression:

$$
\sqrt{f(x)+5}\to\sqrt{4+5}=3,
$$

$$
3h(x)\to3(-2)=-6,
$$

and

$$
f(x)-h(x)g(x)+1\to4-(-2)(0)+1=5.
$$

Therefore

$$
\lim_{x\to1}\frac{\sqrt{f(x)+5}-3h(x)}{f(x)-h(x)g(x)+1}
=
\frac{3-(-6)}{5}
=
\frac95.
$$

</div>

---

## Indeterminate forms and algebraic techniques

Direct substitution sometimes gives an indeterminate form, so substitution alone does not determine the limit. You need to simplify the expression or use another limit technique. Common indeterminate forms include: $$0/0$$, $$\infty/\infty$$, $$0 \cdot \infty$$, $$\infty - \infty$$, $$1^\infty$$, $$0^0$$, and $$\infty^0$$.

Start by checking whether direct substitution works. If it gives an indeterminate form, choose a method that fits the expression.

:::warning
A form that is not indeterminate may already determine the limit. For example, $$\infty/3$$ indicates growth without bound. You can still simplify the expression, but indeterminate-form rules such as L’Hôpital’s Rule do not apply to that form.
:::

### Factoring and canceling

Factoring is useful when direct substitution gives $$0/0$$ and the numerator and denominator share a hidden factor. After canceling, the simplified expression agrees with the original expression for nearby values of $$x$$, even if the original expression is undefined at the exact input.

<div class="theorem-box">

**Example.** Evaluate

$$
\lim_{x\to2}\frac{x^3-6x^2+11x-6}{x-2}.
$$

Direct substitution gives $$0/0$$, so the numerator must have a factor of $$x-2$$. Since the cubic is not immediately obvious to factor by grouping, use synthetic division with $$2$$:

$$
\begin{array}{r|rrrr}
2 & 1 & -6 & 11 & -6 \\
  &   & 2 & -8 & 6 \\\hline
  & 1 & -4 & 3 & 0
\end{array}
$$

So

$$
x^3-6x^2+11x-6=(x-2)(x^2-4x+3).
$$

Cancel the removable factor:

$$
\lim_{x\to2}\frac{x^3-6x^2+11x-6}{x-2}
=
\lim_{x\to2}\frac{(x-2)(x^2-4x+3)}{x-2}.
$$

For $$x\ne2$$, this simplifies to

$$
\lim_{x\to2}(x^2-4x+3).
$$

Now substitute:

$$
2^2-4(2)+3
=
-1.
$$

So the limit is $$-1$$. The original function has a removable discontinuity at $$x=2$$, but the nearby behavior is controlled by the quotient polynomial.

</div>

### Dealing with roots

When radicals create $$0/0$$, multiply by the conjugate. The conjugate changes a radical difference into a difference of squares, which often reveals a canceling factor.

<div class="theorem-box">

**Example.** Evaluate $$\displaystyle\lim_{x\to0}\frac{\sqrt{x+1}-1}{x}.$$

Multiply by the conjugate to remove the radical from the numerator:

$$
\lim_{x\to0}\frac{\sqrt{x+1}-1}{x}
=
\lim_{x\to0}\frac{(\sqrt{x+1}-1)(\sqrt{x+1}+1)}{x(\sqrt{x+1}+1)}.
$$

The numerator becomes a difference of squares:

$$
(\sqrt{x+1}-1)(\sqrt{x+1}+1)
=(x+1)-1=x.
$$

So, for $$x\ne0$$,

$$
\lim_{x\to0}\frac{\sqrt{x+1}-1}{x}
=
\lim_{x\to0}\frac{x}{x(\sqrt{x+1}+1)}
=
\lim_{x\to0}\frac{1}{\sqrt{x+1}+1}.
$$

Now evaluate the simplified limit:

$$
\lim_{x\to0}\frac{1}{\sqrt{x+1}+1}=\frac{1}{2}.
$$

</div>

For roots at infinity, another useful move is to factor the largest power out from inside the radical. The square root of a square produces an absolute value:

$$
\sqrt{x^6}= \lvert x^3\rvert.
$$

The sign of that absolute value depends on whether $$x\to\infty$$ or $$x\to-\infty$$. This matters because end-behavior limits are sensitive to direction.

<div class="theorem-box">

**Example.** Evaluate

$$
\lim_{x\to\infty}\left(\sqrt{x^6+5x^3}-x^3\right).
$$

Direct substitution gives the indeterminate form $$\infty-\infty$$. Factor $$x^6$$ out of the radical:

$$
\lim_{x\to\infty}\left(\sqrt{x^6+5x^3}-x^3\right)
=
\lim_{x\to\infty}\left(\sqrt{x^6\left(1+\frac{5}{x^3}\right)}-x^3\right).
$$

Since $$x\to\infty$$, $$\lvert x^3\rvert=x^3$$, so

$$
\lim_{x\to\infty}\left(\sqrt{x^6\left(1+\frac{5}{x^3}\right)}-x^3\right)
=
\lim_{x\to\infty}\left(x^3\sqrt{1+\frac{5}{x^3}}-x^3\right).
$$

Factor out $$x^3$$:

$$
\lim_{x\to\infty}x^3\left(\sqrt{1+\frac{5}{x^3}}-1\right).
$$

This is still not easy to evaluate directly, so rationalize:

$$
\lim_{x\to\infty}x^3\left(\sqrt{1+\frac{5}{x^3}}-1\right)
=
\lim_{x\to\infty}x^3\left(\frac{\left(1+\frac{5}{x^3}\right)-1}{\sqrt{1+\frac{5}{x^3}}+1}\right).
$$

Simplify:

$$
\lim_{x\to\infty}x^3\left(\frac{\frac{5}{x^3}}{\sqrt{1+\frac{5}{x^3}}+1}\right)
=
\lim_{x\to\infty}\frac{5}{\sqrt{1+\frac{5}{x^3}}+1}.
$$

Now the remaining variable expression has a clear limit:

$$
\lim_{x\to\infty}\frac{5}{\sqrt{1+\frac{5}{x^3}}+1}
=
\frac{5}{\sqrt{1+0}+1}
=
\frac52.
$$

</div>

### Substitution

Substitution for limits works like u-substitution for integrals, but the goal is different: you rename a messy inside expression so the limit becomes a standard form. If

$$
u=g(x)
$$

and $$g(x)\to L$$ as $$x\to a$$, then

$$
\lim_{x\to a} f(g(x))=\lim_{u\to L}f(u),
$$

as long as the new limit exists.

:::warning
Be careful with expressions that approach $$0$$ or $$\infty$$ from only one side, because square roots, logarithms, and absolute values can change the direction of the new variable.
:::

<div class="theorem-box">

**Example.** Evaluate

$$
\lim_{x\to4}\frac{\sqrt{x+5}-3}{x-4}.
$$

Let $$u=\sqrt{x+5}$$. As $$x\to4$$, $$u\to3$$. Also,

$$
u^2=x+5
\quad\Longrightarrow\quad
x=u^2-5.
$$

So

$$
x-4=u^2-9=(u-3)(u+3).
$$

The limit becomes

$$
\lim_{u\to3}\frac{u-3}{(u-3)(u+3)}
=
\lim_{u\to3}\frac{1}{u+3}
=
\frac16.
$$

</div>

---

## Limits at infinity and asymptotic behavior

We also study

$$
\lim_{x \to \infty} f(x), \qquad \lim_{x \to -\infty} f(x),
$$

or as more commonly known as end behavior.

For rational functions:

- If degree numerator < degree denominator: the limit is $$0$$,
- If the degrees are equal: the limit is the ratio of leading coefficients,
- If degree numerator > degree denominator: there is no finite horizontal asymptote (the function may have a slant or oblique asymptote).

For other common function families, compare long-run growth:

| Function type | Typical end behavior idea |
|---|---|
| Polynomial | leading term controls the sign and size |
| Rational | compare degrees after simplifying |
| Trig | sine and cosine oscillate, so many infinity limits do not exist |
| Inverse trig | often approaches a horizontal angle value |

<div class="theorem-box">

**Example.** Evaluate $$\displaystyle\lim_{x\to\infty} \frac{3x^2+5x}{2x^2-7}$$ and identify the horizontal asymptote.

Divide numerator and denominator by $$x^2$$:

$$
\lim_{x\to\infty}\frac{3x^2+5x}{2x^2-7}
=
\lim_{x\to\infty}\frac{3+5/x}{2-7/x^2}.
$$

As $$x\to\infty$$, the terms $$5/x$$ and $$7/x^2$$ vanish (go to $$0$$), leaving the limit

$$
\frac{3}{2}.
$$

Therefore the horizontal asymptote is $$y=\frac32$$.

You can learn more about end behavior for rational functions in AP Precalculus.

</div>

<div class="theorem-box">

**Example.** Evaluate

$$
\lim_{x\to\infty}\arctan x.
$$

The function $$y=\arctan x$$ asks for the angle whose tangent is $$x$$. As $$x$$ becomes very large and positive, that angle approaches the vertical asymptote angle of tangent:

$$
\frac{\pi}{2}.
$$

Therefore

$$
\lim_{x\to\infty}\arctan x=\frac{\pi}{2}.
$$

Similarly,

$$
\lim_{x\to-\infty}\arctan x=-\frac{\pi}{2}.
$$

</div>

<div class="theorem-box">

**Example.** Evaluate

$$
\lim_{x\to\infty}\frac{\sqrt{9x^2+4x}-2x}{x+1}.
$$

At infinity, factor $$x^2$$ inside the square root:

$$
\lim_{x\to\infty}\sqrt{9x^2+4x}
=
\lim_{x\to\infty}\sqrt{x^2\left(9+\frac4x\right)}
=
\lim_{x\to\infty}\lvert x\rvert\sqrt{9+\frac4x}.
$$

Since $$x\to\infty$$, $$x>0$$ eventually, so $$\lvert x\rvert=x$$. Then

$$
\lim_{x\to\infty}\frac{\sqrt{9x^2+4x}-2x}{x+1}
=
\lim_{x\to\infty}\frac{x\sqrt{9+\frac4x}-2x}{x+1}.
$$

Factor $$x$$ from the numerator and denominator:

$$
\lim_{x\to\infty}\frac{x\left(\sqrt{9+\frac4x}-2\right)}{x\left(1+\frac1x\right)}
=
\lim_{x\to\infty}\frac{\sqrt{9+\frac4x}-2}{1+\frac1x}.
$$

Now take the limit:

$$
\frac{\sqrt{9+0}-2}{1+0}
=
1.
$$

Therefore,

$$
\lim_{x\to\infty}\frac{\sqrt{9x^2+4x}-2x}{x+1}=1.
$$

</div>

---

## Continuity

<div class="theorem-box">

**Definition**: A function is said to be *continuous* at $$x = a$$ when:

1. $$f(a)$$ exists,
2. $$\lim_{x \to a} f(x)$$ exists,
3. $$\lim_{x \to a} f(x) = f(a).$$

Continuity means the nearby behavior of the function matches the value at the point. In a simpler sense, a function is continuous if around that point, you can draw the graph without picking up your pencil. A graph that is continuous without any specifications about location is assumed to be continuous everywhere.

</div>

A break in continuity is called a discontinuity, and can come in many types. For example,

- Holes: $$\lim_{x \to a} f(x)$$ exists, but $$\lim_{x \to a} f(x) \ne f(a).$$
- Jumps: Left hand and right hand limits differ
- Infinite discontinuity: A vertical asymptote, basically when any one-sided limit becomes $$\pm \infty$$
- Oscillatory discontinuity: no single nearby trend, most applicable to trig functions

For piecewise functions, continuity at the switching point is a limit-matching problem. The left-hand limit, right-hand limit, and actual function value must all agree.

<div class="theorem-box">

**Example.** Identify all discontinuities of

$$
f(x)=
\begin{cases}
\dfrac{x^2-9}{x-3}, & x<3,\\
7, & x=3,\\
2x+1, & 3<x<5,\\
20, & x=5,\\
\dfrac{1}{x-6}, & x>5.
\end{cases}
$$

Justify each case.

At $$x=3$$, the left-hand branch simplifies for $$x\ne3$$:

$$
\frac{x^2-9}{x-3}
=
\frac{(x-3)(x+3)}{x-3}
=
x+3.
$$

So

$$
\lim_{x\to3^-}f(x)=6.
$$

The right-hand limit comes from $$2x+1$$:

$$
\lim_{x\to3^+}f(x)=7.
$$

Since the one-sided limits differ, $$x=3$$ is a jump discontinuity. The fact that $$f(3)=7$$ does not fix the jump.

At $$x=5$$,

$$
\lim_{x\to5^-}f(x)=2(5)+1=11.
$$

For the right-hand side, use the branch $$1/(x-6)$$:

$$
\lim_{x\to5^+}f(x)=\frac{1}{5-6}=-1.
$$

The one-sided limits differ, so $$x=5$$ is also a jump discontinuity. The value $$f(5)=20$$ is just the actual point value.

At $$x=6$$, the branch $$1/(x-6)$$ has a vertical asymptote. Since

$$
\lim_{x\to6^-}\frac{1}{x-6}=-\infty
\qquad\text{and}\qquad
\lim_{x\to6^+}\frac{1}{x-6}=\infty,
$$

there is an infinite discontinuity at $$x=6$$.

Therefore the discontinuities are $$x=3$$, $$x=5$$, and $$x=6$$.

</div>

### Continuity Theorems

<div class="theorem-box">

**Theorem (Continuity of algebraic combinations).** If $$f$$ and $$g$$ are continuous at $$x=a$$, then the following functions are also continuous at $$x=a$$:

- $$f+g$$,
- $$f-g$$,
- $$fg$$,
- $$cf$$ for any constant $$c$$,
- $$\dfrac{f}{g}$$, as long as $$g(a)\ne0$$.

</div>

We will prove one example below, as all of them are very similar.

<div class="theorem-box">

**Proof (Product of continuous functions).** Suppose $$f$$ and $$g$$ are continuous at $$x=a$$. Then

$$
\lim_{x\to a}f(x)=f(a)
\qquad\text{and}\qquad
\lim_{x\to a}g(x)=g(a).
$$

Using the product rule for limits,

$$
\lim_{x\to a}f(x)g(x)
=
\left(\lim_{x\to a}f(x)\right)\left(\lim_{x\to a}g(x)\right).
$$

So

$$
\lim_{x\to a}f(x)g(x)=f(a)g(a).
$$

But $$f(a)g(a)$$ is exactly the value of the product function at $$a$$. Therefore $$fg$$ is continuous at $$x=a$$.

</div>

:::note
Polynomials, exponential functions, sine, cosine, and rational functions on their domains are continuous everywhere. Root functions, logarithms, tangent, secant, cosecant, cotangent, and inverse trig functions are continuous wherever they are defined (basically excluding asymptotes).
:::

<div class="theorem-box">

**Theorem (Taking out limits).** If

$$
\lim_{x\to a}g(x)=L
$$

and $$f$$ is continuous at $$L$$, then

$$
\lim_{x\to a}f(g(x))
=
f\left(\lim_{x\to a}g(x)\right)
=
f(L).
$$

In words, you can move the limit inside $$f$$ only when the outside function is continuous at the value the inside expression approaches.

</div>

<div class="theorem-box">

**Proof (Taking out limits).** Since $$\lim_{x\to a}g(x)=L$$, the expression $$g(x)$$ gets as close to $$L$$ as we want when $$x$$ is close enough to $$a$$. Since $$f$$ is continuous at $$L$$, making the input to $$f$$ close to $$L$$ forces the output of $$f$$ close to $$f(L)$$.

So as $$x\to a$$, the input $$g(x)$$ approaches $$L$$, and then the output $$f(g(x))$$ approaches $$f(L)$$. Therefore,

$$
\lim_{x\to a}f(g(x))=f(L).
$$

</div>

<div class="theorem-box">

**Example.** Determine where

$$
h(x)=\sqrt{\frac{x+1}{x-2}}
$$

is continuous.

The inside rational expression is continuous wherever $$x\ne2$$. The square root is continuous when its input is nonnegative, so we need

$$
\frac{x+1}{x-2}\ge0.
$$

The critical values are $$x=-1$$ and $$x=2$$. A sign chart gives

$$
\frac{x+1}{x-2}\ge0
\quad\text{on}\quad
(-\infty,-1]\cup(2,\infty).
$$

Therefore $$h$$ is continuous on

$$
(-\infty,-1]\cup(2,\infty).
$$

</div>

<div class="theorem-box">

**Example.** Let

$$
f(u)=
\begin{cases}
u+2, & u<2,\\
5, & u=2,\\
u^2-1, & u>2,
\end{cases}
$$

and

$$
g(x)=
\begin{cases}
1+x^2\sin(1/x), & x<0,\\
1, & x=0,\\
1+x^2, & 0<x<1,\\
x, & x\ge1.
\end{cases}
$$

Determine whether $$h(x)=f(g(x))$$ is continuous at $$x=0$$ and $$x=2$$. Justify both answers.

At $$x=0$$, the inside function approaches $$1$$ from both sides:

$$
\lim_{x\to0^-}g(x)
=
\lim_{x\to0^-}\left(1+x^2\sin(1/x)\right)
=
1
$$

by the Squeeze Theorem, and

$$
\lim_{x\to0^+}g(x)
=
\lim_{x\to0^+}(1+x^2)
=
1.
$$

Also $$g(0)=1$$. Since $$f(u)=u+2$$ near $$u=1$$, $$f$$ is continuous at $$1$$. Therefore

$$
\lim_{x\to0}h(x)
=
\lim_{x\to0}f(g(x))
=
f(1)
=
h(0).
$$

So $$h$$ is continuous at $$x=0$$.

At $$x=2$$, the inside function is simply $$g(x)=x$$ near $$2$$, so $$g(x)\to2$$ and $$g(2)=2$$. But $$f$$ is not continuous at $$u=2$$:

$$
\lim_{u\to2^-}f(u)=4
\qquad\text{and}\qquad
\lim_{u\to2^+}f(u)=3,
$$

while $$f(2)=5$$. This discontinuity gets passed through the composite:

$$
\lim_{x\to2^-}h(x)=4
\qquad\text{and}\qquad
\lim_{x\to2^+}h(x)=3.
$$

So $$h$$ is not continuous at $$x=2$$.

</div>

---

## Squeeze Theorem

<div class="theorem-box">

**Theorem (Squeeze Theorem).** If $$g(x) \le f(x) \le h(x)$$ for all $$x$$ near $$a$$, and

$$
\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L,
$$

then

$$
\lim_{x \to a} f(x) = L.
$$

</div>

<div class="theorem-box">

**Proof (Squeeze Theorem).** If $$g(x) \le f(x) \le h(x)$$ and both outside functions are forced close to $$L$$, then $$f(x)$$ has nowhere else to go. For inputs close enough to $$a$$, both $$g(x)$$ and $$h(x)$$ lie inside a tiny band around $$L$$. Since $$f(x)$$ is trapped between them, it must lie inside the same band.

</div>

<div class="theorem-box">

**Example.** Show that $$\displaystyle\lim_{x\to0}x\sin\frac{1}{x}=0.$$

The sine factor is bounded by $$-1\le\sin\frac{1}{x}\le1$$ for all nonzero $$x$$. Multiply through by $$\lvert x\rvert$$ to obtain

$$
-\lvert x\rvert \le x\sin\frac{1}{x} \le \lvert x\rvert.
$$

Since both outer bounds tend to $$0$$ as $$x\to0$$, the Squeeze Theorem gives

$$
\lim_{x\to0}x\sin\frac{1}{x}=0.
$$

</div>

## Solving Trig Limits

Two key trig limits that appear often are:

$$
\lim_{x \to 0} \frac{\sin x}{x} = 1,
$$

$$
\lim_{x \to 0} \frac{\tan x}{x} = 1.
$$

To use these limits, rewrite the trig expression to match one of these forms. The same result does not hold for $$\cos x$$ in the numerator. Since $$\cos x\to1$$ while $$x\to0$$, the quotient $$\frac{\cos x}{x}$$ becomes unbounded. The two-sided limit does not exist.

:::conditions
These two trig limits are valid only when the angle is measured in **radians**. As an exercise, you can try to derive the corresponding versions when $$x$$ is in degrees.
:::

<div class="theorem-box">

**Proof (The limit of sine over angle).** For $$0<x<\frac{\pi}{2}$$, compare three areas in the unit circle: the inner triangle, the circular sector, and the outer tangent triangle.

```tikz
\usepackage{tikz}
\begin{tikzpicture}[scale=2.2]
\draw[->] (-0.1,0) -- (1.35,0) node[right] {$x$};
\draw[->] (0,-0.1) -- (0,1.2) node[above] {$y$};
\draw[thick] (1,0) arc[start angle=0,end angle=55,radius=1];
\draw[thick] (0,0) -- (1,0);
\draw[thick] (0,0) -- (55:1);
\draw[dashed] (1,0) -- (1,{tan(55)});
\draw[thick] (0,0) -- (1,{tan(55)});
\draw[fill=black] (55:1) circle (0.7pt) node[above left] {$(\cos x,\sin x)$};
\draw (0.28,0) arc[start angle=0,end angle=55,radius=0.28];
\node at (0.36,0.18) {$x$};
\node[below] at (0.5,0) {$1$};
\node[right] at (1,0.72) {$\tan x$};
\end{tikzpicture}
```

For this picture, the inner triangle has area $$\frac12\sin x\cos x$$, the sector has area $$\frac12x$$, and the outer triangle has area $$\frac12\tan x$$. Therefore,

$$
\frac12\sin x\cos x
\le
\frac12x
\le
\frac12\tan x.
$$

Multiply by $$2$$:

$$
\sin x\cos x\le x\le\tan x.
$$

Since $$\tan x=\frac{\sin x}{\cos x}$$ and all quantities are positive on $$0<x<\frac{\pi}{2}$$, divide by $$\sin x$$:

$$
\cos x\le\frac{x}{\sin x}\le\frac{1}{\cos x}.
$$

Taking reciprocals reverses the useful form:

$$
\cos x\le\frac{\sin x}{x}\le1.
$$

As $$x\to0^+$$, both outer expressions approach $$1$$, so the Squeeze Theorem gives

$$
\lim_{x\to0^+}\frac{\sin x}{x}=1.
$$

Since $$\sin x/x$$ is an even function, the left-hand limit is also $$1$$. Therefore,

$$
\lim_{x\to0}\frac{\sin x}{x}=1.
$$

Using this result, we have

$$
\lim_{x\to0}\frac{\tan x}{x} = \lim_{x\to0}\frac{\sin x}{x \cos x} = \lim_{x\to0}\frac{\sin x}{x} \cdot \lim_{x\to0}\frac{1}{\cos x} = 1 \cdot 1 = 1
$$

</div>

Many indeterminate trig limits become standard limits after rewriting the angle or using an identity. Look for a way to create a factor like

$$
\frac{\sin u}{u}
$$

where $$u\to0$$ (or the equivalent tangent version) and then cancel it out of the equation. In fact, $$\lim_{x\to0}\frac{\sin u}{u}$$ is often referred to as the "savior" limit since with almost all indeterminate trig limits, $$\frac{\sin x}{x}$$ shows up and can get cancelled. Note that $$\lim_{x\to0}\frac{u}{\sin u}$$ is equivalent to the savior limit (since the reciprocal of $$1$$ is $$1$$.)

<div class="theorem-box">

**Example.** Evaluate

$$
\lim_{x\to0}\frac{1-\cos(2x)}{x^2}.
$$

Use the identity

$$
1-\cos(2x)=2\sin^2 x.
$$

Then

$$
\lim_{x\to0}\frac{1-\cos(2x)}{x^2}
=
\lim_{x\to0}\frac{2\sin^2 x}{x^2}
=
\lim_{x\to0}2\left(\frac{\sin x}{x}\right)^2.
$$

As $$x\to0$$, $$\frac{\sin x}{x}\to1$$, so

$$
\lim_{x\to0}\frac{1-\cos(2x)}{x^2}=2.
$$

</div>

<div class="theorem-box">

**Example.** Evaluate

$$
\lim_{x\to0}\frac{1-\cos(3x)}{\cos^2(5x)-1}.
$$

Use the identities

$$
1-\cos(3x)=2\sin^2\left(\frac{3x}{2}\right)
$$

and

$$
\cos^2(5x)-1=-\sin^2(5x).
$$

Then

$$
\lim_{x\to0}\frac{1-\cos(3x)}{\cos^2(5x)-1}
=
\lim_{x\to0}
\frac{2\sin^2\left(\frac{3x}{2}\right)}{-\sin^2(5x)}.
$$

Rewrite the sine factors so each has the form $$\sin u/u$$:

$$
\lim_{x\to0}
-2
\left(\frac{\sin\left(\frac{3x}{2}\right)}{\frac{3x}{2}}\right)^2
\left(\frac{\frac{3x}{2}}{5x}\right)^2
\left(\frac{5x}{\sin(5x)}\right)^2.
$$

The two standard-limit factors approach $$1$$, so the limit is

$$
-2\left(\frac{3}{10}\right)^2
=
-\frac{9}{50}.
$$

</div>

<div class="theorem-box">

**Example.** Evaluate

$$
\lim_{x\to0^+}\frac{\sin(1/x)}{1/x}.
$$

Let $$u=\frac{1}{x}$$. As $$x\to0^+$$, $$u\to\infty$$, so the limit becomes

$$
\lim_{u\to\infty}\frac{\sin u}{u}.
$$

The numerator oscillates between $$-1$$ and $$1$$, while the denominator grows without bound. Since

$$
-\frac{1}{u}\le\frac{\sin u}{u}\le\frac{1}{u}
$$

for $$u>0$$, and both outer bounds approach $$0$$ as $$u\to\infty$$, the Squeeze Theorem gives

$$
\lim_{u\to\infty}\frac{\sin u}{u}=0.
$$

Therefore,

$$
\lim_{x\to0^+}\frac{\sin(1/x)}{1/x}=0.
$$

</div>

---

## Formal limit definition

We have talked about limits in the general sense, where it maps out the behavior near a point. But how do we formalize it? The statement

$$
\lim_{x\to a}f(x)=L
$$

means that every small output tolerance around $$L$$ can be guaranteed by choosing a sufficiently small input window around $$a$$, excluding $$x=a$$ itself.

In symbols, for every $$\varepsilon>0$$, there is a $$\delta>0$$ such that

$$
0<\lvert x-a\rvert<\delta
\quad\Longrightarrow\quad
\lvert f(x)-L\rvert<\varepsilon.
$$

The formal definition is also useful for understanding why limit statements are stronger than a graph or table. A table can suggest that the output is approaching $$L$$, but an epsilon-delta proof says that every possible tolerance can be handled.

:::strategy
1. Start with $$\lvert f(x)-L\rvert<\varepsilon$$.
2. Rewrite it until it is controlled by $$\lvert x-a\rvert$$.
3. Choose $$\delta$$ small enough to force the desired inequality.
4. Finish by showing that $$0<\lvert x-a\rvert<\delta$$ implies $$\lvert f(x)-L\rvert<\varepsilon$$.
:::

<div class="theorem-box">

**Example.** Use the epsilon definition to prove

$$
\lim_{x\to 3}(2x+1)=7.
$$

We want to make $$\lvert (2x+1)-7\rvert<\varepsilon$$. Simplify the expression:

$$
\lvert (2x+1)-7\rvert=\lvert 2x-6\rvert=2\lvert x-3\rvert.
$$

So it is enough to require

$$
2\lvert x-3\rvert<\varepsilon,
$$

which is the same as

$$
\lvert x-3\rvert<\frac{\varepsilon}{2}.
$$

Choose

$$
\delta=\frac{\varepsilon}{2}.
$$

Then whenever $$0<\lvert x-3\rvert<\delta$$, we have

$$
\lvert (2x+1)-7\rvert=2\lvert x-3\rvert<2\delta=2\cdot\frac{\varepsilon}{2}=\varepsilon.
$$

Therefore, by the formal definition,

$$
\lim_{x\to3}(2x+1)=7.
$$

</div>

---

## Intermediate Value Theorem

<div class="theorem-box">

**Theorem (Intermediate Value Theorem).** If $$f$$ is continuous on $$[a,b]$$ and $$N$$ lies between $$f(a)$$ and $$f(b)$$, then there exists some $$c \in (a,b)$$ such that $$f(c) = N$$.

</div>

<div class="theorem-box">

**Proof (IVT).** Assume $$f(a)<N<f(b)$$. Define

$$
g(x)=f(x)-N.
$$

Then $$g$$ is continuous on $$[a,b]$$, and

$$
g(a)=f(a)-N<0,
\qquad
g(b)=f(b)-N>0.
$$

Let

$$
S=\{x\in[a,b]\mid g(x)<0\}.
$$

The set $$S$$ is nonempty because $$a\in S$$, and it is bounded above by $$b$$. Let $$c=\sup S$$. Since $$g$$ is continuous, $$g(c)$$ cannot be negative or positive. If $$g(c)<0$$, then values slightly to the right of $$c$$ would still be negative, contradicting that $$c$$ is the least upper bound. If $$g(c)>0$$, then values slightly to the left of $$c$$ would be positive, contradicting the fact that points of $$S$$ can get arbitrarily close to $$c$$ from the left.

Therefore,

$$
g(c)=0.
$$

So

$$
f(c)-N=0
\quad\Longrightarrow\quad
f(c)=N.
$$

The case $$f(b)<N<f(a)$$ follows by applying the same argument to $$-g(x)$$.

This may seem very jargony, and you will learn more about the notations in linear algebra. For now, the proof is not very important to know.

</div>


This theorem guarantees at least one solution, but it does not tell you how many.

<div class="theorem-box">

**Example.** Show that the equation

$$
x^3+x-1=0
$$

has at least one solution on the interval $$[0,1]$$.

Let

$$
f(x)=x^3+x-1.
$$

This function is a polynomial, so it is continuous on $$[0,1]$$. Check the endpoint values:

$$
f(0)=0^3+0-1=-1
$$

and

$$
f(1)=1^3+1-1=1.
$$

Since $$0$$ lies between $$-1$$ and $$1$$, the Intermediate Value Theorem guarantees that there is some number $$c\in(0,1)$$ such that

$$
f(c)=0.
$$

That means

$$
c^3+c-1=0.
$$

So the equation has at least one solution between $$0$$ and $$1$$. Notice that IVT proves the solution exists, but it does not tell us the exact value of $$c$$.

</div>

---

## Tips for the exam

Limit questions are often about deciding which tool is allowed before doing any algebra.

:::checklist
1. Try direct substitution first.
2. If substitution gives a finite value, the limit is usually finished.
3. If substitution gives $$0/0$$, try factoring, conjugates, common denominators, or trig-limit rewrites.
4. If one-sided limits disagree, the two-sided limit does not exist.
5. For continuity, check the value, the two-sided limit, and whether they match.
:::

:::exam{topic="Limit justification"}
When a question asks you to justify existence, say why both sides approach the same value (both one-sided limits exist and agree). When a limit does not exist, name the reason: different one-sided limits, unbounded behavior (asymptote), or oscillation.
:::
