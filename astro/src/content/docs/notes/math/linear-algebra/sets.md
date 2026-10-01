---
title: "Unit 1: Sets"
description: "Linear algebra preliminaries on set notation, number systems, logic, set operations, relations, proof methods, and induction."
sidebar:
  order: 1
---

## Sets and Notation

<div class="theorem-box">

**Definition.** A **set** is a collection of objects. The objects in the set are called its **elements** or **members**. Order does not matter, and repeating an element does not change the set.

We use capital letters to denote sets, and lowercase elements to denote their elements. The statement $$a\in A$$ means that $$a$$ is an element of $$A$$. If $$a$$ is not an element of $$A$$, write $$a\notin A$$. For a finite set, $$\lvert A\rvert$$ is the number of distinct elements in $$A$$, also known as the size or cardinality.

</div>

Sets ignore both order and repetition. For example,

$$
\{1,2,3\}=\{3,2,1\}=\{1,1,2,3,3\}.
$$

All three expressions describe the same set because they have exactly the same members. Each set still has cardinality $$3$$ (including the last set).

The **empty set**, written $$\varnothing$$ or $$\{\}$$, is defined as a set with no elements. A **singleton** is a set that has exactly one element. If you have nested sets (a set within a set), you count that set as one element. For example,

$$
\lvert\varnothing\rvert=0,
\qquad
\lvert\{\varnothing\}\rvert=1.
$$

Note that the second set is not empty (Its one element is $$\varnothing$$ (the empty set)) and thus has a cardinality of $$1$$.

// add the universal set here

There are two common ways to describe a set:

- **Roster notation** lists the elements: $$A=\{1,4,7\}$$.
- **Set-builder notation** describes a property the elements satisfy: $$A=\{x\in\mathbb Z\mid 1\leq x\leq 7\text{ and }x\text{ is odd}\}$$.

The symbol $$\mid$$ in set-builder notation means “such that.” The expression before it gives the form of an element, and the condition after it decides whether that element belongs to the set.

Roster notation is most useful when the list is short or follows an unmistakable pattern. Set-builder notation is better when the membership rule is more important than the list itself. For instance,

$$
\{m\in\mathbb Z\mid mn=60\text{ for some }n\in\mathbb Z\}
$$

is the set of all integer divisors of $$60$$ ($$\mathbb Z$$ means the set of integers). In roster form, the same set is

$$
\{-60,-30,-20,-15,-12,-10,-6,-5,-4,-3,-2,-1,
1,2,3,4,5,6,10,12,15,20,30,60\}.
$$

// this list goes off the page, please change to a smaller number so the list is smaller

// add subset notation somewhere above because you list it below in laters sections but don't introduce it here

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

In set theory, we use many standard number systems.

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

The definition basically means that a well-defined set is very precise so that the values in the set can be determined with no ambiguity, regardless of how difficult it is to actual list out all of the values in the set. The set of prime numbers larger than one million is well-defined; the set of “large numbers” is not unless *large* is given a precise meaning.

There is also a difference between a difficult membership test and a flawed definition. Consider

$$
A=\{n\in\mathbb N\mid n\text{ appears somewhere in the decimal expansion of }\pi\}.
$$

For a very long value of $$n$$, checking membership may be practically impossible. Still, that string either appears or does not appear, so the set is well-defined. By contrast,

$$
B=\{q\in\mathbb Q\mid q\text{ has denominator greater than }100\}
$$

is ambiguous unless a particular representation is specified. The same rational number has many denominators:

$$
\frac12=\frac{51}{102}.
$$

The description would place $$1/2$$ both outside and inside $$B$$ depending on how it is written. Requiring lowest terms with a positive denominator would make the condition precise.

:::tip
When reading set-builder notation, test one candidate at a time: identify the candidate's allowed type, then check every condition after $$\mid$$. This is often clearer than trying to picture the entire set at once.
:::

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

One way to understand this is to treat a conditional as a promise: “whenever $$p$$ happens, $$q$$ happens.” The promise is broken only if $$p$$ happens without $$q$$. If $$p$$ never happens, there is no counterexample to the promise. This convention is what makes statements such as

$$
x\in\varnothing\Rightarrow x\in A
$$

true for every set $$A$$. There is no element of $$\varnothing$$ that could violate the implication, so $$\varnothing\subseteq A$$ for every set $$A$$.

When doing logic problems, we often write out the statements using a truth table:

| $$p$$ | $$q$$ | $$p\land q$$ | $$p\lor q$$ | $$p\Rightarrow q$$ | $$p\Leftrightarrow q$$ |
|---|---|---|---|---|---|
| T | T | T | T | T | T |
| T | F | F | T | F | F |
| F | T | F | T | T | F |
| F | F | F | F | T | T |

Here, “or” is inclusive: $$p\lor q$$ is true when one statement is true or when both are true.

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

// write this out in a theorem (De Morgan's laws) and a definition (converse, inverse, contrapositive)
:::

The statement $$q\Rightarrow p$$ is the **converse** of $$p\Rightarrow q$$. The statement $$\neg p\Rightarrow\neg q$$ is its **inverse**. Neither is automatically equivalent to the original conditional. The **contrapositive**, $$\neg q\Rightarrow\neg p$$, is equivalent.

<div class="theorem-box">

**Example.** Let $$p$$ be the statement “an integer is divisible by $$4$$” and let $$q$$ be the statement “the integer is even.” Write the conditional, converse, inverse, and contrapositive, and decide which are true.

The original conditional is

$$
p\Rightarrow q:
\quad
\text{if an integer is divisible by }4,\text{ then it is even}.
$$

This is true. Its contrapositive is also true:

$$
\neg q\Rightarrow\neg p:
\quad
\text{if an integer is odd, then it is not divisible by }4.
$$

The converse says that every even integer is divisible by $$4$$, which is false because $$2$$ is even but not divisible by $$4$$. The inverse is false for the same reason: $$2$$ is not divisible by $$4$$, but it is even.

</div>

The symbol $$\forall$$ means “for every,” while $$\exists$$ means “there exists.” If $$P(x)$$ is a property of elements in a domain $$D$$, then

$$
\forall x\in D,\ P(x)
$$

claims that every element of $$D$$ has the property, while

$$
\exists x\in D\text{ such that }P(x)
$$

claims that at least one does.

The order of quantifiers changes the meaning. Compare

$$
\forall x\in\mathbb R,\ \exists y\in\mathbb R\text{ such that }x+y=0
$$

with

$$
\exists y\in\mathbb R\text{ such that }\forall x\in\mathbb R,\ x+y=0.
$$

The first statement is true: after $$x$$ is chosen, take $$y=-x$$. The second is false because it asks for one fixed number $$y$$ that cancels every real number at once. In the first statement, $$y$$ may depend on $$x$$; in the second, it may not.

// put this notation in the first section (the notation of "for every", "there exists")

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

<div class="theorem-box">

**Example.** Negate the statement “every real number has a real square root.”

Write the statement as

$$
\forall x\in\mathbb R,\ \exists y\in\mathbb R\text{ such that }y^2=x.
$$

Switch each quantifier and negate the final property:

$$
\exists x\in\mathbb R\text{ such that }\forall y\in\mathbb R,\ y^2\neq x.
$$

In words, “there is a real number that is not the square of any real number.” This negation is true; $$x=-1$$ is a counterexample to the original statement.

</div>

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

// put this in the first section

// add a better intro after moving the set operations

These operations are set versions of the logical operations above. Membership in a union uses “or,” membership in an intersection uses “and,” and membership in a complement uses “not”:

$$
x\in A\cup B\Longleftrightarrow (x\in A)\lor(x\in B),
$$

$$
x\in A\cap B\Longleftrightarrow (x\in A)\land(x\in B),
$$

$$
x\in A^c\Longleftrightarrow \neg(x\in A).
$$

This translation is why logical identities turn into set identities. De Morgan's law for propositions and De Morgan's law for sets are the same pattern written in two languages.

The **set difference** $$B\setminus A$$ contains the elements of $$B$$ that are not in $$A$$:

$$
B\setminus A=B\cap A^c.
$$

Unlike union and intersection, set difference is not symmetric. Usually,

$$
B\setminus A\neq A\setminus B.
$$

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

### Cartesian products

An element of $$A\times B$$ is an **ordered pair**, so position matters. If

$$
A=\{1,2\}
\qquad\text{and}\qquad
B=\{x,y\},
$$

then

$$
A\times B=\{(1,x),(1,y),(2,x),(2,y)\}.
$$

The first coordinate must come from $$A$$ and the second from $$B$$. Consequently, $$A\times B$$ and $$B\times A$$ usually contain different objects. For finite sets,

$$
\lvert A\times B\rvert=\lvert A\rvert\lvert B\rvert,
$$

because each of the $$\lvert A\rvert$$ choices for the first coordinate can be paired with each of the $$\lvert B\rvert$$ choices for the second.

Cartesian products become important immediately in linear algebra. For example,

$$
\mathbb R^2=\mathbb R\times\mathbb R
$$

is the set of all ordered pairs $$(x,y)$$, while $$\mathbb R^3$$ is the set of all ordered triples. A point, a vector, and a list of coordinates can all be viewed as elements of a Cartesian product.

:::warning
The ordered pair $$(a,b)$$ is generally not the same as $$(b,a)$$. Sets ignore order among their elements; ordered pairs do not ignore the order of their coordinates.
:::

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

Membership and containment are different kinds of statements. If

$$
A=\{1,2,3\},
$$

then $$1\in A$$, but $$1\subseteq A$$ makes no sense unless $$1$$ has separately been defined as a set. On the other hand, $$\{1\}\subseteq A$$, but $$\{1\}\notin A$$ because the members of $$A$$ are numbers, not singleton sets.

A **superset** statement reverses the same relationship:

$$
A\supseteq B\quad\Longleftrightarrow\quad B\subseteq A.
$$

Containment is transitive. If every element of $$A$$ lies in $$B$$ and every element of $$B$$ lies in $$C$$, then every element of $$A$$ must lie in $$C$$.

<div class="theorem-box">

**Proof (Transitivity of subsets).** Suppose $$A\subseteq B$$ and $$B\subseteq C$$. Let $$x\in A$$. Since $$A\subseteq B$$, we have $$x\in B$$. Since $$B\subseteq C$$, this gives $$x\in C$$. Therefore, every element of $$A$$ belongs to $$C$$, so

$$
A\subseteq C.
$$

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

**Proof (Cartesian product distributes over union).** We prove

$$
(A\cup B)\times C=(A\times C)\cup(B\times C).
$$

Let $$(x,y)\in(A\cup B)\times C$$. Then $$x\in A\cup B$$ and $$y\in C$$. The first statement means $$x\in A$$ or $$x\in B$$. Therefore, either $$(x,y)\in A\times C$$ or $$(x,y)\in B\times C$$, so

$$
(x,y)\in(A\times C)\cup(B\times C).
$$

This proves the forward containment. For the reverse, let

$$
(x,y)\in(A\times C)\cup(B\times C).
$$

Then $$(x,y)$$ lies in at least one of the two products. In either case, $$x\in A\cup B$$ and $$y\in C$$. Hence, $$(x,y)\in(A\cup B)\times C$$. The two containments prove the sets are equal.

</div>

<div class="theorem-box">

**Proof (Symmetric difference detects equality).** We prove that

$$
A\mathbin{\triangle}B=\varnothing
\quad\Longleftrightarrow\quad
A=B.
$$

Suppose $$A\mathbin{\triangle}B=\varnothing$$. If some element belonged to $$A$$ but not $$B$$, or to $$B$$ but not $$A$$, it would belong to the symmetric difference. Since the symmetric difference is empty, neither kind of mismatch exists. Thus, $$A$$ and $$B$$ have exactly the same elements, so $$A=B$$.

Conversely, if $$A=B$$, no element can belong to exactly one of the sets. Therefore, their symmetric difference has no elements:

$$
A\mathbin{\triangle}B=\varnothing.
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

<div class="theorem-box">

**Example.** Decide which of the following objects belong to $$M_{2\times3}(\mathbb R)$$:

$$
P=\begin{bmatrix}1&0&-2\\3&\pi&5\end{bmatrix},
\qquad
Q=\begin{bmatrix}1&2\\3&4\\5&6\end{bmatrix},
\qquad
R=\begin{bmatrix}1&0&i\\2&3&4\end{bmatrix}.
$$

The matrix $$P$$ has two rows, three columns, and only real entries, so

$$
P\in M_{2\times3}(\mathbb R).
$$

The matrix $$Q$$ has the wrong shape: it is $$3\times2$$. The matrix $$R$$ has the correct shape, but $$i\notin\mathbb R$$. Therefore,

$$
Q,R\notin M_{2\times3}(\mathbb R).
$$

This example shows how a complicated-looking set-builder definition becomes a checklist for membership: check the dimensions, then check every entry.

</div>

---

## Proof Methods

A proof is not just a calculation that ends at the right formula. It is a chain of statements in which each step follows from a definition, an assumption, or an earlier result. The form of the claim usually suggests the proof method.

- For a universal statement, begin with an arbitrary object satisfying the hypothesis.
- For an existence statement, construct one object and verify it works.
- For a set equality, prove both containments.
- For an implication, try a direct proof or its contrapositive.
- If the negation forces an impossibility, use contradiction.
- If the statement is indexed by natural numbers, induction may connect one case to the next.

### Direct proof and contrapositive

A direct proof of $$p\Rightarrow q$$ assumes $$p$$ and logically derives $$q$$. A contrapositive proof instead assumes $$\neg q$$ and derives $$\neg p$$.

The contrapositive is useful when the conclusion contains a condition that is easier to negate. For example, it is awkward to prove directly that $$n^2$$ even implies $$n$$ even. Its contrapositive says that if $$n$$ is odd, then $$n^2$$ is odd, which follows immediately by writing $$n=2k+1$$.

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

The key is that the inductive hypothesis is not a guess that every case is true. It temporarily grants one case, $$P(k)$$, so that the proof can establish the link

$$
P(k)\Rightarrow P(k+1).
$$

The base case starts the chain. The inductive step then carries truth from the base case to the next case, and from there to every later case. Without the base case, the implication alone proves nothing: a row of standing dominoes never falls unless the first one is pushed.

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

### Strong induction

In **strong induction**, the inductive hypothesis assumes all earlier cases through $$k$$:

$$
P(1),P(2),\ldots,P(k).
$$

The goal is still to prove $$P(k+1)$$. Strong induction is useful when the next case depends on more than one earlier case, or when it breaks into a smaller value that may not be exactly $$k$$.

<div class="theorem-box">

**Proof (Prime factorization exists).** We prove that every integer $$n\geq2$$ is prime or can be written as a product of primes.

The base case $$n=2$$ is prime. Now assume every integer from $$2$$ through $$k$$ is prime or a product of primes. Consider $$k+1$$.

If $$k+1$$ is prime, the claim is already true. If it is composite, then

$$
k+1=ab
$$

for integers $$a,b$$ satisfying

$$
2\leq a,b\leq k.
$$

By the strong inductive hypothesis, each of $$a$$ and $$b$$ is prime or a product of primes. Multiplying those factorizations gives a prime factorization of $$k+1$$. Therefore, every integer $$n\geq2$$ is prime or a product of primes.

</div>

:::summary{title="Unit 1 ideas"}
Sets turn mathematical objects into collections with precise membership rules. Logic tells us how those rules combine, and proof methods let us justify relationships between the resulting sets. These same habits carry into the rest of linear algebra: vectors, matrices, and functions are all introduced as carefully defined sets before we study what can be done with them.
:::
