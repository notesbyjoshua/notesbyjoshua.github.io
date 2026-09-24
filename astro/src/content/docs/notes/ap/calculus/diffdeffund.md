---
title: "Unit 2: Differentiation: Definition and Fundamental Properties"
description: "AP Calculus notes on derivative definitions, basic rules, tangent lines, rates of change, and fundamental differentiation skills."
sidebar:
  order: 2
---

## Rates of change and the derivative

How do we measure the slope of a tangent line? Before talking about tangent lines, start with something we already know how to measure: the slope of a secant line. If a curve $$y=f(x)$$ passes through the points $$x=a$$ and $$x=b$$, then the secant slope is

$$
\frac{f(b)-f(a)}{b-a}.
$$

This is the average rate of change on $$[a,b]$$. Geometrically, it is the slope of the line connecting two points on the graph.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle, xmin=-0.4, xmax=3.6, ymin=-0.3, ymax=5.5,
  xtick={0,1,2,3}, ytick={0,1,2,3,4,5},
  grid=both, grid style={gray!18},
  width=8.8cm, height=6.2cm,
  xlabel=$x$, ylabel=$y$,
]
\addplot[blue, very thick, samples=160, domain=0:3.3] {0.5*x^2+0.4};
\addplot[gray!70, dashed, thick, domain=1.15:3.2] {2.25*x-1.85};
\addplot[orange!85!black, thick, domain=0.75:2.45] {1.5*x-0.725};
\addplot[only marks, mark=*, mark size=1.8pt, blue] coordinates {(1.5,1.525)};
\addplot[only marks, mark=*, mark size=1.5pt, gray!70] coordinates {(3,4.9)};
\node[gray!70!black, anchor=west] at (axis cs:1.95,4.35) {secant};
\node[blue, anchor=east] at (axis cs:1.45,1.55) {$x=a$};
\node[orange!85!black, anchor=west] at (axis cs:2.15,2.35) {tangent};
\end{axis}
\end{tikzpicture}
```

To get the slope of the tangent line at $$x=a$$, move the second point closer and closer to $$a$$. Suppose that we want the tangent slope at point $$P = (a, f(a))$$ on $$f(x)$$. Define a point $$Q = (x, f(x))$$ also on $$f(x)$$ and connect the secant line $$PQ$$. The secant line rotates toward the tangent line, so the tangent slope is the limiting value of those secant slopes:

$$
m_{\text{tangent}}
=
\lim_{Q\to P}m_{PQ}.
$$

The slope of the secant line through $$P$$ and $$Q$$ is

$$
m_{PQ}
=
\frac{f(x)-f(a)}{x-a}.
$$

When $$Q\to P$$ along the graph, its $$x$$-coordinate approaches the $$x$$-coordinate of $$P$$. In other words, $$x\to a$$. Therefore,

$$
m_{\text{tangent at }x=a}
=
\lim_{x\to a}\frac{f(x)-f(a)}{x-a}.
$$

The denominator measures horizontal change (the "run" of the slope formula), and the numerator measures vertical change (the "rise" of the slope formula). The limit asks what that ratio becomes when the two points collapse into one point.

Equivalently, instead of naming the nearby input $$x$$, write it as $$a+h$$, where $$h$$ is the horizontal change from $$a$$. Then the secant slope becomes

$$
\frac{f(a+h)-f(a)}{h}.
$$

This is known as the **difference quotient**. As the second point moves toward $$a$$, the horizontal change $$h$$ moves toward $$0$$, so the tangent slope is

$$
\lim_{h\to0}\frac{f(a+h)-f(a)}{h}.
$$

The two formulas are equivalent because $$x=a+h$$, so $$h=x-a$$.

<div class="theorem-box">

**Example.** For $$f(x)=x^2+1$$, find the slope of the tangent line at $$x=3$$ using the first method.

Use $$a=3$$:

$$
\lim_{x\to3}\frac{f(x)-f(3)}{x-3}.
$$

Since $$f(3)=10$$,

$$
\lim_{x\to3}\frac{x^2+1-10}{x-3}
=
\lim_{x\to3}\frac{x^2-9}{x-3}.
$$

Factor and cancel:

$$
\lim_{x\to3}\frac{(x-3)(x+3)}{x-3}
=
\lim_{x\to3}(x+3)
=
6.
$$

So the tangent slope at $$x=3$$ is $$6$$.

</div>

<div class="theorem-box">

**Example.** For $$f(x)=2x^2-x$$, find the slope of the tangent line at $$x=1$$ using the second method.

Start with

$$
\lim_{h\to0}\frac{f(1+h)-f(1)}{h}.
$$

Compute the two function values:

$$
f(1+h)=2(1+h)^2-(1+h)
=1+3h+2h^2,
$$

and

$$
f(1)=1.
$$

Then

$$
\lim_{h\to0}\frac{f(1+h)-f(1)}{h}
=
\lim_{h\to0}\frac{1+3h+2h^2-1}{h}.
$$

Simplify:

$$
\lim_{h\to0}\frac{3h+2h^2}{h}
=
\lim_{h\to0}(3+2h)
=
3.
$$

So the tangent slope at $$x=1$$ is $$3$$.

</div>

### Definition of the derivative

<div class="theorem-box">

**Definition.** The derivative of $$f$$ at $$x$$ is defined as

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}
$$

Equivalently, for a derivative at $$x=a$$, the derivative becomes the tangent line at $$a$$:

$$
f'(a) = \lim_{x \to a} \frac{f(x)-f(a)}{x-a}.
$$

</div>

There are many interpretations of the derivative:

- instantaneous rate of change,
- slope of the tangent line,
- limit of secant slopes,
- local sensitivity of output to input.

<div class="theorem-box">

**Example.** Use the limit definition to find $$f'(x)$$ to find the derivative for $$f(x)=\frac{2}{x}$$.

Start with the $$h$$ form:

$$
f'(x)
=
\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.
$$

Substitute $$f(x)=2/x$$:

$$
f'(x)
=
\lim_{h\to0}\frac{\frac{2}{x+h}-\frac{2}{x}}{h}.
$$

Combine the fractions in the numerator:

$$
\frac{2}{x+h}-\frac{2}{x}
=
\frac{2x-2(x+h)}{x(x+h)}
=
\frac{-2h}{x(x+h)}.
$$

So

$$
f'(x)
=
\lim_{h\to0}\frac{\frac{-2h}{x(x+h)}}{h}.
$$

Dividing by $$h$$ is the same as multiplying by $$1/h$$:

$$
f'(x)
=
\lim_{h\to0}\frac{-2h}{x(x+h)}\cdot\frac{1}{h}.
$$

Cancel $$h$$:

$$
f'(x)
=
\lim_{h\to0}\frac{-2}{x(x+h)}.
$$

Now let $$h\to0$$:

$$
f'(x)
=
\frac{-2}{x^2}.
$$

Therefore,

$$
\frac{d}{dx}\left(\frac{2}{x}\right)
=
-\frac{2}{x^2}.
$$

This formula is valid for $$x\ne0$$, because the original function is not defined at $$x=0$$. Note that $$\frac{d}{dx}$$ is a notation for the derivative.

</div>

### Notation for derivatives

There exists many different notations for derivatives, but the most common ones are:

$$
f'(x),\qquad y',\qquad \frac{dy}{dx},\qquad \frac{d}{dx}[f(x)].
$$

They all refer to rate of change, but they emphasize different things. The notation $$f'(a)$$ is a number. The notation $$f'(x)$$ is a function (as long as $$x$$ is the variable). The notation $$dy/dx$$ emphasizes that the derivative compares a tiny change in $$y$$ to a tiny change in $$x$$.

When a problem asks for "the derivative at $$x=a$$," give a value. When it asks for "the derivative of $$f$$," give a formula.

If $$f(x)$$ has units of output and $$x$$ has units of input, then $$f'(x)$$

has units

$$
\frac{\text{output units}}{\text{input units}}.
$$

For instance, if position is measured in feet and time in seconds, velocity is measured in feet per second. The sign tells direction; the magnitude tells how fast the position is changing.

The Leibniz Notation ($$\frac{dy}{dx}$$) is especially useful for problems that require context. For example, if $$s(t)$$ is position, then $$s'(t)$$ and $$ds/dt$$ both describe velocity. The notation $$ds/dt$$ makes units especially clear because it literally compares a change in position to a change in time.

For a quantity $$Q$$ depending on another quantity $$x$$: $$\frac{dQ}{dx}$$ has units of $$Q$$-units per $$x$$-unit. This unit check is one of the fastest ways to catch an interpretation error.

### Differentiability of functions

<div class="theorem-box">

**Definition.** A function is said to be *differentiable* on an interval $$[a,b]$$ if it's derivative exists in *all* of its domain.

</div>

The domain of $$f'$$ can be smaller than the domain of $$f$$. Even if $$f(a)$$ exists, the derivative at $$a$$ may fail to exist because the nearby slopes do not settle into one finite value or diverge to infinity.

When finding a derivative formula, always ask where that formula is valid. For example,

$$
f(x)=\sqrt{x}
$$

has domain $$[0,\infty)$$, but it's derivative

$$
f'(x)=\frac{1}{2\sqrt{x}}
$$

is valid only for $$x>0$$. The original function exists at $$x=0$$, but the tangent there is vertical, so the ordinary derivative is not finite.

From a graph, differentiability fails at places where the tangent slope is not a single finite number.

// add the theorem where it is like if a function is continuous it is differentiable (so equivalently if it is not differentiable it is not continuous)

// add common types of continuous but not differentiable functions

---

## Basic derivative rules

For constants $$c$$ and differentiable functions $$f,g$$:

$$
\frac{d}{dx}(c) = 0
$$

$$
\frac{d}{dx}(x^n) = nx^{n-1}
$$

$$
\frac{d}{dx}[cf(x)] = cf'(x)
$$

$$
\frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)
$$

$$
\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)
$$

$$
\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right]
=
\frac{f'(x)g(x)-f(x)g'(x)}{[g(x)]^2}
$$

for $$g(x) \ne 0$$.

The theorems can all be proven by just plugging in the parent function into the derivative definition, so I will only show one example proof below.

<div class="theorem-box">

**Proof (Product Rule).** Let $$H(x)=f(x) \cdot g(x)$$

Start from the derivative definition:

$$
\frac{d}{dx}H(x)
=
\lim_{h\to0}\frac{H(x+h)-H(x)}{h}.
$$

Resubstituting:

$$
\frac{d}{dx}H(x)
=
\lim_{h\to0}\frac{f(x+h)g(x+h)-f(x)g(x)}{h}.
$$

Now, do an algebra trick: We can add and then subtract $$f(x+h)g(x)$$ to our expression to factor:

$$
\frac{d}{dx}H(x)
=
\lim_{h\to0}
\frac{
f(x+h)g(x+h)-f(x+h)g(x)
+f(x+h)g(x)-f(x)g(x)
}{h}
$$

Split the fraction into two limits:

$$
\frac{d}{dx}H(x)
=
\lim_{h\to0}f(x+h)\frac{g(x+h)-g(x)}{h}
+
\lim_{h\to0}g(x)\frac{f(x+h)-f(x)}{h}.
$$

Now split off the limits that become derivative definitions:

$$
\frac{d}{dx}H(x)
=
\left(\lim_{h\to0}f(x+h)\right)g'(x)
+g(x)f'(x).
$$

This uses the sum rule for limits and the fact that $$g(x)$$ is constant with respect to $$h$$.

$$
\lim_{h\to0}\frac{g(x+h)-g(x)}{h}=g'(x),
\qquad
\lim_{h\to0}\frac{f(x+h)-f(x)}{h}=f'(x).
$$

Because $$f$$ is differentiable at $$x$$, it is also continuous at $$x$$. Therefore

$$
\lim_{h\to0}f(x+h)=f(x).
$$

Substitute these limits back in:

$$
\frac{d}{dx}H(x)
=f(x)g'(x)+g(x)f'(x).
$$

Since multiplication is commutative, this is usually written as

$$
\frac{d}{dx}[f(x)g(x)]=f'(x)g(x)+f(x)g'(x).
$$

Note that if you have more than two functions, the procedure is the same, giving you a result where you sum up the multiplicative terms between one derivative and the other functions for each derivative.

</div>

<div class="theorem-box">

**Example.** Differentiate $$y = x^3 \sin x$$.

Let $$f(x)=x^3$$ and $$g(x)=\sin x$$, so $$f'(x)=3x^2$$ and $$g'(x)=\cos x$$. The product rule gives

$$
y' = f'(x)g(x) + f(x)g'(x).
$$

Substitute the pieces:

$$
y' = 3x^2\sin x + x^3\cos x.
$$

So $$y' = 3x^2\sin x + x^3\cos x$$.

</div>

<div class="theorem-box">

**Example.** Differentiate $$\displaystyle y = \frac{x^2}{x+1}$$.

Let $$f(x)=x^2$$ and $$g(x)=x+1$$, so $$f'(x)=2x$$ and $$g'(x)=1$$. The quotient rule gives

$$
y' = \frac{f'(x)g(x)-f(x)g'(x)}{[g(x)]^2}.
$$

Substitute the pieces:

$$
y' = \frac{2x(x+1)-x^2(1)}{(x+1)^2}.
$$

Expand and simplify the numerator:

$$
2x(x+1)-x^2 = 2x^2+2x-x^2 = x^2+2x.
$$

Therefore

$$
y' = \frac{x^2+2x}{(x+1)^2}.
$$

</div>

---

## Derivatives of common functions

### Derivatives of trig functions

$$
\frac{d}{dx}(\sin x) = \cos x
$$

$$
\frac{d}{dx}(\cos x) = -\sin x
$$

$$
\frac{d}{dx}(\tan x) = \sec^2 x
$$

$$
\frac{d}{dx}(\sec x)=\sec x\tan x,
$$

$$
\frac{d}{dx}(\csc x)=-\csc x\cot x,
$$

$$
\frac{d}{dx}(\cot x)=-\csc^2 x.
$$

All of the trig derivatives can be proved using the derivative definition and the quotient rule, so we will only use a couple examples.

<div class="theorem-box">

**Proof (Derivative of $$tan x$$).** Start with the identity

$$
\tan x=\frac{\sin x}{\cos x}.
$$

Use the quotient rule:

$$
\frac{d}{dx}(\tan x)
=
\frac{(\frac{d}{dx} \sin x)(\cos x)-(\sin x)(\frac{d}{dx} \cos x)}{\cos^2 x}.
$$

For sine, start with the derivative definition:

$$
\frac{d}{dx}(\sin x)
=
\lim_{h\to0}\frac{\sin(x+h)-\sin x}{h}.
$$

Use $$\sin(x+h)=\sin x\cos h+\cos x\sin h$$:

$$
\frac{\sin(x+h)-\sin x}{h}
=
\sin x\frac{\cos h-1}{h}
+\cos x\frac{\sin h}{h}.
$$

Since

$$
\lim_{h\to0}\frac{\sin h}{h}=1,
\qquad
\lim_{h\to0}\frac{\cos h-1}{h}=0,
$$

we get

$$
\frac{d}{dx}(\sin x)=\cos x.
$$

For cosine, use $$\cos(x+h)=\cos x\cos h-\sin x\sin h$$:

$$
\frac{\cos(x+h)-\cos x}{h}
=
\cos x\frac{\cos h-1}{h}
-\sin x\frac{\sin h}{h}.
$$

Taking the same two standard trig limits gives

$$
\frac{d}{dx}(\cos x)=-\sin x.
$$

Thus,

$$
\frac{d}{dx}(\tan x)
=
\frac{(\cos x)(\cos x)-(\sin x)(-\sin x)}{\cos^2 x}.
$$

Simplify the numerator:

$$
\frac{d}{dx}(\tan x)
=
\frac{\cos^2 x+\sin^2 x}{\cos^2 x}
=
\frac{1}{\cos^2 x}
=
\sec^2 x.
$$

</div>

<div class="theorem-box">

**Proof (Derivative of $$\tan x$$).**

</div>

### Derivatives of exponential and logarithmic functions

Exponential functions are special because their rate of change is proportional to their current value. For $$a^x$$, the derivative is some constant multiple of $$a^x$$:

$$
\frac{d}{dx}(a^x)=a^x\ln a.
$$

The base $$e$$ is the unique positive base where that constant is $$1$$. In other words, $$e^x$$ is the exponential function whose derivative is exactly itself. Logarithm derivatives come from the fact that logarithms are inverse functions of exponentials.

$$
\frac{d}{dx}(e^x) = e^x
$$

$$
\frac{d}{dx}(a^x) = a^x \ln a
$$

$$
\frac{d}{dx}(\ln x) = \frac{1}{x}
$$

$$
\frac{d}{dx}(\log_a x)=\frac{1}{x\ln a},
\qquad a>0,\ a\ne 1.
$$

The proofs for these formulas can be proved using techniques from Unit 3.

### Derivatives of hyperbolic functions

As a reminder, we define

$$
\sinh x=\frac{e^x-e^{-x}}{2},
\qquad
\cosh x=\frac{e^x+e^{-x}}{2}.
$$

The other hyperbolic functions are defined similarly to trig functions (e.g. $$\tanh x = \frac{\sinh x}{\cosh x}$$). Their main derivatives are:

$$
\frac{d}{dx}(\sinh x)=\cosh x,
\qquad
\frac{d}{dx}(\cosh x)=\sinh x,
$$

$$
\frac{d}{dx}(\tanh x)=\operatorname{sech}^2 x.
$$

$$
\frac{d}{dx}(\operatorname{sech} x)=-\operatorname{sech} x\tanh x,
$$

$$
\frac{d}{dx}(\operatorname{csch} x)=-\operatorname{csch} x\coth x,
$$

$$
\frac{d}{dx}(\coth x)=-\operatorname{csch}^2 x.
$$

Since all of the hyperbolic functions can be defined in terms of exponentials, the derivative formula is just repeated derivatives of exponentials. The proofs are left to the reader as an exercise.

<div class="theorem-box">

**Example.** Differentiate $$y = 4e^x - 3\cos x + 2x^5$$.

Differentiate each term separately using the sum rule. The exponential is its own derivative, the derivative of $$\cos x$$ is $$-\sin x$$, and the power rule applies to $$x^5$$:

$$
\frac{d}{dx}(4e^x) = 4e^x,\qquad
\frac{d}{dx}(-3\cos x) = 3\sin x,\qquad
\frac{d}{dx}(2x^5) = 10x^4.
$$

Combining the terms gives

$$
y' = 4e^x + 3\sin x + 10x^4.
$$

</div>

<div class="theorem-box">

**Example.** Differentiate

$$
y=5\log_2 x \cdot 3\sec x+4\sinh x.
$$

This is a product plus one hyperbolic term. First rewrite the product with the constant out front:

$$
y=15(\log_2 x)(\sec x)+4\sinh x.
$$

Use the product rule on $$(\log_2 x)(\sec x)$$:

$$
\frac{d}{dx}\left[(\log_2 x)(\sec x)\right]
=
\frac{1}{x\ln 2}\sec x
+
(\log_2 x)\sec x\tan x.
$$

Also,

$$
\frac{d}{dx}(4\sinh x)=4\cosh x.
$$

Therefore

$$
y'=15\left(\frac{\sec x}{x\ln 2}+(\log_2 x)\sec x\tan x\right)+4\cosh x.
$$

</div>

---

## Choosing derivative procedures

Most derivative problems are not about one isolated rule. They are about choosing the order in which rules apply.

:::strategy
1. Simplify obvious algebra first, especially constants and powers.
2. Identify the outermost operation: sum, product, quotient, power, trig, exponential, or logarithm.
3. Apply the rule for the outermost operation.
4. Use the chain rule whenever the input is more than just $$x$$.
5. Check whether the final expression can be simplified without hiding the structure.
:::

<div class="theorem-box">

**Example.** Differentiate

$$
y=\frac{x^2e^x}{\sqrt{x+1}}.
$$

This can be treated as a quotient, but rewriting the radical as a power makes the product structure easier:

$$
y=x^2e^x(x+1)^{-1/2}.
$$

This rewrite uses the exponent rule $$\sqrt{x+1}=(x+1)^{1/2}$$, so dividing by $$\sqrt{x+1}$$ is the same as multiplying by $$(x+1)^{-1/2}$$. Now the function is a product of three factors instead of a quotient with a radical.

This is a product of three factors. The expanded product rule says to differentiate one factor at a time and leave the other factors alone. For three factors,

$$
(uvw)'=u'vw+uv'w+uvw'.
$$

Here,

$$
u=x^2,\qquad v=e^x,\qquad w=(x+1)^{-1/2}.
$$

Use the product rule in expanded form:

$$
y'=(2x)e^x(x+1)^{-1/2}
+x^2(e^x)(x+1)^{-1/2}
+x^2e^x\left(-\frac12\right)(x+1)^{-3/2}.
$$

Factor the common term $$xe^x(x+1)^{-3/2}$$:

$$
y'=xe^x(x+1)^{-3/2}
\left[2(x+1)+x(x+1)-\frac{x}{2}\right].
$$

This form shows the structure clearly. If desired, it can be combined into one rational expression, but the important part is choosing the rule order correctly.

</div>

---

## Tangent and normal lines

At $$x=a$$:

- tangent slope is $$f'(a)$$,
- tangent line is

$$
y - f(a) = f'(a)(x-a),
$$

- normal slope is $$-1/f'(a)$$ when $$f'(a) \ne 0$$.

<div class="theorem-box">

**Example.** Find the equation of the tangent line to $$f(x)=x^3+e^x$$ at $$x=2$$.

First find the point on the curve:

$$
f(2)=2^3+e^2=8+e^2,
$$

so the point of tangency is $$(2,8+e^2)$$. Next find the slope from the derivative:

$$
f'(x)=3x^2+e^x,\qquad f'(2)=3(2)^2+e^2=12+e^2.
$$

Use point-slope form with slope $$12+e^2$$ at $$(2,8+e^2)$$:

$$
y-(8+e^2) = (12+e^2)(x-2).
$$

Simplifying gives the tangent line

$$
y = (12+e^2)x-(16+3e^2).
$$

</div>

---

## Higher derivatives

The second derivative $$f''(x)$$ measures the rate of change of the first derivative.

The second derivative has many useful interpretations:

- concavity (whether a graph is opening up or down) in pure math
- acceleration when $$f$$ is position or angular frequency when $$f$$ is potential in physics

You may also see $$f^{(n)}(x)$$ for the $$n$$th derivative. Basically, higher order derivatives just means take the derivative of a function $$n$$ times.

<div class="theorem-box">

**Example.** Find $$f''(x)$$ for $$f(x)=x^4-5x^2+3x$$.

Differentiate once using the power rule term by term:

$$
f'(x)=4x^3-10x+3.
$$

Differentiate again to get the second derivative:

$$
f''(x)=12x^2-10.
$$

</div>

### Alternate notation for higher-order derivatives

Higher derivatives have several common notations. If $$y=f(x)$$, then:

| Order | Prime notation | Leibniz notation | Function notation |
|---|---|---|---|
| First | $$y'$$ | $$\frac{dy}{dx}$$ | $$f'(x)$$ |
| Second | $$y''$$ | $$\frac{d^2y}{dx^2}$$ | $$f''(x)$$ |
| Third | $$y'''$$ | $$\frac{d^3y}{dx^3}$$ | $$f'''(x)$$ |
| $$n$$th | $$y^{(n)}$$ | $$\frac{d^ny}{dx^n}$$ | $$f^{(n)}(x)$$ |

The notation $$\frac{d^2y}{dx^2}$$ means "differentiate $$y$$ with respect to $$x$$ twice." It does not mean a fraction where $$dx$$ is squared in the usual algebraic sense.

---

## Differentiation from tables

If you only have values of $$f$$, use the difference quotient for an approximate derivative:

$$
f'(a) \approx \frac{f(a+h)-f(a)}{h}
$$

or a symmetric estimate:

$$
f'(a) \approx \frac{f(a+h)-f(a-h)}{2h}.
$$

<div class="theorem-box">

**Example.** A differentiable function $$f$$ has the values below. Estimate $$f'(2)$$ using a symmetric difference quotient.

$$
\begin{array}{c|ccc}
x & 1 & 2 & 3 \\\hline
f(x) & 3 & 7 & 15
\end{array}
$$

Use the values one step on each side of $$x=2$$, so $$a=2$$ and $$h=1$$:

$$
f'(2)\approx\frac{f(3)-f(1)}{2(1)}=\frac{15-3}{2}.
$$

This simplifies to

$$
f'(2)\approx\frac{12}{2}=6.
$$

The symmetric estimate uses points on both sides, so it usually gives a more accurate approximation than a one-sided difference quotient.

</div>

---

## Tips for the exam

Most derivative questions are rule-recognition questions with algebra mixed in. The safest way to work is to identify the outer structure before differentiating.

:::checklist
1. Simplify constants and obvious powers first.
2. Decide whether the main operation is a sum, product, quotient, composition, or implicit relationship.
3. Write one intermediate derivative step before simplifying.
4. Keep domain restrictions in mind for roots, logarithms, quotients, inverse trig, and tangent/normal line slopes.
5. Attach units when the derivative comes from a context.
:::

:::exam{topic="Derivative notation"}
AP questions may switch among $$f'(x)$$, $$y'$$, $$dy/dx$$, $$d^2y/dx^2$$, and verbal phrases like "rate of change." Translate the notation before choosing a rule.
:::

---

## Practice

::::problem
1. Interpret the limit as a derivative and then evaluate it exactly:

   $$
   \lim_{h\to0}\frac{(2+h)^{7/3}-2^{7/3}}{h}.
   $$

   State the function being differentiated and the input at which its derivative is evaluated.
::::

::::problem
2. Let

   $$
   f(x)=
   \begin{cases}
   ax^2+b, & x<1,\\
   3\ln x+c, & x\ge1.
   \end{cases}
   $$

   Given that $$f(0)=2$$, find $$a$$, $$b$$, and $$c$$ so that $$f$$ is differentiable at $$x=1$$. Then find $$f'(1)$$.
::::

::::problem
3. Define

   $$
   f(x)=\lvert x^2-4x+3\rvert.
   $$

   $$(A)$$ Find every input where $$f$$ is not differentiable and justify each one using one-sided derivatives.

   $$(B)$$ Find the equation of the tangent line to $$f$$ at $$x=2$$.

   $$(C)$$ Determine whether either nondifferentiable point can be repaired by changing only the value of $$f$$ at that point. Explain.
::::

::::problem
4. Differentiable functions $$f$$ and $$g$$ satisfy

   $$
   \begin{array}{c|cccc}
   x & f(x) & f'(x) & g(x) & g'(x) \\\hline
   2 & 3 & 4 & -1 & 5
   \end{array}
   $$

   Let

   $$
   H(x)=\frac{f(x)g(x)}{f(x)+g(x)}.
   $$

   Find $$H(2)$$ and $$H'(2)$$. Then write an equation of the normal line to the graph of $$H$$ at $$x=2$$.
::::

::::problem
5. Differentiate and simplify enough to identify every input where the derivative does not exist:

   $$
   y=\frac{(x^2+1)(e^x+\sin x)}{x^3}.
   $$

   Use the domain of the original function, not only the appearance of your final derivative.
::::

::::problem
6. Let

   $$
   f(x)=\frac{x^2+1}{x-1}.
   $$

   Find every point on the graph of $$f$$ where the tangent line has slope $$-1$$. Write the equation of each tangent line and determine whether the corresponding normal lines are parallel.
::::

::::problem
7. Let $$f(x)=x^2e^x$$. Find $$f^{(12)}(0)$$ without differentiating the function twelve times one line at a time. Develop and justify a pattern for $$f^{(n)}(x)$$ that works for every positive integer $$n$$.
::::

::::problem
8. Define

   $$
   f(x)=
   \begin{cases}
   x\sin(1/x), & x\ne0,\\
   0, & x=0,
   \end{cases}
   \qquad
   g(x)=
   \begin{cases}
   x^2\sin(1/x), & x\ne0,\\
   0, & x=0.
   \end{cases}
   $$

   $$(A)$$ Determine whether each function is continuous at $$x=0$$.

   $$(B)$$ Use the derivative definition to determine whether each function is differentiable at $$x=0$$.

   $$(C)$$ For each derivative that exists, find its value.
::::

::::problem
9. For $$a>0$$, let $$f(x)=a^x$$. The tangent line to the graph of $$f$$ at $$x=0$$ passes through the point $$(2,5)$$.

   $$(A)$$ Find $$a$$ exactly.

   $$(B)$$ Write equations of the tangent and normal lines at $$x=0$$.

   $$(C)$$ Find the $$x$$-intercept of the normal line.
::::

::::problem
10. Starting only from

    $$
    \frac{d}{dx}(\sinh x)=\cosh x,
    \qquad
    \frac{d}{dx}(\cosh x)=\sinh x,
    $$

    prove that $$\cosh^2x-\sinh^2x$$ is constant. Then determine the value of the constant by evaluating the expression at $$x=0$$.
::::

::::problem
11. A particle moves along a line with position

    $$
    s(t)=t\ln t,
    \qquad t>0.
    $$

    Find the exact time $$t\in(1,e)$$ at which the instantaneous velocity equals the average velocity on the interval $$[1,e]$$. Verify directly that your answer lies in the required interval.
::::

::::problem
12. Suppose $$f$$ is differentiable at $$x=a$$.

    $$(A)$$ Rewrite $$f(x)-f(a)$$ as a product involving the difference quotient $$\displaystyle\frac{f(x)-f(a)}{x-a}$$.

    $$(B)$$ Use limit laws and the derivative definition to prove that $$f$$ must be continuous at $$x=a$$.

    $$(C)$$ Give an example showing that the converse is false: a function can be continuous at a point without being differentiable there.
::::
