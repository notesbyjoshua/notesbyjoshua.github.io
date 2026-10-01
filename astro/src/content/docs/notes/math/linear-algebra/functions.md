---
title: "Unit 2: Functions"
description: "Linear algebra notes introducing functions, domains, codomains, well-defined rules, images, and injective, surjective, and bijective maps."
sidebar:
  order: 2
---

## Functions, Domains, and Codomains

<div class="theorem-box">

**Definition.** A **function** $$f:A\to B$$ assigns each element of the input set $$A$$ to exactly one element of the output set $$B$$. The set $$A$$ is the **domain**, and the set $$B$$ is the **codomain**.

</div>

A function can be pictured as a machine or an arrow diagram, but the important rule is simple: **every input gets exactly one output**. Different inputs are allowed to share an output. What is not allowed is one input being sent to two different outputs.

The notation

$$
f:A\to B
$$

specifies three pieces of information:

1. the rule or assignment $$f$$,
2. the domain $$A$$,
3. the codomain $$B$$.

All three are part of the function. A formula by itself is not enough because its behavior depends on which inputs are allowed and which outputs are expected.

The expression $$f(x)$$ is the output assigned to the input $$x$$. The set of outputs the function actually reaches is its **image** or **range**:

$$
\operatorname{im}(f)=\{f(x)\mid x\in A\}\subseteq B.
$$

The codomain is part of the function's definition. Two rules with the same formula but different domains or codomains are different functions.

<div class="theorem-box">

**Example.** Let $$f:\mathbb R\to\mathbb R$$ be defined by $$f(x)=x^2$$. Identify its domain, codomain, and image, and evaluate $$f(-3)$$.

The domain and codomain come from the declaration $$f:\mathbb R\to\mathbb R$$, so both are $$\mathbb R$$. Substituting $$-3$$ gives

$$
f(-3)=(-3)^2=9.
$$

Although the codomain is all real numbers, a real square cannot be negative. Every nonnegative real number does occur as a square, so

$$
\operatorname{im}(f)=[0,\infty).
$$

Thus, the image can be smaller than the codomain.

</div>

The image of a set of inputs is also useful. If $$S\subseteq A$$, then

$$
f(S)=\{f(x)\mid x\in S\}.
$$

For the squaring function above,

$$
f([-2,1])=[0,4].
$$

The interval crosses $$0$$, so the smallest output is $$0$$; the input with the largest magnitude is $$-2$$, which gives the largest output $$4$$.

<div class="theorem-box">

**Definition.** Functions $$f:A\to B$$ and $$g:C\to D$$ are equal if

$$
A=C,\qquad B=D,
$$

and

$$
f(x)=g(x)\quad\text{for every }x\in A.
$$

</div>

The **identity function** on a set $$A$$ is

$$
\operatorname{id}_A:A\to A,
\qquad
\operatorname{id}_A(x)=x.
$$

It leaves every element unchanged.

Identity functions may look trivial, but they give a reference point for what it means to leave a space unchanged. Later, composing a function with $$\operatorname{id}_A$$ will play the same role as multiplying a number by $$1$$.

<div class="theorem-box">

**Example.** Define $$f:\mathbb R\to\mathbb R$$ by $$f(x)=x^2$$ and $$g:[0,\infty)\to\mathbb R$$ by $$g(x)=x^2$$. Determine whether $$f=g$$.

The formulas agree wherever both functions are defined, but the domains do not:

$$
\operatorname{dom}(f)=\mathbb R,
\qquad
\operatorname{dom}(g)=[0,\infty).
$$

Therefore, $$f$$ and $$g$$ are different functions.

</div>

---

## Well-Defined Functions

A proposed function must give one unambiguous output for every input in its domain. This can fail in three main ways: an input has no output, an input has more than one output, or a single mathematical object has several representations and the rule depends on which representation is chosen.

For example, the rule $$f(x)=1/x$$ does not define a function $$f:\mathbb R\to\mathbb R$$ because the allowed input $$x=0$$ has no real output. It does define a function

$$
f:\mathbb R\setminus\{0\}\to\mathbb R
$$

because removing $$0$$ from the domain removes the problem.

<div class="theorem-box">

**Example.** Consider the proposed rule $$f:\mathbb Q\to\mathbb Z$$ given by

$$
f\left(\frac{a}{b}\right)=a+b.
$$

Determine whether $$f$$ is well-defined.

The same rational number can be written in different ways. For example,

$$
\frac12=\frac24,
$$

but the rule gives

$$
f\left(\frac12\right)=1+2=3
$$

and

$$
f\left(\frac24\right)=2+4=6.
$$

One input would have two outputs, so the rule is not well-defined. To repair it, one could require a unique standard representation: $$a/b$$ must be in lowest terms and $$b>0$$. Requiring lowest terms alone is not quite enough because

$$
\frac12=\frac{-1}{-2}
$$

still gives two reduced representations unless the sign convention is fixed.

</div>

:::checklist
When checking whether a rule defines a function, verify that:

1. every input in the domain receives an output,
2. every output lies in the stated codomain,
3. each input receives only one output,
4. equivalent representations of the same input give the same output.
:::

Every sequence is a function whose domain is usually $$\mathbb N$$. A sequence $$a_1,a_2,a_3,\ldots$$ can be written as

$$
a:\mathbb N\to B,
\qquad
a(n)=a_n.
$$

For example, the sequence

$$
2,4,8,16,\ldots
$$

is the function

$$
a:\mathbb N\to\mathbb R,
\qquad
a(n)=2^n.
$$

The input is the position in the sequence, and the output is the term at that position. Thinking of sequences as functions lets the same definitions of image, injectivity, and composition apply to them later.

---

## Injective, Surjective, and Bijective Functions

These three words describe how the arrows from the domain land in the codomain:

| Property | What can go wrong? | Informal picture |
|---|---|---|
| Injective | Two inputs collide at one output | no collisions |
| Surjective | A codomain element is never reached | no gaps |
| Bijective | Neither problem occurs | perfect pairing |

<div class="theorem-box">

**Definition.** A function $$f:A\to B$$ is **injective** or **one-to-one** if different inputs always have different outputs:

$$
a_1\neq a_2\Rightarrow f(a_1)\neq f(a_2).
$$

Equivalently,

$$
f(a_1)=f(a_2)\Rightarrow a_1=a_2.
$$

</div>

The two injectivity statements are contrapositives, so they are logically equivalent. In proofs, the second form is usually easier: assume two outputs are equal, then show the inputs must have been equal.

For a real-valued graph, injectivity is checked by the horizontal line test: every horizontal line may intersect the graph at most once.

<div class="theorem-box">

**Definition.** A function $$f:A\to B$$ is **surjective** or **onto** if every element of the codomain is reached:

$$
\forall b\in B,\ \exists a\in A\text{ such that }f(a)=b.
$$

</div>

Surjectivity compares the image with the stated codomain:

$$
f\text{ is surjective}
\quad\Longleftrightarrow\quad
\operatorname{im}(f)=B.
$$

This is why changing only the codomain can change whether a function is onto. The outputs do not change, but the target the function is expected to cover does.

A function that is both injective and surjective is **bijective**. A bijection pairs every input with exactly one output and reaches every element of the codomain.

A bijection is reversible: every output points back to exactly one input. This is the reason bijections are used to compare the sizes of sets and why invertible linear transformations become so important later.

:::tip
To prove injectivity, start by assuming $$f(a_1)=f(a_2)$$ and work toward $$a_1=a_2$$. To prove surjectivity, begin with an arbitrary $$b$$ in the codomain and solve $$f(a)=b$$ for an input $$a$$ in the domain.
:::

<div class="theorem-box">

**Example.** Classify each version of the squaring rule as injective, surjective, both, or neither:

$$
f:\mathbb R\to\mathbb R,
\qquad
g:[0,\infty)\to\mathbb R,
\qquad
h:[0,\infty)\to[0,\infty),
$$

where each function sends $$x$$ to $$x^2$$.

The function $$f$$ is not injective because

$$
f(1)=f(-1)=1.
$$

It is not surjective because no negative real number is an output. Thus, $$f$$ is neither.

Restricting the domain removes the collision between positive and negative inputs, so $$g$$ is injective. Its codomain is still $$\mathbb R$$, however, so it still misses every negative number and is not surjective.

The function $$h$$ uses the restricted domain and the exact image as its codomain. It is injective and surjective, so it is bijective.

</div>

<div class="theorem-box">

**Proof (A bijection on the rational numbers).** Define $$f:\mathbb Q\to\mathbb Q$$ by

$$
f(q)=3q+2.
$$

To prove injectivity, suppose $$f(q_1)=f(q_2)$$. Then

$$
3q_1+2=3q_2+2,
$$

so $$q_1=q_2$$.

To prove surjectivity, let $$b\in\mathbb Q$$. Choose

$$
q=\frac{b-2}{3}.
$$

Since rational numbers are closed under subtraction and division by a nonzero rational number, $$q\in\mathbb Q$$. Moreover,

$$
f(q)=3\left(\frac{b-2}{3}\right)+2=b.
$$

Thus, $$f$$ is both injective and surjective, so it is bijective.

</div>

<div class="theorem-box">

**Example.** Let $$g:\mathbb C\to\mathbb R$$ be defined by

$$
g(a+bi)=\sqrt{a^2+b^2}.
$$

Determine whether $$g$$ is injective or surjective.

It is not injective because distinct complex numbers can have the same magnitude. For example,

$$
g(1+2i)=g(2+i)=\sqrt5.
$$

It is also not surjective onto $$\mathbb R$$ because magnitudes are never negative. In particular, there is no $$z\in\mathbb C$$ such that $$g(z)=-1$$.

</div>

:::warning
Surjectivity depends on the codomain. The same magnitude rule becomes surjective if its codomain is changed from $$\mathbb R$$ to $$[0,\infty)$$.
:::

### Restricting a domain

A function that is not injective on its full domain may become injective after the domain is restricted. The restriction must remove every repeated output, not just some of them.

<div class="theorem-box">

**Example.** Let

$$
f:[\pi,2\pi]\to[-1,1]
$$

be defined by $$f(x)=\cos x$$. Determine whether $$f$$ is bijective.

On the interval $$[\pi,2\pi]$$, cosine increases from $$-1$$ to $$1$$ without reversing direction. Therefore, no horizontal line meets this part of the graph more than once, so $$f$$ is injective.

Every value between $$-1$$ and $$1$$ occurs as cosine moves continuously from $$-1$$ to $$1$$. Thus,

$$
\operatorname{im}(f)=[-1,1],
$$

which equals the codomain. The function is also surjective, so it is bijective.

</div>

Restricting the domain carelessly may not work. For example, $$x^2$$ is still not injective on

$$
(-\infty,-1)\cup(1,\infty)
$$

because both $$x$$ and $$-x$$ remain in the domain whenever $$\lvert x\rvert>1$$. A restriction makes a function injective only if each output is left with at most one input.

:::strategy
When classifying a function:

1. Check that the rule is well-defined on the stated domain.
2. Look for a collision to test injectivity. If none is obvious, assume equal outputs and solve.
3. Compare the image with the codomain to test surjectivity. Equivalently, choose an arbitrary target and solve for an input.
4. Call the function bijective only after both separate checks succeed.
:::

:::summary{title="The basic function picture"}
A function consists of a rule, a domain, and a codomain. Well-definedness asks whether every allowed input has one unambiguous output. Injectivity asks whether outputs identify their inputs uniquely, while surjectivity asks whether the function reaches its whole codomain. These distinctions become the language for kernels, images, isomorphisms, and invertible matrices later in linear algebra.
:::
