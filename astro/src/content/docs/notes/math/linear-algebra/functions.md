---
title: "Unit 2: Functions"
sidebar:
  order: 2
---

## Functions, Domains, and Codomains

<div class="theorem-box">

**Definition.** A **function** $$f:A\to B$$ assigns each element of the input set $$A$$ to exactly one element of the output set $$B$$. The set $$A$$ is the **domain**, and the set $$B$$ is the **codomain**.

</div>

The expression $$f(x)$$ is the output assigned to the input $$x$$. The set of outputs the function actually reaches is its **image** or **range**:

$$
\operatorname{im}(f)=\{f(x)\mid x\in A\}\subseteq B.
$$

The codomain is part of the function's definition. Two rules with the same formula but different domains or codomains are different functions.

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

---

## Well-Defined Functions

A proposed function must give one unambiguous output for every input in its domain. This can fail when one input has several representations and the rule depends on the chosen representation.

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

One input would have two outputs, so the rule is not well-defined. Requiring $$a/b$$ to be in lowest terms would remove this particular ambiguity.

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

---

## Injective, Surjective, and Bijective Functions

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

For a real-valued graph, injectivity is checked by the horizontal line test: every horizontal line may intersect the graph at most once.

<div class="theorem-box">

**Definition.** A function $$f:A\to B$$ is **surjective** or **onto** if every element of the codomain is reached:

$$
\forall b\in B,\ \exists a\in A\text{ such that }f(a)=b.
$$

</div>

A function that is both injective and surjective is **bijective**. A bijection pairs every input with exactly one output and reaches every element of the codomain.

:::tip
To prove injectivity, start by assuming $$f(a_1)=f(a_2)$$ and work toward $$a_1=a_2$$. To prove surjectivity, begin with an arbitrary $$b$$ in the codomain and solve $$f(a)=b$$ for an input $$a$$ in the domain.
:::

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

