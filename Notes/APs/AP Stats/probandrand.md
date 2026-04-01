---
layout: default
title: "Unit 4: Probability, Random Variables, and Probability Distributions"
parent: AP Statistics
nav_order: 4
permalink: /notes/ap/stats/probandrand/
---

# Unit 4: Probability, Random Variables, and Probability Distributions

Probability: Probability is the measure of the likelihood of an event  

---

## Sample Space

Sample Space: Any process that results in an observation or an outcome is an experiment. An experiment may have more than one possible outcome, and the set of all possible outcomes of an experiment is known as a sample space. It is generally demoted using the letter \( S \)  

A tree diagram representation is useful in determining the sample space for an experiment especially if there are relatively few possible outcomes  

---

## Basic Rules of Probability

Rule 1: For any event \( A \), the probability of \( A \) is always greater than or equal to 0 and less than or equal to 1  

$$
0 \le P(A) \le 1
$$

Rule 2: The sum of probabilities for all possible outcomes in a sample space is always 1  

If an event can never occur (probability is 0), it is an impossible event  

If an event must occur every time (probability is 1), is is a sure event  

The odds in favor of an event is the ratio of the probability of the occurrence of an event to the probability of A given nonoccurence of that event  

$$
\text{Odds in favor of A} = \frac{P(A)}{P(A')}
$$

---

## More Terms

The complement of an event is all the possible outcomes in a sample space that does not lead to the event. The complement of \( A \) is denoted \( A' \) or \( A^C \)  

Disjoint or mutually exclusive events are events that have no outcome in common. Basically, they can’t occur together  

The union of events \( A \) and \( B \) is the set of all possible outcomes that lead to at least one of two events \( A \) and \( B \). It is denoted by \( A \cup B \)  

The intersection of events \( A \) and \( B \) is the set of all possible outcomes that lead to both events \( A \) and \( B \). It is denoted by \( A \cap B \)  

A conditional event: \( A \) given \( B \) is a set of outcomes for event \( A \) that occurs if \( B \) has occurred. It is indicated by  

$$
A \mid B
$$

and reads “A given B”  

Two events \( A \) and \( B \) are considered independent if the occurrence of one event does not depend on the occurrence of the other  

---

## More Probability Rules

Complement:  

$$
P(A') = 1 - P(A)
$$

Union:  

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

(if two objects are disjoint, \( P(A \cap B) = 0 \))  

Intersection:  

$$
P(A \cap B) = P(A)P(B \mid A) = P(B)P(A \mid B)
$$

Conditional Probabilities (Bayes’ Theorem):  

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

Independence:  

If  

$$
P(A \mid B) = P(A) \quad \text{and} \quad P(B \mid A) = P(B)
$$

(or equivalently,  

$$
P(A \cap B) = P(A)P(B)
$$

), then the two events are independent  

---

# Random Variables and Probability Distributions

A variable is a quantity whose value varies from subject to subject (e.g. test scores, height, etc.)  

A probability experiment is an experiment whose possible outcomes may be known but whose exact outcome is a random event and cannot be predicted with certainty in advance. If the outcome is a numeric value, then it is a random variable and is usually denoted using capital letters (like \( X \) and \( Y \))  

A discrete random variable is a quantitative variable that takes a countable number of values  

A continuous random variable is a quantitative variable that can take all possible values in a given range  

---

## Discrete Probability Distributions

A discrete probability distribution is a table, list, graph, or formula giving all possible values taken on by a random variable and their corresponding probabilities  

Let \( X \) be a random variable taking value \( x_1, x_2, \ldots, x_n \) with respective probabilities \( P(x_1), P(x_2), \ldots, P(x_n) \). Then  

$$
\{(x_1, P(x_1)), (x_2, P(x_2)), \ldots, (x_n, P(x_n))\}
$$

gives a valid probability distribution if  

$$
0 \le P(x_i) \le 1 \quad \text{for all } i = 1, 2, \ldots, n
$$

and  

$$
\sum_{i=1}^{n} P(x_i) = 1
$$

---

## Mean of a Discrete Random Variable

Mean of a Discrete Random Variable: The mean \( \mu \) of a discrete random variable \( X \) is also known as the expected value. It is denoted by \( E(X) \) and the formula is  

$$
\mu = E(X) = \sum_{i=1}^{n} x_i P(x_i)
$$

---

## Variance of a Discrete Random Variable

Variance of a Discrete Random Variable: The variance of a discrete random variable is defined as the sum of the product of the squared deviations of the values of the variable from the mean and the corresponding probabilities and is given by  

$$
\sigma^2 = \sum_{i=1}^{n} (x_i - \mu)^2 P(x_i)
$$

---

## Combinations

Combinations: A combination is the number of ways \( r \) items can be selected out of \( n \) items if the order of selection is NOT important. It is denoted by \( \binom{n}{r} \) (and other ways which you should probably already know) and is equal to  

$$
\binom{n}{r} = \frac{n!}{r!(n-r)!}
$$