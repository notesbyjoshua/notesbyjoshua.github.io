---
title: "Probability and Expected Value"
status: developing
progress: 68
sidebar:
  order: 4
description: "Competition math notes on conditional probability, independence, expected value, indicators, and state recurrences with worked examples."
---

## Sample Spaces and Complements

A **sample space** lists the possible outcomes of a random experiment. When these outcomes are equally likely,

$$
\Pr(A)=\frac{\#\text{outcomes in }A}{\#\text{outcomes in the sample space}}.
$$

The equally-likely condition matters. The sums of two dice are not equally likely, but the $$36$$ ordered pairs of face values are.

<div class="theorem-box">

**Example.** Two fair six-sided dice are rolled. Find the probability that at least one die shows a six.

Use the complement, where neither die is a six. Each die then has five allowed outcomes, so

$$
\Pr(\text{at least one six})=1-\frac{5^2}{6^2}=\frac{11}{36}.
$$

Adding the two probabilities $$1/6+1/6$$ without correction would count the outcome $$(6,6)$$ twice.

</div>

---

## Conditional Probability and Independence

Conditional probability restricts attention to an event already known to have happened:

$$
\Pr(A\mid B)=\frac{\Pr(A\cap B)}{\Pr(B)},\qquad\Pr(B)>0.
$$

Events are **independent** if $$\Pr(A\cap B)=\Pr(A)\Pr(B)$$. Disjoint events cannot happen together; independent events do not change each other's probabilities. These are different conditions.

<div class="theorem-box">

**Example.** Two fair dice are rolled, and their sum is known to be even. Find the probability that both dice show odd numbers.

There are $$9$$ odd–odd pairs and $$9$$ even–even pairs, so the conditional sample space has $$18$$ equally likely outcomes. Exactly $$9$$ satisfy the requested event. The probability is $$9/18=1/2$$.

</div>

For sequential sampling without replacement, multiply conditional probabilities. For example, if a bag has three red and two blue balls, the probability of drawing two reds is $$(3/5)(2/4)=3/10$$, since the composition changes after the first draw.

For a partition into cases $$B_i$$, total probability gives $$\Pr(A)=\sum_i\Pr(A\mid B_i)\Pr(B_i)$$. Bayes' formula reverses the conditioning:

$$
\Pr(B_i\mid A)=\frac{\Pr(A\mid B_i)\Pr(B_i)}{\Pr(A)}.
$$

Use it when the outcome is known but the case that produced it is unknown.

---

## Random Variables and Expected Value

A **random variable** assigns a number to each outcome. Its expected value is the probability-weighted average:

$$
\mathbb E[X]=\sum_x x\Pr(X=x).
$$

An expectation need not be an attainable value. A fair die has expected value $$7/2$$ even though no face shows $$3.5$$.

For random variables with finite expectations, **linearity of expectation** states

$$
\mathbb E[X_1+\cdots+X_n]=\mathbb E[X_1]+\cdots+\mathbb E[X_n].
$$

No independence is required. This makes it possible to average a complicated total without finding its entire distribution.

<div class="theorem-box">

**Example.** Six fair dice are rolled. Find the expected sum of their face values.

Each die has mean $$(1+2+3+4+5+6)/6=7/2$$. Add the six expectations to get $$6(7/2)=21$$.

</div>

---

## Indicator Variables

An **indicator** $$I_A$$ equals one when event $$A$$ occurs and zero otherwise. Therefore $$\mathbb E[I_A]=\Pr(A)$$. If $$X$$ counts how many events occur, write it as a sum of indicators.

<div class="theorem-box">

**Example.** A uniformly random permutation of $$n\ge1$$ distinct objects is chosen. Find the expected number of fixed points.

Let $$I_i=1$$ if position $$i$$ contains its original object. Exactly $$(n-1)!$$ of the $$n!$$ permutations fix that position, so $$\mathbb E[I_i]=1/n$$. Thus

$$
\mathbb E[X]=\sum_{i=1}^n\mathbb E[I_i]=n\cdot\frac1n=1.
$$

The indicators are dependent, but linearity still applies.

</div>

<div class="theorem-box">

**Example.** Each of five people independently chooses one of four rooms uniformly. Find the expected number of nonempty rooms.

For a particular room, the probability everyone avoids it is $$(3/4)^5$$. Its nonempty indicator therefore has expectation $$1-(3/4)^5$$. Summing over rooms gives

$$
\mathbb E[X]=4\left(1-\left(\frac34\right)^5\right)=\frac{781}{256}.
$$

</div>

---

## Expected Waiting Times and States

If independent trials each succeed with fixed probability $$p>0$$, the expected waiting time for the first success is $$1/p$$. Let $$E$$ be that expected time. After one trial, success finishes the experiment, while failure returns to the starting situation:

$$
E=1+(1-p)E\quad\Longrightarrow\quad E=\frac1p.
$$

For patterns, success chances depend on recent outcomes. Define a state containing just enough history to describe the next transition.

<div class="theorem-box">

**Example.** A fair coin is tossed repeatedly. Find the expected number of tosses needed to see two consecutive heads.

Let $$E_0$$ be the remaining expectation when there is no trailing head, and $$E_1$$ the expectation after one trailing head. Count the next toss in each equation:

$$
E_0=1+\frac12E_0+\frac12E_1,
$$

$$
E_1=1+\frac12E_0+\frac12(0).
$$

The zero corresponds to another head, which completes the pattern. The first equation gives $$E_0=2+E_1$$. Substituting into the second yields $$E_0=6$$. We start in state zero, so the answer is six tosses.

</div>

:::strategy
For a probability, identify equally likely outcomes or condition on the first step. For an expected count, try one indicator per position, object, pair, or box. For a waiting time, define states and write “one step plus expected remaining time.”
:::

## Choosing Between Binomial and Hypergeometric Models

Repeated independent trials with the same success probability $$p$$ produce a binomial count. Exactly $$k$$ successes in $$n$$ trials have probability

$$
\binom nk p^k(1-p)^{n-k}.
$$

Choose the success positions, then multiply the probabilities along that specified pattern. Independence and a fixed probability are both required.

Sampling without replacement from a finite population gives a different model. If $$K$$ of $$N$$ objects are marked and $$n$$ objects are chosen uniformly, exactly $$k$$ marked objects occur with probability

$$
\frac{\binom Kk\binom{N-K}{n-k}}{\binom Nn}.
$$

This is the hypergeometric formula. The numerator chooses the marked and unmarked portions of the sample. Unlike sequential multiplication, it avoids keeping track of the changing composition after each draw.

<div class="theorem-box">

**Example.** Five objects are chosen uniformly without replacement from eight red and seven blue objects. Find the probability of exactly three reds.

A sample is an unordered five-element subset, so the probability is

$$
\frac{\binom83\binom72}{\binom{15}5}
=\frac{56\cdot21}{3003}
=\frac{56}{143}.
$$

The binomial expression $$\binom53(8/15)^3(7/15)^2$$ would describe replacement sampling instead and is not correct for this experiment.

</div>

---

## Bayes' Formula with a Hidden Choice

When an experiment first selects a source and then produces an observation, condition on the source before calculating the observation probability. Bayes' formula then updates the source probabilities after the observation is known.

<div class="theorem-box">

**Example.** Urn A is chosen with probability one-third and contains white balls with proportion two-thirds. Urn B is chosen with probability two-thirds and has white proportion one-quarter. A ball drawn from the selected urn is white. Find the probability that A was chosen.

The two disjoint ways to observe white have probabilities

$$
\Pr(A\cap W)=\frac13\cdot\frac23=\frac29,\qquad
\Pr(B\cap W)=\frac23\cdot\frac14=\frac16.
$$

Thus $$\Pr(W)=7/18$$, and

$$
\Pr(A\mid W)=\frac{2/9}{7/18}=\frac47.
$$

The posterior is greater than one-third because a white ball is more likely under A. This directional check helps catch an inverted conditional probability.

</div>

The observation mechanism matters. If a host or observer chooses what to reveal, their rule can change the conditional sample space. State the rule before assigning probabilities; “one possibility was removed” does not automatically make the remaining possibilities equally likely.

---

## Indicators for Pairs and Positions

Indicators are useful even when the total is not visibly a count of separate objects. A count of pairs suggests one indicator per pair; a count of adjacency events suggests one per edge or neighboring position.

<div class="theorem-box">

**Example.** A uniformly random permutation of $$1,\ldots,n$$ is chosen. Find the expected number of inversions, pairs $$i<j$$ whose values occur in reverse order.

For each pair of distinct values $$a<b$$, let its indicator be one when $$b$$ appears before $$a$$. The two relative orders are equally likely, so each indicator has expectation one-half. There are $$\binom n2$$ pairs, giving

$$
\mathbb E[X]=\frac12\binom n2=\frac{n(n-1)}4.
$$

Dependence among the pair indicators does not matter for this expectation.

</div>

<div class="theorem-box">

**Example.** In a random permutation of $$1,\ldots,n$$ with $$n\ge2$$, find the expected number of pairs of consecutive values that occupy adjacent positions.

For a specified pair $$\{k,k+1\}$$, treat the values as a block. There are $$2(n-1)!$$ permutations placing them together, so the probability is $$2/n$$. Summing the indicators for the $$n-1$$ consecutive-value pairs gives

$$
\mathbb E[X]=(n-1)\frac2n=2-\frac2n.
$$

A run containing three consecutive values may contribute two indicators, which is appropriate because the requested quantity counts pairs, not runs.

</div>

This last distinction is important. If the problem asks for maximal runs, an indicator for every adjacent match counts the wrong object. Define the random variable before choosing its decomposition.

---

## Tail Sums and Coupon Collection

For a nonnegative integer-valued random variable,

$$
\mathbb E[X]=\sum_{k\ge1}\Pr(X\ge k)
$$

whenever the expectation is finite, with the same identity allowing infinity. An outcome with value $$m$$ contributes one to exactly the first $$m$$ tail indicators. This representation is useful when the probability of exceeding a threshold is easier than the probability of one exact value.

Another useful decomposition splits a waiting process into stages. Collecting a new type after several types are already known is a geometric wait with a changing success probability.

<div class="theorem-box">

**Example.** A fair six-sided die is rolled until every face has appeared. Find the expected number of rolls.

After $$k$$ distinct faces have appeared, the next roll introduces a new face with probability $$(6-k)/6$$. The expected wait for that next new face is $$6/(6-k)$$. Add the six stage expectations:

$$
\mathbb E[T]=6\left(1+\frac12+\frac13+\frac14+\frac15+\frac16\right)
=\frac{147}{10}.
$$

The stage waiting times need not be proved independent to add their expectations. What matters is that they sum to the total collection time and each stage has the stated geometric distribution.

</div>

For $$n$$ equally likely types, the same argument gives $$nH_n$$, where $$H_n=1+1/2+\cdots+1/n$$. If the types have different probabilities, the success chance depends on which types are missing, not just how many. A single count state no longer determines the process.

---

## Hitting Probabilities and Expected Duration

State recurrences can calculate either a probability or an expectation, but the equations differ. A hitting probability averages the next-state probabilities. An expected remaining duration adds one for the next move before averaging.

Consider a fair random walk on integers $$0,1,\ldots,N$$, stopping at either endpoint. Let $$p_i$$ be the probability of reaching $$N$$ first from state $$i$$. Then

$$
p_0=0,\quad p_N=1,\quad
p_i=\frac12p_{i-1}+\frac12p_{i+1}.
$$

The interior equation says consecutive differences are equal, so $$p_i=i/N$$.

For expected duration $$E_i$$, the equations are

$$
E_0=E_N=0,\qquad E_i=1+\frac12E_{i-1}+\frac12E_{i+1}.
$$

A quadratic trial gives $$E_i=i(N-i)$$. It satisfies both boundary values and the recurrence. The finite absorbing system has a unique solution; absorption has finite expectation because every block of sufficiently many moves has a fixed positive chance of reaching a boundary.

<div class="theorem-box">

**Example.** A player starts with three dollars and repeatedly wins or loses one dollar with equal probability, stopping at zero or ten dollars. Find the probability of reaching ten and the expected number of games.

Take $$N=10,i=3$$. The hitting probability is $$3/10$$, while the expected number of games is $$3(10-3)=21$$. These are different random quantities and come from different state equations.

</div>

---

## Variance and Dependence

Expectation describes the average, while **variance** measures spread:

$$
\operatorname{Var}(X)=\mathbb E[(X-\mathbb E[X])^2]
=\mathbb E[X^2]-\mathbb E[X]^2.
$$

For a Bernoulli indicator with success probability $$p$$, the variance is $$p(1-p)$$ because $$I^2=I$$. For independent random variables, variances add. Without independence, covariance terms appear:

$$
\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)
+2\bigl(\mathbb E[XY]-\mathbb E[X]\mathbb E[Y]\bigr).
$$

This is why linearity of expectation cannot be copied blindly into a variance calculation. For example, if $$Y=X$$, then $$\operatorname{Var}(X+Y)=4\operatorname{Var}(X)$$, not twice the variance. A contest problem asking for a second moment usually requires analyzing pairs of indicators and the probability that both events occur.

:::strategy
Identify the random quantity before choosing a formula. Use counting for a finite uniform sample, conditioning for a hidden case, indicators for an expected count, and states for a stopping process. Check independence only where the chosen method actually requires it.
:::

---

## A Second Moment for Fixed Points

Second moments show precisely where dependence enters an indicator calculation. For a random permutation of $$n\ge2$$ objects, let $$X$$ count fixed points and write $$X=\sum_iI_i$$.

Since $$I_i^2=I_i$$,

$$
X^2=\sum_iI_i+2\sum_{i<j}I_iI_j.
$$

A specified pair of positions is fixed in $$(n-2)!$$ of the $$n!$$ permutations, so its joint probability is $$1/[n(n-1)]$$. Therefore

$$
\mathbb E[X^2]=1+2\binom n2\frac1{n(n-1)}=2.
$$

The mean is one, hence $$\operatorname{Var}(X)=2-1=1$$.

This result does not follow by adding the individual indicator variances, because those indicators are not independent. The pair terms supplied the missing information. At $$n=1$$ the fixed-point count is constantly one and has variance zero, so that boundary case must be excluded from the formula.

The same expansion works for counts of collisions, adjacent matches, or intersecting pairs. Separate pairs of indicators by whether their underlying objects overlap, calculate each joint probability, and combine the categories.

---

## Expected Number of Permutation Cycles

A uniform permutation of $$n$$ objects can be built from a uniform permutation of $$n-1$$ objects in cycle notation. Insert the new object after any one of the existing $$n-1$$ objects, or let it form its own cycle. These are $$n$$ equally weighted choices, and deleting the new object reverses the construction uniquely.

Only the singleton choice increases the cycle count. Therefore

$$
\mathbb E[C_n]=\mathbb E[C_{n-1}]+\frac1n,
$$

and the initial value one gives $$\mathbb E[C_n]=H_n$$.

The expected count grows slowly even though a permutation can have anywhere from one to $$n$$ cycles. This is another example where a recursive construction makes the expectation easier than the entire distribution.

Uniformity is the key justification: selecting an insertion position with arbitrary unequal probabilities would not generate a uniform permutation and would change the calculation.

---

## Key Equations

:::equations
| Tool | Formula and conditions |
| --- | --- |
| Complement | $$\Pr(A^c)=1-\Pr(A)$$ |
| Conditional probability | $$\Pr(A\mid B)=\Pr(A\cap B)/\Pr(B)$$, $$\Pr(B)>0$$ |
| Independence | $$\Pr(A\cap B)=\Pr(A)\Pr(B)$$ |
| Expectation | $$\mathbb E[X]=\sum_xx\Pr(X=x)$$ |
| Indicators and linearity | $$\mathbb E[\sum I_i]=\sum\Pr(A_i)$$ |
| Independent repeated trials | $$\mathbb E[T]=1/p$$ for fixed success probability $$p>0$$ |
| Binomial probability | $$\Pr(X=k)=\binom nkp^k(1-p)^{n-k}$$ for independent fixed-probability trials |
| Hypergeometric probability | $$\Pr(X=k)=\binom Kk\binom{N-K}{n-k}/\binom Nn$$ |
| Tail expectation | $$\mathbb E[X]=\sum_{k\ge1}\Pr(X\ge k)$$ for nonnegative integer $$X$$ |
| Coupon collector | $$\mathbb E[T]=nH_n$$ for $$n$$ equally likely types |
| Fair absorbing walk | $$p_i=i/N$$, $$E_i=i(N-i)$$ |
| Variance | $$\operatorname{Var}(X)=\mathbb E[X^2]-\mathbb E[X]^2$$ |
| Random-permutation fixed points | $$\mathbb E[X]=1,\ \operatorname{Var}(X)=1$$ for $$n\ge2$$ |
| Permutation cycles | $$\mathbb E[C_n]=H_n$$ for a uniform permutation |
:::
