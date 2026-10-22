---
title: "Unit 4: Contextual Applications of Differentiation"
description: "AP Calculus notes on interpreting derivatives in context, motion, related rates, linearization, and differential models."
sidebar:
  order: 4
---

---

## Rates of change in context

Many contextual problems describe how a system changes over time. If $$Q(t)$$ is a quantity depending on time, then:

- $$Q'(t)$$ is the instantaneous rate of change of $$Q$$,
- units of $$Q'(t)$$ are units of $$Q$$ per unit of $$t$$.

Always interpret both sign and units and give sufficient context if necessary.

Many contextual problems distinguish between average and instantaneous rates of change. The average rate on $$[a,b]$$ is the slope of the secant line:

$$
\frac{Q(b)-Q(a)}{b-a},
$$

while the instantaneous rate at $$t=a$$ is the derivative:

$$
Q'(a).
$$

If you are trying to figure out a mean or average, use average rate of change, but if you are trying to find your speed or rate of change at a specific moment, use derivatives.

To interpret a derivative in a word problem, include these 4 components:

- the quantity changing,
- the input value or time,
- the direction of change if the sign matters,
- correct units.

For example, if $$H(t)$$ is height in meters and $$H'(3)=-2$$, then at $$t=3$$ the height is decreasing at $$2$$ meters per unit of time. The negative sign means the height is going down, and the magnitude $$2$$ describes the speed of that change.

<div class="theorem-box">

**Example.** Let $$P(t)$$ be the number of fish in a lake, where $$t$$ is measured in years. Write a full sentence interpreting the statement $$P'(5)=40$$.

The quantity changing is the fish population, measured in fish; the input is time in years; the sign is positive, so the population is growing; and the units of the derivative are fish per year. A complete interpretation is:

At time $$t=5$$ years, the fish population is increasing at a rate of $$40$$ fish per year.

Notice that this is a rate, not a total: it does not say there are $$40$$ fish, but rather that the population is growing by about $$40$$ fish for each additional year near $$t=5$$.

</div>

### Estimating a rate from measurements

When a table gives amounts rather than rates, a difference quotient estimates the derivative. Use nearby inputs on both sides of the requested input when they are available. The quotient still measures change in output divided by change in input, so its units do not depend on how the table is arranged.

A symmetric difference quotient often cancels some of the error from using a secant line, but it is still an estimate. A table alone does not tell you exactly how the function behaves between measurements. Even equal endpoint values do not prove that the function was constant between them.

<div class="theorem-box">

**Example.** A tank's volume is measured in liters:

$$
\begin{array}{c|ccc}
t\text{ (minutes)}&4&5&6\\\hline
V(t)\text{ (liters)}&210&201&188
\end{array}
$$

Estimate $$V'(5)$$, interpret the answer, and decide whether the measurements suggest that the rate of change is increasing or decreasing.

Use the measurements on either side of $$t=5$$:

$$
V'(5)\approx\frac{V(6)-V(4)}{6-4}
=\frac{188-210}{2}=-11.
$$

At five minutes, the volume is decreasing at approximately eleven liters per minute. This does not mean the tank contains negative water or that eleven liters have left over the entire experiment.

The adjacent secant slopes are

$$
\frac{201-210}{5-4}=-9,
\qquad
\frac{188-201}{6-5}=-13.
$$

The later average rate is more negative, suggesting that $$V'$$ is decreasing and the volume is falling more rapidly. These three measurements support that interpretation, but they do not by themselves prove $$V''<0$$ at every intermediate time.

</div>

### Composing rates and checking units

If a quantity depends on another changing quantity, chain rule can be used to connect the rates. Suppose temperature depends on height, and height depends on time. Then temperature depends on time through height:

$$
\frac{dT}{dt}=\frac{dT}{dh}\frac{dh}{dt}.
$$

The units explain the relationship. Degrees per meter multiplied by meters per second gives degrees per second. A negative temperature gradient and a negative vertical velocity produce a positive temperature rate: descending through colder air above can make the measured temperature rise. The derivative $$dT/dh$$ is a rate with respect to height, not automatically a rate with respect to time. Multiplying by $$dh/dt$$ is the step that accounts for how quickly the object moves through the changing environment.

<div class="theorem-box">

**Example.** A probe measures temperature $$T(h)=20-0.006h$$ degrees Celsius at altitude $$h$$ meters. At one instant it is descending at $$8$$ meters per second. Find the temperature rate experienced by the probe.

The environmental temperature gradient and the probe's vertical velocity are

$$
\frac{dT}{dh}=-0.006,
\qquad
\frac{dh}{dt}=-8.
$$

Therefore,

$$
\frac{dT}{dt}=(-0.006)(-8)=0.048.
$$

The probe experiences a temperature increase of $$0.048$$ degrees Celsius per second at that instant. The temperature model assumes that temperature depends only on altitude; an independently changing weather pattern would require additional information.

</div>

### Interpreting graphs in context

Given a graph of a function $$f$$:

- slope describes the derivative $$f'$$,
- steep positive slope means rapid increase,
- slope near zero means little short-term change,
- concavity tells whether the rate itself is increasing or decreasing.

Given a graph of a derivative $$f'$$:

- positive derivative means original function is increasing,
- negative derivative means decreasing,
- derivative crossing zero may indicate an extremum in the original function.

:::tip
Problems will often use and expect certain words:

- increasing means derivative positive,
- decreasing means derivative negative,
- at what rate means derivative value,
- how fast often means magnitude, but read carefully,
- changing more rapidly compares derivative magnitudes or second derivatives depending on context.
:::

<div class="theorem-box">

**Example.** A graph of $$P'(t)$$, the rate of change of a lake's fish population in fish per year, is given by $$P'(t)=(t-1)(t-5)$$ for $$0\le t\le6$$ years. Determine when the population is growing, when it is declining, and when it is declining most rapidly. Explain what happens at $$t=3$$.

The graph below represents the rate, not the population:

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle, xmin=-0.3, xmax=6.4, ymin=-5.5, ymax=6.5,
  xtick={0,1,3,5,6}, ytick={-4,0,5},
  grid=both, grid style={gray!15},
  width=9cm, height=5.5cm,
  xlabel=$t$, ylabel=$P'(t)$,
]
\addplot[blue, very thick, samples=120, domain=0:6] {(x-1)*(x-5)};
\addplot[only marks, mark=*, mark size=1.8pt, red!75!black] coordinates {(1,0) (3,-4) (5,0)};
\draw[gray!65, dashed] (axis cs:3,0) -- (axis cs:3,-4);
\node[red!75!black, anchor=north] at (axis cs:3,-4.15) {most negative rate};
\end{axis}
\end{tikzpicture}
```

The derivative is positive on $$(0,1)$$ and $$(5,6)$$, so the population grows there. It is negative on $$(1,5)$$, so the population declines there.

The most rapid decline occurs at the lowest value of the derivative graph, $$P'(3)=-4$$. At three years, the population is decreasing at four fish per year. This is not a minimum of the population: it continues falling until time five.

Before three years the derivative graph is decreasing; afterward it is increasing. Thus $$P$$ is concave down before three and concave up afterward. Between three and five, the population is still falling, but its rate is becoming less negative, so the decline is slowing.

The derivative changes from positive to negative at one, giving a local population maximum, and from negative to positive at five, giving a local population minimum. The actual population values cannot be read from this derivative graph without an initial population.

</div>

---

## Straight line motion

A lot of the contextual problems for AP Calculus regard physics and straight line motion. We denote position as $$s(t)$$ or $$x(t)$$, velocity as $$v(t)$$, and acceleration as $$a(t)$$.

For motion on a line, position, velocity, acceleration, and speed are related but not interchangeable.

Velocity is a *vector*, which means it includes direction:

$$
v(t)=s'(t)
$$

Speed is a *scalar* meaning it is the magnitude of velocity and does not include direction:

$$
\lvert v(t)\rvert
$$

Acceleration is defined as

$$
a(t)=v'(t)
$$

and tells us how velocity is changing. Speed increases when velocity and acceleration point in the same direction, because the velocity value is moving farther from zero. Speed decreases when velocity and acceleration have opposite signs.

For straight-line motion, AP problems often ask for all of the following from one model:

- position at a time,
- velocity at a time,
- acceleration at a time,
- when the particle is at rest,
- when the particle changes direction,
- total distance traveled on an interval.

Changing direction requires velocity to change sign, not merely equal zero. A particle can stop for an instant and continue in the same direction.

<div class="theorem-box">

**Example.** A particle moves along a line with velocity $$v(t)=t^2-5t+6$$

for $$0\le t\le4$$. Determine when it is moving right, when it is moving left, and whether it changes direction.

Factor the velocity:

$$
v(t)=t^2-5t+6=(t-2)(t-3).
$$

The velocity is zero at $$t=2$$ and $$t=3$$. Test intervals:

$$
v(1)=(1-2)(1-3)=2>0,
$$

$$
v(2.5)=(0.5)(-0.5)<0,
$$

and

$$
v(3.5)=(1.5)(0.5)>0.
$$

So the particle moves right on $$(0,2)$$ and $$(3,4)$$, and left on $$(2,3)$$. Since the sign of velocity changes at both $$t=2$$ and $$t=3$$, the particle changes direction at both times.

</div>

<div class="theorem-box">

**Example.** A particle moves along a line with position $$s(t)=t^3-6t^2+9t$$ meters, where $$t$$ is in seconds. Find the velocity and acceleration at $$t=4$$, and determine whether the particle is speeding up or slowing down.

Differentiate to get velocity and acceleration:

$$
v(t)=s'(t)=3t^2-12t+9,\qquad a(t)=v'(t)=6t-12.
$$

Evaluate both at $$t=4$$:

$$
v(4)=3(16)-12(4)+9=48-48+9=9\ \text{m/s},
$$

$$
a(4)=6(4)-12=12\ \text{m/s}^2.
$$

At $$t=4$$ the velocity is $$+9$$ m/s and the acceleration is $$+12$$ m/s$$^2$$. Because velocity and acceleration have the same sign, the velocity is moving farther from zero, so the particle is speeding up.

</div>

### A complete motion sign chart

To determine when a particle speeds up, combine the zeros of velocity and acceleration in one interval chart. Zeros of velocity separate possible direction changes, while zeros of acceleration separate changes in how velocity develops. Neither list alone answers all of the motion questions.

Away from rest, differentiating speed gives a useful explanation:

$$
\frac{d}{dt}\lvert v(t)\rvert
=
\begin{cases}
a(t),&v(t)>0,\\
-a(t),&v(t)<0.
\end{cases}
$$

Thus $$v(t)a(t)>0$$ means increasing speed and $$v(t)a(t)<0$$ means decreasing speed. At an instant when velocity is zero, use the behavior on each side instead of dividing by the speed.

<div class="theorem-box">

**Example.** A particle has velocity $$v(t)=(t-1)^2(t-4)$$ for $$0\le t\le5$$. Find its direction changes and its intervals of speeding up and slowing down.

The velocity vanishes at $$t=1$$ and $$t=4$$. Because the squared factor is positive away from $$t=1$$, velocity is negative before $$4$$ and positive after $$4$$. The particle stops at $$1$$ without changing direction, then changes from leftward to rightward motion at $$4$$.

Differentiate before building the combined chart:

$$
a(t)=2(t-1)(t-4)+(t-1)^2
=3(t-1)(t-3).
$$

The important inputs are now $$1,3,4$$:

| Time interval | Velocity | Acceleration | Speed |
| --- | --- | --- | --- |
| Before $$1$$ | Negative | Positive | Decreasing |
| Between $$1$$ and $$3$$ | Negative | Negative | Increasing |
| Between $$3$$ and $$4$$ | Negative | Positive | Decreasing |
| Between $$4$$ and $$5$$ | Positive | Positive | Increasing |

The particle slows down on $$(0,1)$$ and $$(3,4)$$, and speeds up on $$(1,3)$$ and $$(4,5)$$. In particular, positive acceleration on $$(3,4)$$ makes the negative velocity approach zero, so it reduces speed.

</div>

---

## Related rates

Related rates are the crux of contextual derivative problems. Often in a related rates problem, two (or more) quantities change together, and you need to find the rate of change of one when the other is changing as well. The trick is to write an equation connecting quantities that change together, then implicitly differentiate. These equations often come from:

- Pythagorean theorem,
- volume formulas,
- area formulas,
- similar triangles.

If the problem asks how fast a quantity is changing, the final answer should usually be a value of a derivative with units.

Related rates uses implicit differentiation with respect to time. Treat changing quantities as functions of time, even if the equation does not explicitly contain $$t$$, and keep fixed quantities constant. For example, in $$x^2+y^2=L^2$$, the ladder length $$L$$ is constant, but $$x$$ and $$y$$ change as the ladder slides. That is why differentiating gives rate terms:

$$
\frac{d}{dt}(x^2+y^2)=\frac{d}{dt}(L^2)
\quad\Longrightarrow\quad
2x\frac{dx}{dt}+2y\frac{dy}{dt}=0.
$$

Do not plug in the numerical values before differentiating, and ALWAYS remember to do chain rule on everything!

:::strategy
1. Draw and label a diagram.
2. Write an equation relating the variables.
3. Differentiate implicitly with respect to time.
4. Substitute the requested instant.
5. Keep units consistent.
:::

<div class="theorem-box">

**Example.** A $$10$$ ft ladder leans against a wall. The bottom of the ladder is sliding away from the wall at $$2$$ ft/s. When the bottom is $$6$$ ft from the wall, how fast is the top of the ladder sliding down?

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth, scale=0.9]
\draw[gray!70, thick] (0,0) -- (5.3,0);
\draw[gray!70, thick] (0,0) -- (0,4.6);
\coordinate (A) at (4.2,0);
\coordinate (B) at (0,3.2);
\draw[blue, very thick] (A) -- (B) node[midway, above right] {ladder};
\draw[<->, orange!85!black] (0,-0.35) -- (4.2,-0.35) node[midway, below] {$x(t)$};
\draw[<->, red!75!black] (-0.35,0) -- (-0.35,3.2) node[midway, left] {$y(t)$};
\draw[->, orange!85!black, thick] (A) -- ++(0.65,0);
\node[orange!85!black, anchor=west] at (5.0,0.45) {$\frac{dx}{dt}>0$};
\draw[->, red!75!black, thick] (B) -- ++(0,-0.65);
\node[red!75!black, anchor=east] at (-0.65,2.6) {$\frac{dy}{dt}<0$};
\end{tikzpicture}
```

Let $$x$$ be the distance from the wall to the bottom of the ladder, and let $$y$$ be the height of the top of the ladder. The ladder length is constant, so

$$
x^2+y^2=10^2.
$$

At the moment $$x=6$$, find $$y$$:

$$
6^2+y^2=100
\quad\Longrightarrow\quad
y^2=64
\quad\Longrightarrow\quad
y=8.
$$

Differentiate the equation with respect to time:

$$
2x\frac{dx}{dt}+2y\frac{dy}{dt}=0.
$$

Substitute $$x=6$$, $$y=8$$, and $$\frac{dx}{dt}=2$$:

$$
2(6)(2)+2(8)\frac{dy}{dt}=0.
$$

Solve:

$$
24+16\frac{dy}{dt}=0
\quad\Longrightarrow\quad
\frac{dy}{dt}=-\frac{24}{16}=-\frac32.
$$

The top of the ladder is sliding down at $$\frac32$$ ft/s.

</div>

<div class="theorem-box">

**Example.** Air is pumped into a spherical balloon so that its volume increases at $$\frac{dV}{dt}=100$$ cubic centimeters per second. How fast is the radius changing at the moment when $$r=5$$ cm?

The source equation is the volume of a sphere:

$$
V=\frac{4}{3}\pi r^3.
$$

Differentiate both sides with respect to time, treating $$r$$ as a function of $$t$$:

$$
\frac{dV}{dt}=4\pi r^2\,\frac{dr}{dt}.
$$

Substitute the known values $$\frac{dV}{dt}=100$$ and $$r=5$$:

$$
100=4\pi(5)^2\,\frac{dr}{dt}=100\pi\,\frac{dr}{dt}.
$$

Solve for the radius rate:

$$
\frac{dr}{dt}=\frac{100}{100\pi}=\frac{1}{\pi}\approx 0.318\ \text{cm/s}.
$$

When the radius is $$5$$ cm, it is increasing at about $$0.318$$ centimeters per second. The rate is positive because the balloon is inflating.

</div>

### Related quantities and hidden variables

Contextual problems often include more variables than you actually need. The goal is to write one equation connecting the changing quantities (kind of like chaining them together), then identify which rate the question asks for.

:::strategy
- Define every variable before differentiating
- Record which variables are changing,
- Keep constants as constants
- Substitute numerical values after differentiating.
:::

If the independent variable is time, every changing quantity gets a rate such as $$dx/dt$$, $$dV/dt$$, or $$dA/dt$$.

<div class="theorem-box">

**Example.** A circular puddle has radius $$r$$ feet, and its area is increasing at $$12$$ square feet per minute. How fast is the radius increasing when $$r=3$$?

Start with the relationship between area and radius:

$$
A=\pi r^2.
$$

Differentiate with respect to time:

$$
\frac{dA}{dt}=2\pi r\frac{dr}{dt}.
$$

Now substitute the given values:

$$
12=2\pi(3)\frac{dr}{dt}.
$$

So

$$
\frac{dr}{dt}=\frac{12}{6\pi}=\frac{2}{\pi}.
$$

The radius is increasing at $$\frac{2}{\pi}$$ feet per minute.

</div>

<div class="theorem-box">

**Example.** A changing rectangle has positive side lengths $$x$$ and $$y$$, in meters, constrained by $$2x^2+xy+3y^2=24$$. When $$x=3$$ and $$y=1$$, the side $$x$$ is increasing at two meters per second. Find the rate of change of $$y$$ and of the area. If $$x$$ continues increasing at that constant rate near this instant, also find $$y''$$.

Let $$F=2x^2+xy+3y^2-24$$. Its partial derivatives are

$$
F_x=4x+y,\qquad F_y=x+6y.
$$

At the requested instant, $$F_y=9\ne0$$, so

$$
y'=-\frac{4x+y}{x+6y}x'
=-\frac{13}{9}(2)=-\frac{26}{9}
\text{ meters per second}.
$$

The area is $$A=xy$$. Both sides change, so use the product rule:

$$
A'=x'y+xy'
=2(1)+3\left(-\frac{26}{9}\right)
=-\frac{20}{3}
\text{ square meters per second}.
$$

The rectangle's area decreases even though one side grows. The decrease in the other side has the greater effect at this instant.

For the second rate, keep the first derivative equation in an undivided form:

$$
(4x+y)x'+(x+6y)y'=0.
$$

Differentiating again gives

$$
4(x')^2+2x'y'+6(y')^2
+(4x+y)x''+(x+6y)y''=0.
$$

Because $$x'$$ is constant, $$x''=0$$. Substitute the values:

$$
16-\frac{104}{9}+\frac{4056}{81}+9y''=0,
\qquad
y''=-\frac{1472}{243}
\text{ meters per second squared}.
$$

The negative second derivative means that $$y'$$ is becoming more negative, so the side is shrinking at an increasing rate.

</div>

### Eliminating a changing geometric variable

A container's full dimensions are fixed, but the dimensions of its contents may change. In a cone, the water's surface radius changes with the water depth. Treating that radius as constant would describe a cylinder instead.

Similar triangles often remove this extra variable. Write the radius-to-height ratio using the full cone, solve for the water radius in terms of water depth, and substitute into the volume equation. The resulting single-variable equation captures both changes at once.

<div class="theorem-box">

**Example.** An inverted conical tank is $$12$$ meters tall with top radius $$4$$ meters. Water enters at $$3$$ cubic meters per minute and leaks out at $$h/4$$ cubic meters per minute, where $$h$$ is the water depth. Find the rate of change of depth when $$h=6$$, and determine how that depth rate changes as the water rises through that level.

Similar triangles give

$$
\frac rh=\frac4{12},
\qquad
r=\frac h3.
$$

Substitute before differentiating:

$$
V=\frac13\pi r^2h=\frac{\pi h^3}{27},
\qquad
\frac{dV}{dt}=\frac{\pi h^2}{9}\frac{dh}{dt}.
$$

The net volume rate is $$3-h/4$$, so

$$
\frac{dh}{dt}
=\frac{9(3-h/4)}{\pi h^2}.
$$

At depth $$6$$,

$$
\frac{dh}{dt}=\frac{9(3-6/4)}{36\pi}
=\frac{3}{8\pi}\text{ meters per minute}.
$$

To analyze the depth rate, regard it as a function $$q(h)$$:

$$
q(h)=\frac9\pi\left(3h^{-2}-\frac14h^{-1}\right),
\qquad
q'(h)=\frac9\pi\left(-6h^{-3}+\frac14h^{-2}\right).
$$

At $$h=6$$, $$q'(6)=-3/(16\pi)$$. Since $$h'>0$$ there, the chain rule gives

$$
\frac{d^2h}{dt^2}=q'(6)h'
=-\frac9{128\pi^2}.
$$

The water level is rising, but its upward rate is decreasing. Both the increasing surface area and the increasing leak rate contribute to that behavior.

</div>

### Angles, shadows, and the requested rate

A related-rates equation must use the variable the question actually asks for. A common type of problem is the shadow problem. In a shadow problem, shadow length and the distance from a lamp to the shadow's tip are different quantities. In a tracking problem, an angular rate is different from the speed of the tracked object.

For angle problems, trigonometry often gives the easiest relation (with everything in radians, of course). After differentiating, determine any missing side lengths or trig values from the geometry at the requested instant.

<div class="theorem-box">

**Example.** A camera is $$30$$ meters from a straight road. A cyclist rides along the road at $$8$$ meters per second, moving away from the nearest point to the camera. Let $$\theta$$ be the angle between the camera's perpendicular line to the road and its line of sight. Find $$d\theta/dt$$ when the cyclist is $$40$$ meters along the road from the nearest point.

Let $$x$$ be the cyclist's distance along the road. The right triangle gives

$$
\tan\theta=\frac x{30}.
$$

Differentiate with respect to time:

$$
\sec^2\theta\frac{d\theta}{dt}
=\frac1{30}\frac{dx}{dt}.
$$

At $$x=40$$, the line-of-sight distance is $$50$$, so $$\sec\theta=50/30=5/3$$. Therefore,

$$
\frac{25}{9}\frac{d\theta}{dt}=\frac8{30},
\qquad
\frac{d\theta}{dt}=\frac{12}{125}.
$$

The camera rotates at $$12/125$$ radians per second. Its angular rate will not remain constant even though the cyclist's road speed does, because the same road displacement subtends a smaller angle at larger distances.

</div>

---

## Local linear approximations

Sometimes, we can use derivatives to estimate functions. Let $$L(x)$$ be the estimated value of $$f(x)$$. Near $$x=a$$ define $$L(x)$$ as,

$$
L(x) = f(a) + f'(a)(x-a),
$$

which is the point-slope form for the tangent line. For inputs near $$a$$, the tangent line often gives a useful estimate of $$f(x)$$. The estimate is exact at $$a$$ and matches the derivative there, but its accuracy depends on how much the graph bends over the interval being used.

<div class="theorem-box">

**Proof (Linearization).** Differentiability at $$a$$ means

$$
f'(a)=\lim_{x\to a}\frac{f(x)-f(a)}{x-a}.
$$

For $$x$$ close to $$a$$, the difference quotient is close to $$f'(a)$$, so

$$
\frac{f(x)-f(a)}{x-a}\approx f'(a).
$$

Multiplying by $$x-a$$ gives

$$
f(x)\approx f(a)+f'(a)(x-a).
$$

Linearization is a local approximation near $$a$$. Farther away, the tangent line may no longer approximate the function well.

</div>

The two views below show $$f(x)=\sqrt{x}$$ and its tangent $$L(x)=1+(x-1)/2$$ at $$a=1$$. The left view shows the curve bending away from the line. In the closer view, their heights are almost identical because their value and slope agree at the base point.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  at={(0cm,0cm)}, anchor=south west,
  axis lines=left, xmin=0, xmax=4, ymin=0, ymax=2.7,
  xtick={0,1,2,3,4}, ytick={0,1,2},
  grid=both, grid style={gray!15},
  width=6.4cm, height=5cm, title={Wider view},
  xlabel=$x$, ylabel=$y$,
  legend style={at={(0.03,0.97)}, anchor=north west, font=\small},
]
\addplot[blue, very thick, samples=160, domain=0:4] {sqrt(x)};
\addlegendentry{$f(x)=\sqrt{x}$}
\addplot[red!75!black, thick, domain=0:4] {1+(x-1)/2};
\addlegendentry{$L(x)$}
\addplot[only marks, mark=*, mark size=1.6pt] coordinates {(1,1)};
\end{axis}
\begin{axis}[
  at={(7.1cm,0cm)}, anchor=south west,
  axis lines=left, xmin=0.8, xmax=1.2, ymin=0.89, ymax=1.11,
  xtick={0.8,1,1.2}, ytick={0.9,1,1.1},
  grid=both, grid style={gray!15},
  width=6.4cm, height=5cm, title={Near the base point},
  xlabel=$x$, ylabel=$y$,
]
\addplot[blue, very thick, samples=100, domain=0.8:1.2] {sqrt(x)};
\addplot[red!75!black, thick, dashed, domain=0.8:1.2] {1+(x-1)/2};
\addplot[only marks, mark=*, mark size=1.6pt] coordinates {(1,1)};
\end{axis}
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** Estimate $$\sqrt{27}$$.

Let $$f(x)=\sqrt{x}$$ and choose the nearby easy point $$a=25$$, since $$\sqrt{25}=5$$. The derivative is

$$
f'(x)=\frac{1}{2\sqrt{x}},\qquad f'(25)=\frac{1}{2\cdot 5}=\frac{1}{10}.
$$

The linearization at $$a=25$$ is

$$
L(x)=f(25)+f'(25)(x-25)=5+\frac{1}{10}(x-25).
$$

Estimate at $$x=27$$:

$$
\sqrt{27}\approx L(27)=5+\frac{1}{10}(2)=5.2.
$$

So $$\sqrt{27}\approx 5.2$$. The true value is about $$5.196$$, so the linear estimate is accurate to within a couple thousandths because $$27$$ is close to $$25$$.

</div>

<div class="theorem-box">

**Example.** The upper branch of $$x^2+xy+y^2=7$$ passes through $$(1,2)$$. Use linearization to estimate the branch's height at $$x=1.04$$, then determine whether the estimate is too high or too low.

Differentiate the constraint:

$$
2x+y+xy'+2yy'=0,
\qquad
y'=-\frac{2x+y}{x+2y}.
$$

At $$(1,2)$$ the slope is $$-4/5$$, so the tangent estimate is

$$
L(x)=2-\frac45(x-1).
$$

Therefore,

$$
y(1.04)\approx L(1.04)=2-\frac45(0.04)=1.968.
$$

To establish the direction of error, differentiate the undivided derivative equation again:

$$
2+2y'+2(y')^2+(x+2y)y''=0.
$$

Hence

$$
y''=-\frac{2[1+y'+(y')^2]}{x+2y}.
$$

The numerator inside the brackets is always positive because

$$
1+y'+(y')^2=\left(y'+\frac12\right)^2+\frac34.
$$

On the upper branch, $$x+2y=\sqrt{28-3x^2}>0$$ throughout $$[1,1.04]$$. Thus $$y''<0$$ there: the branch is moving more downward than a straight line (if $$y''=0$$, then the function is moving in a straight line because the derivative is constant). The estimate $$1.968$$ is thus an overestimate.

This approximation requires only a convenient point and the local slope. Finding an explicit formula for the whole branch is unnecessary.

</div>

### Differential notation and small changes

<div class="theorem-box">

**Definition.** If $$y=f(x)$$, then the *differential* is defined as

$$
dy=f'(x)\,dx.
$$

Here $$dx$$ is a chosen input change and $$dy$$ is the corresponding change predicted by the tangent line. At a fixed base point, $$dy$$ depends linearly on $$dx$$. This is consistent with derivative notation, but $$dy$$ need not equal the actual change in the function.

</div>

The differential models the change in $$y$$ caused by a small change $$dx$$ in $$x$$. This is the same idea as linearization, written in a compact way:

$$
\Delta y\approx dy=f'(a)\Delta x.
$$

The actual change is

$$
\Delta y=f(a+\Delta x)-f(a),
$$

while the differential estimate is

$$
dy=f'(a)\Delta x.
$$

Differentials are especially useful for error estimates. If a measurement changes by the signed amount $$dx=\Delta x$$, the resulting signed output error is approximately

$$
\Delta y\approx dy=f'(a)\,dx.
$$

The sign records the direction of the change. The same method estimates how measurement errors affect calculated quantities in physics.

The distinction is easiest to see on the graph. Starting from $$(a,f(a))$$, $$dy$$ measures the vertical change along the tangent line after a horizontal move $$dx=\Delta x$$. The actual change $$\Delta y$$ measures the vertical change along the curve over that same move. Their difference is exactly the error in the predicted final height:

$$
\Delta y-dy=f(a+\Delta x)-L(a+\Delta x).
$$

For a linear function, these changes agree for every input change. For a nonlinear function, they generally agree only approximately near the base point. The notation $$dy$$ does not assert that this approximation is exact or that the chosen change must literally be infinitesimal.

<div class="theorem-box">

**Example.** Let $$y=x^3$$. When $$x$$ changes from $$2$$ to $$1.9$$, find $$dx$$, $$dy$$, and $$\Delta y$$. Compare the predicted and actual final outputs.

The input change is $$dx=\Delta x=-0.1$$. The derivative at the starting point is $$f'(2)=3(2)^2=12$$, so

$$
dy=12(-0.1)=-1.2.
$$

The actual change uses the function values:

$$
\Delta y=f(1.9)-f(2)=1.9^3-8=-1.141.
$$

The tangent predicts a final output of $$8-1.2=6.8$$, while the actual output is $$6.859$$. Their difference is

$$
\Delta y-dy=0.059.
$$

Both changes are negative, but the tangent predicts a larger decrease. Expanding the exact change at $$a=2$$ explains the discrepancy:

$$
(2+h)^3-8=12h+6h^2+h^3.
$$

The differential retains $$12h$$; the omitted terms give $$6(-0.1)^2+(-0.1)^3=0.059$$.

</div>

### Error measurement

For a variable $$x$$ with a small signed error $$dx$$, the relative error estimate is simply $$dx/x$$, and the percentage error estimate is $$100(dx/x)\%$$:

$$
\text{error in original units}=dx,
\qquad
\text{relative error}=\frac{dx}{x},
\qquad
\text{percentage error}=100\frac{dx}{x}\%,
\qquad x\ne0.
$$

Here the denominator is the reference value, and $$dx$$ is the signed error relative to that value. A positive or negative error records which side of the reference the perturbed value lies on. When a measurement has symmetric uncertainty, use $$dx=\pm\varepsilon$$ to indicate both possible directions.

For a calculated quantity $$y=f(x)$$, apply the same idea to the output:

$$
dy=f'(x)\,dx,
\qquad
\frac{dy}{y}=\frac{f'(x)}{f(x)}\,dx,
\qquad
\text{percentage error estimate}=100\frac{dy}{y}\%.
$$

The differential $$dy$$ estimates the actual error $$\Delta y$$, so $$dy/y$$ estimates $$\Delta y/y$$. Relative and percentage error are undefined when the reference is zero, although the error in the original units still makes sense. An error of one cubic centimeter is substantial for a tiny ball and negligible for a large planet.

These formulas use **signed error**. The conventional term *absolute error* means the nonnegative size of an error; reporting a maximum uncertainty asks for that size. We will keep the sign in the calculations and report the positive endpoint when a maximum is requested.

For a power relationship $$y=Cx^n$$ with nonzero $$x$$ and $$y$$, the relative-error formula simplifies further:

$$
\frac{dy}{y}=\frac{nCx^{n-1}\,dx}{Cx^n}
=n\frac{dx}{x}.
$$

Thus the relative error in a sphere's volume is approximately three times the relative error in its radius.

Concavity determines the direction of a tangent estimate when the concavity has one sign throughout the interval between the base point and the target. A concave-up graph lies above its tangent, so linearization underestimates. A concave-down graph lies below its tangent, so linearization overestimates.

<div class="theorem-box">

**Example.** A spherical ball has measured radius $$10$$ centimeters with possible measurement error $$0.02$$ centimeters. Estimate the largest resulting volume error and its percentage. If the true radius is $$10.02$$, determine whether the differential underestimates or overestimates the true increase.

For a sphere, $$V=4\pi r^3/3$$, so $$dV/V=3\,dr/r$$. At $$r=10$$ with $$dr=\pm0.02$$,

$$
dV=4\pi(10)^2(\pm0.02)=\pm8\pi
\text{ cubic centimeters}.
$$

The signed relative error estimate is

$$
\frac{dV}{V}=3\frac{\pm0.02}{10}=\pm0.006.
$$

The estimated percentage error is therefore $$\pm0.6\%$$, with maximum size $$0.6\%$$ and maximum volume-error size $$8\pi$$ cubic centimeters. Since $$V''(r)=8\pi r>0$$ for positive radii, the tangent estimate underestimates the actual increase from $$10$$ to $$10.02$$. The differential allowance is symmetric, while the exact volume changes for positive and negative radius errors are not.

</div>

<div class="theorem-box">

**Example.** A hollow sphere has a fixed inner radius of $$9$$ centimeters. Its outer radius is measured as $$10$$ centimeters with possible error $$0.02$$ centimeters. Estimate the maximum absolute and percentage uncertainty in the material volume. Then estimate the outer-radius tolerance needed to keep the volume within $$0.5\%$$ of its nominal value, and compare it with an exact tolerance.

Only the outer radius changes, so the material volume is

$$
V(R)=\frac{4\pi}{3}(R^3-9^3),
\qquad
V_0=V(10)=\frac{1084\pi}{3}.
$$

The inner radius is fixed, making its derivative contribution zero. Therefore,

$$
V'(R)=4\pi R^2,
\qquad
dV=400\pi(\pm0.02)=\pm8\pi
\text{ cubic centimeters}.
$$

The relative uncertainty estimate is

$$
\frac{dV}{V_0}
=\frac{\pm8\pi}{1084\pi/3}
=\pm\frac6{271}\approx\pm0.02214.
$$

Thus the estimated percentage uncertainty is about $$\pm2.21\%$$, with maximum size $$2.21\%$$. This exceeds that of a solid sphere with the same outer-radius error because the same volume-error size is compared with a smaller amount of material.

Let $$\delta$$ be the allowed outer-radius error. The differential estimate requires

$$
\frac{400\pi\delta}{1084\pi/3}\le0.005,
\qquad
\delta\le\frac{271}{60000}
\approx0.0045167\text{ cm}.
$$

This is a first-order tolerance estimate, not an exact guarantee. Since $$V$$ is increasing and convex for positive radii, the positive radius error produces the larger absolute volume deviation. An exact symmetric tolerance therefore satisfies

$$
\frac{V(10+\delta)-V(10)}{V(10)}\le0.005,
$$

or

$$
\frac{(10+\delta)^3-1000}{271}\le0.005.
$$

Solving gives

$$
\delta\le\sqrt[3]{1001.355}-10
\approx0.0045146\text{ cm}.
$$

The exact allowance is slightly smaller because the differential underestimates the increase for a positive radius error. When a problem asks for a rigorous tolerance rather than an estimate, that small distinction matters.

</div>

---

## L'Hôpital's Rule

You may remember solving indeterminate limits (limits involving $$\frac{0}{0}$$, $$\frac{\infty}{\infty}$$, etc.) in Unit 1, where you had to do some tedious algebra to simplify. However, we learn a simpler way to solve, known as L'Hôpital's Rule.

<div class="theorem-box">

**Theorem (L'Hôpital's Rule).** For a quotient with form $$0/0$$ or $$\infty/\infty$$ (sign does not matter), the conditions below allow us to replace the quotient by a quotient of derivatives:

$$
\lim_{x \to a} \frac{f(x)}{g(x)}
=
\lim_{x \to a} \frac{f'(x)}{g'(x)}
$$

The word *hypotheses* means the assumptions needed before the theorem can be used. For a one-sided limit toward a finite input $$a$$, check:

1. **An allowed original form.** Both $$f(x)$$ and $$g(x)$$ approach zero, or their magnitudes both approach infinity. A nonzero number divided by zero is not an allowed indeterminate form.
2. **Differentiability and continuous derivatives.** The functions $$f$$ and $$g$$ are differentiable, and their derivatives $$f'$$ and $$g'$$ are continuous, throughout a one-sided interval next to $$a$$. These conditions are imposed near the target, not necessarily at $$a$$ itself. A *punctured* interval simply excludes that target input.
3. **Nonzero denominator and denominator derivative.** The quotient must be defined near $$a$$, and $$g'(x)\ne0$$ on the interval where the rule is being applied. It is acceptable for $$g'(x)$$ to approach zero, provided it does not equal zero at nearby inputs.
4. **A derivative-quotient limit.** The quotient of derivatives must approach a finite real number or a signed infinity:

$$
\lim_{x\to a}\frac{f'(x)}{g'(x)}=L,
\qquad
L\in\mathbb R\cup\{-\infty,\infty\}.
$$

Then $$f(x)/g(x)$$ approaches that same $$L$$. An infinite limit describes unbounded behavior in one direction; an oscillating quotient with no limit does not satisfy this condition. Continuity of $$f'$$ and $$g'$$ is a sufficient extra assumption in the version above.

</div>

For a two-sided limit, apply the theorem on each side and check that the results agree. For a limit at infinity, use a sufficiently far-out interval instead of an interval next to a finite input.

<div class="theorem-box">

**Proof (L'Hôpital's Rule using local linear approximations).** For this basic zero-over-zero case, assume $$f(a)=g(a)=0$$, both functions are differentiable at $$a$$, their derivatives are continuous at $$a$$, and $$g'(a)\ne0$$.

Near $$x=a$$, the tangent-line approximations are

$$
f(x)\approx f(a)+f'(a)(x-a)=f'(a)(x-a)
$$

and

$$
g(x)\approx g(a)+g'(a)(x-a)=g'(a)(x-a).
$$

Both contain the same input change, suggesting

$$
\frac{f(x)}{g(x)}
\approx\frac{f'(a)(x-a)}{g'(a)(x-a)}
=\frac{f'(a)}{g'(a)}.
$$

To justify passing from this approximation to an exact limit, write $$h=x-a$$ and retain the approximation errors:

$$
f(a+h)=f'(a)h+r_f(h),
\qquad
g(a+h)=g'(a)h+r_g(h).
$$

Differentiability means that each error becomes negligible compared with $$h$$:

$$
\lim_{h\to0}\frac{r_f(h)}h=0,
\qquad
\lim_{h\to0}\frac{r_g(h)}h=0.
$$

For nonzero $$h$$, divide the numerator and denominator by $$h$$. Since $$g'(a)\ne0$$, the resulting denominator approaches a nonzero number, so the quotient limit law gives

$$
\lim_{x\to a}\frac{f(x)}{g(x)}
=\lim_{h\to0}
\frac{f'(a)+r_f(h)/h}{g'(a)+r_g(h)/h}
=\frac{f'(a)}{g'(a)}.
$$

Continuity of the derivatives at $$a$$ also gives

$$
\lim_{x\to a}\frac{f'(x)}{g'(x)}
=\frac{f'(a)}{g'(a)}.
$$

The original quotient and the derivative quotient therefore have the same limit:

$$
\lim_{x\to a}\frac{f(x)}{g(x)}
=\lim_{x\to a}\frac{f'(x)}{g'(x)}.
$$

But what if we have the $$\frac{\infty}{\infty}$$ case?

Let $$u(x)=1/f(x)$$ and $$v(x)=1/g(x)$$, and extend them by $$u(a)=v(a)=0$$. Under the assumptions above, the zero-over-zero result already proved gives

$$
\lim_{x\to a}\frac{f(x)}{g(x)}
=\lim_{x\to a}\frac{v(x)}{u(x)}
=\frac{v'(a)}{u'(a)}=K,
\qquad K\ne0.
$$

This is the ratio of the reciprocals' local linear approximations. To compare with the derivative quotient in L'Hôpital's Rule, differentiate the reciprocals:

$$
u'=-\frac{f'}{f^2},
\qquad
v'=-\frac{g'}{g^2}.
$$

Rearranging gives

$$
\frac{f'}{g'}
=\frac{u'}{v'}\left(\frac{f}{g}\right)^2.
$$

Continuity and the nonzero reciprocal slopes now give

$$
\lim_{x\to a}\frac{f'(x)}{g'(x)}
=\frac{u'(a)}{v'(a)}K^2
=\frac1K K^2=K.
$$

Both quotients approach the same value. Note that a full, rigorous proof would require Cauchy's Mean Value Theorem which will not be covered here.

</div>

### Applying the rule

Before each application, write the numerator limit and denominator limit separately to establish the indeterminate form. In routine worked examples, a full differentiability or continuity checklist is unnecessary; discuss those conditions explicitly when a domain restriction or other unusual feature makes them relevant.

You can use L'Hôpital's Rule more than once! After each application, check the new quotient again. Another application is justified only if the new quotient still has an allowed indeterminate form and satisfies the hypotheses. If the derivative quotient fails to have a limit, the original limit may still exist, so an unsuccessful application does not prove divergence.

Note that this only applies to indeterminate forms (specifically $$\frac{0}{0}$$ and $$\frac{\infty}{\infty}$$). If the limit is NOT indeterminate, you CANNOT apply L'Hôpital's Rule.
For indeterminate forms that are not $$\frac{0}{0}$$ and $$\frac{\infty}{\infty}$$, you have to rewrite the limit before using the rule. For instance, products, differences, and powers may need algebra or logarithms before they become a quotient form.

Common rewrites:

| Original form | Possible rewrite |
|---|---|
| $$0\cdot\infty$$ | move one factor to the denominator |
| $$\infty-\infty$$ | combine into one fraction or rationalize |
| $$1^\infty,\ 0^0,\ \infty^0$$ | take logs, find the limit of $$\ln y$$, then exponentiate |

<div class="theorem-box">

**Example.** Evaluate $$\lim_{x\to0^+}x\ln x.$$

Directly, this has the indeterminate form $$0\cdot(-\infty)$$. Rewrite it as a quotient:

$$
x\ln x=\frac{\ln x}{1/x}.
$$

Check the numerator and denominator separately:

$$
\lim_{x\to0^+}\ln x=-\infty,
$$

$$
\lim_{x\to0^+}\frac1x=\infty.
$$

The form is $$-\infty/\infty$$, so L'Hopital's Rule applies:

$$
\lim_{x\to0^+}\frac{\ln x}{1/x}
=
\lim_{x\to0^+}\frac{1/x}{-1/x^2}.
$$

Simplify:

$$
\frac{1/x}{-1/x^2}=-x.
$$

Therefore

$$
\lim_{x\to0^+}x\ln x
=
\lim_{x\to0^+}(-x)=0.
$$

</div>

<div class="theorem-box">

**Example.** Evaluate $$\lim_{x\to0^+}(1+x)^{1/x}.$$

Let

$$
y=(1+x)^{1/x}.
$$

Take the natural logarithm:

$$
\ln y=\frac{\ln(1+x)}{x}.
$$

For the logarithmic quotient, check

$$
\lim_{x\to0^+}\ln(1+x)=0,
$$

$$
\lim_{x\to0^+}x=0.
$$

The form is $$0/0$$, so use L'Hopital's Rule:

$$
\lim_{x\to0^+}\frac{\ln(1+x)}{x}
=
\lim_{x\to0^+}\frac{1/(1+x)}{1}
=1.
$$

Thus

$$
\lim_{x\to0^+}\ln y=1.
$$

Exponentiate to return to $$y$$:

$$
\lim_{x\to0^+}(1+x)^{1/x}=e^1=e.
$$

</div>

<div class="theorem-box">

**Example.** Find the real parameter $$c$$ for which the two-sided limit

$$
\lim_{x\to0}
\left(\frac{e^{\tan x-cx^2}}{1+\sin x}\right)^{1/x^3}
$$

exists as a finite, nonzero number, and evaluate it using L'Hôpital's Rule.

The base approaches one and is positive near zero, while the exponent becomes unbounded. Take a logarithm before differentiating. If the expression is $$Y(x)$$, then

$$
\ln Y(x)
=\frac{\tan x-cx^2-\ln(1+\sin x)}{x^3}.
$$

Let the numerator be $$N(x)$$. Check the two limits:

$$
\lim_{x\to0}[\tan x-cx^2-\ln(1+\sin x)]=0,
$$

$$
\lim_{x\to0}x^3=0.
$$

The form is $$0/0$$. Work on each side of zero separately until the parameter is determined. A first application on either side gives

$$
\lim_{x\to0^\pm}\ln Y(x)
=\lim_{x\to0^\pm}
\frac{\sec^2x-2cx-\dfrac{\cos x}{1+\sin x}}{3x^2}.
$$

Before applying the rule again, check the new numerator and denominator:

$$
\lim_{x\to0}\left[\sec^2x-2cx-\frac{\cos x}{1+\sin x}\right]
=1-0-1=0,
$$

$$
\lim_{x\to0}3x^2=0.
$$

This is still $$0/0$$ for every $$c$$. To differentiate the remaining quotient in the numerator, simplify its derivative:

$$
\frac{d}{dx}\left(\frac{\cos x}{1+\sin x}\right)
=\frac{-\sin x(1+\sin x)-\cos^2x}{(1+\sin x)^2}
=-\frac1{1+\sin x}.
$$

The second application therefore gives

$$
\lim_{x\to0^\pm}\ln Y(x)
=\lim_{x\to0^\pm}
\frac{2\sec^2x\tan x-2c+\dfrac1{1+\sin x}}{6x}.
$$

For the new quotient, the separate limits are

$$
\lim_{x\to0}\left[2\sec^2x\tan x-2c+\frac1{1+\sin x}\right]
=1-2c,
$$

$$
\lim_{x\to0}6x=0.
$$

If $$c\ne1/2$$, the numerator approaches a nonzero constant while the denominator changes sign at zero. The one-sided logarithmic limits are opposite signed infinities, so one side of $$Y$$ approaches zero and the other grows without bound. There is no finite, nonzero two-sided limit.

For $$c=1/2$$, check explicitly that

$$
\lim_{x\to0}\left[2\sec^2x\tan x-1+\frac1{1+\sin x}\right]=0,
$$

$$
\lim_{x\to0}6x=0.
$$

The form is $$0/0$$ again, so apply the rule once more:

$$
\lim_{x\to0}\ln Y(x)
=\lim_{x\to0}
\frac{
4\sec^2x\tan^2x+2\sec^4x
-\dfrac{\cos x}{(1+\sin x)^2}
}{6}
=\frac{0+2-1}{6}=\frac16.
$$

The last quotient has denominator six, so direct substitution finishes the calculation.

Finally, exponentiate the logarithmic limit:

$$
c=\frac12,
\qquad
\lim_{x\to0}Y(x)=e^{1/6}.
$$

The parameter cancels the quadratic contribution before the cubic scale in the exponent can produce a finite answer. Differentiating the original powered expression directly would hide this cancellation.

</div>

## Tips for the exam

Contextual derivative questions are translation problems first and calculus problems second. Before differentiating, decide what each symbol measures and what its derivative would mean.

:::variables
- Position: $$s(t)$$, usually measured in distance units.
- Velocity: $$v(t)=s'(t)$$, measured in distance per time.
- Acceleration: $$a(t)=v'(t)=s''(t)$$, measured in distance per time squared.
- Rate in/out: positive and negative contributions to a total amount.
:::

When writing interpretations:

- "Increasing" means the derivative is positive.
- "Decreasing" means the derivative is negative.
- "Speeding up" means velocity and acceleration have the same sign.
- "Slowing down" means velocity and acceleration have opposite signs.
- "Approximately" usually signals linearization or a tangent-line estimate.

:::exam{topic="Context wording"}
AP free-response scoring usually expects a complete sentence with units. A correct number without context can lose the interpretation point.
:::

:::equations
| Idea | Equation and conditions |
| --- | --- |
| Average rate | $$[Q(b)-Q(a)]/(b-a),\quad a\ne b$$ |
| Instantaneous rate | $$Q'(t)=\lim_{h\to0}[Q(t+h)-Q(t)]/h$$ |
| Composed rates | $$dQ/dt=(dQ/dx)(dx/dt)$$ |
| Motion | $$v=s',\quad a=v',\quad\text{speed}=\lvert v\rvert$$ |
| Speed derivative away from rest | $$\dfrac d{dt}\lvert v\rvert=\begin{cases}a,&v>0,\\-a,&v<0.\end{cases}$$ |
| Speed changes away from rest | $$va>0:\text{ speeding up};\quad va<0:\text{ slowing down}$$ |
| Net rate | $$V'=\text{rate in}-\text{rate out}$$ |
| Ladder constraint, fixed length | $$x^2+y^2=L^2,\quad xx'+yy'=0$$ |
| Circle area rate | $$A=\pi r^2,\quad A'=2\pi r\,r'$$ |
| Sphere volume rate | $$V=\frac43\pi r^3,\quad V'=4\pi r^2r'$$ |
| Cone volume and similar triangles | $$V=\frac13\pi r^2h,\quad r/h=R/H\quad\text{for a fixed cone of radius }R\text{ and height }H$$ |
| Implicit rate shortcut | $$y'=-(F_x/F_y)x',\quad F(x,y)=0,\quad F_y\ne0$$ |
| Explicit time in a constraint | $$y'=-[F_x\,x'+F_t]/F_y,\quad F(x,y,t)=0,\quad F_y\ne0$$ |
| Tangent-line model | $$L(x)=f(a)+f'(a)(x-a),\quad f(x)\approx L(x)\text{ near }a$$ |
| Predicted and actual changes | $$dx=\Delta x,\quad dy=f'(a)\,dx,\quad\Delta y=f(a+dx)-f(a)$$ |
| Approximation error | $$\Delta y-dy=f(a+\Delta x)-L(a+\Delta x)$$ |
| Signed relative and percentage error | $$E_{\mathrm{rel}}=dx/x,\quad E_{\mathrm{percent}}=100(dx/x)\%,\quad x\ne0$$ |
| Propagated relative error | $$dy/y=[f'(x)/f(x)]\,dx,\quad y=f(x)\ne0$$ |
| Power-law relative error | $$dy/y=n\,dx/x,\quad y=Cx^n,\quad x,y\ne0$$ |
| Reciprocal rewrite | $$f/g=(1/g)/(1/f),\quad f,g\ne0$$ |
| L'Hôpital, under its hypotheses | $$\lim_{x\to a}f(x)/g(x)=L,\quad L=\lim_{x\to a}f'(x)/g'(x)\in\mathbb R\cup\{-\infty,\infty\}$$ |
:::
