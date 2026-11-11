---
title: "Unit 5: Analytical Applications of Differentiation"
description: "AP Calculus notes on mean value theorems, derivative sign charts, extrema, concavity, constrained optimization, and curve sketching."
sidebar:
  order: 5
---

## Mean Value Theorem (MVT) and Rolle's Theorem

<div class="theorem-box">

**Theorem (Mean Value Theorem).** If $$f$$ is continuous on $$[a,b]$$ and differentiable on $$(a,b)$$, then there exists $$c \in (a,b)$$ such that

$$
f'(c) = \frac{f(b)-f(a)}{b-a}.
$$

**Rolle's Theorem** is the special case where $$f(a)=f(b)$$.

</div>

The Mean Value Theorem says that under the right smoothness conditions, some instantaneous rate equals the average rate over the interval.

The hypotheses are essential:

:::conditions
- Continuous on $$[a,b]$$
- Differentiable on $$(a,b)$$
:::

If either hypothesis fails, the theorem may not apply, even if the conclusion happens to be true.

Rolle's Theorem is the same idea when the average rate is zero. If a smooth function starts and ends at the same height, then somewhere in between it has a horizontal tangent.

<div class="theorem-box">

**Proof (MVT).** Define the secant-line function through the endpoints:

$$
L(x)=f(a)+\frac{f(b)-f(a)}{b-a}(x-a).
$$

Now define

$$
g(x)=f(x)-L(x).
$$

Because $$f$$ and $$L$$ are continuous on $$[a,b]$$ and differentiable on $$(a,b)$$, so is $$g$$. Also,

$$
g(a)=f(a)-L(a)=0,
$$

and

$$
g(b)=f(b)-L(b)=0.
$$

By Rolle's Theorem, there is some $$c\in(a,b)$$ such that $$g'(c)=0$$. Since

$$
g'(x)=f'(x)-\frac{f(b)-f(a)}{b-a},
$$

we get

$$
0=f'(c)-\frac{f(b)-f(a)}{b-a}.
$$

Therefore,

$$
f'(c)=\frac{f(b)-f(a)}{b-a}.
$$

// prove MVT without Rolle's theorem (its circular reasoning)

</div>

<div class="theorem-box">

**Example.** Verify Rolle's Theorem for

$$
f(x)=x^2-4x+3
$$

on $$[1,3]$$, then find the value of $$c$$.

The function is a polynomial, so it is continuous on $$[1,3]$$ and differentiable on $$(1,3)$$. Check the endpoint values:

$$
f(1)=1-4+3=0,
$$

and

$$
f(3)=9-12+3=0.
$$

Since $$f(1)=f(3)$$, Rolle's Theorem applies. Differentiate:

$$
f'(x)=2x-4.
$$

Set $$f'(c)=0$$:

$$
2c-4=0
\quad\Longrightarrow\quad
c=2.
$$

The value $$c=2$$ lies in $$(1,3)$$, so it is the point guaranteed by Rolle's Theorem.

</div>

<div class="theorem-box">

**Example.** For $$f(x)=x+1/x$$ on $$[1,4]$$, find the value $$c$$ guaranteed by the Mean Value Theorem.

The function is continuous on $$[1,4]$$ and differentiable on $$(1,4)$$ because the interval excludes zero. The average rate of change is

$$
\frac{f(4)-f(1)}{4-1}=\frac{17/4-2}{3}=\frac34.
$$

Since $$f'(x)=1-1/x^2$$, set the instantaneous rate equal to the average rate:

$$
1-\frac1{c^2}=\frac34\quad\Longrightarrow\quad c^2=4.
$$

Only $$c=2$$ lies in $$(1,4)$$, so it is the value guaranteed by the theorem.

</div>

---

## Using the derivative in graphs

When looking at a function, its first derivative can tell you a lot about the direction, as we know from previous units:

- $$f'(x) > 0$$ on an interval implies $$f$$ is increasing there.
- $$f'(x) < 0$$ on an interval implies $$f$$ is decreasing there.

Sign charts are the easiest way to justify interval behavior.

When looking at a function, its second derivative can tell you a lot about the shape:

- $$f''(x)>0$$, then $$f'(x)$$ is increasing. The graph of $$f$$ bends upward (concave up) because its slopes are becoming more positive or less negative.
- $$f''(x)<0$$, then $$f'(x)$$ is decreasing. The graph of $$f$$ bends downward (concave down) because its slopes are becoming less positive or more negative.

An inflection point is a point on the graph where concavity changes. Find candidates where $$f''(x)=0$$ or $$f''(x)$$ is undefined, then test the sign of $$f''$$ on either side. A change from positive to negative or negative to positive gives an inflection point when the function is continuous at the candidate. A zero of $$f''$$ alone is not enough, and an excluded input cannot be a point on the graph.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle, xmin=-2.5, xmax=3.5, ymin=-5, ymax=5,
  xtick={-2,-1,0,1,2,3}, ytick={-4,-2,0,2,4},
  grid=both, grid style={gray!18},
  width=9cm, height=6.3cm,
  xlabel=$x$, ylabel=$f(x)$,
]
\addplot[blue, very thick, samples=220, domain=-2.2:3.2] {x^3-3*x^2};
\addplot[only marks, mark=*, mark size=1.8pt, orange!85!black] coordinates {(0,0) (2,-4) (1,-2)};
\node[orange!85!black, anchor=south east] at (axis cs:0,0) {local max};
\node[orange!85!black, anchor=north west] at (axis cs:2,-4) {local min};
\node[orange!85!black, anchor=south west] at (axis cs:1,-2) {inflection};
\node[align=center, font=\small] at (axis cs:-1.55,-4.1) {$f^{\prime}>0$\\$f^{\prime\prime}<0$};
\node[align=center, font=\small] at (axis cs:2.7,2.6) {$f^{\prime}>0$\\$f^{\prime\prime}>0$};
\end{axis}
\end{tikzpicture}
```

A **local maximum** at $$x=c$$ means $$f(c)$$ is at least as large as all nearby function values; a **local minimum** means it is at most as large as all nearby values. These are local comparisons, so a higher or lower value may occur elsewhere. In the graph, $$(0,0)$$ is a local maximum and $$(2,-4)$$ is a local minimum.

### Critical Points

Interior local extrema occur at critical points, although an inflection point does not have to be a critical point. In the graph above, the inflection point at $$x=1$$ has a nonzero derivative.

<div class="theorem-box">

**Definition.** A critical point of $$f$$ occurs at $$x=c$$ when:

- $$f'(c) = 0$$, or
- $$f'(c)$$ does not exist,

provided $$c$$ is in the domain of $$f$$.

</div>

<div class="theorem-box">

**Theorem.** If $$f$$ has a local extremum at an interior point $$c$$ and $$f'(c)$$ exists, then

$$
f'(c)=0.
$$

</div>

<div class="theorem-box">

**Proof (Fermat's theorem).** Suppose $$f$$ has a local maximum at an interior point $$c$$ and is differentiable there. For sufficiently small positive $$h$$,

$$
\frac{f(c+h)-f(c)}h\le0,
$$

because the numerator is nonpositive. For sufficiently small negative $$h$$, the numerator is still nonpositive, but dividing by a negative denominator gives

$$
\frac{f(c+h)-f(c)}h\ge0.
$$

If the two-sided derivative exists, its value must be both nonpositive and nonnegative. Therefore $$f'(c)=0$$. At a local minimum, the inequalities reverse and give the same result.

</div>

This theorem explains why critical numbers matter, but it does not say every critical number is an extremum. It only says that if an interior local extremum happens at a differentiable point, the derivative must be zero there.

:::warning
A point where $$f'(c)=0$$ is not automatically a maximum or minimum. For example, $$f(x)=x^3$$ has $$f'(0)=0$$, but $$x=0$$ is not an extremum.
:::

// add an example question

---

## The First Derivative Test

The First Derivative Test classifies interior critical points by the signs of the derivative nearby. It applies both where the derivative is zero and where it is undefined, provided the function is continuous at the point and differentiable on the nearby intervals being tested.

<div class="theorem-box">

**Theorem (First Derivative Test).** If $$f'$$ changes:

- positive to negative at $$c$$: local maximum,
- negative to positive at $$c$$: local minimum,
- no sign change: neither.

Assume $$f$$ is continuous at $$c$$ and differentiable on each side near $$c$$, with the stated strict derivative signs on those intervals.

</div>

<div class="theorem-box">

**Proof (First Derivative Test).** Suppose $$f'$$ changes from positive to negative at $$c$$. Then $$f$$ is increasing just to the left of $$c$$ and decreasing just to the right of $$c$$. So values near $$c$$ on the left rise toward $$f(c)$$, and values near $$c$$ on the right fall away from $$f(c)$$. This makes $$f(c)$$ a local maximum.

If $$f'$$ changes from negative to positive, the same reasoning reverses: $$f$$ decreases into $$c$$ and increases after $$c$$, so $$f(c)$$ is a local minimum.

If $$f'$$ does not change sign, then $$f$$ keeps increasing on both sides or keeps decreasing on both sides. In that case, $$c$$ is not a local extremum.

</div>

<div class="theorem-box">

**Example.** Find and classify the critical points of $$f(x)=x^3-3x^2$$.

Differentiate and factor:

$$
f'(x)=3x^2-6x=3x(x-2).
$$

So $$f'(x)=0$$ at $$x=0$$ and $$x=2$$. Test the sign of $$f'$$ on each interval:

Test one point in each interval:

$$
f'(-1)=3(-1)(-3)=9>0.
$$

$$
f'(1)=3(1)(-1)=-3<0.
$$

$$
f'(3)=3(3)(1)=9>0.
$$

The derivative goes positive to negative at $$x=0$$, so $$f$$ has a local maximum there, with $$f(0)=0$$. The derivative goes negative to positive at $$x=2$$, so $$f$$ has a local minimum there, with $$f(2)=8-12=-4$$.

</div>

<div class="theorem-box">

**Example.** Find and classify all critical points of $$f(x)=x^4-4x^3+4x^2$$.

Factoring the derivative gives

$$
f'(x)=4x(x-1)(x-2).
$$

Its signs on $$(-\infty,0)$$, $$(0,1)$$, $$(1,2)$$, and $$(2,\infty)$$ are negative, positive, negative, and positive, respectively. Therefore $$f$$ has local minima at $$(0,0)$$ and $$(2,0)$$ and a local maximum at $$(1,1)$$. A derivative sign chart distinguishes the three critical points even though the derivative is zero at all of them.

</div>

---

## Concavity and the second derivative

Concavity describes how the slopes of a function are changing.

- If $$f''(x)>0$$, then $$f'$$ is increasing and the graph is concave up.
- If $$f''(x)<0$$, then $$f'$$ is decreasing and the graph is concave down.

An inflection point occurs where concavity changes. The equation $$f''(x)=0$$ gives possible inflection points, but it is not enough by itself. You still need to check that $$f''$$ changes sign or that the graph actually changes concavity.

<div class="theorem-box">

**Example.** Find the concavity intervals and inflection point of

$$
f(x)=x^3-3x^2.
$$

Compute the second derivative:

$$
f'(x)=3x^2-6x,
\qquad
f''(x)=6x-6.
$$

Set $$f''(x)=0$$:

$$
6x-6=0
\quad\Longrightarrow\quad
x=1.
$$

Test around $$x=1$$. If $$x<1$$, then $$f''(x)<0$$, so the graph is concave down. If $$x>1$$, then $$f''(x)>0$$, so the graph is concave up. Since concavity changes at $$x=1$$, there is an inflection point there:

$$
f(1)=1-3=-2.
$$

The inflection point is $$(1,-2)$$.

</div>



### The Second Derivative Test

The Second Derivative Test is an alternate way of finding minima and maxima.

<div class="theorem-box">

**Theorem (Second Derivative Test).** If $$f'(c)=0$$ and:

- $$f''(c)>0$$, then $$f$$ has a local minimum at $$c$$,
- $$f''(c)<0$$, then $$f$$ has a local maximum at $$c$$,
- $$f''(c)=0$$, the test is inconclusive.

</div>

<div class="theorem-box">

**Proof (Second Derivative Test).** Suppose $$f'(c)=0$$ and $$f''(c)>0$$. By the definition of the derivative of $$f'$$,

$$
\lim_{h\to0}\frac{f'(c+h)-f'(c)}{h}=f''(c)>0.
$$

For sufficiently small nonzero $$h$$, this quotient is positive. Since $$f'(c)=0$$, the sign of $$f'(c+h)$$ is the sign of $$h$$: it is negative to the left and positive to the right. The First Derivative Test therefore gives a local minimum. If $$f''(c)<0$$, the signs reverse and give a local maximum. This argument does not require $$f''$$ to be continuous near $$c$$.

</div>

When $$f''(c)=0$$, why is the test inconclusive? Compare $$x^4$$, $$-x^4$$, and $$x^3$$ at zero. All three have zero first and second derivatives there, but their behaviors differ: the first has a minimum, the second has a maximum, and the third has neither. Therefore an inconclusive second derivative test requires another method, usually a sign chart for the first derivative.

Inflection points require a change in concavity and a point on the graph where the change occurs. For $$x^4$$, the second derivative $$12x^2$$ is positive on both sides of zero, so there is no inflection. For $$x^{1/3}$$, the second derivative is undefined at zero, but concavity changes across the continuous point, so there is an inflection there.

For $$1/x$$, concavity changes sign across zero, but zero is outside the domain. There is no inflection point at the vertical asymptote. A sign change across an excluded input describes two separate branches.

<div class="theorem-box">

**Example.** Use the second derivative test to classify the critical points of $$f(x)=x^3-12x$$.

First find the critical points:

$$
f'(x)=3x^2-12=3(x^2-4)=3(x-2)(x+2),
$$

so $$f'(x)=0$$ at $$x=-2$$ and $$x=2$$. The second derivative is

$$
f''(x)=6x.
$$

Evaluate at each critical point:

$$
f''(2)=12>0,\qquad f''(-2)=-12<0.
$$

Since $$f''(2)>0$$, there is a local minimum at $$x=2$$, with $$f(2)=8-24=-16$$. Since $$f''(-2)<0$$, there is a local maximum at $$x=-2$$, with $$f(-2)=-8+24=16$$.

</div>

### Choosing between the tests

The First Derivative Test is usually more reliable because it checks what the function is actually doing on both sides of the critical point. It works for critical points where $$f'(c)=0$$ and for critical points where $$f'(c)$$ does not exist, as long as you can test signs around $$c$$.

The Second Derivative Test is faster when it applies, but it has two limits:

- it only applies when $$f'(c)=0$$,
- if $$f''(c)=0$$, the test gives no conclusion.

:::tip
Use the First Derivative Test when a sign chart is already natural or when $$f'$$ is undefined at the critical point. Use the Second Derivative Test when $$f''(c)$$ is easy to compute and clearly positive or negative.
:::

### Corners, cusps, and vertical tangents

When doing the First Derivative Test, we often talk about cases where $$f'(x)=0$$, but we also know that we have the case where $$f'(x)= UND$$. At each of these points a function can be *continuous* even though its ordinary derivative does not exist. To distinguish them, compare the slopes as you approach from each side:

- A **corner** has different finite one-sided slopes. For $$f(x)=\lvert x\rvert$$ at zero, they are $$-1$$ and $$1$$.
- A **cusp** has slopes that become infinite with opposite signs. For $$f(x)=x^{2/3}$$ at zero, the left slopes approach $$-\infty$$ and the right slopes approach $$+\infty$$.
- A **vertical tangent** has slopes that become infinite with the same sign from both sides. For $$f(x)=x^{1/3}$$ at zero, both approach $$+\infty$$.

All three are critical points when they lie in the domain. A cusp or corner can be an extremum, but the vertical tangent is usually not: the function increases on both sides. Check the first-derivative signs rather than assuming the point is an extremum.

// add an example of graphing with vertical tangents/cusps and stuff

---

## Curve sketching framework

When sketching curves, you should always include:

- intercepts,
- asymptotes if relevant,
- intervals increasing/decreasing,
- local extrema,
- intervals concave up/down,
- inflection points,
- end behavior.

You do not need a perfect drawing at first. The goal is to collect enough structure that the graph has the correct shape. Start with the domain and discontinuities, then use derivatives to decide how the graph moves.

:::checklist
1. Find the domain and any vertical asymptotes or holes.
2. Find intercepts if they are easy.
3. Use $$f'$$ to make increasing/decreasing intervals.
4. Use $$f''$$ to make concavity intervals.
5. Mark local extrema and inflection points.
6. Add end behavior or horizontal/slant asymptotes.
:::

:::warning
A critical point is only a candidate. Do not label it a maximum or minimum until a derivative sign change, second derivative test, or value comparison supports it.
:::

<div class="theorem-box">

**Example.** Sketch the important features of

$$
f(x)=x^{2/3}(x-4).
$$

The domain is all real numbers. The intercepts are $$(0,0)$$ and $$(4,0)$$. For $$x\ne0$$,

$$
f'(x)=\frac{5x-8}{3x^{1/3}},
\qquad
f''(x)=\frac{10x+8}{9x^{4/3}}.
$$

The first derivative is undefined at $$0$$ and zero at $$8/5$$. Its signs show that $$f$$ increases on $$(-\infty,0)$$, decreases on $$(0,8/5)$$, and increases on $$(8/5,\infty)$$. Thus $$(0,0)$$ is a cusp and local maximum, while the local minimum is

$$
\left(\frac85,-\frac{12}{5}\left(\frac85\right)^{2/3}\right).
$$

The denominator of $$f''$$ is positive wherever it is defined. The numerator changes from negative to positive at $$x=-4/5$$, so the graph is concave down on $$(-\infty,-4/5)$$ and concave up on $$(-4/5,0)$$ and $$(0,\infty)$$. The inflection point is

$$
\left(-\frac45,-\frac{24}{5}\left(\frac45\right)^{2/3}\right).
$$

Although $$f''$$ is undefined at the cusp, concavity is up on both sides, so zero is not an inflection point. Finally, $$f(x)\to-\infty$$ as $$x\to-\infty$$ and $$f(x)\to\infty$$ as $$x\to\infty$$; there are no asymptotes.

// give a graph of the function

</div>

<div class="theorem-box">

**Example.** Sketch $$f(x)=x+2\sin x$$ on $$[0,2\pi]$$, marking its extrema and inflection point.

We have $$f'(x)=1+2\cos x$$ and $$f''(x)=-2\sin x$$. The first derivative is zero at $$2\pi/3$$ and $$4\pi/3$$. It is positive, negative, and positive on the three successive intervals, so the interior local maximum and minimum are

$$
\left(\frac{2\pi}{3},\frac{2\pi}{3}+\sqrt3\right),
\qquad
\left(\frac{4\pi}{3},\frac{4\pi}{3}-\sqrt3\right).
$$

The second derivative is negative on $$(0,\pi)$$ and positive on $$(\pi,2\pi)$$, giving an inflection point at $$(\pi,\pi)$$. The endpoints are $$(0,0)$$ and $$(2\pi,2\pi)$$; these, together with the two extrema and the inflection point, determine the shape of the sketch.

// give a graph of the function

</div>

---

## Absolute extrema on a closed interval

<div class="theorem-box">

**Definition.** The absolute extrema of an interval $$[a,b]$$ is defined as the point $$x=c$$ where

- $$f(c)$$ is at a maximum (for absolute maxima),
- $$f(c)$$ is at a minimum (for absolute minima).

</div>

The largest output is the absolute maximum, and the smallest output is the absolute minimum. Absolute extrema can occur on open or unbounded domains, but their existence is not guaranteed there: for example, $$f(x)=x$$ on $$(0,1)$$ has neither one.

### Extreme Value Theorem (EVT)

How can we find absolute extrema? The Extreme Value Theorem (EVT) guarantees that a continuous function on a closed interval has both an absolute maximum and an absolute minimum.

<div class="theorem-box">

**Theorem (EVT).** If $$f$$ is continuous on $$[a,b]$$, then there are numbers $$m$$ and $$M$$ in $$[a,b]$$ such that

$$
f(m)\le f(x)\le f(M)
$$

for every $$x$$ in $$[a,b]$$.

</div>

The two conditions matter. The interval must be closed, so endpoints are included, and the function must be continuous, so it cannot jump over or miss its highest or lowest value. While EVT tells you the extrema exist, it does not tell you where they are. In order to find those points, we can use critical points and endpoints. The proof for EVT uses topics outside of AP Calc so I will not cover it here.

Thus, when graphing, there are two different candidate lists:

- for local extrema, check interior critical points,
- for absolute extrema on a closed interval, check interior critical points and endpoints.

Endpoints matter for absolute extrema because EVT guarantees the largest and smallest output somewhere on the whole closed interval. Endpoints are included in that interval, even though they are not usually called local extrema in AP Calculus.

:::strategy
1. Check that $$f$$ is continuous on the closed interval.
2. Find critical points inside the interval.
3. Evaluate $$f$$ at those critical points and at both endpoints.
4. Compare the output values.
:::

The interior condition allows changes to the left and right. At an endpoint, only one of those directions is available, so there is no reason for the derivative to be zero. For example, $$f(x)=x$$ reaches its maximum on $$[0,1]$$ at $$1$$ even though its slope is always one.

This also proves Rolle's Theorem once EVT is available. Equal endpoint values either belong to a constant function, whose derivative is zero throughout, or force a nonconstant continuous function to have an absolute extremum somewhere inside the interval. Differentiability at that interior extremum then gives a horizontal tangent.

### One critical point and an absolute extremum

On an interval, if a continuous function has a critical point $$c$$ and is differentiable elsewhere, a first-derivative sign change from negative to positive at $$c$$ with $$f'<0$$ everywhere to its left and $$f'>0$$ everywhere to its right proves that $$f(c)$$ is an absolute minimum. Reverse the signs for an absolute maximum. The sign information establishes the comparison over the entire domain, including any endpoints by continuity.

A single local extremum by itself is not a substitute for checking the domain and global behavior. For example, $$f(x)=x^3-3x$$ on the disconnected domain $$[-2,0]\cup[3,4]$$ has only one interior local extremum, a local maximum at $$x=-1$$, but $$f(4)>f(-1)$$. Verify the sign pattern on the whole feasible interval before using the shortcut.

<div class="theorem-box">

**Example.** Find the absolute extrema of $$f(x)=x^3-3x^2-9x+5$$ on $$[-2,5]$$.

Since $$f$$ is continuous on the closed interval, EVT guarantees both extrema. Its derivative is $$f'(x)=3(x+1)(x-3)$$, so the interior critical numbers are $$-1$$ and $$3$$. Compare their outputs with both endpoints:

$$
f(-2)=3,\qquad f(-1)=10,\qquad f(3)=-22,\qquad f(5)=10.
$$

The absolute maximum is $$10$$, attained at $$x=-1$$ and $$x=5$$; the absolute minimum is $$-22$$, attained at $$x=3$$. The endpoint comparison matters even when a local maximum has already been found.

</div>

---

## Optimization

Optimization problems mix modeling with calculus. The derivative only works after the quantity being optimized is written as a one-variable function. Most optimization problems ask for a local or absolute minimum (such as the least time) or maximum (such as the greatest profit).

The hardest part of optimization is usually building the one-variable function. A good setup keeps three pieces separate:

- the target quantity, which is what you want to maximize or minimize,
- the constraint equation, which connects the variables,
- the feasible domain, which says what values make sense in the context (e.g. side lengths cannot be negative)

If the target quantity has two variables, use the constraint to solve for one variable and substitute. After that, the calculus part is standard: differentiate, find critical points, and test candidates.

If the allowed domain is closed, we can use EVT to determine the extrema. If the domain is open or unbounded, we can use critical points and do limits at the endpoints.

:::strategy
1. Identify the quantity to optimize.
2. Write it as a function of one variable.
3. Determine the feasible domain.
4. Differentiate and find critical points.
5. Test candidates and interpret.
:::

:::mistakes
- Optimizing the constraint instead of the target quantity.
- Forgetting endpoints on a closed interval.
- Ignoring domain restrictions like positive lengths or nonzero denominators.
- Reporting only the critical value of the variable instead of answering the original question.
:::

<div class="theorem-box">

**Example.** A rectangular pen is divided into two smaller pens by one fence parallel to a pair of its sides. If $$120$$ meters of fencing are available for the perimeter and the divider, find the dimensions that maximize the total enclosed area.

Let $$x$$ be the length of each of the three parallel fences, including the divider, and let $$y$$ be the other side length. The fencing constraint is

$$
3x+2y=120\quad\Longrightarrow\quad y=60-\frac32x.
$$

The area, written as a one-variable function, is

$$
A(x)=x\left(60-\frac32x\right)=60x-\frac32x^2,
\qquad 0<x<40.
$$

Differentiate and find the critical point:

$$
A'(x)=60-3x=0\quad\Longrightarrow\quad x=20.
$$

The derivative is positive on $$(0,20)$$ and negative on $$(20,40)$$. Thus area increases up to $$x=20$$ and decreases afterward throughout the feasible interval, so this is the absolute maximum. Then $$y=30$$, and the pen measures $$20$$ meters by $$30$$ meters, with maximum area

$$
A(20)=20\cdot30=600\ \text{square meters}.
$$

</div>

<div class="theorem-box">

**Example.** A rectangular box with a square base and no top must have volume $$500$$ cubic centimeters. Find the dimensions that minimize the surface area.

Let $$x$$ be the side length of the square base and $$h$$ be the height. The volume constraint is

$$
x^2h=500,
$$

so

$$
h=\frac{500}{x^2}.
$$

The surface area includes the square base and four side rectangles:

$$
S=x^2+4xh.
$$

Substitute the constraint:

$$
S(x)=x^2+4x\left(\frac{500}{x^2}\right)=x^2+\frac{2000}{x},
\qquad x>0.
$$

Differentiate:

$$
S'(x)=2x-\frac{2000}{x^2}.
$$

Set the derivative equal to zero:

$$
2x-\frac{2000}{x^2}=0.
$$

Multiply by $$x^2$$:

$$
2x^3-2000=0
\quad\Longrightarrow\quad
x^3=1000
\quad\Longrightarrow\quad
x=10.
$$

Then

$$
h=\frac{500}{10^2}=5.
$$

For every $$x>0$$, the sign of $$S'(x)=2(x^3-1000)/x^2$$ is negative when $$x<10$$ and positive when $$x>10$$. The surface area therefore decreases up to its only critical point and increases afterward on the entire feasible interval, so this point gives the absolute minimum. The box should have square base side length $$10$$ cm and height $$5$$ cm.

</div>

### Optimizing a model with unequal costs

Symmetry of the geometry does not guarantee symmetry of the best design. If different sides have different costs, optimize cost rather than area or perimeter. The variable being eliminated must still come from the physical constraint.

<div class="theorem-box">

**Example.** A rectangular enclosure beside a straight river must have area $$1800$$ square meters. No fence is needed along the river. The opposite side costs $$20$$ dollars per meter, and each side perpendicular to the river costs $$10$$ dollars per meter. Find the dimensions minimizing fencing cost.

Let $$x$$ be each perpendicular length and $$y$$ the length parallel to the river. The area constraint is $$xy=1800$$, so $$y=1800/x$$ for $$x>0$$.

There are two sides of length $$x$$ and one fenced side of length $$y$$. Therefore,

$$
C(x)=2(10)x+20\frac{1800}{x}
=20x+\frac{36000}{x}.
$$

The critical-point equation is

$$
C'(x)=20-\frac{36000}{x^2}=0,
$$

which gives $$x^2=1800$$ and $$x=30\sqrt2$$. The other dimension is

$$
y=\frac{1800}{30\sqrt2}=30\sqrt2.
$$

For $$x>0$$, the denominator of $$C'(x)=(20x^2-36000)/x^2$$ is positive, while the numerator is negative for $$0<x<30\sqrt2$$ and positive for $$x>30\sqrt2$$. Thus cost decreases up to the only critical point and increases afterward throughout the feasible interval, making this design the absolute minimum.

The minimizing enclosure happens to be square because the total cost of the two perpendicular sides matches the cost coefficient of the parallel side. With uniform cost per meter instead, the optimal parallel side would be twice a perpendicular side. The objective function, not a memorized rectangle pattern, determines the dimensions.

</div>

---

## Newton's method

As a reminder, linearization is the process of estimating the value of a function using its derivative:

$$
L(x) = f(a)+f'(a)(x-a).
$$

Using linearization, we can approximate the roots of a function using Newton's method (also known as the Newton-Raphson method) for approximating roots. Newton's method uses tangent lines to approximate roots.

<div class="theorem-box">

**Theorem (Newton's Method).** To approximate a root of $$f(x)=0$$, start with a guess $$x_n$$ and repeatedly use

$$
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}.
$$

</div>

The input $$x_n$$ is the current approximation, and $$x_{n+1}$$ is the next approximation. Convergence is not automatic: the method works best near a root when the derivative is nonzero and the local tangent gives a useful prediction. A nearly horizontal tangent can send the next approximation far away.

<div class="theorem-box">

**Proof (Newton's Method).** The linearization of $$f$$ at $$x_n$$ is

$$
L(x)=f(x_n)+f'(x_n)(x-x_n).
$$

Newton's method uses the root of this tangent line as the next guess, so set $$L(x)=0$$:

$$
0=f(x_n)+f'(x_n)(x-x_n).
$$

Solve for $$x$$:

$$
f'(x_n)(x-x_n)=-f(x_n),
$$

$$
x-x_n=-\frac{f(x_n)}{f'(x_n)}.
$$

Therefore,

$$
x=x_n-\frac{f(x_n)}{f'(x_n)}.
$$

This new $$x$$-value is called $$x_{n+1}$$.

</div>

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle, xmin=0.2, xmax=2.8, ymin=-1.3, ymax=5.2,
  xtick={1,1.545,2.2}, ytick={0,2,4},
  grid=both, grid style={gray!18},
  width=9cm, height=6.2cm,
  xlabel=$x$, ylabel=$y$,
]
\addplot[blue, thick, samples=220, domain=0.25:2.65] {x^2-2};
\addplot[orange!85!black, thick, domain=1.05:2.55] {4.4*(x-2.2)+2.84};
\addplot[red!75!black, thick, domain=1.2:1.95] {3.109*(x-1.5455)+0.3884};
\addplot[gray!70, dashed] coordinates {(2.2,0) (2.2,2.84)};
\addplot[gray!70, dashed] coordinates {(1.5545,0) (1.5545,0.4165)};
\addplot[gray!70, dashed] coordinates {(1.4207,0) (1.4207,0.0184)};
\addplot[only marks, mark=*, mark size=1.8pt, orange!85!black] coordinates {(2.2,2.84)};
\addplot[only marks, mark=*, mark size=1.8pt, red!75!black] coordinates {(1.5455,0.3884)};
\addplot[only marks, mark=*, mark size=1.6pt, gray!80] coordinates {(1.5545,0) (1.4207,0)};
\node[orange!85!black, anchor=south west] at (axis cs:1.55,3.2) {tangent at $x_0$};
\node[gray!80!black, anchor=north] at (axis cs:1.7,0.5) {$x_1$};
\node[red!75!black, anchor=south east] at (axis cs:1.55,0.62) {tangent at $x_1$};
\node[gray!80!black, anchor=north east] at (axis cs:1.4,0.6) {$x_2$};
\end{axis}
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** Use Newton's method to approximate $$\sqrt2$$ by solving $$x^2-2=0$$, starting with $$x_0=1.5$$.

Let

$$
f(x)=x^2-2,
\qquad
f'(x)=2x.
$$

The Newton update is

$$
x_{n+1}=x_n-\frac{x_n^2-2}{2x_n}.
$$

Starting with $$x_0=1.5$$:

$$
x_1=1.5-\frac{1.5^2-2}{2(1.5)}
=1.5-\frac{0.25}{3}
\approx1.4167.
$$

Apply the formula again:

$$
x_2=1.4167-\frac{1.4167^2-2}{2(1.4167)}
\approx1.4142.
$$

So $$\sqrt2\approx1.4142$$.

</div>

<div class="theorem-box">

**Example.** Use Newton's method to approximate a solution of $$\cos x=x$$, starting with $$x_0=1$$.

Write the equation as a root problem:

$$
f(x)=\cos x-x.
$$

Then

$$
f'(x)=-\sin x-1.
$$

Newton's method gives

$$
x_{n+1}=x_n-\frac{\cos x_n-x_n}{-\sin x_n-1}.
$$

Starting with $$x_0=1$$:

$$
x_1=1-\frac{\cos(1)-1}{-\sin(1)-1}\approx0.7504.
$$

One more iteration gives

$$
x_2=0.7504-\frac{\cos(0.7504)-0.7504}{-\sin(0.7504)-1}\approx0.7391.
$$

So the solution is approximately $$x\approx0.7391$$.

</div>


---

### Recognizing a failed iteration

Before accepting a decimal answer, check that it approximately satisfies the original equation. Nearby successive guesses are useful evidence only if the formula was implemented correctly and the original function is defined there.

For $$f(x)=x^3-2x+2$$, starting at $$x_0=0$$ gives $$x_1=1$$, and starting from $$1$$ gives $$x_2=0$$. The iteration repeats forever even though the polynomial has a real root elsewhere. The tangent construction itself is valid, but this starting value produces a cycle.

For a root at which $$f'=0$$, the update may become undefined or converge more slowly. If an iterate hits a point where the denominator vanishes, choose a different starting value or another numerical method. Newton's method supplies an approximation procedure, not the existence guarantee supplied by IVT or the uniqueness argument supplied by monotonicity.

## Tips for the exam

Analytical applications ask you to turn derivative information into a story about the original function. The safest approach is to separate **where candidates occur** from **what those candidates mean**.

:::strategy
1. Find the domain first, because endpoints and discontinuities matter.
2. Find critical numbers from $$f'(x)=0$$ and places where $$f'$$ is undefined.
3. Build a sign chart for $$f'$$ to determine increasing/decreasing behavior.
4. Build a sign chart for $$f''$$ to determine concavity.
5. Use endpoint values and critical values for absolute extrema on closed intervals.
6. Use derivative sign changes, not just derivative zeros, to justify local extrema.
:::

:::exam{topic="Justification language"}
Write conclusions in terms of signs and changes: "$$f$$ has a local maximum at $$x=c$$ because $$f'$$ changes from positive to negative there." This is stronger than saying "$$f'(c)=0$$."
:::

For optimization, the derivative work is only the middle of the problem. A complete solution should also define variables, state the constraint, state the domain, and answer in the original units.

:::equations
| Idea | Equation and conditions |
| --- | --- |
| Mean Value Theorem | $$f'(c)=[f(b)-f(a)]/(b-a),\quad a<c<b$$; continuous on $$[a,b]$$, differentiable on $$(a,b)$$ |
| Interior candidates | $$f'(c)=0\text{ or }f'(c)\text{ undefined},\quad c\in\operatorname{dom}f$$ |
| Local maximum | $$f':+\to-$$ |
| Local minimum | $$f':-\to+$$ |
| Concavity | $$f''>0:\text{ up};\quad f''<0:\text{ down}$$ |
| Inflection candidate | $$f''(c)=0$$ or undefined; check for a concavity change at a continuous point |
| Second derivative test | $$f'(c)=0,\quad f''(c)>0:\text{ min};\quad f''(c)<0:\text{ max}$$ |
| Newton update | $$x_{n+1}=x_n-f(x_n)/f'(x_n),\quad f'(x_n)\ne0$$ |
:::
