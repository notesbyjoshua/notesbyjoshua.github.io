---
title: "Functional Equations"
status: developing
progress: 68
sidebar:
  order: 7
description: "Competition math notes on functional equations, useful substitutions, injectivity, surjectivity, and iteration, with fully verified worked solutions."
---

## What a Functional Equation Asks For

A functional equation gives a relation involving unknown function values and asks for **all** functions that satisfy it. Both the domain and codomain matter. A function on the integers can behave differently from a function on the reals, and continuity cannot be assumed unless it is given or proved.

A complete solution has two parts: derive a list of possible functions, then substitute every candidate into the original equation. Trying $$f(x)=x$$ or $$f(x)=x^2$$ can suggest an answer, but it does not prove that other functions are impossible.

For an equation in two variables, write $$P(x,y)$$ for the assertion at the inputs $$x,y$$. This makes it easier to track which substitutions justify each step.

---

## Zero Inputs and Constant Functions

Inputs such as $$0$$ and $$1$$ often turn products or powers into simpler expressions. Before dividing by $$f(0)$$ or $$f(1)$$, check whether it could be zero.

<div class="theorem-box">

**Example.** Find all functions $$f:\mathbb R\to\mathbb R$$ satisfying $$f(x+y)=f(x)+f(y)+2xy$$ and $$f(1)=1$$, assuming $$f$$ is continuous.

Putting $$x=y=0$$ gives $$f(0)=0$$. The cross term $$2xy$$ suggests removing a square. Define $$g(x)=f(x)-x^2$$. Then

$$
g(x+y)=g(x)+g(y),\qquad g(1)=0.
$$

Additivity gives $$g(n)=0$$ for integers and then $$g(m/n)=0$$ for rationals with $$n\ne0$$. For any real $$x$$, choose rationals $$q_k\to x$$. Continuity gives $$g(x)=\lim g(q_k)=0$$. Thus $$f(x)=x^2$$.

Finally, $$(x+y)^2=x^2+y^2+2xy$$ and $$f(1)=1$$, so the candidate works.

</div>

Without continuity or another suitable regularity condition, an additive function on $$\mathbb R$$ need not be linear. On $$\mathbb Q$$, additivity alone does force $$g(q)=qg(1)$$. Keep this distinction in mind whenever an argument starts by checking integers and rationals.

Constant candidates can be checked quickly by substituting $$f(x)=c$$ into the full equation. Do this before an argument that assumes the function takes at least two values.

---

## Injectivity and Surjectivity

A function is **injective** if $$f(a)=f(b)$$ implies $$a=b$$. It is **surjective** onto its codomain if every target value occurs. Injectivity lets us remove an outer $$f$$ from an equality; surjectivity lets us choose an input giving a desired function value.

<div class="theorem-box">

**Example.** A function $$f:\mathbb R\to\mathbb R$$ satisfies $$f(f(x))=x$$. Prove that it is injective and surjective.

If $$f(a)=f(b)$$, apply $$f$$ to both sides:

$$
a=f(f(a))=f(f(b))=b.
$$

For any real target $$t$$, the input $$f(t)$$ satisfies $$f(f(t))=t$$, so every real number is attained. Both claims follow directly from the equation.

</div>

This equation does not force $$f(x)=x$$. For example, $$f(x)=-x$$ also works. Proving a useful property of the function is different from classifying it.

---

## Symmetry and Cancellation

If an equation has both $$x$$ and $$y$$, compare $$P(x,y)$$ and $$P(y,x)$$. The difference may eliminate the complicated part. Another useful move is to choose inputs so that two function arguments become equal.

<div class="theorem-box">

**Example.** Find all functions $$f:\mathbb R\to\mathbb R$$ satisfying

$$
f(x+y)+xf(y)=f(x)+y
$$

for all real $$x,y$$.

Set $$x=0$$. We get $$f(y)=f(0)+y$$, so write $$f(t)=t+c$$. Substituting this candidate into the original equation leaves

$$
x+y+c+x(y+c)=x+c+y,
$$

which requires $$x(y+c)=0$$ for every $$x,y$$. Taking $$x=1$$ would force $$y=-c$$ for every real $$y$$, which is impossible. There are no solutions.

</div>

A necessary formula found from a special input may fail elsewhere. This is why verification is part of the solution.

<div class="theorem-box">

**Example.** Find all functions $$f:\mathbb R\to\mathbb R$$ satisfying $$f(x+y)=f(x-y)+2y$$.

Choose $$y=x$$ so that one argument becomes zero:

$$
f(2x)=f(0)+2x.
$$

Every real input can be written as $$2x$$, so $$f(t)=t+c$$ for a real constant $$c$$. Conversely,

$$
f(x-y)+2y=x-y+c+2y=x+y+c=f(x+y),
$$

so every such function works.

</div>

---

## Iteration and Domain Restrictions

If the equation contains $$f(f(x))$$, compute $$f(f(f(x)))$$ in two ways: apply $$f$$ to the original relation, and substitute $$f(x)$$ for $$x$$. This can produce a shift relation that is easier to use.

<div class="theorem-box">

**Example.** Find all strictly increasing functions $$f:\mathbb Z\to\mathbb Z$$ satisfying $$f(f(n))=n+2$$.

The two evaluations of the triple iterate give

$$
f(n+2)=f(f(f(n)))=f(n)+2.
$$

Strict increase and integer outputs imply

$$
f(n)<f(n+1)<f(n+2)=f(n)+2.
$$

The only integer strictly between the endpoints is $$f(n)+1$$, so $$f(n+1)=f(n)+1$$. Hence $$f(n)=n+c$$ for an integer $$c$$. Substitution gives $$n+2c=n+2$$, so $$c=1$$. The function $$f(n)=n+1$$ is strictly increasing and satisfies the original equation.

</div>

:::strategy
Start with admissible zero and unit inputs, test constant solutions, and record every function value you determine. Then look for equal arguments, variable swaps, injectivity, surjectivity, or iteration. Use a substitution only when its inputs lie in the stated domain.
:::

## Normalizing an Equation

A constant term can obscure an otherwise familiar relation. If the equation resembles additivity but includes a fixed offset, try replacing $$f$$ by $$g(x)=f(x)+c$$. If it contains a cross term $$2xy$$, subtract a quadratic. The purpose is to isolate the part of the function whose behavior is still unknown.

This is different from assuming a candidate formula. The substitution is reversible, so solving the new equation solves the old one. Write down the reverse conversion to avoid losing a constant when you return to $$f$$.

<div class="theorem-box">

**Example.** Find every function $$f:\mathbb Z\to\mathbb Z$$ satisfying $$f(m+n)=f(m)+f(n)+1$$ and $$f(1)=4$$.

Set $$g(n)=f(n)+1$$. Then $$g(m+n)=g(m)+g(n)$$ and $$g(1)=5$$. Repeated addition gives $$g(n)=5n$$ for positive integers. Also $$g(0)=0$$ and $$g(-n)=-g(n)$$, so the formula holds for every integer.

Thus $$f(n)=5n-1$$. Substitution gives $$5(m+n)-1=(5m-1)+(5n-1)+1$$, and the initial condition holds. The candidate is verified on the entire domain.

</div>

On the integers, an additive function is determined by its value at one. On the rationals, division extends this conclusion. On the reals, a further argument is necessary; knowing a formula on a dense set does not determine an arbitrary discontinuous function.

---

## Additivity Plus an Order Condition

An additive real function that is nonnegative on nonnegative inputs is increasing in the weak sense. If $$y\ge x$$, then

$$
f(y)-f(x)=f(y-x)\ge0.
$$

Monotonicity is enough to extend the rational formula to all real inputs. Suppose $$f(1)=c$$. Choose rationals $$r<x<s$$ as close to $$x$$ as desired. Then $$cr=f(r)\le f(x)\le f(s)=cs$$. Letting the rational bounds approach $$x$$ forces $$f(x)=cx$$.

The important point is where the order condition comes from. Some equations express a value at a square as another square, automatically proving nonnegativity. This can eliminate pathological additive functions without an explicit continuity assumption.

<div class="theorem-box">

**Example.** Find every function $$f:\mathbb R\to\mathbb R$$ satisfying

$$
f(x^2+y)=f(x)^2+f(y)
$$

for all real $$x,y$$.

Set $$x=0$$ to obtain $$f(0)^2=0$$, so $$f(0)=0$$. Then $$y=0$$ gives $$f(x^2)=f(x)^2\ge0$$. Every nonnegative real number is a square, hence $$f(t)\ge0$$ for $$t\ge0$$.

For $$t\ge0$$, choose $$x=\sqrt t$$. The equation becomes $$f(y+t)=f(y)+f(t)$$. Taking $$y=-t$$ proves $$f(-t)=-f(t)$$. Consequently the same addition rule extends to negative increments, so $$f$$ is additive on all the reals.

The nonnegativity just proved makes $$f$$ monotone. Therefore $$f(x)=cx$$. Finally, $$f(1)=f(1)^2$$ gives $$c=c^2$$, hence $$c=0$$ or $$1$$.

Both $$f(x)=0$$ and $$f(x)=x$$ satisfy the original equation. These are the complete solutions, with no continuity assumption needed.

</div>

The solution has a useful order of operations: first obtain a special value, then a sign restriction, then a simpler functional law, and only afterward classify the function. Guessing a line at the start would miss the reason no other functions survive.

---

## Additive and Multiplicative Functions Together

A function may satisfy more than one structural relation. If

$$
f(x+y)=f(x)+f(y),\qquad f(xy)=f(x)f(y),
$$

the product relation constrains $$f(1)$$ and the sum relation propagates it to integers and rationals. Squares then provide the order condition needed on the reals.

<div class="theorem-box">

**Example.** Classify all real-valued functions on $$\mathbb R$$ satisfying both displayed relations.

Multiplicativity at one gives $$f(1)=f(1)^2$$. If $$f(1)=0$$, then $$f(x)=f(x\cdot1)=f(x)f(1)=0$$ for every $$x$$.

Otherwise $$f(1)=1$$. Additivity gives $$f(q)=q$$ for rational $$q$$. For $$t\ge0$$, write $$t=u^2$$; multiplicativity gives $$f(t)=f(u)^2\ge0$$. Thus additivity makes $$f$$ monotone, and rational bounds force $$f(x)=x$$ for every real $$x$$.

Both the zero function and the identity function work. The proof also identifies which condition rules out the discontinuous additive possibilities: multiplicativity forces positivity through squares.

</div>

This method should not be applied to a function on an arbitrary field as though order were available. Over the complex numbers, nonnegative inputs and rational bracketing do not have the same meaning. Domain information is part of the argument, not introductory decoration.

---

## Surjectivity Before Choosing a Special Output

A common mistake is to write “choose $$t$$ such that $$f(t)=0$$” without proving zero is in the range. Sometimes the original equation does prove surjectivity, but that proof must come first. Isolate a function value equal to an expression that ranges over the full codomain.

<div class="theorem-box">

**Example.** Find all continuous functions $$f:\mathbb R\to\mathbb R$$ satisfying

$$
f(x+f(y))=f(x)+y.
$$

Let $$c=f(0)$$. Setting $$x=0$$ gives $$f(f(y))=c+y$$, proving surjectivity. Choose $$t$$ with $$f(t)=0$$. The original equation at $$y=t$$ becomes $$f(x)=f(x)+t$$, so $$t=0$$. Hence $$f(0)=0$$ and $$f(f(y))=y$$.

Now every real $$u$$ equals $$f(y)$$ for some $$y$$. Since $$f(u)=y$$, the original equation becomes

$$
f(x+u)=f(x)+f(u).
$$

Thus $$f$$ is additive. Continuity implies $$f(x)=ax$$, and the double-iterate relation gives $$a^2=1$$. The two candidates $$f(x)=x$$ and $$f(x)=-x$$ both satisfy the equation, so both are solutions.

</div>

Without continuity, this argument reaches additive involutions rather than only those two lines. The regularity assumption is used at one specific step, and the proof should make that dependence visible.

---

## Comparing Different Routes to the Same Input

Associativity can produce a relation even when swapping the visible variables does not. If an equation supplies $$f(x+y)$$, compute $$f(x+y+z)$$ by grouping $$(x+y)+z$$ and $$x+(y+z)$$. If it supplies composition, compare different evaluations of a triple iterate.

For polynomial-looking equations, match arguments before simplifying outputs. Solving an auxiliary equation such as $$A(x,y)=B(x,y)$$ can make two unknown function values cancel. The substitution may look unusual, but it is motivated by the terms you want to eliminate.

Another useful maneuver is to replace $$x$$ by $$-x$$ or $$y$$ by $$-y$$ after determining $$f(0)$$. This can reveal oddness, evenness, or the value of $$f(-x)$$ in terms of $$f(x)$$. Check whether negative inputs belong to the domain; for a positive-real domain, reciprocals or ratios may play the corresponding role.

:::checklist
- Record the domain and every quantified input before substituting.
- Determine zero, unit, or constant cases before division.
- Prove that a desired output occurs before selecting its preimage.
- State exactly where continuity, monotonicity, positivity, or integrality enters.
- Substitute each final candidate into the original equation.
:::

A strong functional-equation solution distinguishes established identities from guesses throughout. It is fine to test linear or quadratic candidates during exploration, but the written argument must explain why the equation forces that form and why every proposed function works for every allowed input.

---

## Multiplicative Cauchy Equations

An equation can turn addition in the input into multiplication in the output. For continuous real functions, the basic classification is exponential, but zero and sign cases must be settled before taking logarithms.

<div class="theorem-box">

**Example.** Find all continuous functions $$f:\mathbb R\to\mathbb R$$ satisfying $$f(x+y)=f(x)f(y)$$.

At zero, $$f(0)=f(0)^2$$. If $$f(0)=0$$, then $$f(x)=f(x)f(0)=0$$ for all $$x$$.

Otherwise $$f(0)=1$$. The relation $$f(x)f(-x)=1$$ shows that no value is zero. Also $$f(x)=f(x/2)^2$$, so every value is positive. It is now legitimate to define $$g(x)=\ln f(x)$$.

The new function is continuous and additive, hence $$g(x)=cx$$. Thus $$f(x)=e^{cx}$$ for an arbitrary real constant $$c$$. Every such exponential satisfies the equation, as does the zero function.

</div>

Taking logarithms before establishing positivity would leave a gap. The equation itself supplies that positivity, and the proof should use it explicitly.

---

## Periods and Continuity

A period relation alone leaves many functions possible. The equation $$f(x+1)=f(x)$$ admits every one-periodic function, so it does not force constancy or linearity.

Two incommensurable periods behave differently with continuity. Suppose one and $$\sqrt2$$ are periods. Integer combinations are periods, including nonzero periods arbitrarily close to zero: the fractional-part pigeonhole argument supplies integers $$p,q$$ with $$q\sqrt2-p$$ arbitrarily small.

For any real $$x$$ and small positive period $$\delta$$, choose an integer multiple $$k\delta$$ within $$\delta$$ of $$x$$. Periodicity gives $$f(k\delta)=f(0)$$. As the available periods tend to zero, those multiples approach $$x$$, and continuity gives $$f(x)=f(0)$$.

Thus the function is constant. The decisive extra condition is continuity; a function can otherwise be constant on each coset of the additive subgroup generated by the periods while taking different values on different cosets. This illustrates why a dense set of controlled inputs still needs a regularity argument to control every real input.

---

## Key Relations

:::equations
| Idea | Relation or condition |
| --- | --- |
| Injectivity | $$f(a)=f(b)\Longrightarrow a=b$$ |
| Surjectivity | For every target $$t$$, some input $$x$$ has $$f(x)=t$$ |
| Additivity over the rationals | $$g(q)=qg(1)$$ for $$q\in\mathbb Q$$ |
| Additivity over the reals | $$g(x)=cx$$ follows with continuity; additivity alone is insufficient |
| Iteration | Evaluate $$f(f(f(x)))$$ using both composition and substitution |
| Constant shift | $$g(x)=f(x)+c$$ can remove an additive offset |
| Additive order argument | Additivity and $$f(t)\ge0$$ for $$t\ge0$$ imply monotonicity |
| Real linearity | An additive monotone or continuous real function has form $$f(x)=cx$$ |
| Square positivity | $$f(u^2)=f(u)^2\ge0$$ can supply the needed order condition |
| Involution | $$f(f(x))=x$$ implies injectivity and surjectivity |
| Continuous multiplicative Cauchy | $$f(x+y)=f(x)f(y)$$ gives $$f\equiv0$$ or $$f(x)=e^{cx}$$ |
:::
