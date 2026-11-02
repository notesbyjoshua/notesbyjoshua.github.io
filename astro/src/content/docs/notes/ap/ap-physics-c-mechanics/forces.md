---
title: "Unit 2: Force and Translational Dynamics"
description: "AP Physics C Mechanics notes on forces, Newton's laws, free-body diagrams, friction, drag, circular motion, and dynamics."
sidebar:
  order: 2
---

:::variables
- $$\vec{F}$$ = force (Units: newtons, $$\text{N} = \text{kg}\cdot\text{m}/\text{s}^2$$)
- $$m$$ = mass (Units: kilograms, $$\text{kg}$$)
- $$\vec{a}$$ = acceleration (Units: $$\text{m}/\text{s}^2$$)
- $$g$$ = gravitational field strength near Earth = $$9.8\ \text{m}/\text{s}^2$$
- $$\vec{W}$$ or $$\vec{F}_g$$ = weight / gravitational force
- $$F_N$$ or $$N$$ = normal force
- $$T$$ = tension
- $$f_s$$ = static friction
- $$f_k$$ = kinetic friction
- $$\mu_s$$ = coefficient of static friction
- $$\mu_k$$ = coefficient of kinetic friction
- $$k$$ = spring constant (Units: $$\text{N/m}$$)
- $$r$$ = radius of circular path
- $$v$$ = speed
- $$\omega$$ = angular speed (Units: $$\text{rad/s}$$)
:::

---

## The Basics of Forces

What is a force? A force is a push or pull done by or on an object. Forces act like vectors. When a force is applied through contact, it is known as a contact force (e.g. friction, normal force) and when a force is applied with no contact, it is called a non-contact force (e.g. gravity, E&M force). Forces are commonly denoted with $$\vec F$$ and have units of Newtons ($$N$$)

### Newton's Three Laws of Motion

In 1687, Newton formulated the three laws of motion. They work extremely well for ordinary macroscopic objects moving much slower than the speed of light. At quantum, relativistic, or very strong-gravity scales, Newtonian mechanics must be replaced or extended, but for AP purposes, Newtonian mechanics suffices.

<div class="theorem-box">

**Theorem (Newton's Three Laws).**

1. **First Law**: An object has constant velocity unless acted on by a nonzero net external force. If $$\sum \vec{F} = 0$$, then $$\vec{a} = 0$$ (the converse is true as well).
2. **Second Law**: The net external force equals mass times acceleration, $$\sum \vec{F} = m\vec{a}$$.
3. **Third Law**: If object $$A$$ exerts a force on object $$B$$, then object $$B$$ exerts an equal-magnitude, opposite-direction force on object $$A$$, $$\vec{F}_{A\text{ on }B} = -\vec{F}_{B\text{ on }A}$$.

</div>

Third-law forces act on different objects, so they never cancel for one object. They can cancel only when you treat both interacting objects as one system and the force pair becomes internal.

### Free-body diagrams

A **free-body diagram** is a force diagram for one object or one chosen system. Start a force problem by drawing one, showing only external forces acting on the chosen object or system, not forces it applies to something else. Add the forces as vectors. An example of a free-body diagram is shown below:

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing,angles,quotes}
\begin{tikzpicture}[>=Stealth, font=\small]
\draw[fill=gray!15] (-0.5,-0.5) rectangle (0.5,0.5); \node at (0,0) {$m$};
\draw[->, very thick, blue] (0,0.5) -- (0,2) node[above] {$F_N$};
\draw[->, very thick, red] (0,-0.5) -- (0,-2) node[below] {$F_W$};
\draw[->, very thick, green!50!black] (0.5,0) -- (2,0) node[right] {$F_1$};
\draw[->, very thick, orange!90!black] (-0.5,0) -- (-1.8,0) node[left] {$F_f$};
\end{tikzpicture}
```

:::strategy
1. Choose the object or system.
2. Draw a dot or simple sketch.
3. Add one arrow for each external force (make sure to draw where the force originates from).
4. Choose axes, usually one axis parallel to the expected acceleration or along a surface.
5. Resolve angled forces into components using vector decomposition.
6. Write Newton's second law separately for each direction.
:::

For a particle in two dimensions, you should split up force into components using vector decomposition like for velocity:

$$
\sum F_x = ma_x, \qquad \sum F_y = ma_y.
$$

If acceleration is zero in one direction, the net force in that direction is zero even if forces are present (basically they cancel out each other).

### Inertial and non-inertial frames

Newton's laws have their simplest form in an **inertial frame**, a frame that is not accelerating. However, in an accelerating frame (e.g. a moving train), you may introduce a **pseudo-force** so Newton's second law appears to work inside that frame. Just like how you deal with relative velocity or acceleration,  for a frame accelerating with $$\vec{a}_{\text{frame}}$$, the pseudo-force on a mass $$m$$ is

$$
\vec{F}_{\text{pseudo}} = -m\vec{a}_{\text{frame}}.
$$

Pseudo-forces are not interaction forces and do not have third-law partners (since they don't actually exist!). Think of it like this: if a bus suddenly accelerates forward, you feel thrown backward, but no mysterious object pushed you backward. Your body was trying to keep its original velocity while the bus floor moved forward underneath you.

---

## Common types of forces

In AP Physics C, most force problems are built from a small set of common forces.

### Weight

**Weight** is the gravitational force on an object. Near Earth's surface,

$$
\vec{F}_g = m\vec{g},
$$

so its magnitude is

$$
F_g = mg.
$$

Weight points downward, toward Earth's center. Note that mass is not weight: mass is an object's inertia, while weight is a force caused by gravity. Weight is always drawn from the center of the object, and sometimes drawing out the whole object (as opposed to just a dot) is very important! For example, when the force of gravity passes through the corner of the object, it will start to topple!

### Normal force

The **normal force** is a contact force *perpendicular* to a surface that pushes contacting objects apart. It adjusts to prevent objects from passing through each other, but it is not automatically equal to $$mg$$. For example, on an incline or in an accelerating elevator, the normal force differs from the object's weight. Normally, you need to solve out force equations to get the normal force. The normal force acts along the entire surface of contact but is usually drawn out in the center of the contact plane.

A concrete case where $$F_N \ne mg$$: suppose you push down on a box resting on the floor with an extra force whose downward component is $$P$$. The vertical equation with no vertical acceleration is $$F_N - mg - P = 0$$, so $$F_N = mg + P > mg$$. If instead you pull up on the box with a force $$P$$ (not enough to lift it), then $$F_N = mg - P < mg$$. The normal force only equals $$mg$$ in the special case of a horizontal surface with no other vertical forces and no vertical acceleration.

:::warning
Always get $$F_N$$ from the perpendicular equation, never by assumption, because friction limits like $$\mu_s F_N$$ depend on it.
:::

### Tension

**Tension** is a pulling force transmitted by a rope, string, or cable. In an ideal world, strings are massless and inextensible, and pulleys are massless and frictionless. Under those assumptions, the tension is the same throughout a continuous string. Tension will always point *away* from an object along the direction of the string. If a string or pulley has mass, or if the pulley has rotational inertia, tension may differ on different sides, which won't be covered here.

To solve for tension, draw a separate free-body diagram for each attached object and write its force equation, noting that tension will point away from whatever object (even if it seeems tensions are pointing towards each other). Note which way the object will accelerate (the acceleration may not be the same for every object, but the direction should be consistent with real-life/common sense) and solve the systems.

<img class="note-img note-img--w640" src="/assets/physics/forces-atwood.svg" alt="Atwood setup and separate free-body diagrams for both masses and the massless pulley." loading="lazy" decoding="async" />

The rope pulls upward on each mass and downward on the pulley. These forces act on different bodies; the support supplies the upward force on the pulley.

### Friction

**Friction** is a contact force parallel to a surface that opposes slipping or impending slipping between the contacting surfaces (e.g. for an object sliding down a stationary ramp, friction points up the ramp). It need not oppose the object’s motion relative to the ground. There are two types: static and kinetic friction.

Static friction prevents relative slipping between contacting surfaces and adjusts up to a maximum value (never exceeding the applied force):

$$
0 \le f_s \le f_{s,\text{max}} = \mu_s F_N.
$$

Kinetic friction is friction an object experiences while moving and has approximately constant magnitude:

$$
f_k = \mu_k F_N.
$$

$$\mu_s$$ and $$\mu_k$$ are the coefficients of static and kinetic friction, respectively. Problems usually give these values; otherwise, determining them without additional information requires an experiment. Static friction is not always equal to $$\mu_sF_N$$; that expression gives the maximum possible static friction before slipping begins. For most objects, $$\mu_s > \mu_k$$.

### Spring force

For an ideal spring, **Hooke's law** gives the force required for displacement:

$$
\vec{F}_s = -k\vec{x},
$$

where $$\vec{x}$$ is displacement from equilibrium. The negative sign means the spring force points opposite the displacement. This force is more relevant in [Unit 7: Oscillations](/notes/ap/ap-physics-c-mechanics/oscillations/). The value $$k$$ is called the spring constant.

### Drag and resistive forces

Air resistance and fluid drag is friction experienced by an object going through a medium (usually liquid/air). They are often ignored in AP mechanics unless specified. When included, drag points opposite velocity (air resistance is drag in air). Two most common models are

$$
\vec{F}_d = -b\vec{v}
$$

for low-speed linear drag, and

$$
\vec{F}_d = c\vec{v}^2
$$

for high-speed quadratic drag, as seen in kinematics. The model that you should use for a problem will usually be stated.

Essentially, drag acts like a friction force for falling objects. At some point, the amount of drag pulling up will equal the force of gravity pulling down, allowing an object to go at a constant velocity (terminal velocity). Usually, drag force can never exceed gravity (that's why skydivers don't just go back up after reaching terminal velocity!).

---

## Solving Newton's second law problems

:::strategy
1. Choose the object or system, then draw its free-body diagram. For acceleration, start with the whole system when its objects share an acceleration. Internal contact forces will cancel.
2. If relevant, for tension or a contact force, isolate an object or subsystem on which that force is external and match the mass to the chosen system.
3. Pick axes that simplify the motion (e.g. $$x$$/$$y$$, radial/centripetal, etc.).
4. Write $$\sum F = ma$$ along each axis. Keep the algebra symbolic until the constraints and signs are settled, then check the units and whether the result agrees with the assumed direction of acceleration. Always include pseudo-forces if necessary.
5. Connect objects with constraints, such as equal tensions for an ideal string.
6. Solve algebraically before substituting numbers.
7. Check the sign and units of the result.
:::

:::mistakes
- Do not assume $$T=mg$$ or $$F_N=mg$$. Other forces and acceleration can change either value.
- Do not count both a force and its components in the same sum. Components replace the original vector in that equation.
- Newton's third-law partners act on different objects. They cancel in a combined system only when both objects are included.
:::

If the question asks only for acceleration of a connected system, the system approach is often faster. If the question asks for tension or contact force, individual free-body diagrams are usually required.

<div class="theorem-box">

**Example.** In the setup shown, $$m_1=3.0\ \text{kg}$$ and $$m_2=2.0\ \text{kg}$$. The table is frictionless and the taut rope and pulley are ideal. Find the acceleration and tension.

<img class="note-img note-img--w640" src="/assets/physics/forces-table.svg" alt="Table and hanging mass setup, with separate free-body diagrams." loading="lazy" decoding="async" />

Both blocks share the same acceleration magnitude $$a$$ because the string is inextensible: as $$m_2$$ falls, $$m_1$$ slides forward by the same amount.

First, we can treat the blocks as one system. The only external force along the direction of motion is the weight of the hanging mass, $$m_2 g$$, and the moving mass is $$m_1 + m_2$$:

$$
m_2 g = (m_1 + m_2)a \quad\Rightarrow\quad a = \frac{m_2 g}{m_1 + m_2} = \frac{(2.0)(9.8)}{5.0} = 3.9\ \text{m/s}^2.
$$

Now find the tension, which requires an individual free-body diagram. For the block on the table (horizontal direction, frictionless):

$$
T = m_1 a = (3.0)(3.9) = 11.8\ \text{N}.
$$

As a check, write Newton's second law for the hanging mass with down positive:

$$
m_2 g - T = m_2 a \quad\Rightarrow\quad T = m_2(g - a) = (2.0)(9.8 - 3.9) = 11.8\ \text{N}.
$$

Both routes agree. Notice the system method gave $$a$$ instantly, but the tension only appeared once we cut the system into individual diagrams: tension is an internal force, invisible to the system equation.

</div>

---

## Apparent weight and elevators

:::mistakes
- Apparent weightlessness means $$F_N=0$$, even while gravity acts.
- Use the direction of acceleration to decide whether the scale reading increases or decreases. An elevator traveling upward while slowing down accelerates downward.
- A negative calculated normal force means ordinary floor contact cannot persist: the floor cannot pull the person downward.
:::

A scale does not directly measure your weight, it insteads measures the **apparent weight**, which is the normal force applied to the scale. In an elevator (or any condition with nonzero acceleration),

$$
F_N - mg = ma
$$

if upward is positive.

So,

$$
F_N = m(g + a).
$$

If the elevator accelerates upward, $$F_N > mg$$. If it accelerates downward, $$F_N < mg$$. In free fall, $$a = -g$$ and $$F_N = 0$$, so the object is weightless in the apparent-weight sense even though gravity still acts.

<div class="theorem-box">

**Example.** A person of mass $$m = 70\ \text{kg}$$ stands on a bathroom scale in an elevator. Find the reading when (a) the elevator accelerates upward at $$2.0\ \text{m/s}^2$$, and (b) the elevator accelerates downward at $$2.0\ \text{m/s}^2$$.

Take up as positive. The scale reads $$F_N$$, where $$F_N - mg = ma$$, so $$F_N = m(g + a)$$.

(a) Upward acceleration, $$a = +2.0\ \text{m/s}^2$$:

$$
F_N = 70(9.8 + 2.0) = 70(11.8) = 826\ \text{N}.
$$

The person feels heavier than their true weight $$mg = 686\ \text{N}$$.

(b) Downward acceleration, $$a = -2.0\ \text{m/s}^2$$:

$$
F_N = 70(9.8 - 2.0) = 70(7.8) = 546\ \text{N}.
$$

The person feels lighter. Note the sign of $$a$$ is what matters, not the direction of motion: an elevator moving up but slowing down has $$a < 0$$ and gives the lighter reading.

</div>

---

## Inclined planes

:::tip
Always decompose forces along axes perpendicular and parallel to the surface of the incline. Check the gravity components against a horizontal surface: at $$\theta=0$$, the down-slope component $$mg\sin\theta$$ vanishes and the perpendicular component $$mg\cos\theta$$ becomes $$mg$$.

If a bob hangs perpendicular to the ceiling of a car translating along a straight incline, with its ceiling parallel to the incline, tension has no component along the slope. If the bob stays fixed relative to the car, its force equations give the car's downhill acceleration $$a=g\sin\theta$$ and the tension $$T=mg\cos\theta$$.
:::

For a block on an incline of angle $$\theta$$, it is usually best to choose axes parallel and perpendicular to the plane. The weight decomposes into

$$
F_{g,\parallel} = mg\sin\theta,
$$

down the incline, and

$$
F_{g,\perp} = mg\cos\theta,
$$

into/perpendicular to the incline.

If there is no acceleration perpendicular to the surface and no other force has a perpendicular component,

$$
F_N = mg\cos\theta.
$$

For a frictionless incline, the acceleration down the plane is

$$
a = g\sin\theta.
$$

With friction, decide whether the block is moving or about to move. If it is moving, use kinetic friction. If it is at rest, static friction takes whatever value is needed up to $$\mu_sF_N$$. It is also helpful to use geometry/similar triangles to determine certain angles for vector decompositions. ALWAYS remember your normal force!

<div class="theorem-box">

**Example.** A car of mass $$m$$ drives uphill on a road of angle $$\theta$$. Its tires roll without slipping, the coefficient of static friction is $$\mu_s$$, and air resistance is negligible. Treat the car as a particle and neglect wheel rotational inertia. Find the greatest uphill acceleration and the condition for maintaining constant uphill speed.

<img class="note-img note-img--w640" src="/assets/physics/forces-car.svg" alt="Car on an incline and separate force diagram with uphill tire friction." loading="lazy" decoding="async" />

The road supplies uphill static friction $$f_s$$, which provides traction. No force acts away from the road except its normal force, so

$$
N=mg\cos\theta,\qquad f_s-mg\sin\theta=ma.
$$

At maximum traction, $$f_s=\mu_sN$$, giving

$$
a_{\max}=g(\mu_s\cos\theta-\sin\theta).
$$

Constant uphill speed requires $$a=0$$ and therefore $$f_s=mg\sin\theta$$. This is possible only if $$\mu_s\ge\tan\theta$$. If the inequality fails, a car already traveling uphill must slow down even at maximum traction. Static friction here points in the direction of travel because it opposes slipping of the driven tires against the road.

</div>

<div class="theorem-box">

**Example.** A $$4.0\ \text{kg}$$ block slides uphill on a $$30^\circ$$ incline with $$\mu_k=0.20$$. A rope at adjustable angle $$\alpha$$ above the slope gives it uphill acceleration $$1.2\ \text{m/s}^2$$. Find the angle that minimizes tension, that tension, and the normal force. Check contact.

<img class="note-img note-img--w640" src="/assets/physics/forces-incline.svg" alt="Angled rope pulling a block uphill, with a separate four-force diagram." loading="lazy" decoding="async" />

Perpendicular balance gives $$N=mg\cos\theta-T\sin\alpha$$. Friction points downhill, so

$$
T\cos\alpha-mg\sin\theta-\mu_k(mg\cos\theta-T\sin\alpha)=ma.
$$

Thus

$$
T=\frac{m[a+g(\sin\theta+\mu_k\cos\theta)]}{\cos\alpha+\mu_k\sin\alpha}.
$$

The numerator is fixed. Write the denominator as
$$\sqrt{1+\mu_k^2}\cos(\alpha-\arctan\mu_k)$$, which is largest at $$\alpha=\arctan\mu_k=11.3^\circ$$. Therefore

$$
T_{\min}=\frac{4.0[1.2+9.8(0.5+0.20\cos30^\circ)]}{\sqrt{1.04}}
=30.6\ \text{N}.
$$

Then $$N=4.0(9.8)\cos30^\circ-30.6\sin11.3^\circ=27.9\ \text{N}>0$$. The optimum is physically admissible. Tilting the rope reduces friction, but tilting it too far sacrifices too much uphill force.

</div>

---

## Connected objects and pulleys

:::tip
For a massless rope passing over ideal massless, frictionless pulleys, tension is the same along each continuous rope (which we assume is true for these types of problems). Different ropes can have different tensions, so count every segment pulling directly on your chosen system.

A movable pulley supported by two vertical segments feels an upward force $$2T$$ (since tension is the same throughout the string). For a combined load and pulley of mass $$M$$, write $$2T-Mg=Ma_y$$, taking up as positive. Only when $$a_y=0$$ does this give $$T=Mg/2$$.

For a person pulling themselves up in a chair, count the rope's pull on both the chair and the person's hand. If each receives an upward tension $$T$$, the person-plus-chair system satisfies $$2T-Mg=Ma_y$$, where $$M$$ is their total mass.
:::

For ideal ropes and pulleys, connected objects share related accelerations. A common Atwood machine is a very simple pulley that contains two hanging masses connected by a massless string over a frictionless pulley.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing,angles,quotes}
\begin{tikzpicture}[>=Stealth, font=\small, scale=0.65]
\draw[thick] (0,2) circle (0.55); \draw[thick] (-0.55,2) -- (-0.55,0.2); \draw[thick] (0.55,2) -- (0.55,-0.5);
\draw[fill=gray!20] (-1.0,-0.6) rectangle (-0.1,0.2); \node at (-0.55,-0.2) {$m_1$};
\draw[fill=gray!20] (0.1,-1.3) rectangle (1.0,-0.5); \node at (0.55,-0.9) {$m_2$};
\draw[->, blue, thick] (-0.55,0.2) -- (-0.55,1.1) node[left] {$T$}; \draw[->, red, thick] (-0.55,-0.6) -- (-0.55,-1.5) node[left] {$m_1g$};
\draw[->, blue, thick] (0.55,-0.5) -- (0.55,0.4) node[right] {$T$}; \draw[->, red, thick] (0.55,-1.3) -- (0.55,-2.2) node[right] {$m_2g$};
\end{tikzpicture}
```

If $$m_2 > m_1$$, the acceleration magnitude is

$$
a = \frac{(m_2 - m_1)g}{m_1 + m_2},
$$

and the tension is

$$
T = \frac{2m_1m_2}{m_1 + m_2}g.
$$

<div class="theorem-box">

**Proof (Atwood tension and acceleration).** Two masses $$m_1$$ and $$m_2$$ ($$m_2 > m_1$$) hang from a massless, inextensible string over a massless, frictionless pulley. Find the acceleration $$a$$ and tension $$T$$.

Since the string is inextensible, whatever distance $$m_2$$ falls, $$m_1$$ rises by the same amount, so both masses have the same acceleration magnitude $$a$$. Take the direction of motion as positive for each mass: $$m_2$$ accelerates downward and $$m_1$$ accelerates upward, with the same $$a$$. The tension $$T$$ is the same on both sides because the string and pulley are ideal.

<img class="note-img note-img--w640" src="/assets/physics/forces-atwood.svg" alt="Separate diagrams of both Atwood masses show upward tension and downward weight." loading="lazy" decoding="async" />

Free-body diagram for $$m_1$$ (taking up as positive):

$$
T - m_1 g = m_1 a.
$$

Free-body diagram for $$m_2$$ (taking down as positive):

$$
m_2 g - T = m_2 a.
$$

Add the two equations to eliminate $$T$$:

$$
m_2 g - m_1 g = (m_1 + m_2)a,
$$

so

$$
a = \frac{(m_2 - m_1)g}{m_1 + m_2}.
$$

To find $$T$$, substitute $$a$$ back into the first equation:

$$
T = m_1(g + a) = m_1 g\left(1 + \frac{m_2 - m_1}{m_1 + m_2}\right) = m_1 g\cdot\frac{2m_2}{m_1 + m_2},
$$

so

$$
T = \frac{2m_1 m_2}{m_1 + m_2}g.
$$

As a check, if $$m_1 = m_2$$ the acceleration is zero and $$T = m_1 g$$, as expected for balanced masses. If $$m_2 \gg m_1$$, then $$a \to g$$ (near free fall) and $$T \to 2m_1 g$$, never $$m_2 g$$.

</div>

For pulley systems with movable pulleys, the acceleration constraints may involve factors of 2. Write the string-length constraint (the length of the string is always constant) first, then differentiate with respect to time to relate velocities and accelerations.

### Multiple pulleys and mechanical advantage

What if there is more than one pulley? For ideal pulleys, we can assign one tension to each continuous rope and write one fixed-length equation for each rope. Different ropes need not have the same tension, but each pulley can have a free-body diagram to balance the tensions.

Suppose a load of total mass $$M$$ is supported by $$n$$ vertical segments of the same ideal rope. Each segment pulls upward with tension $$T$$, so

$$
nT-Mg=Ma,
$$

where $$a$$ is positive upward. If the free end is pulled with force $$F=T$$, the upward force delivered to the load is $$nF$$. This force multiplication is the ideal **mechanical advantage**, $$n$$. When the load is stationary or moves at constant velocity, $$F=Mg/n$$. If it accelerates, instead use $$F=M(g+a)/n$$.

The rope's fixed length explains the accompanying displacement ratio. If the load rises by $$\Delta y$$, each supporting segment shortens by $$\Delta y$$. The free end must therefore take up $$n\Delta y$$ of rope:

$$
\Delta s=n\Delta y,\qquad v_{\mathrm{pull}}=nv_{\mathrm{load}},
\qquad a_{\mathrm{pull}}=na_{\mathrm{load}},
$$

with pull distance positive in the direction that lifts the load. A larger mechanical advantage requires a greater pull distance. These relations assume vertical supporting segments and unchanged geometry; for angled segments, write their actual lengths and resolve their tensions.

:::strategy
1. Label/draw the FBD of each independently moving load, pulley, and rope end (remember all friction, normal force, and directions of tension)
2. Express every rope's length in terms of those positions, including every segment whose length changes, then differentiate twice to relate accelerations with consistent coordinate signs.
3. Write force equations for the loads and movable pulleys. For a massless pulley, its net force is zero even if it accelerates.
4. Solve the force equations and length constraints together, then check that every tension is nonnegative.
:::

<div class="theorem-box">

**Example.** The ideal two-rope system shown has upper mass $$M$$ and lower masses $$m$$ and $$2m$$. The upper rope supports the lower pulley by its axle. Released from rest with both ropes taut, find all three mass accelerations, both tensions, and the values of $$M$$ for which the lower masses initially move in opposite directions.

<img class="note-img note-img--w640" src="/assets/physics/forces-pulley.svg" alt="Compound Atwood machine: upper rope supports M and a movable lower pulley carrying m and 2m." loading="lazy" decoding="async" />

Take every vertical coordinate positive downward. Let $$a_p$$ be the lower pulley's acceleration, $$S$$ the upper-rope tension, and $$T$$ the lower-rope tension. The two fixed lengths give

$$
a_M+a_p=0,\qquad a_1+a_2-2a_p=0,
$$

so $$a_1+a_2=-2a_M$$. The massless lower pulley requires $$S=2T$$. The three mass equations are

$$
Mg-2T=Ma_M,\qquad mg-T=ma_1,\qquad 2mg-T=2ma_2.
$$

Substitute $$a_1=g-T/m$$ and $$a_2=g-T/(2m)$$ into the constraint, then use $$a_M=g-2T/M$$:

$$
2g-\frac{3T}{2m}=-2g+\frac{4T}{M}.
$$

Solving gives

$$
T=\frac{8mMg}{3M+8m},\qquad S=\frac{16mMg}{3M+8m},
$$

$$
a_M=\frac{3M-8m}{3M+8m}g,\quad
a_1=\frac{8m-5M}{3M+8m}g,\quad
a_2=\frac{8m-M}{3M+8m}g.
$$

Both tensions are positive. The lower masses initially move in opposite directions when $$a_1<0<a_2$$, or $$8m/5<M<8m$$. At either boundary one lower mass initially has zero acceleration. Their accelerations need not be equal and opposite relative to the ground because their pulley moves.

</div>

---

## Circular motion

### Uniform circular motion

Kinematics tells us that an object moving in a circle needs an inward acceleration. Here, the new question is what **real forces** produce that acceleration. At each instant, choose a radial axis pointing toward the center and apply Newton's second law along that axis:

$$
\sum F_{\text{inward}}=ma_c=m\frac{v^2}{r}=m\omega^2r.
$$

The expression $$mv^2/r$$ is not an additional force to draw on a free-body diagram. It is the required **net** inward force. Draw only forces that come from physical interactions, such as tension, gravity, friction, or a normal force, and then add their radial components.

Since the inward direction changes as the object moves, the signs of individual forces depend on the object's location. A force pointing toward the center contributes positively to $$\sum F_{\text{inward}}$$; a force pointing away from the center contributes negatively; and a purely tangential force contributes zero to the radial equation.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing,angles,quotes}
\begin{tikzpicture}[>=Stealth, font=\small]
\draw[blue, thick] (0,0) circle (1.6); \fill (0,0) circle (1.5pt) node[below] {center};
\fill (1.35,0.85) circle (2pt) node[above right] {$m$};
\draw[->, very thick, red] (1.35,0.85) -- (0,0) node[above left] {$\sum \vec F_r$};
\draw[->, very thick, blue] (1.35,0.85) -- (0.75,1.8) node[above] {$v$};
\end{tikzpicture}
```

Examples:

- A ball on a string: tension can provide the inward force.
- A car on a flat curve: static friction provides the inward force.
- A satellite in orbit: gravity provides the inward force.
- A roller coaster at the bottom of a loop: normal force and gravity combine to give the net inward force.

:::strategy
1. Draw a free-body diagram containing only real forces.
2. Mark the inward radial direction at the object's current position.
3. Resolve each force into radial and tangential components.
4. Write $$\sum F_{\text{inward}}=mv^2/r$$. Use a separate tangential equation only if the speed is changing.
:::

<div class="theorem-box">

**Example.** A car takes a flat (unbanked) curve of radius $$r = 50\ \text{m}$$. The coefficient of static friction between the tires and road is $$\mu_s = 0.60$$. What is the maximum speed at which the car can round the curve without skidding?

<img class="note-img note-img--w640" src="/assets/physics/forces-flatcar.svg" alt="Car on a flat circular path and a separate diagram showing inward static friction, normal force, and weight." loading="lazy" decoding="async" />

On a flat road the only horizontal force available to turn the car is static friction, which must supply the centripetal force. At the maximum speed friction is at its limit:

$$
\frac{mv_{\max}^2}{r} = \mu_s F_N = \mu_s mg.
$$

The mass cancels, leaving

$$
v_{\max} = \sqrt{\mu_s g r} = \sqrt{(0.60)(9.8)(50)} = \sqrt{294} \approx 17\ \text{m/s}.
$$

That is about $$62\ \text{km/h}$$. Because $$m$$ cancels, a fully loaded truck and a light car can take the same curve at the same maximum speed (assuming equal $$\mu_s$$). Going faster than $$v_{\max}$$ means the required centripetal force exceeds what friction can supply, and the car slides outward.

</div>

<div class="theorem-box">

**Example.** A ball of mass $$m$$ on a string of length $$L$$ swings in a horizontal circle, with the string tracing a cone at a constant angle $$\theta$$ from the vertical. Find the period $$\mathcal{T}$$ of the motion.

<img class="note-img note-img--w640" src="/assets/physics/forces-cone.svg" alt="Conical pendulum setup and separate bob diagram showing tension toward the pivot and weight downward." loading="lazy" decoding="async" />

The ball moves in a horizontal circle of radius $$r = L\sin\theta$$, so its acceleration is purely horizontal and points toward the center. Two forces act: tension $$T$$ along the string and weight $$mg$$ down. There is no vertical acceleration, so the vertical components balance:

$$
T\cos\theta = mg.
$$

The horizontal component of tension provides the centripetal force:

$$
T\sin\theta = \frac{mv^2}{r} = m\omega^2 r.
$$

Divide the second equation by the first to eliminate $$T$$ and $$m$$:

$$
\tan\theta = \frac{\omega^2 r}{g} = \frac{\omega^2 L\sin\theta}{g}.
$$

Cancel $$\sin\theta$$ using $$\tan\theta = \sin\theta/\cos\theta$$:

$$
\frac{1}{\cos\theta} = \frac{\omega^2 L}{g} \quad\Rightarrow\quad \omega = \sqrt{\frac{g}{L\cos\theta}}.
$$

Since $$\omega = 2\pi/\mathcal{T}$$,

$$
\mathcal{T} = 2\pi\sqrt{\frac{L\cos\theta}{g}}.
$$

As $$\theta \to 0$$ the period approaches $$2\pi\sqrt{L/g}$$, the small-angle pendulum result. As $$\theta \to 90^\circ$$ the period goes to zero — you would need infinite tension to hold the string horizontal, which is why the string can never be perfectly horizontal.

</div>

### Circular-motion tips and limiting conditions

:::tip
- Draw the inward direction before assigning signs. At the bottom of an inside loop, $$F_N-mg=mv^2/r$$; at its top, $$F_N+mg=mv^2/r$$. At the crest of a hill with the object on top of the track, $$mg-F_N=mv^2/r$$.
- The condition $$F_N=0$$ occurs when an object loses contact with a surface, but the geometry decides whether it gives a maximum or minimum speed. At a hill's crest it gives $$v_{\max}=\sqrt{gr}$$; at the top of an inside loop it gives $$v_{\min}=\sqrt{gr}$$. These assume the track can only push, with gravity and the normal force as the only radial forces.
- For changing speed, $$v^2/r$$ is only the radial acceleration. Also write $$\sum F_t=ma_t$$, and use $$a=\sqrt{a_r^2+a_t^2}$$ for the total magnitude.
:::

<div class="theorem-box">

**Example.** A car travels over the crest of a circular hill of radius $$R$$ at speed $$v$$. At that instant, its tangential acceleration has magnitude $$b$$. A small package rests on its horizontal roof, and the coefficient of static friction is $$\mu_s>0$$. Find the largest instantaneous speed for which the package can remain in contact without slipping, and find its total acceleration at that limiting speed.

<img class="note-img note-img--w640" src="/assets/physics/forces-crest.svg" alt="Hill-crest package setup and separate package forces; friction points right for rightward tangential acceleration." loading="lazy" decoding="async" />

At the crest, inward is downward. Gravity and the normal force determine the radial acceleration:

$$
mg-F_N=m\frac{v^2}{R},
\qquad F_N=m\left(g-\frac{v^2}{R}\right).
$$

Static friction supplies the horizontal, tangential acceleration, so its required magnitude is $$f_s=mb$$. No slipping requires

$$
mb\le\mu_s m\left(g-\frac{v^2}{R}\right).
$$

Consequently, for $$0\le b\le\mu_s g$$,

$$
v_{\max}=\sqrt{R\left(g-\frac{b}{\mu_s}\right)}.
$$

If $$b>\mu_s g$$, even a stationary package at the crest cannot share the prescribed tangential acceleration without slipping. For $$b>0$$, the friction limit is reached while $$F_N>0$$, before the contact-only limit $$\sqrt{gR}$$.

At the limiting speed, the radial and tangential accelerations are perpendicular:

$$
a=\sqrt{\left(g-\frac{b}{\mu_s}\right)^2+b^2}.
$$

</div>

### Horizontal circles and hanging objects

:::tip
- Determine the actual path radius before substituting into $$mv^2/r$$. For a conical pendulum, $$r=L\sin\theta$$. For a swing attached at platform radius $$R$$ and tilted outward, $$r=R+L\sin\theta$$, where $$\theta$$ is measured from vertical.
- Divide the horizontal and vertical tension equations to eliminate tension. A bob fixed relative to a car with horizontal acceleration magnitude $$a$$ satisfies $$T\sin\theta=ma$$ and $$T\cos\theta=mg$$, so $$\tan\theta=a/g$$. On a level constant-speed turn, substitute $$a=v^2/r$$.
- In a rotating-cylinder ride, the wall's normal force supplies the radial acceleration: $$F_N=m\omega^2r$$. Static friction supports the rider vertically, so $$f_s=mg\le\mu_sF_N$$. Thus $$\omega_{\min}=\sqrt{g/(\mu_s r)}$$. Convert angular speed to revolutions per second using $$f=\omega/(2\pi)$$.
:::

<div class="theorem-box">

**Example.** A swing ride attaches a mass $$m$$ to a chain of length $$L$$ at the edge of a horizontal platform of radius $$R$$. In steady rotation, the chain tilts outward at angle $$\theta$$ from vertical. Its tension must not exceed $$2mg$$. Find the largest permitted angular speed and the corresponding seat speed, treating the seat and rider as a point mass and neglecting air resistance.

<img class="note-img note-img--w640" src="/assets/physics/forces-swing.svg" alt="Swing ride with platform radius and chain geometry, plus the seat and rider force diagram." loading="lazy" decoding="async" />

The seat's path radius includes the chain's horizontal projection:

$$
r=R+L\sin\theta.
$$

Vertical balance and inward acceleration give

$$
T\cos\theta=mg,\qquad
T\sin\theta=m\omega^2(R+L\sin\theta).
$$

The tension limit implies $$\cos\theta\ge1/2$$, so $$\theta\le60^\circ$$. Dividing the two force equations gives

$$
\omega^2=\frac{g\tan\theta}{R+L\sin\theta}.
$$

To check that the largest angle also gives the largest angular speed, differentiate the angle-dependent factor, using radians:

$$
\frac{d}{d\theta}\left(\frac{\tan\theta}{R+L\sin\theta}\right)
=\frac{R+L\sin^3\theta}{\cos^2\theta(R+L\sin\theta)^2}>0
$$

for $$0<\theta<90^\circ$$. The tension limit is therefore reached at the maximum angular speed:

$$
\omega_{\max}=\sqrt{\frac{\sqrt3g}{R+(\sqrt3/2)L}}.
$$

Finally, use the seat's radius, not the platform radius, to obtain

$$
v_{\max}=\omega_{\max}\left(R+\frac{\sqrt3}{2}L\right)
=\sqrt{\sqrt3g\left(R+\frac{\sqrt3}{2}L\right)}.
$$

</div>

### Banked curves

:::tip
Resolve forces horizontally toward the center and vertically. Even though the road is tilted, a car following a level circular path has no vertical acceleration. Determine whether it would slide up or down the bank without friction, then point static friction against that tendency.
:::

Sometimes, circular motion is not confined on a flat surface. For a frictionless banked (raised) curve, the horizontal component of the normal force provides centripetal acceleration, while the vertical component balances weight:

$$
F_N\cos\theta = mg,
$$

$$
F_N\sin\theta = \frac{mv^2}{r}.
$$

Dividing gives

$$
\tan\theta = \frac{v^2}{rg}.
$$

So the design speed is

$$
v = \sqrt{rg\tan\theta}.
$$

With friction, static friction points whichever way prevents slipping: up the slope if the car would slide down, and down the slope if the car would slide up.

<div class="theorem-box">

**Proof (banked-curve design speed).** A car rounds a curve of radius $$r$$ on a road banked at angle $$\theta$$, with no friction needed. Find the speed at which it can do so.

Only two forces act: the normal force $$N$$, perpendicular to the road surface, and the weight $$mg$$, straight down. Use horizontal and vertical axes (not axes along the incline), because the acceleration is horizontal — it points toward the center of the circle, which lies in the horizontal plane.

The normal force tilts inward by the bank angle $$\theta$$ from vertical. Resolve it: its vertical component is $$N\cos\theta$$ and its horizontal (inward) component is $$N\sin\theta$$.

Vertically, there is no acceleration, so the vertical forces balance:

$$
N\cos\theta = mg.
$$

Horizontally, the inward component of the normal force is the entire centripetal force:

$$
N\sin\theta = \frac{mv^2}{r}.
$$

Divide the horizontal equation by the vertical equation. Both $$N$$ and $$m$$ cancel:

$$
\tan\theta = \frac{v^2}{rg}.
$$

Solving for $$v$$ gives the design speed:

$$
v = \sqrt{rg\tan\theta}.
$$

At exactly this speed friction is not required at all. The mass cancels, so the design speed is the same for every vehicle.

</div>

:::tip
For a banked curve, choose horizontal inward and vertical upward axes. At the high-speed limit the car tends to slide up the bank, so friction points down the bank. At the low-speed limit it tends to slide down, so friction points up. Set $$f_s=\mu_sN$$ only at a slipping threshold.

At the high-speed limit,
$$
N\sin\theta+\mu_sN\cos\theta=mv^2/r,\qquad
N\cos\theta-\mu_sN\sin\theta=mg.
$$

At the low-speed limit,
$$
N\sin\theta-\mu_sN\cos\theta=mv^2/r,\qquad
N\cos\theta+\mu_sN\sin\theta=mg.
$$

Eliminate $$N$$ between the equations for each case:
$$
v_{\max}^2=rg\frac{\sin\theta+\mu_s\cos\theta}{\cos\theta-\mu_s\sin\theta},\qquad
v_{\min}^2=rg\frac{\sin\theta-\mu_s\cos\theta}{\cos\theta+\mu_s\sin\theta}.
$$

If the lower expression is negative, set $$v_{\min}=0$$: friction can hold a stationary car. The finite upper bound assumes $$\mu_s\tan\theta<1$$; otherwise this ideal model supplies no finite upper speed limit. Check the force equations and contact rather than taking the square root of a negative expression.
:::

<div class="theorem-box">

**Example.** A highway curve of radius $$r = 120\ \text{m}$$ is to be banked so that a car traveling at $$v = 25\ \text{m/s}$$ (about $$90\ \text{km/h}$$) needs no friction. Find the required bank angle $$\theta$$.

From the design-speed relation,

$$
\tan\theta = \frac{v^2}{rg} = \frac{(25)^2}{(120)(9.8)} = \frac{625}{1176} = 0.531,
$$

so

$$
\theta = \arctan(0.531) \approx 28^\circ.
$$

A car going faster than $$25\ \text{m/s}$$ on this bank would tend to slide outward and up the slope, so static friction would point down the slope; a slower car would tend to slide inward and down, so friction would point up the slope. Friction therefore widens the safe range of speeds around the design speed.

</div>

<div class="theorem-box">

**Example.** A car takes a banked curve of radius $$r$$ and angle $$\theta$$ with static friction coefficient $$\mu_s$$. An aerodynamic force $$D=kv^2$$ acts vertically downward, where $$k>0$$. Derive the permitted speed range, assuming $$0<\mu_s<\tan\theta$$ and $$\mu_s\tan\theta<1$$.

<img class="note-img note-img--w640" src="/assets/physics/forces-bank.svg" alt="Banked road cross-section and high-speed force diagram with downward aerodynamic force." loading="lazy" decoding="async" />

Define
$$
C_+=\frac{\sin\theta+\mu_s\cos\theta}{\cos\theta-\mu_s\sin\theta},\qquad
C_-=\frac{\sin\theta-\mu_s\cos\theta}{\cos\theta+\mu_s\sin\theta}.
$$

The vertical load is now $$mg+kv^2$$. Eliminating $$N$$ from the component equations gives the no-slip inequalities

$$
(mg+kv^2)C_-\le\frac{mv^2}{r}\le(mg+kv^2)C_+.
$$

For the lower bound,
$$
\left(\frac mr-kC_-\right)v^2\ge mgC_-.
$$
If $$m/r\le kC_-$$, no speed is possible: the downward force creates too much tendency to slide down the bank. Otherwise,
$$
v_{\min}^2=\frac{mgC_-}{m/r-kC_-}.
$$

For the upper bound, if $$m/r>kC_+$$,
$$
v_{\max}^2=\frac{mgC_+}{m/r-kC_+}.
$$

If $$m/r\le kC_+$$, that inequality gives no finite upper bound in this idealized model. The downforce changes with speed, so it must stay in the equations until after solving for $$v^2$$.

</div>

## Universal Gravitation

You may be familiar with the "force of gravity" on you, or in other words, your weight. However, $$F=mg$$ is a large simplification because gravity acts between *two* objects (by Newton's third law), not just one, and we are assuming that the Earth experiences negligible force (and thus does not move) when compared with the weight you experience. In general, Newton's law of universal gravitation gives the attractive force between two masses:

$$
F_g=\frac{Gm_1m_2}{r^2}.
$$

The force points along the line connecting the masses and both reactionary forces point towards each other. For a mass $$m$$ near a planet of mass $$M$$,

$$
F_g=\frac{GMm}{r^2}=mg(r),
$$

so the local gravitational field strength is

$$
g(r)=\frac{GM}{r^2}.
$$

Near Earth's surface, $$r\approx R_E$$ changes very little over ordinary heights, so $$g(r)$$ is treated as constant and becomes the familiar $$9.8\ \text{m/s}^2$$. Far from the surface, however, you must use the inverse-square form.

<div class="theorem-box">

**Example.** A satellite orbits Earth in a circular orbit of radius $$r=7.0\times10^6\ \text{m}$$ from Earth's center. Using $$GM_E=3.99\times10^{14}\ \text{m}^3/\text{s}^2$$, find its orbital speed.

For a circular orbit, gravity supplies the centripetal force:

$$
\frac{GM_Em}{r^2}=m\frac{v^2}{r}.
$$

The satellite mass cancels, giving

$$
v=\sqrt{\frac{GM_E}{r}}
=\sqrt{\frac{3.99\times10^{14}}{7.0\times10^6}}
=7.5\times10^3\ \text{m/s}.
$$

The satellite is falling toward Earth, but its sideways speed is large enough that it keeps missing the surface.

</div>

<div class="theorem-box">

**Example.** A planet of mass $$M$$ has a moon in a circular orbit of radius $$r$$ with measured orbital speed $$v_{\text{orbit}}$$. A second moon orbits the same planet at radius $$4r$$. Using only Newton's law of universal gravitation and circular-motion force balance, find the second moon's orbital speed in terms of $$v_{\text{orbit}}$$.

For the first moon, gravity supplies the centripetal force:

$$
\frac{GMm}{r^2}=m\frac{v_{\text{orbit}}^2}{r}.
$$

Cancel $$m$$ and solve for $$GM$$:

$$
GM=v_{\text{orbit}}^2r.
$$

For the second moon at radius $$4r$$,

$$
\frac{GMm_2}{(4r)^2}=m_2\frac{v_2^2}{4r}.
$$

Cancel $$m_2$$:

$$
v_2^2=\frac{GM}{4r}.
$$

Substitute $$GM=v_{\text{orbit}}^2r$$:

$$
v_2^2=\frac{v_{\text{orbit}}^2r}{4r}
=\frac{v_{\text{orbit}}^2}{4},
$$

so

$$
v_2=\frac{v_{\text{orbit}}}{2}.
$$

The farther moon moves more slowly because the gravitational field is weaker and a larger orbit needs less centripetal acceleration for a given speed.

</div>

---

## Variable forces and calculus form

For constant mass, Newton's second law can be written as

$$
\vec{F}_{\text{net}} = m\frac{d\vec{v}}{dt} = m\frac{d^2\vec{r}}{dt^2}.
$$

For variable-mass systems, you will have to use methods that are learned later.

<div class="theorem-box">

**Example.** A block of mass $$m$$ slides at initial speed $$v_0$$ along the inside of a stationary vertical cylindrical wall of radius $$R$$. A smooth horizontal ledge keeps its height fixed. The wall has kinetic friction coefficient $$\mu_k$$; the ledge has no friction. Derive $$v(t)$$, the wall normal force, and the block's acceleration vector.

<img class="note-img note-img--w640" src="/assets/physics/forces-cylinder.svg" alt="Top view of cylindrical wall and local three-direction force diagram." loading="lazy" decoding="async" />

Use local unit vectors $$\hat r$$ outward from the cylinder axis, $$\hat t$$ along the motion, and $$\hat z$$ vertically upward. The wall normal $$N$$ points inward, wall friction opposes sliding, and the ledge's upward normal $$S$$ balances weight. The three equations are

$$
N=\frac{mv^2}{R},\qquad
m\frac{dv}{dt}=-\mu_kN,\qquad
S-mg=0.
$$

Friction acts horizontally because the block's relative sliding is horizontal. The vertical support is supplied by the ledge, not by wall friction. Substituting the radial equation into the tangential one,

$$
\frac{dv}{dt}=-\frac{\mu_k}{R}v^2.
$$

Separate variables and apply $$v(0)=v_0$$:

$$
\int_{v_0}^{v(t)}\frac{du}{u^2}=-\frac{\mu_k}{R}\int_0^t dt',
\qquad
\frac1{v(t)}=\frac1{v_0}+\frac{\mu_k t}{R}.
$$

Hence
$$
v(t)=\frac{v_0}{1+\mu_kv_0t/R},\qquad
N(t)=\frac{mv_0^2}{R(1+\mu_kv_0t/R)^2},\qquad S=mg.
$$

The acceleration has both inward and backward components:
$$
\vec a=-\frac{v^2}{R}\hat r-\frac{\mu_kv^2}{R}\hat t+0\hat z,
\qquad
\lvert\vec a\rvert=\frac{v^2}{R}\sqrt{1+\mu_k^2}.
$$

The speed approaches zero asymptotically. While it is positive, the required wall normal remains positive, so the contact assumption is consistent.

</div>

---

## Working checklist

:::checklist
1. Choose the system carefully.
2. Draw a clean free-body diagram.
3. Pick axes that match the geometry or acceleration.
4. Break forces into components.
5. Write $$\sum F_x = ma_x$$ and $$\sum F_y = ma_y$$.
6. Add constraints for ropes, pulleys, or circular motion.
7. Solve symbolically when possible.
8. Check limiting cases: frictionless, very large mass, zero angle, or zero acceleration.
9. For circular motion, point one axis along the radius (toward the center) and set the net radial force equal to $$mv^2/r$$.
:::

---

:::equations

| Idea | Equation |
| --- | --- |
| Newton's second law | $$\sum \vec{F} = m\vec{a}$$ |
| Components | $$\sum F_x = ma_x,\quad \sum F_y = ma_y$$ |
| Weight near Earth | $$F_g = mg$$ |
| Static friction | $$0 \le f_s \le \mu_sF_N$$ |
| Kinetic friction | $$f_k = \mu_kF_N$$ |
| Hooke's law | $$\vec{F}_s = -k\vec{x}$$ |
| Incline components | $$mg\sin\theta,\quad mg\cos\theta$$ |
| Uniform circular acceleration | $$a_c = v^2/r = \omega^2r$$ |
| Radial Newton's second law | $$\sum F_r = mv^2/r$$ |
| Frictionless banked curve | $$v = \sqrt{rg\tan\theta}$$ |
| Flat-curve max speed | $$v_{\max} = \sqrt{\mu_s g r}$$ |
| Atwood machine | $$a = \dfrac{(m_2 - m_1)g}{m_1 + m_2},\quad T = \dfrac{2m_1 m_2}{m_1 + m_2}g$$ |
| Apparent weight (elevator) | $$F_N = m(g + a)$$ |
| Top-of-loop minimum speed | $$v_{\text{top}} = \sqrt{gr}$$ |
| Terminal velocity (linear drag) | $$v_t = mg/b$$ |
| Banked curve with friction (finite upper bound: $$\mu_s\tan\theta<1$$) | $$v_{\max}^2=rg\frac{\sin\theta+\mu_s\cos\theta}{\cos\theta-\mu_s\sin\theta}$$ |
| Banked curve lower limit | $$v_{\min}^2=\max\!\left(0,rg\frac{\sin\theta-\mu_s\cos\theta}{\cos\theta+\mu_s\sin\theta}\right)$$ |
| Cylinder wall with smooth horizontal support | $$N=mv^2/R,\quad S=mg,\quad dv/dt=-\mu_kv^2/R$$ |
| Cylinder sliding speed | $$v(t)=v_0/(1+\mu_kv_0t/R)$$ |
| Uphill car traction limit | $$a_{\max}=g(\mu_s\cos\theta-\sin\theta)$$ |
| Optimal pulling angle for uphill sliding (contact maintained) | $$\alpha_{\mathrm{opt}}=\arctan\mu_k$$ |
| Compound Atwood constraints (downward coordinates) | $$a_M+a_p=0,\quad a_1+a_2=2a_p,\quad S=2T$$ |
| Tangential calculus on a circular track | $$a_t=v\,dv/ds=(v/R)\,dv/d\theta$$ |
| Linear drag with initial speed $$v_i$$, down positive | $$v(t)=mg/b+(v_i-mg/b)e^{-bt/m}$$ |
| Center of mass dynamics | $$\sum \vec{F}_{\text{ext}} = M\vec{a}_{\text{CM}}$$ |
| Ideal hoist, $$n$$ vertical supporting segments (up positive) | $$nF-Mg=Ma,\quad \mathrm{MA}=n,\quad \Delta s_{\mathrm{pull}}=n\Delta y_{\mathrm{load}}$$ |
| Ideal hoist, unchanged geometry | $$v_{\mathrm{pull}}=nv_{\mathrm{load}},\quad a_{\mathrm{pull}}=na_{\mathrm{load}}$$ |
| Hill crest with tangential acceleration magnitude $$b$$ | $$F_N=m(g-v^2/R),\quad mb\le\mu_sF_N$$ |
| Swing ride, outward tilt $$\theta$$ from vertical | $$r=R+L\sin\theta,\quad T=mg/\cos\theta,\quad \omega^2=g\tan\theta/r$$ |
| Fixed pulley, both coordinates downward | $$y_1+y_2=\text{constant},\quad a_1+a_2=0$$ |
| Movable pulley, two supporting segments, downward coordinates | $$2y_p+y_e=\text{constant},\quad 2a_p+a_e=0$$ |
| Two vertical supporting tensions (up positive) | $$2T-Mg=Ma_y$$ |
| Incline, rope at angle $$\alpha$$ above slope, contact maintained | $$F_N=mg\cos\theta-T\sin\alpha$$ |
| Sliding uphill, uphill positive | $$T\cos\alpha-mg\sin\theta-\mu_kF_N=ma$$ |
| Impending slip, gravity-only incline | $$\tan\theta_{\max}=\mu_s$$ |
| Tangential force equation | $$\sum F_t=ma_t$$ |
| Conical pendulum ($$\theta$$ from vertical) | $$T\cos\theta=mg,\quad T\sin\theta=mv^2/r,\quad r=L\sin\theta$$ |
| Hill crest, ordinary contact | $$mg-F_N=mv^2/r,\quad v_{\max}=\sqrt{gr}$$ |
| Pendulum ($$\theta$$ from downward vertical) | $$T-mg\cos\theta=mv^2/L,\quad ma_t=-mg\sin\theta$$ |
| Bob fixed in horizontally accelerating car | $$\tan\theta=a/g$$ |
| Rotating cylinder, rider not slipping | $$F_N=m\omega^2r,\quad mg\le\mu_sF_N,\quad \omega_{\min}=\sqrt{g/(\mu_s r)}$$ |
| Universal gravitation and field | $$F_g=Gm_1m_2/r^2,\quad g(r)=GM/r^2$$ |
| Circular orbit about a dominant central mass | $$v=\sqrt{GM/r}$$ |
| Constant-mass calculus form | $$\vec F_{\mathrm{net}}=m\,d\vec v/dt=m\,d^2\vec r/dt^2$$ |
| Linear drag force, falling from rest (down positive) | $$m\,dv/dt=mg-bv,\quad v(t)=\frac{mg}{b}(1-e^{-bt/m}),\quad \tau=m/b$$ |
:::

## Practice

### Multiple Choice

::::problem
1. A block stays fixed on a stationary incline of angle $$\theta$$. A force $$P$$ pulls parallel uphill, with $$0<P<mg\sin\theta$$. What minimum static friction coefficient prevents slipping?

(A) $$\tan\theta$$

(B) $$\dfrac{mg\sin\theta-P}{mg\cos\theta}$$

(C) $$\dfrac{mg\sin\theta+P}{mg\cos\theta}$$

(D) $$\dfrac{P}{mg}$$

:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth,scale=1.3,font=\small]
\fill (0,0) circle (2pt);
\draw[->,thick] (0,0) -- (-0.5,1) node[left] {$N$};
\draw[->,thick] (0,0) -- (0,-1) node[below] {$mg$};
\draw[->,thick] (0,0) -- (1,0.5) node[right] {$P$};
\draw[->,thick] (0,0) -- (0.75,0.375) node[right] {$f_s$};
\end{tikzpicture}
```

Take uphill and outward-normal axes. The pull has no normal component, so $$N-mg\cos\theta=0$$. Along the slope, zero acceleration requires $$P+f_s-mg\sin\theta=0$$. The stated bound on $$P$$ makes the required friction positive uphill; only at the minimum coefficient does it equal $$\mu_sN$$.

Perpendicular balance gives $$N=mg\cos\theta$$. Gravity's downhill component exceeds the pull, so uphill friction must supply $$f_s=mg\sin\theta-P$$. The smallest coefficient is $$f_s/N$$, giving **B**.
:::
::::

::::problem
2. A force $$F$$ presses a block against a vertical wall at angle $$\alpha$$ above horizontal. The static friction coefficient is $$\mu_s$$. What is the smallest $$F$$ that can hold the block at rest?

(A) $$mg/(\mu_s\cos\alpha)$$

(B) $$mg/(\cos\alpha+\mu_s\sin\alpha)$$

(C) $$mg/(\sin\alpha+\mu_s\cos\alpha)$$

(D) $$mg/\sin\alpha$$

:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth,scale=1.3,font=\small]
\fill (0,0) circle (2pt);
\draw[->,thick] (0,0) -- (-1,0) node[left] {$N$};
\draw[->,thick] (0,0) -- (0.9,0.7) node[right] {$F$};
\draw[->,thick] (0,0) -- (0,1) node[above] {$f_s$};
\draw[->,thick] (0,0) -- (0,-1) node[below] {$mg$};
\end{tikzpicture}
```

Choose horizontal and vertical axes. The applied force's horizontal component presses the block into the wall, while its vertical component already supports part of the weight. At the smallest possible force, the remaining weight is supported by the maximum upward static friction. A larger applied force need not leave friction at its maximum.

The wall normal is $$N=F\cos\alpha$$. At the lower force threshold, upward friction reaches $$\mu_sN$$. Vertical balance is $$F\sin\alpha+\mu_sF\cos\alpha=mg$$, so **C**. The upward component of the applied force reduces the friction needed.
:::
::::

::::problem
3. Blocks $$m$$ and $$2m$$ slide right on a table, connected by a taut ideal rope. Their kinetic friction coefficients are $$\mu$$ and $$2\mu$$, respectively. A horizontal force $$F>5\mu mg$$ pulls the $$2m$$ block right. Find the tension.

(A) $$F/3-2\mu mg/3$$

(B) $$F/3$$

(C) $$F/3+2\mu mg/3$$

(D) $$2F/3-\mu mg$$

:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth,scale=1.3,font=\small]
\fill (0,0) circle (2pt);
\draw[->,thick] (0,0) -- (0,1) node[above] {$N_1$};
\draw[->,thick] (0,0) -- (0,-1) node[below] {$mg$};
\draw[->,thick] (0,0) -- (1,0) node[right] {$T$};
\draw[->,thick] (0,0) -- (-1,0) node[left] {$f_{k1}$};
\begin{scope}[xshift=4cm]
\fill (0,0) circle (2pt);
\draw[->,thick] (0,0) -- (0,1) node[above] {$N_2$};
\draw[->,thick] (0,0) -- (0,-1) node[below] {$2mg$};
\draw[->,thick] (0,0) -- (1,0) node[right] {$F$};
\draw[->,thick] (0,0.12) -- (-1,0.12) node[left] {$T$};
\draw[->,thick] (0,-0.12) -- (-1,-0.12) node[below] {$f_{k2}$};
\end{scope}
\end{tikzpicture}
```

The diagram shows the smaller block. Its friction is $$\mu mg$$, whereas the larger block's friction is $$(2\mu)(2mg)=4\mu mg$$. When the two horizontal equations are added, the internal tensions cancel. After finding their common acceleration, return to the smaller block to recover tension. Equal acceleration does not imply equal net forces because the masses differ.

Total friction is $$\mu mg+(2\mu)(2mg)=5\mu mg$$, so $$a=(F-5\mu mg)/(3m)$$. For the smaller block, $$T-\mu mg=ma$$. Substitution gives $$T=F/3-2\mu mg/3$$, so **A**.
:::
::::

::::problem
4. A mass falls from rest with linear drag coefficient $$b$$. At the instant its downward acceleration is $$g/3$$, what are its downward speed and drag magnitude?

(A) $$mg/(3b),\ mg/3$$

(B) $$2mg/(3b),\ 2mg/3$$

(C) $$mg/b,\ mg$$

(D) $$2mg/b,\ 2mg$$

:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth,scale=1.3,font=\small]
\fill (0,0) circle (2pt);
\draw[->,thick] (0,0) -- (0,1) node[above] {$bv$};
\draw[->,thick] (0,0) -- (0,-1) node[below] {$mg$};
\end{tikzpicture}
```

The object is moving downward, so the upward arrow is drag. Acceleration is also downward but smaller than $$g$$, which means drag cancels part of the weight. The net force is $$mg/3$$, not the drag itself. Subtracting that net force from the weight gives the drag magnitude.

With downward positive, $$mg-bv=m(g/3)$$. Thus $$bv=2mg/3$$ and $$v=2mg/(3b)$$. The answer is **B**; terminal speed has not yet been reached.
:::
::::

::::problem
5. A horizontal force pushes a block rightward against an incline rising rightward at angle $$\theta$$. With $$\mu_s<\tan\theta$$, what minimum force prevents downhill slip?

(A) $$\dfrac{mg(\sin\theta-\mu_s\cos\theta)}{\cos\theta+\mu_s\sin\theta}$$

(B) $$mg\tan\theta$$

(C) $$\dfrac{mg(\sin\theta+\mu_s\cos\theta)}{\cos\theta-\mu_s\sin\theta}$$

(D) $$mg(\sin\theta-\mu_s\cos\theta)$$

:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth,scale=1.3,font=\small]
\fill (0,0) circle (2pt);
\draw[->,thick] (0,0) -- (-0.5,1) node[left] {$N$};
\draw[->,thick] (0,0) -- (0,-1) node[below] {$mg$};
\draw[->,thick] (0,0) -- (1,0) node[right] {$F$};
\draw[->,thick] (0,0) -- (0.8,0.4) node[right] {$f_s$};
\end{tikzpicture}
```

Resolve the horizontal push along the tilted axes. Its uphill component is $$F\cos\theta$$ and its into-surface component is $$F\sin\theta$$. Friction acts uphill at the lower force threshold because gravity would otherwise pull the block down. Substituting the perpendicular equation into the parallel equation gives
$$
F(\cos\theta+\mu_s\sin\theta)=mg(\sin\theta-\mu_s\cos\theta).
$$
The condition on $$\mu_s$$ ensures a positive minimum force.

The push both acts uphill and increases the normal force: $$N=mg\cos\theta+F\sin\theta$$. At impending downhill slip, $$F\cos\theta+\mu_sN=mg\sin\theta$$. Solving gives **A**. Using $$N=mg\cos\theta$$ would omit the extra friction supplied by the push.
:::
::::

::::problem
6. A bob stays fixed relative to a cabin accelerating rightward at $$a_x$$ and upward at $$a_y$$. Its string makes angle $$\theta$$ from vertical. Which pair gives its tension and tilt?

(A) $$T=mg,\ \tan\theta=a_x/g$$

(B) $$T=m\sqrt{a_x^2+(g+a_y)^2},\ \tan\theta=a_x/(g+a_y)$$

(C) $$T=m(g+a_y),\ \tan\theta=a_x/g$$

(D) $$T=m\sqrt{a_x^2+a_y^2},\ \tan\theta=a_x/a_y$$

:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth,scale=1.3,font=\small]
\fill (0,0) circle (2pt);
\draw[->,thick] (0,0) -- (0.65,1) node[right] {$T$};
\draw[->,thick] (0,0) -- (0,-1) node[below] {$mg$};
\end{tikzpicture}
```

Use the ground frame: being fixed in the cabin does not make the bob's acceleration zero. The tension's vertical component must exceed weight by $$ma_y$$, so it is $$m(g+a_y)$$. The horizontal component is $$ma_x$$. These perpendicular components form a right triangle whose hypotenuse is the full tension.

The bob shares the cabin's acceleration. Its component equations are $$T\sin\theta=ma_x$$ and $$T\cos\theta-mg=ma_y$$. Dividing yields the tilt; squaring and adding yields the tension. Both results appear in **B**.
:::
::::

::::problem
7. At the crest of a circular hill of radius $$R$$, a package has normal force $$mg/3$$. The roof-package static friction coefficient is $$\mu_s$$. What is the greatest tangential acceleration magnitude the package can share without slipping?

(A) $$\mu_sg$$

(B) $$2\mu_sg/3$$

(C) $$\mu_sg/3$$

(D) $$g/3$$

:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth,scale=1.3,font=\small]
\fill (0,0) circle (2pt);
\draw[->,thick] (0,0) -- (0,1) node[above] {$N$};
\draw[->,thick] (0,0) -- (0,-1) node[below] {$mg$};
\draw[->,thick] (0,0) -- (1,0) node[right] {$f_s$};
\end{tikzpicture}
```

At the hilltop, inward is downward. The package is not in vertical equilibrium: $$mg-N=mv^2/R$$. Friction lies along the horizontal tangent, so it alone changes the speed. The friction threshold depends on the given normal force, even though that force is smaller than weight.

The radial equation gives $$v^2/R=2g/3$$, but the tangential acceleration comes from friction: $$mb\le\mu_sN=\mu_smg/3$$. Therefore $$b_{\max}=\mu_sg/3$$, answer **C**. The reduced normal force limits traction even though gravity is unchanged.
:::
::::

::::problem
8. A bead on a smooth vertical circular hoop of radius $$R$$ passes its rightmost point with total acceleration magnitude $$2g$$. What are its speed and normal force magnitude?

(A) $$\sqrt{2gR},\ 2mg$$

(B) $$\sqrt{gR},\ mg$$

(C) $$\sqrt{\sqrt3gR},\ \sqrt3mg$$

(D) $$\sqrt{3gR},\ 3mg$$

:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth,scale=1.3,font=\small]
\fill (0,0) circle (2pt);
\draw[->,thick] (0,0) -- (-1,0) node[left] {$N$};
\draw[->,thick] (0,0) -- (0,-1) node[below] {$mg$};
\end{tikzpicture}
```

The inward normal and gravity are perpendicular at the rightmost point. Therefore the given total acceleration cannot be substituted directly for $$v^2/R$$. First remove the tangential contribution using the Pythagorean relation, then use the radial component to find speed and normal force.

At the side, gravity is entirely tangential, so $$a_t=-g$$. The normal supplies radial acceleration $$a_r=v^2/R$$. Thus $$(v^2/R)^2+g^2=4g^2$$, giving $$v^2/R=\sqrt3g$$. Since $$N=mv^2/R$$, **C** gives both results.
:::
::::

::::problem
9. A mass hangs from a scale in an elevator accelerating upward at $$g/2$$. A horizontal force $$F$$ holds it fixed relative to the elevator, and the scale reads $$2mg$$. Find $$F$$.

(A) $$mg/2$$

(B) $$\sqrt7mg/2$$

(C) $$\sqrt3mg$$

(D) $$3mg/2$$

:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth,scale=1.3,font=\small]
\fill (0,0) circle (2pt);
\draw[->,thick] (0,0) -- (-0.65,1) node[left] {$T$};
\draw[->,thick] (0,0) -- (1,0) node[right] {$F$};
\draw[->,thick] (0,0) -- (0,-1) node[below] {$mg$};
\end{tikzpicture}
```

The diagram takes the applied force rightward, so tension points upward and leftward. There is no horizontal acceleration relative to the ground, but the mass shares the elevator's upward acceleration. The scale measures the magnitude of tension, not its vertical component. Squaring the perpendicular tension components eliminates the unknown string angle.

The vertical tension component must be $$m(g+g/2)=3mg/2$$. The horizontal component balances $$F$$. Therefore $$F^2+(3mg/2)^2=(2mg)^2$$, giving $$F=\sqrt7mg/2$$, answer **B**.
:::
::::

::::problem
10. A wedge rising rightward at angle $$\theta$$ accelerates rightward at $$a<g\cot\theta$$. A block stays fixed on its surface. What minimum static friction coefficient is required?

(A) $$\tan\theta$$

(B) $$\dfrac{a\cos\theta+g\sin\theta}{g\cos\theta-a\sin\theta}$$

(C) $$\dfrac{g\sin\theta-a\cos\theta}{g\cos\theta+a\sin\theta}$$

(D) $$a/g$$

:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth,scale=1.3,font=\small]
\fill (0,0) circle (2pt);
\draw[->,thick] (0,0) -- (-0.5,1) node[left] {$N$};
\draw[->,thick] (0,0) -- (0.9,0.45) node[right] {$f_s$};
\draw[->,thick] (0,0) -- (0,-1) node[below] {$mg$};
\end{tikzpicture}
```

The outward normal points upward and leftward, giving the rightward acceleration a negative normal projection $$-a\sin\theta$$. Its uphill projection is $$a\cos\theta$$. Friction must both oppose gravity's downhill component and supply the uphill projection of acceleration. The upper bound on $$a$$ ensures a positive normal force so that division by $$N$$ is valid.

The block's ground-frame acceleration is rightward. Projecting perpendicular gives $$N=m(g\cos\theta-a\sin\theta)>0$$. Projecting uphill gives $$f_s-mg\sin\theta=ma\cos\theta$$. Divide the required friction by $$N$$ to obtain **B**. Both acceleration components matter.
:::
::::

::::problem
11. A mass moves on a taut string in a vertical circle of radius $$R$$, with an applied tangential force controlling its speed. Its top tension is $$mg/2$$, and its bottom speed is twice its top speed. What is its bottom tension?

(A) $$5mg$$

(B) $$6mg$$

(C) $$7mg$$

(D) $$9mg$$

:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth,scale=1.3,font=\small]
\fill (0,0) circle (2pt);
\draw[->,thick] (-0.12,0) -- (-0.12,-1) node[left] {$T_t$};
\draw[->,thick] (0.12,0) -- (0.12,-1.6) node[right] {$mg$};
\draw[->,thick] (0,0) -- (1,0) node[right] {$F_{\rm tan}$};
\end{tikzpicture}
```

The diagram shows the top; at the bottom the tension arrow reverses upward while weight remains downward. The applied drive is tangential and contributes nothing to either radial equation. Doubling speed quadruples $$v^2/R$$. This is why the bottom tension cannot be found by merely doubling the top tension.

At the top, $$T_t+mg=mv_t^2/R$$, so $$v_t^2/R=3g/2$$. Since $$v_b=2v_t$$, $$v_b^2/R=6g$$. At the bottom, $$T_b-mg=mv_b^2/R$$, giving $$T_b=7mg$$, answer **C**. The specified speed ratio is used directly; no energy relation is assumed.
:::
::::

::::problem
12. A cabin accelerates upward at $$a_y$$ while following a level circular path of radius $$R$$ with speed $$v$$ and tangential acceleration $$b$$. A block remains fixed on its horizontal floor. What minimum static friction coefficient is required?

(A) $$\dfrac{\sqrt{(v^2/R)^2+b^2}}{g+a_y}$$

(B) $$\dfrac{v^2/R+b}{g+a_y}$$

(C) $$\dfrac{v^2}{Rg}$$

(D) $$\dfrac{b}{g+a_y}$$

:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth,scale=1.3,font=\small]
\fill (0,0) circle (2pt);
\draw[->,thick] (0,0) -- (0,1) node[above] {$N$};
\draw[->,thick] (0,0) -- (0,-1) node[below] {$mg$};
\draw[->,thick] (0,0) -- (1,0.35) node[right] {$\vec f_s$};
\end{tikzpicture}
```

The horizontal friction vector has radial and tangential components; the slanted arrow is schematic, not an additional force. The normal force supplies the required upward acceleration in addition to balancing gravity. Horizontal acceleration is the vector sum of two perpendicular components, so the required friction magnitude follows from the Pythagorean theorem.

The normal force is $$N=m(g+a_y)$$. Friction must provide both perpendicular horizontal acceleration components, radial $$v^2/R$$ and tangential $$b$$. Its required magnitude is $$m\sqrt{(v^2/R)^2+b^2}$$. Dividing by $$N$$ gives **A**; adding the two components as scalars overestimates the required friction.
:::
::::

### FRQ

::::frq{id=ap-physics-c-mechanics-forces-1}
1. A block of mass $$m$$ is inside a box that accelerates horizontally with acceleration $$a$$. The block is pressed against the box's vertical wall and does not slip. The coefficient of static friction between the block and wall is $$\mu_s$$.

   $$(A)$$ Draw a free-body diagram for the block in the ground frame.

   $$(B)$$ Derive the normal force exerted by the wall on the block.

   $$(C)$$ Determine the condition on $$a$$ for the block not to slide down.

   $$(D)$$ If the box also accelerates upward with acceleration $$a_y$$, derive the new no-slip condition.

   $$(E)$$ Now let the box's horizontal acceleration increase as $$a_x(t)=ct$$, with $$c>0$$, and set its vertical acceleration to zero. At $$t=0$$ the block is released from rest against the wall. With kinetic coefficient $$\mu_k<\mu_s$$, find when its downward relative speed is greatest, when it first stops sliding, and how far it drops before stopping. Explain whether it can then stick.

:::solution
$$(A)$$ The block is accelerating horizontally with the box, so the wall must push it horizontally. The block would slide downward without friction, so static friction points upward.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,decorations.pathmorphing}
\begin{tikzpicture}[>=Stealth, font=\small, scale=0.85]
  \draw[fill=gray!5, thick] (0,0) rectangle (3.2,2.6);
  \fill[gray!20] (0,0) rectangle (0.22,2.6);
  \draw[fill=blue!10, thick] (0.22,0.95) rectangle (1.32,1.75);
  \coordinate (c) at (0.77,1.35);
  \draw[->, thick] (c) -- ++(1.15,0) node[right] {$N$};
  \draw[->, thick] (c) -- ++(0,-1.15) node[right] {$mg$};
  \draw[->, thick, green!55!black] (c) -- ++(0,1.15) node[above] {$f_s$};
  \draw[->, thick, red!75] (1.55,2.25) -- ++(1.15,0) node[right] {$a$};
\end{tikzpicture}
```

Thus the forces on the block are weight $$mg$$ downward, normal force $$N$$ from the wall horizontally, and static friction $$f_s$$ upward. Note that friction would act on the contacting surface but is drawn in the middle of the block for a clearer demonstration.

$$(B)$$ Horizontally,

$$
\boxed{N=ma}.
$$

This equation is not a friction condition; it is just Newton's second law in the horizontal direction. The normal force is the only horizontal force on the block, so it must provide the block's horizontal acceleration.

$$(C)$$ To avoid sliding,

$$
mg\le \mu_sN=\mu_sma,
$$

so

$$
\boxed{a\ge \frac{g}{\mu_s}}.
$$

At the threshold, static friction is at its maximum. If $$a$$ is smaller than this, then $$N=ma$$ is too small, so $$\mu_sN$$ cannot support the weight.

$$(D)$$ If the box accelerates upward, the required friction is $$m(g+a_y)$$. Since $$N=ma$$,

$$
m(g+a_y)\le \mu_sma,
$$

so

$$
\boxed{a\ge \frac{g+a_y}{\mu_s}}.
$$

The upward acceleration increases the required upward net force. Friction must now both balance gravity and create upward acceleration, which is why $$g$$ becomes $$g+a_y$$.

$$(E)$$ While the block slides downward, kinetic friction points upward and $$N=mct$$. Taking downward as positive for its relative vertical motion,
$$
\frac{dv}{dt}=g-\mu_kct,\qquad v(t)=gt-\frac12\mu_kct^2.
$$
Its speed peaks when the acceleration changes sign, at $$t_*=g/(\mu_kc)$$. It does not stop there: it continues downward while slowing. The nonzero root of $$v(t)=0$$ is
$$
t_s=\frac{2g}{\mu_kc}.
$$
Integrating velocity gives the drop:
$$
h= \frac12gt_s^2-\frac16\mu_kct_s^3
=\frac{2g^3}{3\mu_k^2c^2}.
$$
At that instant, static friction needs to supply only $$mg$$. Its available maximum is $$\mu_sN(t_s)=2(\mu_s/\mu_k)mg>mg$$, so the block can stick. The kinetic equation must not be continued into upward motion after this event.
:::
::::

::::frq{id=ap-physics-c-mechanics-forces-2}
2. A particle of mass $$m$$ slides on the smooth inside surface of a circular track of radius $$R$$ fixed in a vertical plane. The track can push inward but cannot pull outward. At an angle $$\theta$$ measured from the bottom, the particle has speed $$v$$.

   $$(A)$$ Draw a force diagram for the bead.

   $$(B)$$ Write Newton's second law in the radial direction.

   $$(C)$$ Write Newton's second law in the tangential direction.

   $$(D)$$ At angle $$\theta$$, determine the speed at which the bead would just lose contact with the hoop, if such a speed is possible.

   $$(E)$$ The object instead slides on the inside surface of a smooth circular track, which can push inward but cannot pull outward. It starts at the bottom moving toward increasing $$\theta$$ with speed $$v_0$$, where $$2gR<v_0^2<5gR$$. Use $$a_t=v\,dv/ds$$ and $$s=R\theta$$ to derive $$v^2(\theta)$$ and find the first loss-of-contact angle. Do not use conservation of energy.

:::solution
$$(A)$$ The bead only touches the hoop, so the contact force is normal to the hoop. Since the hoop is frictionless, there is no tangential contact force.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,angles,quotes}
\begin{tikzpicture}[>=Stealth, font=\small, scale=0.95]
  \coordinate (O) at (0,0); \coordinate (B) at (0.95,-0.95); \coordinate (D) at (0,-1.35);
  \draw[thick] (O) circle (1.35); \fill (O) circle (1.5pt);
  \draw[dashed] (O) -- (D); \draw[dashed] (O) -- (B);
  \fill[blue!65] (B) circle (4pt);
  \draw[->, thick] (B) -- (0.18,-0.18) node[midway,above] {$N$};
  \draw[->, thick] (B) -- ++(0,-1.15) node[below] {$mg$};
  \draw pic[draw, "$\theta$", angle radius=0.45cm] {angle=D--O--B};
\end{tikzpicture}
```

The forces are weight $$mg$$ downward and normal force $$N$$ along the radius.

$$(B)$$ Taking inward as positive,

$$
\boxed{N-mg\cos\theta=\frac{mv^2}{R}}.
$$

The term $$mg\cos\theta$$ appears because the angle is measured from the bottom, so the component of gravity along the outward radial direction is $$mg\cos\theta$$. With inward positive, that component enters with a minus sign.

$$(C)$$ Taking increasing $$\theta$$ as positive tangential direction,

$$
\boxed{-mg\sin\theta=ma_t}.
$$

The normal force has no tangential component, so only gravity changes the bead's speed along the hoop.

$$(D)$$ Loss of contact means $$N=0$$, so

$$
-mg\cos\theta=\frac{mv^2}{R}.
$$

Thus

$$
\boxed{v=\sqrt{-gR\cos\theta}},
$$

which is possible only when $$\cos\theta\le0$$.

That condition says the bead can only lose contact in the upper half of the hoop. In the lower half, gravity's radial component points the wrong way to supply the required inward centripetal acceleration by itself.

$$(E)$$ The tangential equation gives
$$
\frac{v}{R}\frac{dv}{d\theta}=-g\sin\theta.
$$
Integrate from the bottom to angle $$\theta$$:
$$
\frac12(v^2-v_0^2)=gR(\cos\theta-1),
\qquad v^2=v_0^2-2gR(1-\cos\theta).
$$
Substitution into the radial equation yields
$$
N=\frac{mv_0^2}{R}-2mg+3mg\cos\theta.
$$
The first zero occurs at
$$
\theta_c=\arccos\left(\frac{2gR-v_0^2}{3gR}\right).
$$
The given speed range puts $$\theta_c$$ strictly between $$90^\circ$$ and $$180^\circ$$. At that angle $$v^2=-gR\cos\theta_c>0$$, so contact is lost before the object stops. This conclusion requires the one-sided track contact specified in this part; a bead threaded onto a wire cannot simply detach.
:::
::::

::::frq{id=ap-physics-c-mechanics-forces-3}
3. A mass $$m$$ falls from rest through a fluid with drag force $$F_d=bv$$ upward. Take downward as positive.

   $$(A)$$ Write the differential equation for $$v(t)$$.

   $$(B)$$ Determine the terminal speed.

   $$(C)$$ Without solving fully for $$v(t)$$, determine whether the acceleration is increasing, decreasing, or constant as the object falls.

   $$(D)$$ Design a linear graph that could be used to determine $$b$$ from measurements of speed and acceleration.

   $$(E)$$ At time $$t=\tau=m/b$$, the object enters a second fluid with drag coefficient $$2b$$. Neglect buoyancy and any impulse at the boundary. Derive its speed for $$t\ge\tau$$, determine whether it initially speeds up or slows down in the second fluid, and find the time after entry when its speed differs from the new terminal speed by only 10% of the initial difference.

:::solution
$$(A)$$ Taking downward as positive, gravity is positive and drag is negative because it points opposite the downward velocity.

$$
\boxed{m\frac{dv}{dt}=mg-bv}.
$$

$$(B)$$ At terminal speed, the velocity is no longer changing, so $$dv/dt=0$$. The drag force has grown large enough to balance the weight:

$$
\boxed{v_t=\frac{mg}{b}}.
$$

$$(C)$$ Divide the differential equation by $$m$$:

$$
a=\frac{dv}{dt}=g-\frac{b}{m}v.
$$

As the object speeds up, $$v$$ increases, so the drag term $$bv/m$$ increases. Therefore the acceleration decreases, approaching zero as $$v$$ approaches terminal speed.

$$(D)$$ Graph $$a$$ on the vertical axis versus $$v$$ on the horizontal axis.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth, font=\small, x=2.0cm, y=1.7cm]
  \draw[->] (0,0) -- (2.25,0) node[right] {$v$};
  \draw[->] (0,0) -- (0,1.35) node[above] {$a$};
  \draw[very thick, blue!70] (0,1) node[left] {$g$} -- (1.65,0) node[below] {$v_t=mg/b$};
  \node[blue!70, rotate=-27] at (0.95,0.62) {slope $=-b/m$};
\end{tikzpicture}
```

The equation $$a=g-(b/m)v$$ is linear with slope $$-b/m$$, so $$b=-m(\text{slope})$$.

$$(E)$$ In the first fluid, separating the differential equation gives
$$
v(t)=\frac{mg}{b}(1-e^{-t/\tau}).
$$
Hence the continuous entry speed is $$v_1=(mg/b)(1-e^{-1})$$. The second fluid's terminal speed is $$V=mg/(2b)$$. For elapsed time $$u=t-\tau$$, the new equation is $$dv/du=-(2b/m)(v-V)$$, whose solution is
$$
v=V+(v_1-V)e^{-2bu/m}.
$$
Since $$1-e^{-1}>1/2$$, the object enters faster than the new terminal speed and initially slows down. Drag can exceed weight in this situation. The remaining difference is 10% when
$$
e^{-2bu/m}=0.10,\qquad u=\frac{m}{2b}\ln10.
$$
Velocity stays continuous at entry, but acceleration changes abruptly because the drag coefficient changes.
:::
::::
