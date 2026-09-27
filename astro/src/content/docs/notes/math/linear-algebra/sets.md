---
title: "Unit 1: Sets"
description: "Linear algebra preliminaries on set notation, number systems, logic, set operations, relations, proof methods, and induction."
sidebar:
  order: 1
---

## Sets and Notation

<div class="theorem-box">

**Definition.** A **set** is a collection of objects. The objects in the set are called its **elements** or **members**. Order does not matter, and repeating an element does not change the set.

</div>

Capital letters usually name sets, while lowercase letters name their elements. The statement

$$
a\in A
$$

means that $$a$$ is an element of $$A$$. If $$a$$ is not an element of $$A$$, write $$a\notin A$$. For a finite set, $$\lvert A\rvert$$ is the number of distinct elements in $$A$$.

There are two common ways to describe a set:

- **Roster notation** lists the elements: $$A=\{1,4,7\}$$.
- **Set-builder notation** describes a property the elements satisfy: $$A=\{x\in\mathbb Z\mid 1\leq x\leq 7\text{ and }x\text{ is odd}\}$$.

The symbol $$\mid$$ in set-builder notation means “such that.” The expression before it gives the form of an element, and the condition after it decides whether that element belongs to the set.

<div class="theorem-box">

**Example.** Rewrite $$A=\{x\in\mathbb Z\mid x^2<10\}$$ using roster notation.

The integers whose squares are less than $$10$$ are $$-3,-2,-1,0,1,2,3$$. Therefore,

$$
A=\{-3,-2,-1,0,1,2,3\}.
$$

</div>

:::warning
The braces describe one set. For example, $$\{1,2\}$$ is a set with two elements, while $$\{\{1,2\}\}$$ is a set with one element—the set $$\{1,2\}$$.
:::

### Important number sets

The standard number systems are

$$
\mathbb N=\{1,2,3,\ldots\},
$$

$$
\mathbb Z=\{\ldots,-2,-1,0,1,2,\ldots\},
$$

$$
\mathbb Q=\left\{\frac{a}{b}\mid a,b\in\mathbb Z,\ b\neq0\right\},
$$

$$
\mathbb R=\{\text{real numbers}\},
$$

and

$$
\mathbb C=\{a+bi\mid a,b\in\mathbb R,\ i^2=-1\}.
$$

They satisfy

$$
\mathbb N\subseteq\mathbb Z\subseteq\mathbb Q\subseteq\mathbb R\subseteq\mathbb C.
$$

<div class="theorem-box">

**Definition.** A set is **well-defined** if every object either belongs to the set or does not belong to it, but not both.

</div>

The definition does not need to make membership easy to check. It only needs to make membership unambiguous. The set of prime numbers larger than one million is well-defined; the set of “large numbers” is not unless *large* is given a precise meaning.

---

## Logic and Quantifiers

Set-builder notation and proofs both rely on statements that can be true or false.

<div class="theorem-box">

**Definition.** A **proposition** is a declarative statement with exactly one truth value: true or false.

</div>

For propositions $$p$$ and $$q$$, the main logical operations are:

| Operation | Notation | Meaning |
|---|---|---|
| Negation | $$\neg p$$ | not $$p$$ |
| Conjunction | $$p\land q$$ | $$p$$ and $$q$$ |
| Disjunction | $$p\lor q$$ | $$p$$ or $$q$$, inclusively |
| Conditional | $$p\Rightarrow q$$ | if $$p$$, then $$q$$ |
| Biconditional | $$p\Leftrightarrow q$$ | $$p$$ if and only if $$q$$ |

A conditional is false only when its hypothesis is true and its conclusion is false. In particular, if $$p$$ is false, then $$p\Rightarrow q$$ is true regardless of $$q$$; this is called **vacuous truth**.

:::key{name="Logical equivalences"}
The identities used most often in proofs are

$$
p\Rightarrow q\equiv\neg p\lor q,
$$

$$
p\Rightarrow q\equiv\neg q\Rightarrow\neg p,
$$

and De Morgan's laws

$$
\neg(p\lor q)\equiv\neg p\land\neg q,
\qquad
\neg(p\land q)\equiv\neg p\lor\neg q.
$$
:::

The statement $$q\Rightarrow p$$ is the **converse** of $$p\Rightarrow q$$. The statement $$\neg p\Rightarrow\neg q$$ is its **inverse**. Neither is automatically equivalent to the original conditional. The **contrapositive**, $$\neg q\Rightarrow\neg p$$, is equivalent.

### First-order logic

The symbol $$\forall$$ means “for every,” while $$\exists$$ means “there exists.” If $$P(x)$$ is a property of elements in a domain $$D$$, then

$$
\forall x\in D,\ P(x)
$$

claims that every element of $$D$$ has the property, while

$$
\exists x\in D\text{ such that }P(x)
$$

claims that at least one does.

Negating a quantified statement switches the quantifier:

$$
\neg\left(\forall x\in D,\ P(x)\right)
\equiv
\exists x\in D\text{ such that }\neg P(x),
$$

$$
\neg\left(\exists x\in D\text{ such that }P(x)\right)
\equiv
\forall x\in D,\ \neg P(x).
$$

:::tip
To disprove a universal statement, one counterexample is enough. To prove an existence statement, give one object and verify that it has the required property.
:::

---

## Set Operations

Let $$A$$ and $$B$$ be subsets of a universal set $$U$$.

<div class="theorem-box">

**Definition.** The main set operations are

$$
A\cup B=\{x\mid x\in A\text{ or }x\in B\},
$$

$$
A\cap B=\{x\mid x\in A\text{ and }x\in B\},
$$

$$
A\times B=\{(a,b)\mid a\in A\text{ and }b\in B\},
$$

$$
A^c=\{x\in U\mid x\notin A\},
$$

and the **symmetric difference**

$$
A\mathbin{\triangle}B=(A\cap B^c)\cup(A^c\cap B).
$$

</div>

The union contains elements in at least one set. The intersection contains elements shared by both. The symmetric difference contains elements in exactly one of the two sets.

<div class="theorem-box">

**Example.** Let $$U=\{1,2,3,4,5,6\}$$, $$A=\{1,2,3\}$$, and $$B=\{2,3,4\}$$. Find $$A\cup B$$, $$A\cap B$$, $$A^c$$, and $$A\mathbin{\triangle}B$$.

Combining all distinct elements gives

$$
A\cup B=\{1,2,3,4\}.
$$

The shared elements are

$$
A\cap B=\{2,3\}.
$$

The elements of the universe outside $$A$$ are

$$
A^c=\{4,5,6\}.
$$

Finally, the elements belonging to exactly one set are

$$
A\mathbin{\triangle}B=\{1,4\}.
$$

</div>

:::warning
A complement depends on the universal set. If $$A=[0,1]$$, its complement is different when the universe is $$\mathbb R$$ than when the universe is $$[0,2]$$.
:::

---

## Relations Between Sets

<div class="theorem-box">

**Definition.** The set $$A$$ is a **subset** of $$B$$, written $$A\subseteq B$$, if every element of $$A$$ is also an element of $$B$$:

$$
A\subseteq B
\quad\Longleftrightarrow\quad
\forall x\,(x\in A\Rightarrow x\in B).
$$

If $$A\subseteq B$$ and $$A\neq B$$, then $$A$$ is a **proper subset** of $$B$$, written $$A\subsetneq B$$.

</div>

Set equality is proved by mutual containment:

$$
A=B
\quad\Longleftrightarrow\quad
A\subseteq B\text{ and }B\subseteq A.
$$

:::strategy
To prove two sets are equal, start with an arbitrary element of the first set and show it belongs to the second. Then reverse the argument. This avoids relying on a picture or an incomplete list of examples.
:::

<div class="theorem-box">

**Proof (De Morgan's Law for sets).** We prove

$$
(A\cup B)^c=A^c\cap B^c.
$$

Let $$x\in(A\cup B)^c$$. Then $$x\notin A\cup B$$, so $$x$$ is not in $$A$$ and is not in $$B$$. Therefore, $$x\in A^c\cap B^c$$, which proves

$$
(A\cup B)^c\subseteq A^c\cap B^c.
$$

Conversely, let $$x\in A^c\cap B^c$$. Then $$x\notin A$$ and $$x\notin B$$, so $$x\notin A\cup B$$. Thus, $$x\in(A\cup B)^c$$, proving the reverse containment. Therefore,

$$
(A\cup B)^c=A^c\cap B^c.
$$

</div>

<div class="theorem-box">

**Proof (A set described by squares).** Let

$$
A=\{x\in\mathbb R\mid x\geq0\}
$$

and

$$
B=\{z\in\mathbb R\mid \exists y\in\mathbb R\text{ such that }y^2=z\}.
$$

We prove $$A=B$$. If $$x\in A$$, then $$x\geq0$$, so $$\sqrt{x}\in\mathbb R$$ and $$(\sqrt{x})^2=x$$. Hence, $$x\in B$$, and therefore $$A\subseteq B$$.

If $$x\in B$$, then $$x=y^2$$ for some real number $$y$$. Every real square is nonnegative, so $$x\geq0$$ and $$x\in A$$. Therefore, $$B\subseteq A$$, and $$A=B$$.

</div>

---

## Common Sets in Linear Algebra

The objects studied in linear algebra are often collected into sets of their own. If $$A$$ is a set of allowed coefficients, then

$$
A[x]=\{a_nx^n+\cdots+a_1x+a_0\mid n\in\mathbb N,\ a_i\in A\}
$$

is the set of polynomials with coefficients in $$A$$. The notation

$$
A_n[x]=\{f(x)\in A[x]\mid \deg f<n\}
$$

restricts the degree.

The set of all $$m\times n$$ matrices with entries in $$A$$ is

$$
M_{m\times n}(A)
=
\left\{
\begin{bmatrix}
a_{11}&\cdots&a_{1n}\\
\vdots&\ddots&\vdots\\
a_{m1}&\cdots&a_{mn}
\end{bmatrix}
\mathrel{\mid}
a_{ij}\in A
\right\}.
$$

When $$m=n$$, this is often shortened to $$M_n(A)$$.

Another useful example is

$$
C^n(\mathbb R)=\{f:\mathbb R\to\mathbb R\mid f\text{ has continuous derivatives through order }n\}.
$$

These examples look different, but each is still just a set: membership is determined by a precise rule.

---

## Proof Methods

### Direct proof and contrapositive

A direct proof of $$p\Rightarrow q$$ assumes $$p$$ and logically derives $$q$$. A contrapositive proof instead assumes $$\neg q$$ and derives $$\neg p$$.

<div class="theorem-box">

**Proof (Divisibility of $$n^3-n$$).** Let $$n\in\mathbb N$$. Factor

$$
n^3-n=n(n-1)(n+1).
$$

These are three consecutive integers. At least one is even, so their product is divisible by $$2$$. One of every three consecutive integers is divisible by $$3$$, so the product is also divisible by $$3$$. Since $$2$$ and $$3$$ are relatively prime,

$$
6\mid(n^3-n).
$$

</div>

### Proof by contradiction

To prove a statement by contradiction, assume the statement is false and derive an impossibility.

<div class="theorem-box">

**Proof (There are infinitely many primes).** Suppose there were only finitely many primes, listed as

$$
p_1,p_2,\ldots,p_n.
$$

Consider

$$
N=p_1p_2\cdots p_n+1.
$$

No listed prime divides $$N$$, because division by any $$p_i$$ leaves remainder $$1$$. But every integer greater than $$1$$ is prime or has a prime factor. Therefore, $$N$$ has a prime factor not in the supposedly complete list, a contradiction. Thus, there are infinitely many primes.

</div>

### Mathematical induction

Induction proves a statement $$P(n)$$ for every natural number from a starting value onward.

1. Prove the base case.
2. Assume $$P(k)$$ is true for an arbitrary allowed $$k$$.
3. Use that assumption to prove $$P(k+1)$$.

<div class="theorem-box">

**Proof (Sum of the first $$n$$ squares).** We prove

$$
1^2+2^2+\cdots+n^2=\frac{n(n+1)(2n+1)}{6}
$$

for every $$n\in\mathbb N$$. For $$n=1$$, both sides equal $$1$$.

Assume the formula holds for some $$k\in\mathbb N$$. Then

$$
1^2+2^2+\cdots+k^2+(k+1)^2
=\frac{k(k+1)(2k+1)}{6}+(k+1)^2.
$$

Factor and simplify:

$$
\frac{k(k+1)(2k+1)+6(k+1)^2}{6}
=\frac{(k+1)(k+2)(2k+3)}{6}.
$$

This is exactly the claimed formula with $$n=k+1$$. Therefore, the formula holds for all $$n\in\mathbb N$$.

</div>

:::warning
In the inductive step, assume only $$P(k)$$. Assuming $$P(k+1)$$ would assume the very statement that still needs to be proved.
:::
