---
title: "Unit 8: Applications of Integration"
description: "AP Calculus notes on area, volume, average value, arc length, improper integrals, and integration applications."
sidebar:
  order: 8
---

## Average value of a function

The average value of $$f$$ on $$[a,b]$$ is the constant height that would produce the same signed area over the interval:

On $$[a,b]$$:

$$
f_{\text{avg}} = \frac{1}{b-a}\int_a^b f(x)\,dx.
$$

This is different from the average rate of change. Average value averages outputs; average rate of change compares endpoint outputs.

<div class="theorem-box">

**Proof (Average value formula).** Suppose the average value of $$f$$ on $$[a,b]$$ is the constant height $$H$$. The rectangle with base length $$b-a$$ and height $$H$$ should have the same signed area as the graph:

$$
H(b-a)=\int_a^b f(x)\,dx.
$$

Solving for $$H$$ gives

$$
H=\frac{1}{b-a}\int_a^b f(x)\,dx.
$$

So the average value is

$$
f_{\text{avg}} = \frac{1}{b-a}\int_a^b f(x)\,dx.
$$

</div>

<div class="theorem-box">

**Example.** Find the average value of $$f(x)=x^2$$ on $$[0,3]$$.

Apply the average value formula with $$a=0$$ and $$b=3$$:

$$
f_{\text{avg}} = \frac{1}{3-0}\int_0^3 x^2\,dx.
$$

The definite integral was computed earlier as $$\int_0^3 x^2\,dx = 9$$, so

$$
f_{\text{avg}} = \frac{1}{3}\cdot 9 = 3.
$$

The average value is $$3$$: a constant height of $$3$$ would enclose the same area over $$[0,3]$$ as the curve does.

</div>

### Average value, average rate, and average speed

Average value measures a typical output over a whole interval. Average rate of change measures net output change per input change. They can have different units even when they refer to the same original function.

For position $$s(t)$$, average velocity is $$[s(b)-s(a)]/(b-a)$$. This is also the average value of the velocity function, because integrating velocity gives displacement. Average speed instead divides total distance by elapsed time, so its integral uses $$\lvert v\rvert$$.

An average of endpoint values is generally not the average value of a function. The expression $$[f(a)+f(b)]/2$$ is the average height of the secant segment, and is exact for the function's average only in special situations, such as a linear function.

<div class="theorem-box">

**Example.** A temperature is modeled by $$T(t)=20+12\sin(\pi t/6)$$ degrees Celsius for $$0\le t\le6$$ hours. Find its average temperature, its average rate of change, and the times when it equals its average temperature.

The average temperature is

$$
T_{\mathrm{avg}}
=\frac16\int_0^6\left(20+12\sin\frac{\pi t}{6}\right)\,dt
=20+\frac{24}{\pi}.
$$

The average rate of change is zero because both endpoint temperatures are twenty:

$$
\frac{T(6)-T(0)}6=0.
$$

To find where the temperature equals its average, solve

$$
\sin\frac{\pi t}{6}=\frac2\pi.
$$

On the stated interval there are two solutions:

$$
t=\frac6\pi\arcsin\frac2\pi,
\qquad
t=6-\frac6\pi\arcsin\frac2\pi.
$$

The temperature spends the interior of the interval above its endpoint values, so an average rate of zero does not imply an average temperature of twenty. Continuity guarantees at least one input where the temperature equals its average value, but it does not guarantee exactly one.

</div>

---

## Straight line motion and integration

If velocity is $$v(t)$$, then:

$$
\text{displacement} = \int_a^b v(t)\,dt
$$

$$
\text{total distance} = \int_a^b \lvert v(t) \rvert\,dt
$$

Note that displacement is your net change (signed area), meaning if you traveled around the Earth and traveled back to where you started you have $$0$$ displacement. However, distance measures your total travel, meaning that it is geometric area.

If acceleration is given, integrate acceleration to get change in velocity. If velocity is given, integrate velocity to get change in position. This is just the Fundamental Theorem of Calculus in motion language:

$$
\int_a^b v(t)\,dt=s(b)-s(a),
$$

because $$v(t)=s'(t)$$. Similarly,

$$
\int_a^b a(t)\,dt=v(b)-v(a),
$$

because $$a(t)=v'(t)$$.

So integration does not directly give the final position or final velocity unless you also know an initial value:

$$
s(b)=s(a)+\int_a^b v(t)\,dt,
$$

and

$$
v(b)=v(a)+\int_a^b a(t)\,dt.
$$

<div class="theorem-box">

**Example.** A particle moves with velocity $$v(t)=t^2-4$$ (in suitable units) for $$0\le t\le 3$$. Find its displacement and its total distance traveled.

First find where the velocity changes sign:

$$
t^2-4=0 \;\Longrightarrow\; t=2,
$$

(taking the positive root in the interval). For $$0\le t<2$$ the velocity is negative, and for $$2<t\le3$$ it is positive.

The displacement is the signed integral over the whole interval:

$$
\int_0^3 (t^2-4)\,dt
= \left[\frac{t^3}{3}-4t\right]_0^3
= (9-12)-0
= -3.
$$

For total distance, split at $$t=2$$ and integrate $$\lvert v(t)\rvert$$:

$$
\int_0^2 (4-t^2)\,dt
= \left[4t-\frac{t^3}{3}\right]_0^2
= 8-\frac83
= \frac{16}{3},
$$

$$
\int_2^3 (t^2-4)\,dt
= \left[\frac{t^3}{3}-4t\right]_2^3
= (9-12)-\left(\frac83-8\right)
= -3+\frac{16}{3}
= \frac{7}{3}.
$$

Adding the two pieces,

$$
\text{total distance}=\frac{16}{3}+\frac{7}{3}=\frac{23}{3}.
$$

So the displacement is $$-3$$ while the total distance is $$\frac{23}{3}$$, confirming that the two quantities differ once the velocity changes sign.

</div>

### Recovering motion from acceleration and initial data

An acceleration formula determines velocity only after an initial velocity is supplied. Velocity then determines position only after an initial position is supplied. Each integration introduces its own constant or initial-value term.

For total distance, find where the recovered velocity changes sign. Zeros of acceleration do not determine when position reverses direction. A particle can continue moving forward while its velocity increases and decreases.

<div class="theorem-box">

**Example.** A particle has acceleration $$a(t)=6t-6$$ meters per second squared, with $$v(0)=0$$ and $$s(0)=4$$ meters. Find its position at $$t=3$$, its displacement, and its distance traveled on $$[0,3]$$.

Integrate acceleration using the initial velocity:

$$
v(t)=0+\int_0^t(6u-6)\,du=3t^2-6t.
$$

The velocity is negative between zero and two and positive after two. Recover position:

$$
s(t)=4+\int_0^t(3u^2-6u)\,du
=4+t^3-3t^2.
$$

Thus $$s(3)=4$$, giving displacement zero. However, $$s(2)=0$$, so the particle first moves from position four to zero and then returns from zero to four.

The total distance is

$$
\int_0^2(-3t^2+6t)\,dt
+\int_2^3(3t^2-6t)\,dt=4+4=8
$$

meters. Its average velocity is zero, while its average speed is $$8/3$$ meters per second. The equal initial and final positions erase net change, but they do not erase the intermediate travel.

</div>

### Net rates and the largest amount

For a tank, population, or inventory, integrate the net rate to recover the amount:

$$
Q(t)=Q(a)+\int_a^t[\text{input rate}-\text{output rate}]\,du.
$$

To find when the amount is largest, analyze this net rate as the derivative of $$Q$$. The largest input rate is not necessarily the time of largest amount: accumulation can keep rising after the input rate has already begun falling, as long as it still exceeds the output rate.

<div class="theorem-box">

**Example.** A tank contains fifty liters at time zero. Water enters at $$10+2t$$ liters per minute and leaves at $$t^2$$ liters per minute for $$0\le t\le5$$. Find the maximum volume and verify that the model never predicts an empty tank.

The volume derivative is

$$
V'(t)=10+2t-t^2.
$$

Its positive root is $$c=1+\sqrt{11}$$. The other root is negative and outside the time domain. The net rate is positive before $$c$$ and negative afterward, so the maximum occurs at $$c$$.

The amount function is

$$
V(t)=50+10t+t^2-\frac{t^3}{3}.
$$

Using $$c^2=2c+10$$ and $$c^3=14c+20$$ simplifies the maximum:

$$
V(c)=\frac{182+22\sqrt{11}}3
\text{ liters}.
$$

Because the function increases and then decreases, its minimum on this interval is at an endpoint. The endpoint values are $$V(0)=50$$ and $$V(5)=250/3$$, both positive. Thus the model remains physically consistent with a nonempty tank throughout the interval.

</div>

---

## Areas between curves

Area between curves is still an accumulation problem. Instead of adding rectangles from the $$x$$-axis to one curve, each thin rectangle measures the distance between two curves, and integrates the function of the distances.

For vertical slices, if $$f(x)$$ is the top function and $$g(x)$$ is the bottom function (in terms of $$y$$ location):

$$
A=\int_a^b f(x) - g(x) \,dx.
$$

For horizontal slices, if $$h(y)$$ is the right function and $$j(y)$$ is the left function (in terms of $$x$$ location)

$$
A=\int_c^d h(y) - j(y) \,dy.
$$

:::warning
Do not assume the first function listed is on top. Test a point or inspect the graph. If the curves cross, split the interval at the crossing.
:::

The subtraction order is chosen so each slice length is nonnegative.

:::strategy
1. Sketch or reason about the region.
2. Find intersection points to determine bounds.
3. Decide whether vertical or horizontal slices describe the region more cleanly.
4. Write top minus bottom for $$dx$$, or right minus left for $$dy$$.
5. Split the integral if the top/bottom or right/left relationship changes.
:::

<div class="theorem-box">

**Example.** Find the area enclosed by $$y=x$$ and $$y=x^2$$.

First find the intersection points:

$$
x=x^2
\quad\Longrightarrow\quad
x(x-1)=0.
$$

So the curves meet at $$x=0$$ and $$x=1$$. On $$[0,1]$$, the line $$y=x$$ is above $$y=x^2$$. Therefore

$$
A=\int_0^1 (x-x^2)\,dx.
$$

Evaluate:

$$
A=\left[\frac{x^2}{2}-\frac{x^3}{3}\right]_0^1
=
\frac12-\frac13
=
\frac16.
$$

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle, xmin=-0.2, xmax=1.25, ymin=-0.1, ymax=1.25,
  xtick={0,0.5,1}, ytick={0,0.5,1},
  grid=both, grid style={gray!18},
  width=7.5cm, height=6.5cm,
  xlabel=$x$, ylabel=$y$,
]
\addplot[blue, very thick, domain=0:1, samples=80] {x};
\addplot[red!75!black, very thick, domain=0:1, samples=80] {x^2};
\draw[orange!18, fill=orange!18] (axis cs:0.55,0.3025) -- (axis cs:0.58,0.3364) -- (axis cs:0.58,0.58) -- (axis cs:0.55,0.55) -- cycle;
\node[blue, anchor=south west] at (axis cs:0.25,0.65) {top $y=x$};
\node[red!75!black, anchor=north west] at (axis cs:0.65,0.42) {bottom $y=x^2$};
\draw[<->, orange!85!black, thick] (axis cs:0.565,0.319) -- (axis cs:0.565,0.565);
\end{axis}
\end{tikzpicture}
```

</div>

<div class="theorem-box">

**Example.** Find the area of the region bounded by $$x=y^2$$ and $$x=2-y$$.

These equations are easier to compare using horizontal slices because both are already written as $$x$$ in terms of $$y$$. Find intersections:

$$
y^2=2-y
\quad\Longrightarrow\quad
y^2+y-2=0
\quad\Longrightarrow\quad
(y+2)(y-1)=0.
$$

So $$y=-2$$ and $$y=1$$. On this interval, the right curve is $$x=2-y$$ and the left curve is $$x=y^2$$. The area is

$$
A=\int_{-2}^{1}\left[(2-y)-y^2\right]\,dy.
$$

Evaluate:

$$
A=\left[2y-\frac{y^2}{2}-\frac{y^3}{3}\right]_{-2}^{1}
=
\frac{9}{2}.
$$

</div>

### Curves that exchange top and bottom

An intersection can separate two different bounded regions. Integrating one signed difference over both regions can cancel part or all of their geometric area. Find every relevant intersection first, then test which function is above on each interval.

<div class="theorem-box">

**Example.** Find the total area enclosed by $$y=x^3$$ and $$y=x$$.

Solve $$x^3=x$$:

$$
x(x-1)(x+1)=0,
$$

so the intersections occur at negative one, zero, and one. On $$(-1,0)$$, the cubic is above the line. On $$(0,1)$$, the line is above the cubic.

Therefore,

$$
A=\int_{-1}^{0}(x^3-x)\,dx
+\int_0^1(x-x^3)\,dx.
$$

The two regions are symmetric, so

$$
A=2\int_0^1(x-x^3)\,dx
=2\left(\frac12-\frac14\right)=\frac12.
$$

By contrast, $$\int_{-1}^1(x^3-x)\,dx=0$$ because that integrand is odd. This signed cancellation cannot be the area of two nonempty regions.

</div>

### Choosing the slice direction before solving for bounds

Horizontal slices can avoid splitting a region into several vertical pieces. For the region between $$x=y^2$$ and $$x=2-y$$, a horizontal slice has one continuous left boundary and one continuous right boundary for $$-2\le y\le1$$.

If you insist on vertical slices, the parabola becomes $$y=\pm\sqrt{x}$$. Part of the upper boundary follows $$\sqrt{x}$$ and another part follows $$2-x$$, so a split is needed. Both approaches describe the same region, but the horizontal setup keeps its geometry visible with one integral.

Do not choose a variable merely because one equation is written as $$y=f(x)$$. Sketch one candidate slice in each direction and ask whether its two endpoints can be described consistently over the entire region.

---

## Calculating volumes

Volume problems use the same slicing idea as area problems, but each slice has area instead of length. The general structure is

$$
V=\int A(\text{slice})\,d(\text{slice variable}).
$$

The main work is deciding what the cross-sectional area $$A$$ is.

### Volumes with known cross sections

If a solid has cross-sectional area $$A(x)$$ perpendicular to the $$x$$-axis, then

$$
V=\int_a^b A(x)\,dx.
$$

Common cross sections include squares, rectangles, semicircles, and equilateral triangles.

The length of a segment in the base determines a dimension of the cross section, but you must identify which dimension. If the segment of length $$s$$ is a semicircle's diameter, its area is $$\pi s^2/8$$, not $$\pi s^2/2$$. For an equilateral triangle with side $$s$$, the altitude is $$\sqrt3s/2$$, giving area $$\sqrt3s^2/4$$.

The area formula belongs inside the volume integral. A base segment is a length, its associated cross-sectional formula has square units, and multiplying by slice thickness produces cubic units. This unit sequence catches missing squares and mistaken radius factors.

```tikz
\usepackage{tikz}
\begin{tikzpicture}[scale=0.9]
\draw[->, gray!70] (-0.3,0) -- (5.2,0) node[right] {$x$};
\draw[->, gray!70] (0,-0.2) -- (0,2.9) node[above] {$y$};
\draw[blue, very thick] plot[smooth] coordinates {(0,0) (1,0.7) (2,1.2) (3,1.45) (4,1.65)};
\draw[red!75!black, very thick] plot[smooth] coordinates {(0,0) (1,0.2) (2,0.35) (3,0.45) (4,0.5)};
\foreach \x/\top/\bot in {1/0.7/0.2,2/1.2/0.35,3/1.45/0.45,4/1.65/0.5} {
  \draw[orange!85!black, thick] (\x,\bot) -- (\x,\top);
  \draw[orange!30, fill=orange!15] (\x,\top) -- ++(0.45,0.28) -- ++(0,-{\top-\bot}) -- (\x,\bot) -- cycle;
}
\node[blue] at (3.3,2.15) {base region};
\node[orange!85!black, align=center] at (5.0,1.35) {cross sections\\perpendicular to $x$};
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** A solid has base bounded by $$y=x$$ and $$y=x^2$$ for $$0\le x\le1$$. Cross sections perpendicular to the $$x$$-axis are squares. Find the volume.

The side length of each square is top minus bottom:

$$
s=x-x^2.
$$

So the cross-sectional area is

$$
A(x)=s^2=(x-x^2)^2.
$$

Therefore

$$
V=\int_0^1 (x-x^2)^2\,dx.
$$

Expand and integrate:

$$
V=\int_0^1 (x^2-2x^3+x^4)\,dx
=
\left[\frac{x^3}{3}-\frac{x^4}{2}+\frac{x^5}{5}\right]_0^1
=
\frac{1}{30}.
$$

</div>

### Cross sections with a diameter instead of a radius

<div class="theorem-box">

**Example.** A solid has base bounded by $$y=2x$$ and $$y=x^2$$. Its cross sections perpendicular to the horizontal axis are semicircles whose diameters lie in the base. Find the volume. Then compare with the solid formed using semicircular cross sections perpendicular to the vertical axis.

For vertical slices, the intersections are at zero and two, and the diameter is $$d=2x-x^2$$. A semicircle with diameter $$d$$ has radius $$d/2$$ and area $$\pi d^2/8$$. Therefore,

$$
V_x=\frac\pi8\int_0^2(2x-x^2)^2\,dx
=\frac\pi8\cdot\frac{16}{15}
=\frac{2\pi}{15}.
$$

For horizontal slices, rewrite the boundaries as $$x=y/2$$ and $$x=\sqrt y$$. Over $$0\le y\le4$$, the right endpoint is $$\sqrt y$$ and the left endpoint is $$y/2$$, so

$$
V_y=\frac\pi8\int_0^4\left(\sqrt y-\frac y2\right)^2\,dy.
$$

Expand before integrating:

$$
V_y=\frac\pi8\int_0^4\left(y-y^{3/2}+\frac{y^2}{4}\right)\,dy
=\frac\pi8\left(8-\frac{64}{5}+\frac{16}{3}\right)
=\frac\pi{15}.
$$

These volumes differ because changing the direction of the prescribed cross sections creates a different solid. This differs from choosing two integration methods for the same solid of revolution, where correct setups must agree.

</div>

### Disk and washer methods

When a region is revolved around an axis, a slice perpendicular to the axis forms a disk or washer.

If every perpendicular slice reaches the axis and leaves no central hole, use the disk method:

$$
V=\pi\int_a^b [R(x)]^2\,dx.
$$

If every perpendicular slice has an outer radius and a smaller positive inner radius, use the washer method:

$$
V=\pi\int_a^b \left([R(x)]^2-[r(x)]^2\right)\,dx.
$$

Here $$R$$ is the larger distance to the axis and $$r$$ is the smaller distance. They need not correspond to the top and bottom functions in that order. Subtract the squared radii to remove the central hole. Squaring the difference of the radii would instead describe an entirely different disk.

```tikz
\usepackage{tikz}
\begin{tikzpicture}[scale=0.9]
\draw[gray!70, thick, ->] (-0.6,0) -- (6.4,0) node[right] {axis};
\fill[blue!15] (0.8,0) ellipse (0.32 and 1.2);
\draw[blue, very thick] (0.8,0) ellipse (0.32 and 1.2);
\draw[orange!85!black, <->] (0.8,0) -- (0.8,1.2) node[midway, right] {$R$};
\node[blue] at (0.8,-1.65) {disk};
\fill[blue!15, even odd rule] (4,0) ellipse (0.42 and 1.35) (4,0) ellipse (0.18 and 0.55);
\draw[blue, very thick] (4,0) ellipse (0.42 and 1.35);
\draw[red!75!black, very thick] (4,0) ellipse (0.18 and 0.55);
\draw[orange!85!black, <->] (4.55,0) -- (4.55,1.35) node[midway, right] {$R$};
\draw[red!75!black, <->] (4,0) -- (4,0.55) node[midway, left] {$r$};
\node[blue] at (4,-1.95) {washer};
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** Find the volume formed by revolving the region between $$y=\sqrt{x}$$ and the $$x$$-axis on $$[0,4]$$ about the $$x$$-axis.

The radius is $$R(x)=\sqrt{x}$$. There is no hole, so this is a disk problem:

$$
V=\pi\int_0^4(\sqrt{x})^2\,dx
=
\pi\int_0^4x\,dx.
$$

Evaluate:

$$
V=\pi\left[\frac{x^2}{2}\right]_0^4=8\pi.
$$

</div>

### Rotation about a shifted axis

When rotating about $$y=k$$, the radius to a point at height $$y$$ is $$\lvert y-k\rvert$$. For an axis above the whole region, the lower boundary is farther away and supplies the outer radius. For a vertical axis $$x=k$$, horizontal washers use the distances $$\lvert x-k\rvert$$.

<div class="theorem-box">

**Example.** Revolve the region between $$y=x$$ and $$y=x^2$$ for $$0\le x\le1$$ about $$y=2$$. Find the volume.

The axis is above both curves. Since $$x^2\le x$$ on this interval, the lower curve $$x^2$$ lies farther from the axis:

$$
R(x)=2-x^2,
\qquad
r(x)=2-x.
$$

The washer setup is

$$
V=\pi\int_0^1\left[(2-x^2)^2-(2-x)^2\right]\,dx.
$$

After expanding,

$$
V=\pi\int_0^1(4x-5x^2+x^4)\,dx
=\pi\left(2-\frac53+\frac15\right)
=\frac{8\pi}{15}.
$$

Using the top function as the outer radius would reverse the subtraction and produce a negative volume. The distance to the axis decides the order.

</div>

### When the axis passes through the region

If a slice crosses the axis, rotating it fills the center. There is no hole to subtract, even if both original endpoints have nonzero distance from the axis. The radius is the larger of their two distances.

<div class="theorem-box">

**Example.** The region $$0\le x\le1$$, $$0\le y\le x$$ is rotated about $$y=1/2$$. Set up and evaluate its volume.

For $$0\le x\le1/2$$, the slice lies below the axis. It produces a washer with outer radius $$1/2$$ and inner radius $$1/2-x$$.

For $$1/2\le x\le1$$, the slice crosses the axis. Its lower endpoint is always at distance $$1/2$$, while the upper endpoint has distance $$x-1/2\le1/2$$. Rotation fills a disk of radius $$1/2$$.

Thus

$$
V=\pi\int_0^{1/2}\left[\frac14-\left(\frac12-x\right)^2\right]\,dx
+\pi\int_{1/2}^1\frac14\,dx.
$$

The first integral contributes $$\pi/12$$ and the second contributes $$\pi/8$$, giving

$$
V=\frac{5\pi}{24}.
$$

The switch occurs because the slice first touches and then crosses the axis. Treating every slice as a washer would remove material from a center that is actually filled.

</div>

<div class="theorem-box">

**Example.** Find the volume formed by revolving the region between $$y=4-x^2$$ and $$y=0$$ about the line $$y=-1$$.

The axis is below the region, so each washer has outer radius from $$y=-1$$ to $$y=4-x^2$$:

$$
R(x)=5-x^2.
$$

The inner radius is from $$y=-1$$ to $$y=0$$:

$$
r(x)=1.
$$

The curve meets the $$x$$-axis at $$x=-2$$ and $$x=2$$. Therefore

$$
V=\pi\int_{-2}^{2}\left[(5-x^2)^2-1^2\right]\,dx.
$$

Expand:

$$
(5-x^2)^2-1=25-10x^2+x^4-1=24-10x^2+x^4.
$$

So

$$
V=\pi\left[24x-\frac{10x^3}{3}+\frac{x^5}{5}\right]_{-2}^{2}
=\frac{1216\pi}{15}.
$$

</div>

### Cylindrical shells

Shells come from slices parallel to the axis of rotation. A thin shell has approximate volume

$$
dV=2\pi(\text{radius})(\text{height})(\text{thickness}).
$$

Thus

$$
V=2\pi\int_a^b(\text{radius})(\text{height})\,d(\text{slice variable}).
$$

Shells are often cleaner when washers would require solving for inverse functions or splitting the region.

Choose shells when the slice is parallel to the axis, and washers when it is perpendicular. The differential follows the slice thickness, not the axis label: vertical shells use $$dx$$, while horizontal shells use $$dy$$. Around a vertical axis $$x=k$$, a vertical shell's radius is $$\lvert x-k\rvert$$ and its height is the vertical length of the region.

If the axis passes through the base region, shells from opposite sides can sweep out overlapping material. Do not add those shell volumes blindly. A perpendicular-slice setup often makes the filled cross sections easier to describe without double counting.

```tikz
\usepackage{tikz}
\begin{tikzpicture}[scale=0.9]
\draw[gray!70, thick, ->] (-0.5,0) -- (5.6,0) node[right] {axis};
\draw[blue, very thick] (2.8,0) ellipse (0.55 and 1.55);
\draw[blue!50, thick] (2.5,-1.55) -- (2.5,1.55);
\draw[blue!50, thick] (3.1,-1.55) -- (3.1,1.55);
\draw[orange!85!black, <->] (0,0.25) -- (2.8,0.25) node[midway, above] {radius};
\draw[red!75!black, <->] (3.55,-1.55) -- (3.55,1.55) node[midway, right] {height};
\draw[gray!60, <->] (2.5,-1.85) -- (3.1,-1.85) node[midway, below] {thickness};
\node[blue] at (2.8,2.0) {thin cylindrical shell};
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** Find the volume formed by revolving the region under $$y=x^2$$ from $$x=0$$ to $$x=2$$ about the $$y$$-axis using shells.

A vertical slice has radius $$x$$ and height $$x^2$$. Therefore

$$
V=2\pi\int_0^2 x(x^2)\,dx
=
2\pi\int_0^2 x^3\,dx.
$$

Evaluate:

$$
V=2\pi\left[\frac{x^4}{4}\right]_0^2
=
8\pi.
$$

</div>

### Two descriptions of the same rotated solid

The region between $$y=x$$ and $$y=x^2$$ on $$[0,1]$$ gives volume $$\pi/6$$ when revolved about the vertical axis using shells. Horizontal washers must give that same result because the region and axis are unchanged.

For a fixed height $$0\le y\le1$$, the region extends from $$x=y$$ to $$x=\sqrt y$$. These are distances from the vertical axis, so the outer radius is $$\sqrt y$$ and the inner radius is $$y$$. Therefore,

$$
V=\pi\int_0^1\left[(\sqrt y)^2-y^2\right]\,dy
=\pi\int_0^1(y-y^2)\,dy=\frac\pi6.
$$

This comparison explains why the shell and washer integrands have different forms. Shells accumulate cylindrical layers by radius; washers accumulate circular cross sections by height. A method changes how the solid is partitioned, not which solid is being measured.

When the two answers disagree, check whether the slice direction changed without changing the variable, whether a boundary was inverted incorrectly, or whether the radius was measured from the wrong axis. Comparing methods is especially helpful for shifted-axis problems where a familiar-looking formula can conceal a missing constant.

<div class="theorem-box">

**Example.** Find the volume formed by revolving the region bounded by $$y=x$$ and $$y=x^2$$ about the $$y$$-axis using shells.

The curves intersect where

$$
x=x^2
\quad\Longrightarrow\quad
x=0,1.
$$

Using vertical shells, the radius is $$x$$ and the height is top minus bottom:

$$
h(x)=x-x^2.
$$

Thus

$$
V=2\pi\int_0^1 x(x-x^2)\,dx
=2\pi\int_0^1(x^2-x^3)\,dx.
$$

Evaluate:

$$
V=2\pi\left[\frac{x^3}{3}-\frac{x^4}{4}\right]_0^1
=2\pi\left(\frac13-\frac14\right)
=\frac{\pi}{6}.
$$

</div>

---

## Arc length (BC-only)

Suppose you wanted to find the length traveled along a graph from point $$a$$ to point $$b$$. If you zoom in far enough, each tiny part of a smooth curve looks almost like a straight line (linearization). Arc length adds those tiny straight-line distances.

For one tiny piece of curve, the horizontal change is $$dx$$ and the vertical change is $$dy$$. By the Pythagorean theorem,

$$
dL\approx \sqrt{(dx)^2+(dy)^2}.
$$

Since

$$
dy=f'(x)\,dx,
$$

the length element becomes

$$
dL=\sqrt{1+[f'(x)]^2}\,dx.
$$

For a smooth function $$y=f(x)$$ on $$[a,b]$$:

$$
L = \int_a^b \sqrt{1+[f'(x)]^2}\,dx.
$$

<div class="theorem-box">

**Example.** Find the arc length of $$y=\frac{2}{3}x^{3/2}$$ on $$0\le x\le3$$.

Differentiate:

$$
y'=\sqrt{x}.
$$

Then

$$
L=\int_0^3 \sqrt{1+(\sqrt{x})^2}\,dx
=
\int_0^3 \sqrt{1+x}\,dx.
$$

Use $$u=1+x$$, so $$du=dx$$. The bounds change from $$x=0$$ to $$u=1$$ and from $$x=3$$ to $$u=4$$:

$$
L=\int_1^4 u^{1/2}\,du
=
\left[\frac{2}{3}u^{3/2}\right]_1^4.
$$

So

$$
L=\frac{2}{3}(8-1)=\frac{14}{3}.
$$

</div>

---

## Surface area of revolution (extension)

Surface area is different from volume: instead of adding cross-sectional areas, it adds thin bands of surface.

If $$y=f(x)\ge0$$ is revolved around the $$x$$-axis on $$[a,b]$$, then the surface area is

$$
S=2\pi\int_a^b f(x)\sqrt{1+[f'(x)]^2}\,dx.
$$

If $$x=g(y)\ge0$$ is revolved around the $$y$$-axis on $$[c,d]$$, then

$$
S=2\pi\int_c^d g(y)\sqrt{1+[g'(y)]^2}\,dy.
$$

The radius is the distance to the axis of rotation. The square-root factor comes from arc length.

The formula comes from approximating the surface with many thin bands. A tiny piece of curve has length $$ds$$. When that tiny piece rotates around an axis, it sweeps out a thin band whose circumference is $$2\pi r$$ and whose width along the surface is approximately $$ds$$. So

$$
dS\approx 2\pi r\,ds.
$$

For $$y=f(x)$$ revolved around the $$x$$-axis, $$r=f(x)$$ and

$$
ds=\sqrt{1+[f'(x)]^2}\,dx.
$$

<div class="theorem-box">

**Example.** Set up and solve the surface area integral formed by revolving $$y=\sqrt{x}$$ on $$1\le x\le4$$ about the $$x$$-axis.

The radius is

$$
r=f(x)=\sqrt{x}.
$$

The derivative is

$$
f'(x)=\frac{1}{2\sqrt{x}}.
$$

So the surface area is

$$
S=2\pi\int_1^4 \sqrt{x}\sqrt{1+\left(\frac{1}{2\sqrt{x}}\right)^2}\,dx.
$$

Simplify the integrand:

$$
\sqrt{x}\sqrt{1+\frac{1}{4x}}
=
\sqrt{x}\sqrt{\frac{4x+1}{4x}}
=
\frac12\sqrt{4x+1}.
$$

Thus

$$
S=2\pi\int_1^4 \frac12\sqrt{4x+1}\,dx
=
\pi\int_1^4 \sqrt{4x+1}\,dx.
$$

Let $$u=4x+1$$, so $$du=4\,dx$$. When $$x=1$$, $$u=5$$. When $$x=4$$, $$u=17$$. Therefore

$$
S=\frac{\pi}{4}\int_5^{17}u^{1/2}\,du
=
\frac{\pi}{4}\left[\frac{2}{3}u^{3/2}\right]_5^{17}.
$$

So

$$
S=\frac{\pi}{6}\left(17^{3/2}-5^{3/2}\right)
=
\frac{\pi}{6}(17\sqrt{17}-5\sqrt5).
$$

</div>

### Checking arc length against displacement

Arc length measures travel along a curve and must be at least the straight-line distance between the endpoints. It is also at least the magnitude of the net horizontal change, because $$\sqrt{1+(f')^2}\ge1$$.

The integral $$\int_a^b f'(x)\,dx$$ gives vertical change, not curve length. Integrating $$\lvert f'(x)\rvert$$ gives total vertical variation, which still omits the horizontal component of each piece of travel.

For a line of slope $$m$$, the arc-length formula becomes $$(b-a)\sqrt{1+m^2}$$. This agrees with the Pythagorean theorem using horizontal change $$b-a$$ and vertical change $$m(b-a)$$, providing a direct check on the square-root factor.

Surface area adds circumference times arc length, whereas volume adds cross-sectional area times thickness. These formulas use different pieces even when the same radius appears in both. Surface area also excludes end caps unless the problem explicitly asks to include them.

---

## Applications to statistics: Probability density functions (extension)

A probability density function $$p(x)$$ must satisfy

$$
p(x)\ge0
$$

and

$$
\int_{-\infty}^{\infty}p(x)\,dx=1.
$$

For a continuous random variable,

$$
P(a\le X\le b)=\int_a^b p(x)\,dx.
$$

The mean, or expected value, is

$$
\mu=\int_{-\infty}^{\infty}x\,p(x)\,dx.
$$

<div class="theorem-box">

**Example.** Let

$$
p(x)=kx
$$

on $$0\le x\le2$$ and $$p(x)=0$$ elsewhere. Find $$k$$ so that $$p$$ is a probability density function.

The total probability must be $$1$$:

$$
\int_0^2 kx\,dx=1.
$$

Evaluate:

$$
k\left[\frac{x^2}{2}\right]_0^2=1
\quad\Longrightarrow\quad
2k=1.
$$

Thus

$$
k=\frac12.
$$

</div>

### Density height is not a probability

A probability density can have a height greater than one; what must remain between zero and one is the area over an event interval. For a continuous random variable, a single point has probability zero because an interval of zero width contributes zero area.

Expected value is a weighted average, with $$p(x)\,dx$$ representing probability weight. It is different from the average value of the density graph. Integrating $$xp(x)$$ weights each possible output by how likely nearby values are.

<div class="theorem-box">

**Example.** Let $$p(x)=kx(2-x)$$ on $$[0,2]$$ and zero elsewhere. Find $$k$$, the probability that $$X\le1/2$$, and the expected value.

Normalization gives

$$
1=k\int_0^2(2x-x^2)\,dx=\frac{4k}{3},
\qquad k=\frac34.
$$

The requested probability is

$$
P(X\le1/2)
=\frac34\left[x^2-\frac{x^3}{3}\right]_0^{1/2}
=\frac5{32}.
$$

For the expected value,

$$
E[X]=\frac34\int_0^2(2x^2-x^3)\,dx=1.
$$

The density is symmetric about one, which independently confirms that mean. The probability calculation uses an interval area, while the mean calculation includes the extra factor $$x$$.

</div>

---

### Interpreting an integral when only data are available

A formula is not required to apply the accumulation principle. With a rate table, an integral can be estimated using the measured values and actual subinterval widths. A nonlinear quantity such as a volume radius must still be formed before the numerical rule is applied.

<div class="theorem-box">

**Example.** A pump's flow rate is measured in liters per minute:

$$
\begin{array}{c|cccc}
t\text{ (minutes)}&0&1&3&6\\\hline
R(t)&4&7&5&2
\end{array}
$$

Use trapezoids to estimate the amount pumped over six minutes and its average flow rate.

The widths are one, two, and three minutes, so

$$
\int_0^6R(t)\,dt
\approx\frac12(4+7)(1)
+\frac12(7+5)(2)
+\frac12(5+2)(3)
=28.
$$

The amount is approximately twenty-eight liters. The average flow rate is therefore

$$
R_{\mathrm{avg}}\approx\frac{28}{6}=\frac{14}{3}
\text{ liters per minute}.
$$

A simple average of the four measured rates would give equal weight to measurements representing intervals of different lengths. It would not be the same calculation. Also, the table does not establish concavity between measurements, so it does not justify calling the trapezoidal estimate an overestimate or underestimate.

</div>

---

## Tips for the exam

Applications of integration are mostly about choosing the correct tiny piece.

Before evaluating, check what one integrand term represents and multiply its units by the units of the differential. A volume setup needs area times length, a motion setup needs speed times time, and an average-value setup divides the accumulated quantity by interval width. Then check the geometry independently: slice lengths and radii are nonnegative, holes are subtracted only when they actually exist, and a region should be counted once. These checks are especially useful when the antiderivative is easy, since a quick calculation can otherwise hide an incorrect model.

:::strategy
1. Area between curves: slice vertically for top minus bottom or horizontally for right minus left.
2. Volume by cross sections: identify the base interval and write the cross-sectional area $$A(x)$$ or $$A(y)$$.
3. Washers/disks: radii are perpendicular to the axis of rotation.
4. Shells: radius is distance to the axis, and height is the length of the slice.
5. Motion: signed velocity gives displacement, while speed gives total distance.
:::

:::exam{topic="Set up before evaluate"}
AP free-response questions often award setup points even when the integral is not evaluated. A correct integral with correct bounds, radii, and slice direction is the main goal.
:::

When curves cross, split the interval at every intersection point. The expression "top minus bottom" or "right minus left" can change from one subinterval to the next.

:::equations
| Idea | Equation and conditions |
| --- | --- |
| Average value | $$f_{\mathrm{avg}}=\dfrac1{b-a}\int_a^bf(x)\,dx,\quad a<b$$ |
| Position from velocity | $$s(b)=s(a)+\int_a^bv(t)\,dt$$ |
| Total distance | $$D=\int_a^b\lvert v(t)\rvert\,dt$$ |
| Geometric area | $$A=\int_a^b\lvert f(x)-g(x)\rvert\,dx$$ |
| Known cross sections | $$V=\int_a^bA(x)\,dx$$ |
| Washers | $$V=\pi\int_a^b(R^2-r^2)\,dx,\quad R\ge r\ge0$$ |
| Shells | $$V=2\pi\int(\text{radius})(\text{height})\,d(\text{slice variable})$$ |
| Graph arc length | $$L=\int_a^b\sqrt{1+[f'(x)]^2}\,dx$$ |
| Surface area extension | $$S=2\pi\int r\,ds$$ |
| Density extension | $$P(a\le X\le b)=\int_a^bp(x)\,dx,\quad E[X]=\int xp(x)\,dx$$ |
:::
