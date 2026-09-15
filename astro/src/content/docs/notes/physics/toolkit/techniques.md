---
title: "Problem Solving Techniques"
description: "Physics notes on problem-solving techniques, including diagrams, units, approximations, conservation laws, and equation selection."
sidebar:
  order: 3
---

## Dimensional analysis

Before solving, ask what combination of the given quantities even *has the right units* for the answer. Often there's only one, which pins down the answer up to a dimensionless constant.

<div class="theorem-box">

**Example.** Derive the formula for the period of a pendulum up to constants.

Suppose you forgot the pendulum formula. The period $$T$$ (units: s) could depend on length $$L$$ (m), mass $$m$$ (kg), and gravity $$g$$ (m/s²). The only way to build a time from these is $$\sqrt{L/g}$$: mass cannot appear, because there's no other mass to cancel its kg. So $$T=C\sqrt{L/g}$$ for some dimensionless $$C$$ (which turns out to be $$2\pi$$). Dimensional analysis gives the dependence on length and gravity and shows that mass drops out. It does not determine the dimensionless constant or any dependence on the swing angle.

</div>

The method's one blind spot is **dimensionless constants** (the $$2\pi$$) and dimensionless ratios (like angles or the Reynolds number), which it cannot determine. Most of the time, problems using dimensional analysis will ask you to solve up to constants or give you certain relations which you can use to determine the final formula.

---

## D'Alembert's principle

Newton's second law can be written as $$\vec F_i-m_i\vec a_i=0$$. For a system with ideal constraints, take the dot product with each allowed **virtual displacement** $$\delta\vec r_i$$ and sum:

$$
\sum_i(\vec F_i^{\,\mathrm{applied}}-m_i\vec a_i)\cdot\delta\vec r_i=0.
$$

This is **D'Alembert's principle**. A virtual displacement compares nearby configurations at the same instant; it obeys the constraints but need not equal the actual displacement during a time interval. Ideal constraint forces contribute zero total virtual work, so tensions and normal forces can drop out.

The term $$-m_i\vec a_i$$ is an inertial term that lets us write a dynamics problem in a form resembling equilibrium. It is not an extra physical interaction. Setting all accelerations to zero recovers the ordinary virtual-work condition below.

<div class="theorem-box">

**Example.** Masses $$m_1$$ and $$m_2>m_1$$ hang from an ideal string over a massless, frictionless pulley. Use D'Alembert's principle to find their acceleration.

Let $$q$$ increase when $$m_2$$ moves down, so $$m_1$$ moves up by the same amount. The applied gravitational virtual work is $$(m_2-m_1)g\,\delta q$$. Both masses contribute inertial virtual work $$-m_i\ddot q\,\delta q$$. Thus

$$
\big[(m_2-m_1)g-(m_1+m_2)\ddot q\big]\delta q=0,
$$

giving

$$
\ddot q=\frac{m_2-m_1}{m_1+m_2}g.
$$

The tension does not appear because the ideal string ties the two virtual displacements together.

</div>

---

## Virtual Work Method

The virtual work method is a way to find equilibrium conditions (or the force needed to hold something) without drawing a single free-body diagram or worrying about internal/constraint forces. It rests on one principle:

> For a system in equilibrium, the total work done by the applied forces under any small displacement consistent with the constraints is zero. In other words, $$\;\delta W=0$$.

For the ideal constraints considered here, **constraint forces do no virtual work**: normal forces, tensions in inextensible strings, and frictionless contact forces are all *perpendicular* to the allowed motion (or internal and canceling), so they drop out entirely. You only ever deal with the forces you care about (gravity, applied loads, springs).

:::strategy
1. Identify the **degrees of freedom** and pick a single coordinate $$q$$ (e.g. Cartesian, polar, etc.) that is best suited for the problem.
2. Write the positions of every point where a force acts in terms of $$q$$.
3. Give the system a virtual displacement $$\delta q$$ and compute the total work $$\delta W=\sum_i \vec F_i\cdot\delta\vec r_i$$.
4. Set $$\delta W=0$$ and solve.
:::

Equivalently, if the forces are conservative, equilibrium is where the potential energy is stationary: $$dU/dq=0$$.

<div class="theorem-box">

**Example.** A uniform ladder of length $$L$$ and mass $$M$$ rests against a smooth vertical wall on a smooth horizontal floor. A person of mass $$m$$ stands a distance $$s$$ along the ladder from its foot. A horizontal force $$F$$ applied to the foot toward the wall holds the ladder at angle $$\theta$$ above the floor. Find $$F$$ by virtual work.

<img class="note-img note-img--w480" src="/assets/physics/usapho/comments/ladder.svg" alt="Ladder against a smooth wall, person at distance s from its foot, and a horizontal holding force toward the wall" loading="lazy" decoding="async" />

Let $$x=L\cos\theta$$ be the foot's distance from the wall. Its virtual displacement is $$\delta x=-L\sin\theta\,\delta\theta$$. Since the applied force points toward the wall, its work is $$-F\delta x=FL\sin\theta\,\delta\theta$$.

The ladder's center rises by $$(L/2)\cos\theta\,\delta\theta$$, and the person rises by $$s\cos\theta\,\delta\theta$$. Gravity does negative work. The wall and floor normals do no work because each contact moves along its supporting surface. Therefore

$$
\delta W=\left[FL\sin\theta-\left(\frac{MgL}{2}+mgs\right)\cos\theta\right]\delta\theta=0.
$$

Solving,

$$
F=g\left(\frac{M}{2}+\frac{ms}{L}\right)\cot\theta.
$$

A person higher up the ladder requires a larger holding force. As the ladder approaches vertical, the required force tends to zero.

</div>

---

## Exploiting symmetry

If a problem has a symmetry, the answer must respect it. This lets you skip enormous amounts of computation:

- **Cancellation:** in computing a field or force, components that the symmetry maps onto their own negatives must sum to zero. (The field on the axis of a charged ring has no transverse component — every element's transverse contribution is canceled by the element opposite it.)
- **Gauss's law / Ampère's law:** symmetry is what makes these usable — it forces the field to be constant over a well-chosen surface or loop, pulling it out of the integral.
- **Superposition tricks:** a charged disk with a hole is a full disk *minus* a small disk; a sphere with an off-center cavity is a full sphere minus a smaller one. Adding back the missing piece restores symmetry and makes each part trivial. To solve, just set the would-be cavity to have negative mass/charge/whatever variable you are solving for and solve from there.

Always pause to ask: "what does this setup look the same under?" Reflection, rotation, and translation symmetries each kill some terms before you compute anything.

---

## Limiting cases

After getting an answer (or to choose between answer choices), test it in extreme cases where you already know what should happen:

- Let a mass, length, or angle go to $$0$$ or $$\infty$$ and check the formula behaves sensibly.
- Set two quantities equal, or make one much larger than another, and see if it reduces to a simpler known result.
- Check the **units** of the final expression.
- Check **signs and directions** make physical sense.

For example, the two-body reduced mass $$\mu=\dfrac{m_1 m_2}{m_1+m_2}$$ (shown later) should reduce to $$m$$ when one mass is infinite (a fixed center) and to $$m/2$$ when the masses are equal — both of which it does. On a multiple-choice exam, limiting cases often eliminate every wrong option in seconds.

<div class="theorem-box">

**Example.** A cart of mass $$m$$ moving at speed $$v$$ sticks to a stationary cart of mass $$M$$. Two proposed final speeds are $$u_1=mv/(m+M)$$ and $$u_2=Mv/(m+M)$$. Use limiting cases to decide which can be correct.

As $$M\to0$$, the moving cart picks up almost no mass, so its speed should approach $$v$$. The first formula does; the second tends to zero. As $$M\to\infty$$, the combined carts should move extremely slowly: again $$u_1\to0$$ while $$u_2\to v$$. For $$M=m$$ both give $$v/2$$, so that check alone would not distinguish them.

Thus only $$u_1$$ survives these checks. Momentum conservation confirms it:

$$
mv=(m+M)u\quad\Longrightarrow\quad u=\frac{m}{m+M}v.
$$

Passing limiting checks supports a result but does not prove it for every parameter value.

</div>

---

## Problem-solving strategy

Since this whole page is a toolbox, the decision tree is a meta one: when a problem looks ugly, which technique do you reach for first?

:::strategy
1. **Asked for an equilibrium force or condition, with messy tensions/normals/constraints**: Virtual work. Pick one coordinate $$q$$, write $$\delta W=\sum_i\vec F_i\cdot\delta\vec r_i=0$$, and the constraint forces drop out — or use $$dU/dq=0$$ if forces are conservative.
2. **You only need the *form* of the answer, or you're sanity-checking algebra**: Dimensional analysis. Build the unique combination with the right units; e.g. a time from length and gravity can only be $$\sqrt{L/g}$$. Just remember it cannot fix dimensionless constants like the $$2\pi$$.
3. **Computing a field, force, or integral over a symmetric configuration**: Exploit symmetry. Components mapped to their negatives cancel, and Gauss's/Ampère's law become usable because the field is constant over a chosen surface or loop.
4. **A shape is "almost" symmetric (a disk with a hole, a sphere with a cavity)**: Superposition — add back the missing piece as negative mass/charge, solve each symmetric part, subtract.
5. **You have a candidate answer and want to test it (or kill MC options)**: Limiting cases. Send a length, mass, or angle to $$0$$ or $$\infty$$, set two quantities equal, and check units, signs, and directions reduce to something known.
6. **Dynamics with ideal constraints and unwanted tensions or normals:** Use D'Alembert's principle, $$\sum_i(\vec F_i^{\,\mathrm{applied}}-m_i\vec a_i)\cdot\delta\vec r_i=0$$. Write both the acceleration and allowed virtual displacement in terms of the same coordinate; do not set the acceleration to zero unless the system is actually in equilibrium.
:::

:::mistakes
- Trusting dimensional analysis for numerical prefactors — it gives the scaling, never the $$2\pi$$ or other dimensionless factors and ratios.
- Forgetting that virtual work needs the displacement to be *consistent with the constraints*; an arbitrary $$\delta q$$ that violates a constraint reintroduces the forces you tried to eliminate.
- Claiming a symmetry the setup doesn't actually have — a broken symmetry (off-axis point, non-uniform density) means the "obviously zero" component is not zero.
- In the superposition trick, mismatching the sign or location of the subtracted piece so it doesn't exactly fill the would-be cavity.
- Treating D'Alembert's inertial term as an additional physical force, or using displacements that violate the constraints.
- Reading off a limiting case carelessly: $$0/0$$ or $$\infty-\infty$$ forms need an actual expansion, not a guess.
:::
