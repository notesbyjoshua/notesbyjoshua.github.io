---
title: "Unit 3: Differentiation: Composite, Implicit, and Inverse Differentiation"
description: "AP Calculus notes on chain rule, implicit differentiation, inverse functions, logarithmic differentiation, and inverse trig derivatives."
sidebar:
  order: 3
---

## Chain rule

<div class="theorem-box">

**Theorem (Chain Rule).** If $$y = f(g(x))$$, then

$$
\frac{dy}{dx} = f'(g(x))g'(x).
$$

</div>

The outside derivative is evaluated at the inside function, and then multiplied by the derivative of the inside function.

<div class="theorem-box">

**Proof (Chain rule).** Let $$u=g(x)$$ and $$y=f(u)$$. A small change in $$x$$ creates a small change in $$u$$, and that creates a small change in $$y$$. The ratio can be split as

$$
\frac{\Delta y}{\Delta x}
=
\frac{\Delta y}{\Delta u}\cdot\frac{\Delta u}{\Delta x}.
$$

As $$\Delta x\to0$$, the intermediate change $$\Delta u\to0$$ for a differentiable inside function. The two ratios approach $$f'(u)$$ and $$g'(x)$$, so

$$
\frac{dy}{dx}=f'(g(x))g'(x).
$$

</div>

The chain rule is about layered change. If $$x$$ changes, then the inside function $$g(x)$$ changes first. That change then causes the outside function $$f(g(x))$$ to change.

Symbolically,

$$
\frac{dy}{dx}
=
\frac{dy}{du}\cdot\frac{du}{dx}.
$$

The notation makes the chain rule look like canceling fractions. That is a useful way to remember it, but derivatives are limits of ratios, so algebra with derivative notation still needs a rule that justifies it.

AP problems often hide the chain rule inside:

- powers of expressions,
- trig functions with nontrivial angles,
- exponentials with nontrivial exponents,
- logarithms of expressions,
- inverse trig functions with expressions inside.

Whenever you differentiate an outside function, pause and ask what the inside function is.

<div class="theorem-box">

**Example.** Differentiate $$y=(3x^2+1)^5$$.

The outside function is a fifth power and the inside function is $$3x^2+1$$. Differentiate the outside power, keeping the inside unchanged, then multiply by the derivative of the inside:

$$
\frac{dy}{dx}=5(3x^2+1)^4\cdot\frac{d}{dx}(3x^2+1).
$$

Since $$\frac{d}{dx}(3x^2+1)=6x$$,

$$
\frac{dy}{dx}=5(3x^2+1)^4(6x)=30x(3x^2+1)^4.
$$

</div>

Note that the chain rule should be used for all layers of a function. For example, if you have a function $$f(g(h(x)))$$, the derivative is equal to:

$$
\frac{d}{dx} f(g(h(x))) = f'(g(h(x)))g'(h(x))h'(x).
$$

This is correct because each layer contributes its own derivative factor, starting from the outside layer and moving inward.

### General chain rule

For a composition with any number of layers,

$$
F(x)=f_1(f_2(\cdots f_n(x)\cdots)),
$$

differentiate each layer once, from the outside toward the inside:

$$
F'(x)
=
f_1'(f_2(\cdots f_n(x)\cdots))
f_2'(f_3(\cdots f_n(x)\cdots))
\cdots
f_n'(x).
$$

Every derivative factor is evaluated at the expression immediately inside its layer. The process stops only when the derivative reaches $$x$$.

:::strategy
1. Mark the layers before differentiating.
2. Differentiate the outside layer while copying everything inside it unchanged.
3. Move inward one layer and multiply by its derivative.
4. Repeat until the innermost expression has been differentiated.
5. Apply product or quotient rules to the larger structure when the composition is only one factor of the function.
:::

<div class="theorem-box">

**Example.** Differentiate

$$
y=e^{\sin((3x^2-1)^4)}.
$$

There are four changing layers: the exponential, sine, fourth power, and quadratic. Differentiate them in that order:

$$
\frac{dy}{dx}
=
e^{\sin((3x^2-1)^4)}
\cos((3x^2-1)^4)
\cdot4(3x^2-1)^3
\cdot6x.
$$

Therefore,

$$
\frac{dy}{dx}
=
24x(3x^2-1)^3
\cos((3x^2-1)^4)
e^{\sin((3x^2-1)^4)}.
$$

</div>

<div class="theorem-box">

**Example.** Let

$$
F(x)=\frac{(x^2+1)e^{(x-1)^2}}{x+1}.
$$

Find the equation of the tangent line to $$F$$ at $$x=2$$.

The numerator is a product containing a composite exponential. Let

$$
N(x)=(x^2+1)e^{(x-1)^2}.
$$

Use the product and chain rules:

$$
N'(x)
=
2xe^{(x-1)^2}
+(x^2+1)e^{(x-1)^2}\cdot2(x-1).
$$

Now apply the quotient rule:

$$
F'(x)
=
\frac{N'(x)(x+1)-N(x)}{(x+1)^2}.
$$

At $$x=2$$,

$$
N(2)=5e
\qquad\text{and}\qquad
N'(2)=4e+10e=14e.
$$

Thus

$$
F(2)=\frac{5e}{3}
$$

and

$$
F'(2)
=
\frac{(14e)(3)-5e}{9}
=
\frac{37e}{9}.
$$

The tangent line is

$$
y-\frac{5e}{3}
=
\frac{37e}{9}(x-2).
$$

</div>

---

## Implicit differentiation

Implicit equations describe a relationship rather than a solved function, meaning that the $$x$$s and $$y$$s of the equation are not fully separated. To take $$\frac{dy}{dx}$$ of such function we can use implicit differentiation.

:::tip
When differentiating with respect to $$x$$, attach $$dy/dx$$ when the term you are differentiating includes $$y$$. Another way to think about it is that you are differentiating using $$\frac{d}{dx}$$, so any term with $$y$$ will have to add a $$y$$ to the fraction, meaing it will have to include a $$\frac{dy}{dx}$$ (or $$y'$$) term.

- $$\frac{d}{dx}(y^2)=2y\frac{dy}{dx}$$
- $$\frac{d}{dx}(\sin y)=\cos y\frac{dy}{dx}$$
- $$\frac{d}{dx}(xy)=x\frac{dy}{dx}+y$$

Terms involving only $$x$$, such as $$x^2$$ or $$\sin x$$, do not get an extra $$dy/dx$$. The derivative rules (you can treat everything in $$x$$ as one function and everything in $$y$$ as another function) still apply even during implicit differentiation.
:::

After differentiating, collect every term containing $$dy/dx$$ on one side. Factor out $$dy/dx$$ only after all product and chain rules have been expanded. The remaining coefficient determines the slope. If that coefficient is zero while the other side is nonzero, the curve may have a vertical tangent rather than an ordinary finite slope.

<div class="theorem-box">

**Example.** Find the slope of the tangent line of the circle $$x^2+y^2=25$$ at the point $$(3,4)$$.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle, axis equal image,
  xmin=-5.5, xmax=5.5, ymin=-5.5, ymax=5.5,
  xtick={-5,0,3,5}, ytick={-5,0,4,5},
  grid=both, grid style={gray!18},
  width=8cm, height=8cm,
  xlabel=$x$, ylabel=$y$,
]
\addplot[blue, very thick, samples=240, domain=0:360] ({5*cos(x)},{5*sin(x)});
\addplot[orange!85!black, thick, domain=-1:5.3] {-0.75*(x-3)+4};
\addplot[gray!70, dashed] coordinates {(0,0) (3,4)};
\addplot[only marks, mark=*, mark size=1.8pt, blue] coordinates {(3,4)};
\node[blue, anchor=south west] at (axis cs:3,4) {$(3,4)$};
\node[orange!85!black, anchor=south east] at (axis cs:1.1,5.4) {tangent slope $-\frac{x}{y}$};
\end{axis}
\end{tikzpicture}
```

Differentiate both sides with respect to $$x$$, remembering that $$y$$ depends on $$x$$:

$$
2x+2y\frac{dy}{dx}=0.
$$

Solve for $$\frac{dy}{dx}$$:

$$
\frac{dy}{dx}=-\frac{x}{y}.
$$

Now substitute the point $$(3,4)$$:

$$
\frac{dy}{dx}\Big|_{(3,4)}=-\frac{3}{4}.
$$

So the tangent line at $$(3,4)$$ has slope $$-\frac34$$.

</div>

<div class="theorem-box">

**Example.** The curve

$$
x^2y+\sin(xy)=x+\sin1
$$

passes through $$(1,1)$$. Find the equation of its tangent line at that point.

Differentiate both sides with respect to $$x$$. The term $$x^2y$$ needs the product rule, while $$\sin(xy)$$ needs both the chain rule and another product rule:

$$
2xy+x^2\frac{dy}{dx}
+\cos(xy)\left(x\frac{dy}{dx}+y\right)
=1.
$$

Collect the derivative terms:

$$
\left(x^2+x\cos(xy)\right)\frac{dy}{dx}
=
1-2xy-y\cos(xy).
$$

Therefore,

$$
\frac{dy}{dx}
=
\frac{1-2xy-y\cos(xy)}{x^2+x\cos(xy)}.
$$

At $$(1,1)$$,

$$
\frac{dy}{dx}
=
\frac{-1-\cos1}{1+\cos1}
=-1.
$$

The tangent line is

$$
y-1=-(x-1),
$$

or

$$
y=-x+2.
$$

</div>

---

## Derivatives of inverse functions

<div class="theorem-box">

**Theorem (Inverse Function Derivative).** If $$f$$ is differentiable and invertible with $$f'(a) \ne 0$$, then

$$
(f^{-1})'(b) = \frac{1}{f'(a)}
$$

where $$b = f(a)$$.

Equivalent formula:

$$
(f^{-1})'(x) = \frac{1}{f'(f^{-1}(x))}.
$$

</div>

The derivative of an inverse is a reciprocal slope, but the reciprocal is taken at the matching point on the original function. If $$f(a)=b$$, then the point $$(a,b)$$ on $$f$$ becomes $$(b,a)$$ on $$f^{-1}$$. The slope $$f'(a)$$ belongs to the original point, while $$(f^{-1})'(b)$$ belongs to the reflected point.

The condition $$f'(a)\ne0$$ matters. A horizontal tangent on $$f$$ reflects to a vertical tangent on its inverse, so the inverse does not have a finite derivative there.

<div class="theorem-box">

**Proof (Inverse Function Derivative).** If $$y=f(x)$$ and $$x=f^{-1}(y)$$, then composing the functions gives

$$
f(f^{-1}(x))=x.
$$

Differentiate both sides:

$$
f'(f^{-1}(x))(f^{-1})'(x)=1.
$$

Solving for the inverse derivative gives

$$
(f^{-1})'(x)=\frac{1}{f'(f^{-1}(x))}.
$$

</div>

<div class="theorem-box">

**Example.** Let $$f(x)=x^3+x$$. Given that $$f(1)=2$$, find $$(f^{-1})'(2)$$.

Here $$a=1$$ and $$b=2$$, since $$f(1)=1^3+1=2$$. First compute the derivative of $$f$$:

$$
f'(x)=3x^2+1.
$$

Evaluate it at $$a=1$$:

$$
f'(1)=3(1)^2+1=4.
$$

By the inverse function rule,

$$
(f^{-1})'(2)=\frac{1}{f'(1)}=\frac{1}{4}.
$$

</div>

<div class="theorem-box">

**Example.** Suppose $$f(2)=5$$ and $$f'(2)=-3$$. Define

$$
g(x)=f^{-1}(x^2+1).
$$

Find the equation of the tangent line to $$g$$ at $$x=2$$.

First find the point on $$g$$:

$$
g(2)=f^{-1}(5)=2.
$$

Differentiate the composite inverse function:

$$
g'(x)
=
(f^{-1})'(x^2+1)\cdot2x
=
\frac{2x}{f'(f^{-1}(x^2+1))}.
$$

At $$x=2$$,

$$
g'(2)
=
\frac4{f'(f^{-1}(5))}
=
\frac4{f'(2)}
=
-\frac43.
$$

Using the point $$(2,2)$$, the tangent line is

$$
y-2=-\frac43(x-2).
$$

</div>

---

## Derivatives of inverse trig functions

$$
\frac{d}{dx}(\arcsin x) = \frac{1}{\sqrt{1-x^2}}
$$

$$
\frac{d}{dx}(\arccos x) = -\frac{1}{\sqrt{1-x^2}}
$$

$$
\frac{d}{dx}(\arctan x) = \frac{1}{1+x^2}
$$

$$
\frac{d}{dx}(\operatorname{arcsec} x) = \frac{1}{\lvert x\rvert\sqrt{x^2-1}}
$$

$$
\frac{d}{dx}(\operatorname{arccsc} x) = -\frac{1}{\lvert x\rvert\sqrt{x^2-1}}
$$

$$
\frac{d}{dx}(\operatorname{arccot} x) = -\frac{1}{1+x^2}
$$

For AP work, $$\arcsin$$, $$\arccos$$, and $$\arctan$$ are the most common inverse trig functions. All six formulas follow from the inverse-function derivative formula; one proof is shown below.

The listed formulas give the derivative of the inverse trig function itself. If its input is another function $$u(x)$$, the chain rule adds a factor of $$u'(x)$$. For example,

$$
\frac{d}{dx}\arcsin(u)
=
\frac{u'}{\sqrt{1-u^2}},
$$

and

$$
\frac{d}{dx}\arctan(u)
=
\frac{u'}{1+u^2}.
$$

Domain restrictions still matter after differentiating. The derivative of $$\arcsin x$$ becomes unbounded at $$x=\pm1$$, and the absolute value in the arcsec and arccsc formulas cannot be dropped without knowing the sign of the input.

<div class="theorem-box">

**Proof (Derivative of $$\arcsin x$$).** 

**Method 1 (Implicit Differentiation).** Let $$y=\arcsin x.$$

This means

$$
\sin y=x,
\qquad -\frac{\pi}{2}\le y\le \frac{\pi}{2}.
$$

Differentiate implicitly with respect to $$x$$:

$$
\cos y\frac{dy}{dx}=1.
$$

So

$$
\frac{dy}{dx}=\frac{1}{\cos y}.
$$

Since $$\sin y=x$$ and $$y$$ is in the principal range of arcsine, $$\cos y\ge0$$. Using $$\sin^2 y+\cos^2 y=1$$,

$$
\cos y=\sqrt{1-\sin^2 y}=\sqrt{1-x^2}.
$$

Therefore

$$
\frac{d}{dx}\arcsin x=\frac{1}{\sqrt{1-x^2}}.
$$

**Method 2 (Inverse Function Formula).** Let $$f(y)=\sin y$$, so $$f^{-1}(x)=\arcsin x$$. The inverse derivative formula gives

$$
(f^{-1})'(x)=\frac{1}{f'(f^{-1}(x))}.
$$

Since $$f'(y)=\cos y$$,

$$
\frac{d}{dx}\arcsin x
=
\frac{1}{\cos(\arcsin x)}.
$$

If $$\theta=\arcsin x$$, then $$\sin\theta=x$$ and $$\theta$$ is in the principal range where $$\cos\theta\ge0$$. Therefore

$$
\cos(\arcsin x)=\sqrt{1-x^2},
$$

so

$$
\frac{d}{dx}\arcsin x=\frac{1}{\sqrt{1-x^2}}.
$$

</div>

<div class="theorem-box">

**Example.** Differentiate $$y=\arctan(x^2)$$.

Use the chain-rule form with inside function $$u=x^2$$, so $$u'=2x$$:

$$
\frac{dy}{dx}=\frac{u'}{1+u^2}=\frac{2x}{1+(x^2)^2}.
$$

Simplifying the square gives

$$
\frac{dy}{dx}=\frac{2x}{1+x^4}.
$$

</div>

<div class="theorem-box">

**Example.** Differentiate and simplify

$$
y=\arcsin\left(\frac{x}{\sqrt{1+x^2}}\right).
$$

Let

$$
u=\frac{x}{\sqrt{1+x^2}}
=
x(1+x^2)^{-1/2}.
$$

Differentiate $$u$$ using the product and chain rules:

$$
u'
=
(1+x^2)^{-1/2}
-x^2(1+x^2)^{-3/2}
=
\frac1{(1+x^2)^{3/2}}.
$$

Also,

$$
1-u^2
=
1-\frac{x^2}{1+x^2}
=
\frac1{1+x^2}.
$$

Since $$1+x^2>0$$,

$$
\sqrt{1-u^2}=\frac1{\sqrt{1+x^2}}.
$$

Apply the chain-rule form of the arcsine derivative:

$$
\frac{dy}{dx}
=
\frac{u'}{\sqrt{1-u^2}}
=
\frac{1/(1+x^2)^{3/2}}{1/\sqrt{1+x^2}}
=
\frac1{1+x^2}.
$$

</div>

---

## Logarithmic differentiation

Logarithmic differentiation is useful when a function has products, quotients, powers, or variables in both the base and exponent. The idea is to take the natural logarithm of both sides, use log laws to simplify, and then differentiate implicitly.

For example, if

$$
y=(x^2+1)^3\sqrt{x-4},
$$

then taking logs gives

$$
\ln y=3\ln(x^2+1)+\frac12\ln(x-4).
$$

Differentiate both sides:

$$
\frac{1}{y}\frac{dy}{dx}
=3\cdot\frac{2x}{x^2+1}+\frac12\cdot\frac{1}{x-4}.
$$

Then multiply by $$y$$:

$$
\frac{dy}{dx}
=(x^2+1)^3\sqrt{x-4}
\left(\frac{6x}{x^2+1}+\frac{1}{2(x-4)}\right).
$$

:::warning
Logarithmic differentiation does not remove the chain rule. It reorganizes the expression so the chain rule is easier to apply.
:::

Logarithmic differentiation is a strategy, not a new derivative rule. It works because logarithms turn complicated multiplication, division, and powers into simpler operations:

$$
\ln(ab)=\ln a+\ln b,
$$

$$
\ln\left(\frac{a}{b}\right)=\ln a-\ln b,
$$

$$
\ln(a^r)=r\ln a.
$$

This is especially helpful when a function has many factors or when a variable appears in both the base and the exponent.

For a variable power $$u(x)^{v(x)}$$ with $$u(x)>0$$, logarithmic differentiation turns the exponent into a factor:

$$
\ln y=v(x)\ln(u(x)).
$$

Differentiating gives

$$
\frac{y'}{y}
=
v'(x)\ln(u(x))
+v(x)\frac{u'(x)}{u(x)}.
$$

This contains both the derivative of the exponent and the derivative of the base. Treating $$v(x)$$ as a constant would miss the first term.

After differentiating, remember that differentiating $$\ln y$$ gives

$$
\frac{1}{y}\frac{dy}{dx},
$$

so the final derivative usually comes from multiplying by $$y$$, where you resubstitude the original function (if $$y=f(x)$$).

<div class="theorem-box">

**Example.** Use logarithmic differentiation to find $$\frac{dy}{dx}$$ for $$y=x^x$$ (with $$x>0$$).

The variable appears in both the base and the exponent, so take the natural logarithm of both sides:

$$
\ln y=\ln\left(x^x\right)=x\ln x.
$$

Differentiate both sides with respect to $$x$$. The left side uses the chain rule, and the right side uses the product rule:

$$
\frac{1}{y}\frac{dy}{dx}=\ln x+x\cdot\frac{1}{x}=\ln x+1.
$$

Multiply both sides by $$y$$ and substitute $$y=x^x$$:

$$
\frac{dy}{dx}=x^x(\ln x+1).
$$

</div>

<div class="theorem-box">

**Example.** Use logarithmic differentiation to find $$dy/dx$$ for

$$
y=\frac{(x^2+1)^{\sin x}}{x^3\sqrt{x-1}},
\qquad x>1.
$$

Take the natural logarithm and expand using log laws:

$$
\ln y
=
\sin x\ln(x^2+1)
-3\ln x
-\frac12\ln(x-1).
$$

Differentiate both sides. The first term requires the product rule:

$$
\frac1y\frac{dy}{dx}
=
\cos x\ln(x^2+1)
+\frac{2x\sin x}{x^2+1}
-\frac3x
-\frac1{2(x-1)}.
$$

Multiply by $$y$$ and substitute the original expression:

$$
\frac{dy}{dx}
=
\frac{(x^2+1)^{\sin x}}{x^3\sqrt{x-1}}
\left(
\cos x\ln(x^2+1)
+\frac{2x\sin x}{x^2+1}
-\frac3x
-\frac1{2(x-1)}
\right).
$$

</div>

---

## Tips for the exam

This unit is about recognizing when the derivative is hidden inside another relationship.

- Chain rule problems hide a changing input inside an outer function.
- Implicit differentiation hides $$y$$ as a function of $$x$$.
- Inverse-function problems hide the slope relationship between a function and its inverse.
- Related rates hide time dependence inside geometry or context.

:::checklist
1. Identify the outer and inner functions before applying the chain rule.
2. In implicit equations, attach $$dy/dx$$ to every differentiated $$y$$ term.
3. In inverse-function questions, match the input/output pair correctly: if $$f(a)=b$$, then $$(f^{-1})'(b)=1/f'(a)$$.
4. In related rates, do not substitute variable values until after differentiating with respect to time.
:::

:::exam{topic="Composite and implicit derivatives"}
AP often mixes rules. A single derivative might require product rule, chain rule, and implicit differentiation in the same line, so write intermediate steps clearly enough that the structure is visible.
:::

Before moving on, make sure you can explain which rule is being used at each step. On AP-style questions, the hardest part is often choosing the rule order, not doing the algebra afterward.
