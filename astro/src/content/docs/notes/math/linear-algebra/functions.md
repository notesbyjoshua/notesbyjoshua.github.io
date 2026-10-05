---
title: "Unit 2: Functions"
description: "Linear algebra notes on functions, domains, images, well-defined rules, bijections, composition, inverses, preimages, and function operators."
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

Images behave predictably with unions. If $$S_1,S_2\subseteq A$$, then

$$
f(S_1\cup S_2)=f(S_1)\cup f(S_2).
$$

An output is on the left exactly when it comes from an input in $$S_1$$ or an input in $$S_2$$, which is exactly what the right side says.

For intersections, only one direction is always guaranteed:

$$
f(S_1\cap S_2)\subseteq f(S_1)\cap f(S_2).
$$

If an input belongs to both sets, its output certainly belongs to both images. The reverse direction can fail because two different inputs may produce the same output.

<div class="theorem-box">

**Example.** Let $$f:\mathbb R\to\mathbb R$$ be given by $$f(x)=x^2$$, and set

$$
S_1=\{-1,0\},
\qquad
S_2=\{0,1\}.
$$

Their intersection is $$S_1\cap S_2=\{0\}$$, so

$$
f(S_1\cap S_2)=\{0\}.
$$

However,

$$
f(S_1)=f(S_2)=\{0,1\},
$$

and therefore

$$
f(S_1)\cap f(S_2)=\{0,1\}.
$$

The output $$1$$ belongs to both images, but it comes from $$-1$$ in the first set and $$1$$ in the second. There is no common input producing it. If $$f$$ is injective, this kind of collision cannot happen, and equality does hold for intersections.

</div>

### Functions as sets of ordered pairs

There is also a formal set-based definition of a function. A function $$f:A\to B$$ is a subset of the Cartesian product $$A\times B$$ in which every element of $$A$$ appears exactly once as a first coordinate. The ordered pair $$(a,b)$$ means that $$f(a)=b$$.

This definition captures both requirements at once: every input must appear, and it must appear with only one output. A general subset of $$A\times B$$ is called a **relation**. A relation becomes a function only when it satisfies the exactly-one-output condition.

<div class="theorem-box">

**Example.** Let $$A=\{1,2,3\}$$ and $$B=\{2,3,4\}$$. The relation $$R$$ defined by $$a\leq b$$ is

$$
R=\{(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3),(3,4)\}.
$$

This relation is not a function from $$A$$ to $$B$$. The input $$1$$ appears with three different second coordinates, so it would have three outputs. By contrast, the identity function on $$A$$ lives in $$A\times A$$ and is the set

$$
\operatorname{id}_A=\{(1,1),(2,2),(3,3)\},
$$

where each input appears exactly once.

</div>

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

---

## Function Composition

Functions can be connected so that the output of one becomes the input of another. If

$$
f:A\to B
\qquad\text{and}\qquad
g:B\to C,
$$

then the **composition of $$g$$ with $$f$$** is the function

$$
g\circ f:A\to C
$$

defined by

$$
(g\circ f)(a)=g(f(a)).
$$

The rightmost function acts first: begin with $$a$$, apply $$f$$, and then apply $$g$$ to the result. The codomain of $$f$$ must fit the domain of $$g$$ so that the second step is meaningful.

:::tip
Read $$g\circ f$$ from right to left. The notation records the order in which the functions act, not the order in which their names are spoken.
:::

<div class="theorem-box">

**Example.** Let $$f,g:\mathbb R\to\mathbb R$$ be defined by

$$
f(x)=x^3+1
\qquad\text{and}\qquad
g(x)=x^3.
$$

For $$f\circ g$$, apply $$g$$ first:

$$
(f\circ g)(x)=f(x^3)=(x^3)^3+1=x^9+1.
$$

For $$g\circ f$$, apply $$f$$ first:

$$
(g\circ f)(x)=g(x^3+1)=(x^3+1)^3
=x^9+3x^6+3x^3+1.
$$

The two compositions are different. For instance,

$$
(f\circ g)(1)=2,
\qquad
(g\circ f)(1)=8.
$$

Thus, function composition is generally **not commutative**: changing the order can change the result.

</div>

Although composition is not usually commutative, it is associative.

<div class="theorem-box">

**Proof (Associativity of function composition).** Suppose

$$
f:A\to B,
\qquad
g:B\to C,
\qquad
h:C\to D.
$$

For every $$a\in A$$,

$$
\bigl(h\circ(g\circ f)\bigr)(a)
=h\bigl((g\circ f)(a)\bigr)
=h(g(f(a))).
$$

On the other hand,

$$
\bigl((h\circ g)\circ f\bigr)(a)
=(h\circ g)(f(a))
=h(g(f(a))).
$$

The two functions have the same domain, codomain, and output at every input, so

$$
h\circ(g\circ f)=(h\circ g)\circ f.
$$

</div>

The identity function behaves like doing nothing before or after a function:

$$
f\circ\operatorname{id}_A=f,
\qquad
\operatorname{id}_B\circ f=f
$$

for every $$f:A\to B$$. Also, the composition of two bijections is again a bijection, so several reversible steps can be joined into one reversible process.

---

## Inverse Functions

An inverse function reverses another function. If $$f:A\to B$$, an **inverse** of $$f$$ is a function $$g:B\to A$$ satisfying both

$$
f\circ g=\operatorname{id}_B
$$

and

$$
g\circ f=\operatorname{id}_A.
$$

The first identity says that starting in $$B$$, moving backward with $$g$$, and then forward with $$f$$ returns to the original element. The second says the same thing for an element that starts in $$A$$. When an inverse exists, it is unique and is written $$f^{-1}$$.

<div class="theorem-box">

**Theorem.** A function is invertible if and only if it is bijective.

**Proof.** First suppose $$f:A\to B$$ has an inverse $$g:B\to A$$. If $$f(a_1)=f(a_2)$$, applying $$g$$ gives

$$
g(f(a_1))=g(f(a_2)),
$$

so $$a_1=a_2$$. Thus, $$f$$ is injective. For any $$b\in B$$, choose $$a=g(b)$$. Then

$$
f(a)=f(g(b))=b,
$$

so $$f$$ is surjective.

Conversely, suppose $$f$$ is bijective. For each $$b\in B$$, surjectivity guarantees at least one $$a\in A$$ with $$f(a)=b$$, and injectivity guarantees that this $$a$$ is unique. Define $$g(b)$$ to be that unique input. Then $$f\circ g=\operatorname{id}_B$$ and $$g\circ f=\operatorname{id}_A$$, so $$g=f^{-1}$$.

</div>

This theorem explains both possible failures of reversibility. If a function is not injective, one output does not reveal which input produced it. If it is not surjective, some element of the codomain has no input to return to.

<div class="theorem-box">

**Example.** The bijection $$f:\mathbb Q\to\mathbb Q$$ defined by

$$
f(q)=3q+2
$$

has an inverse. To find it, set $$y=3q+2$$ and solve for $$q$$:

$$
q=\frac{y-2}{3}.
$$

Therefore,

$$
f^{-1}(y)=\frac{y-2}{3}.
$$

Checking both directions gives

$$
f\left(f^{-1}(y)\right)
=3\left(\frac{y-2}{3}\right)+2
=y
$$

and

$$
f^{-1}(f(q))
=\frac{(3q+2)-2}{3}
=q.
$$

</div>

The squaring rule on all of $$\mathbb R$$ has no inverse because it is not injective. After restricting it to

$$
h:[0,\infty)\to[0,\infty),
\qquad
h(x)=x^2,
$$

it becomes bijective, and its inverse is

$$
h^{-1}(y)=\sqrt y.
$$

The domain restriction is not a technical detail: it is what makes each nonnegative output point back to exactly one input.

### Preimages of sets

The notation $$f^{-1}(T)$$ is also used for the **preimage** of a subset $$T\subseteq B$$:

$$
f^{-1}(T)=\{a\in A\mid f(a)\in T\}.
$$

A preimage asks which inputs land inside a chosen set of outputs. It exists for every function; $$f$$ does not need to be invertible. The context makes clear whether $$f^{-1}$$ means an inverse function or the preimage operation on sets.

Preimages preserve both unions and intersections exactly:

$$
f^{-1}(T_1\cup T_2)=f^{-1}(T_1)\cup f^{-1}(T_2)
$$

and

$$
f^{-1}(T_1\cap T_2)=f^{-1}(T_1)\cap f^{-1}(T_2).
$$

There is no injectivity requirement here. A single input has only one output, so checking whether that output belongs to both target sets creates no ambiguity.

<div class="theorem-box">

**Example.** Let $$f:\mathbb R\to\mathbb R$$ be defined by $$f(x)=x^2$$. Find the preimage of $$[1,4]$$.

We need all real inputs whose squares lie between $$1$$ and $$4$$:

$$
1\leq x^2\leq 4.
$$

This occurs when $$1\leq\lvert x\rvert\leq 2$$, so

$$
f^{-1}([1,4])=[-2,-1]\cup[1,2].
$$

The function itself is not invertible on $$\mathbb R$$, but the preimage of a set is still perfectly well-defined.

</div>

---

## Functions Beyond Real-Valued Formulas

Many important functions in linear algebra take vectors, matrices, or even other functions as inputs. What matters is not whether there is a familiar algebraic formula, but whether every allowed input receives exactly one output in the stated codomain.

<div class="theorem-box">

**Example.** Let $$\mathbb R[x]$$ be the set of polynomials with real coefficients, and define the derivative operator

$$
D:\mathbb R[x]\to\mathbb R[x],
\qquad
D(p)=p'.
$$

This function is not injective because different polynomials can have the same derivative. For example,

$$
D(x^2)=2x=D(x^2+1).
$$

It is surjective. If

$$
q(x)=\sum_{k=0}^{n}a_kx^k,
$$

then the polynomial

$$
p(x)=\sum_{k=0}^{n}\frac{a_k}{k+1}x^{k+1}
$$

satisfies $$D(p)=q$$. In other words, every polynomial has a polynomial antiderivative.

If the domain is restricted to polynomials satisfying $$p(0)=1$$, the arbitrary constant is fixed. On that restricted domain, differentiation becomes bijective, with inverse

$$
D^{-1}(q)(x)=1+\int_0^x q(t)\,dt.
$$

</div>

<div class="theorem-box">

**Example.** Define $$m:\mathbb R^2\to\mathbb R$$ by

$$
m(x,y)=xy.
$$

This function is not injective because, for example,

$$
m(1,2)=m(2,1)=2.
$$

It is surjective because any real number $$r$$ is the output of the input $$(r,1)$$:

$$
m(r,1)=r.
$$

This example also shows that having more input coordinates does not prevent a function from being onto a smaller-looking codomain.

</div>

<div class="theorem-box">

**Example.** The **trace** function sends a square matrix to the sum of its diagonal entries:

$$
\operatorname{Tr}:M_n(\mathbb R)\to\mathbb R,
\qquad
\operatorname{Tr}(A)=a_{11}+a_{22}+\cdots+a_{nn}.
$$

It is surjective: for any $$r\in\mathbb R$$, the diagonal matrix with first diagonal entry $$r$$ and all other entries $$0$$ has trace $$r$$.

It is not injective because many matrices have the same trace. For example, when $$n=2$$,

$$
\operatorname{Tr}\begin{pmatrix}1&0\\0&0\end{pmatrix}
=1
=\operatorname{Tr}\begin{pmatrix}0&0\\0&1\end{pmatrix}.
$$

Trace keeps one useful number while discarding most of the information in the matrix. This is a common theme: a function can compress a complicated object into a simpler output without being reversible.

</div>

:::equations
| Idea | Formula |
|---|---|
| Image of a subset | $$f(S)=\{f(a)\mid a\in S\}$$ |
| Image of a union | $$f(S_1\cup S_2)=f(S_1)\cup f(S_2)$$ |
| Image of an intersection | $$f(S_1\cap S_2)\subseteq f(S_1)\cap f(S_2)$$ |
| Composition | $$(g\circ f)(a)=g(f(a))$$ |
| Associativity | $$h\circ(g\circ f)=(h\circ g)\circ f$$ |
| Inverse identities | $$f\circ f^{-1}=\operatorname{id}_B$$ and $$f^{-1}\circ f=\operatorname{id}_A$$ |
| Preimage of a subset | $$f^{-1}(T)=\{a\in A\mid f(a)\in T\}$$ |
:::

:::summary{title="The basic function picture"}
A function consists of a rule, a domain, and a codomain. Well-definedness asks whether every allowed input has one unambiguous output. Injectivity prevents collisions, while surjectivity guarantees that the whole codomain is reached. Composition connects functions, and a function can be reversed exactly when it is bijective. These ideas apply just as naturally to polynomials and matrices as they do to real-number formulas, which is why they become the language for kernels, images, isomorphisms, and invertible matrices later in linear algebra.
:::
