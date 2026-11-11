---
title: "Graph Theory"
status: developing
progress: 68
sidebar:
  order: 7
description: "Competition math notes on graph models, degrees, trees, connectivity, bipartite graphs, and extremal arguments with worked proof examples."
---

## Turning a Problem into a Graph

A **graph** consists of vertices and edges joining pairs of vertices. Vertices might represent people, cities, or objects; edges record a relation such as friendship or a direct connection.

Unless stated otherwise, use a finite **simple undirected graph**: no loops, no repeated edges, and no directions. Results about such graphs may change when those assumptions change.

A **complete graph** $$K_n$$ connects every pair of distinct vertices, so it has $$\binom n2$$ edges. A graph is **connected** if every pair of vertices can be joined by a path.

<div class="theorem-box">

**Example.** Eight teams each play every other team once. How many games are played?

Represent teams by vertices and games by edges. A game is an unordered pair of teams, so the graph is $$K_8$$ and has $$\binom82=28$$ edges. Counting eight opponents per team would incorrectly include self-play; counting seven per team would count each game twice.

</div>

---

## Degrees and the Handshake Lemma

The **degree** $$\deg(v)$$ is the number of edges incident to vertex $$v$$. Summing degrees counts each edge twice, once at each endpoint:

$$
\sum_v\deg(v)=2E,
$$

where $$E$$ is the number of edges. In particular, the number of odd-degree vertices is even, since an odd number of odd summands would make the sum odd.

<div class="theorem-box">

**Example.** Can a group of seven people each have shaken hands with exactly three others in the group?

The proposed degree sum is $$7\cdot3=21$$. But every handshake contributes two to that sum, so it must be even. Such a configuration is impossible.

</div>

Another useful consequence is that some degree is at least the average $$2E/V$$ and some is at most it. This provides a starting vertex for many extremal arguments.

---

## Paths, Cycles, and Trees

A **path** is a sequence of distinct vertices joined by edges. A **cycle** returns to its starting vertex, with at least three vertices and no other repeated vertices. A **tree** is a connected graph with no cycles.

A tree on $$V$$ vertices has $$V-1$$ edges. One proof repeatedly removes a **leaf**, a vertex of degree one. A longest path in a tree with at least two vertices has leaf endpoints: any extra neighbor would extend the path or create a cycle. Removing a leaf preserves the tree property and removes one vertex and one edge.

<div class="theorem-box">

**Example.** A tree has three vertices of degree three, some leaves, and no other vertices. Find the number of leaves.

Let there be $$L$$ leaves. The tree has $$L+3$$ vertices and $$L+2$$ edges. The degree sum gives

$$
L+3\cdot3=2(L+2),
$$

so $$L=5$$.

</div>

A connected graph with a cycle is not a tree, but it contains a **spanning tree**: repeatedly remove an edge from a cycle without disconnecting the graph. Thus any connected graph has at least $$V-1$$ edges.

---

## Bipartite Graphs and Coloring

A graph is **bipartite** if its vertices can be split into two groups so every edge runs between the groups. Equivalently, its vertices can be colored with two colors so adjacent vertices have different colors.

A bipartite graph contains no odd cycle because colors must alternate around a cycle. Conversely, a graph with no odd cycle is bipartite: in each component, color vertices according to the parity of their distance from a chosen starting vertex. An edge joining equal parities would produce an odd cycle.

<div class="theorem-box">

**Example.** Vertices represent squares of a chessboard, with an edge for each legal knight move. Prove the graph has no odd cycle.

A knight moves two squares in one coordinate and one in the other, changing the parity of the coordinate sum. It therefore switches checkerboard color on every move. The graph is bipartite, so every cycle has even length.

</div>

If the two parts have sizes $$a$$ and $$b$$, there can be at most $$ab$$ edges. For example, a bipartite graph with ten vertices has at most $$25$$ edges because $$ab\le(a+b)^2/4=25$$.

---

## Extremal Arguments

Choosing a vertex of maximum degree or an endpoint of a longest path can force information about its neighbors. Sometimes a local case split gives a global existence result.

<div class="theorem-box">

**Example.** Among any six people, prove there are three mutual acquaintances or three mutual strangers, assuming acquaintance is symmetric.

Fix a person $$P$$. Of the other five people, at least three are all acquaintances of $$P$$ or all strangers to $$P$$.

Suppose $$A,B,C$$ are acquaintances of $$P$$. If any two of them are acquainted, those two and $$P$$ form three mutual acquaintances. If no two are acquainted, $$A,B,C$$ are three mutual strangers.

If instead $$A,B,C$$ are strangers to $$P$$, reverse the roles of acquaintances and strangers in the argument. One of the required triples always exists.

</div>

:::strategy
Define the graph so the conclusion becomes a familiar structure: a triangle, path, matching, or coloring. Count degrees for global restrictions, use a longest path for extension arguments, and try bipartite coloring when every move switches a parity.
:::

## Trails, Euler Tours, and Parity

A path has no repeated vertices. A **trail** has no repeated edges but may revisit vertices. An **Euler trail** uses every edge exactly once; if it returns to its starting vertex, it is an Euler circuit.

At every vertex other than a trail's endpoints, arriving along an unused edge must be paired with leaving along another unused edge. Thus an Euler circuit requires all degrees even, and an open Euler trail requires exactly two odd-degree vertices.

These conditions are also sufficient when all vertices incident to edges belong to one connected component. To construct a circuit in an even-degree graph, follow unused edges until returning to the starting point. If unused edges remain, connectivity supplies a vertex on the current circuit from which another unused circuit can be formed. Splice it into the first circuit and repeat. For two odd vertices, temporarily join them by one extra edge, construct a circuit, and remove the extra edge to obtain an open trail.

<div class="theorem-box">

**Example.** Can a drawing of the complete graph on five vertices be traced using every edge once without lifting the pen or retracing an edge?

Every vertex has degree four, and the graph is connected. Therefore an Euler circuit exists. The fact that five vertices cannot be drawn in the plane without crossings does not prevent such a tracing; a crossing is not an additional vertex unless the problem defines it that way.

</div>

Do not confuse an Euler problem with a Hamiltonian one. A Hamiltonian cycle visits every vertex once rather than every edge once. Degree parity characterizes Euler trails, but it does not supply a corresponding simple test for Hamiltonian cycles.

---

## Matchings and Hall's Theorem

A **matching** is a collection of edges sharing no endpoints. In a bipartite graph, it can represent assigning distinct jobs to people when an edge means an assignment is allowed.

For a set $$S$$ of people, write $$N(S)$$ for all jobs adjacent to at least one member of $$S$$. A matching covering every person requires $$\lvert N(S)\rvert\ge\lvert S\rvert$$ for every subset $$S$$: those people collectively need at least that many available jobs.

**Hall's marriage theorem** states that this necessary condition is sufficient. The condition must hold for every subset, not merely for each person separately or for the entire group.

<div class="theorem-box">

**Example.** Four students need four distinct tasks. A, B, and C can each do only tasks one and two, while D can do tasks three and four. Explain why no complete assignment exists even though every student has two choices.

For $$S=\{A,B,C\}$$, the neighborhood is only $$\{1,2\}$$. Thus $$\lvert N(S)\rvert=2<3=\lvert S\rvert$$. Hall's necessary condition fails, so a complete assignment is impossible.

Counting the total number of allowed edges would not detect this bottleneck. The shortage is concentrated in one subset.

</div>

For the sufficiency idea, start with a maximum matching. If some person remains unmatched, explore paths that alternate between edges outside the matching and edges in the matching, starting there. Reaching an unmatched job would allow the path's matched and unmatched edges to be swapped, increasing the matching, which is impossible.

Let $$S$$ be the reached people and $$T=N(S)$$ the reached jobs. Every reached job is matched to a reached person, while the initial person is unmatched. The exploration therefore gives $$\lvert T\rvert=\lvert S\rvert-1$$, contradicting Hall's condition. This is the augmenting-path proof.

---

## Triangle-Free Graphs and Mantel's Theorem

A graph may have many edges without containing a triangle: complete bipartite graphs provide examples. The balanced example has approximately $$n^2/4$$ edges, and this is the largest possible number.

**Mantel's theorem** states that a simple triangle-free graph on $$n$$ vertices has at most $$\lfloor n^2/4\rfloor$$ edges.

<div class="theorem-box">

**Proof (Mantel's edge bound).** For an edge $$uv$$, the neighborhoods of $$u$$ and $$v$$ are disjoint, since a common neighbor would form a triangle. Hence $$\deg(u)+\deg(v)\le n$$.

Sum over every edge. Vertex $$v$$ contributes its degree once for each incident edge, giving

$$
\sum_v\deg(v)^2\le nE.
$$

Cauchy–Schwarz and the handshake lemma give

$$
\sum_v\deg(v)^2\ge\frac{(\sum_v\deg(v))^2}{n}=\frac{4E^2}{n}.
$$

If $$E>0$$, combine and divide to obtain $$E\le n^2/4$$. If $$E=0$$, the bound is immediate. Since $$E$$ is an integer, take the floor.

</div>

<div class="theorem-box">

**Example.** Prove that a graph with ten vertices and twenty-six edges contains a triangle, and show twenty-five edges do not suffice.

A triangle-free graph has at most $$10^2/4=25$$ edges by Mantel. The complete bipartite graph with five vertices in each part has twenty-five edges and no triangle, showing sharpness.

</div>

This proof combines a local structural fact with a global sum. The same pattern appears often: obtain an inequality at each edge or vertex, sum it, then use an average or a standard algebraic inequality.

---

## Ramsey Arguments and Sharp Constructions

The six-person acquaintance argument proves that every red/blue coloring of the edges of $$K_6$$ contains a monochromatic triangle. To establish that six is the smallest guarantee, a five-vertex coloring avoiding both kinds is needed.

Arrange five vertices on a pentagon. Color its five boundary edges red and its five diagonals blue. The red graph is a five-cycle, so it has no triangle. The blue graph is also a five-cycle, so it has no triangle either.

This supplies the missing construction and proves the exact Ramsey value $$R(3,3)=6$$. In an extremal problem, a clean construction often deserves as much attention as the upper-bound argument, since it explains why the bound cannot improve.

For larger monochromatic configurations, fixing one vertex and splitting its neighbors by edge color can produce recursive bounds. Keep track of how many neighbors are required in each color; an informal “at least half” is not always enough when the target sizes differ.

---

## Planar Graphs and Face Counting

A graph is **planar** if it has a drawing in the plane where edges meet only at common endpoints. For a connected planar drawing, Euler's formula is

$$
V-E+F=2,
$$

where $$F$$ includes the unbounded outer face. Counting sides around faces counts each edge twice, including a bridge once on each side.

For a simple connected planar graph with $$V\ge3$$, every face boundary has at least three edge occurrences, so $$3F\le2E$$. Combining with Euler gives $$E\le3V-6$$. If the graph is bipartite, there are no odd cycles; the corresponding face count gives $$E\le2V-4$$.

<div class="theorem-box">

**Example.** Prove that $$K_5$$ and $$K_{3,3}$$ are not planar.

The graph $$K_5$$ has five vertices and ten edges. A simple planar graph with five vertices has at most $$3(5)-6=9$$ edges, a contradiction.

The graph $$K_{3,3}$$ has six vertices and nine edges. Because it is bipartite, a planar drawing would require at most $$2(6)-4=8$$ edges, again a contradiction.

</div>

The ordinary edge bound alone would not rule out $$K_{3,3}$$, since nine is at most twelve. The bipartite structure supplies the stronger inequality needed for the problem.

---

## Counting Walks by States

A **walk** may repeat both vertices and edges. Counting walks is naturally recursive: the number reaching a vertex after $$n+1$$ steps is the sum of the counts reaching its neighbors after $$n$$ steps.

<div class="theorem-box">

**Example.** Starting at a specified vertex of a triangle graph, how many walks of length six return to the starting vertex?

Let $$a_n$$ count walks ending at the starting vertex, and let $$b_n$$ count walks ending at one particular other vertex. Symmetry makes the counts at the two other vertices equal. Then

$$
a_{n+1}=2b_n,\qquad b_{n+1}=a_n+b_n,\qquad a_0=1,\ b_0=0.
$$

These give $$a_n=(2^n+2(-1)^n)/3$$, either by solving the recurrence or by checking it with the initial values. Therefore $$a_6=(64+2)/3=22$$.

</div>

For a larger graph, put the state counts in a vector and multiply by its adjacency matrix. The entry in row $$i$$, column $$j$$ of the $$n$$th matrix power counts length-$$n$$ walks from one specified endpoint to the other under the chosen row/column convention. This connects graph counting with the recurrence and matrix methods used elsewhere in competition math.

:::strategy
First identify the requested structure: an edge-covering trail, a vertex-covering cycle, a matching, or a walk. Then use the corresponding information. Parity governs Euler trails, neighborhoods govern matchings, local degree inequalities control extremal edge counts, and state recurrences count walks.
:::

---

## Key Equations

:::equations
| Graph fact | Formula or condition |
| --- | --- |
| Complete graph | $$E(K_n)=\binom n2$$ |
| Handshake lemma | $$\sum_v\deg(v)=2E$$ |
| Average degree | $$\overline d=2E/V$$ for $$V>0$$ |
| Tree | $$E=V-1$$ for a connected acyclic graph |
| Bipartite maximum | $$E\le ab\le V^2/4$$, where $$a+b=V$$ |
| Two-color characterization | Bipartite exactly when there is no odd cycle |
| Euler trail | A connected nontrivial edge component has zero or two odd-degree vertices |
| Hall condition | $$\lvert N(S)\rvert\ge\lvert S\rvert$$ for every subset of the left part |
| Mantel | $$E\le\lfloor V^2/4\rfloor$$ for a simple triangle-free graph |
| Planar edge bound | $$E\le3V-6$$ for simple connected planar graphs, $$V\ge3$$ |
| Bipartite planar bound | $$E\le2V-4$$ for simple connected bipartite planar graphs, $$V\ge3$$ |
| Walk recurrence | $$w_{n+1}(v)=\sum_{u\sim v}w_n(u)$$ |
:::
