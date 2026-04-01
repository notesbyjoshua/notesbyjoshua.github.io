---
layout: default
title: "Unit 1: Exploring Univariate Data"
parent: AP Statistics
nav_order: 1
permalink: /notes/ap/stats/univardata/
---

# Unit 1: Exploring Univariate Data

## Types of Variables

Categorical/Qualitative: The data is placed into individual categories groups/categories, and researches generally determine the count or percent of individuals in each category  

Quantitative: Outcomes are numerical and can be analyzed using arithmetic operations (e.g. taking the average); can be classified as discrete (has individual points) or continuous (on a spectrum)  

Univariate data: One measurement on each object (e.g. taking height of children only)  

Bivariate data: Two measurements on each object (e.g. taking height and weight of children)  

---

## Types of Descriptive Methods

A descriptive method is a way to organize and summary data  

### Tabular Methods

Methods relating to frequency  

The letter \( n \) is used to denote the number of observations in a dataset  

The frequency of a value is the number of times that observation occurs (denoted with \( f \))  

The relative frequency of a value is the ratio of the frequency (\( f \)) to the total number of observations (\( n \)) (denoted as \( rf = \frac{f}{n} \))  

The cumulative frequency gives the number of observations less than or equal to a specified value (denoted as \( cf \))  

A frequency distribution table is a table giving all possible values of a variable and their frequencies  

---

## Graphical Methods (Qualitative)

Methods relating to graphing a dataset  

Bar charts: Draw bars (rectangles) with the categorical data on the x-axis and the frequency on the y-axis, where the height of the bar matches the frequency of that category (for horizontal bar chart, flip axes)  

Pie charts: Draw a circle and then for each relative frequency fill in that much of the circle with that variable (e.g. 36% relative frequency corresponds to 36% filled in a circle), and each slice of the pie represents one category  

---

## Graphical Methods (Quantitative)

Dotplots: Graph each value in your dataset and then a dot for each time it appears  

Stemplots: Separate each observation into a left part (the stem) and a right part (the leaf), and choose the division appropriately (there is no definition on where to take the division). Then, organize the stem in numerical order and the leaves as well.  

Histograms: Create groups from continuous data (called “binning”), and do the same as a bar chart but ensure that the bars are drawn next to each other without any gaps  

Cumulative Frequency Charts: Draw x and y-axes such that the x-axis encompasses the range of all of the groups and mark the upper bound of each group. Scale the y-axis from 0 to 100% (or 0 to 1) and place a dot at the height equal to the cumulative frequency for that group above the upper boundary for each group. Connect the dots with straight lines  

Boxplots: A boxplot is a graphical data summary based on measures of position. Draw a rectangular box from the first quartile to the third quartile, and draw a line as the median. Compute the “whisker” length = \( 1.5 \times IQR \) and connect them to the middle boxes. Plot outliers as individual points  

---

## Examining Graphs

The center of a discritbution describes the point around which the data points are spread. There will roughly be the same number of data points to the left and right of the center (for most graphs, the center will be roughly the same as the median/mean)  

The spread of a distribution describes how far the data points are from the center. Spread can be quantified through the range, standard deviations, or variance of a distribution  

The shape of a distribution can tell us where most of the data is. For example:  

Symmetric distribution: If the left half of the distribution is approximately a mirror image of the right half, then the distribution is described as symmetric  

Skewed distribution: If there are extreme values in only one direction that causes one side to have a longer tail, we call that distribution skewed. It is right-skewed if the right side is the tail, and left-skewed if the left side is the tail  

---

## Patterns and Deviation from Patterns

Clusters and gaps: As the name implies, clusters are places where values are clustered together, and gaps and places where the data tends to be missing abnormally  

Outliers: An outlier is an observation that is surprisingly different from the rest of the data  

$$
\text{Outlier} > Q_3 + 1.5 \cdot IQR \quad \text{or} \quad \text{Outlier} < Q_1 - 1.5 \cdot IQR
$$

---

## Summarizing Distributions

Population is the entire group of individuals or things we are interested in  

Sample is the part of the population that is actually studied  

---

## Numerical Methods for Continuous Variables

### Measures of Central Tendency

Mean:  

$$
\mu = \frac{\sum_{i=1}^{N} X_i}{N}
$$

$$
\bar{X} = \frac{\sum_{i=1}^{n} X_i}{n}
$$

Median:  

$$
M = \text{l+1 \over 2 th term in the data if dataset is odd, the average of l/2 th and (l+1)/2 th term}
$$

---

### Measures of Variation

Range:  

$$
\text{Range} = \text{max} - \text{min}
$$

Interquartile Range:  

$$
IQR = Q_3 - Q_1
$$

Standard Deviation:  

$$
\sigma = \sqrt{\frac{\sum_{i=1}^{N} (X_i - \mu)^2}{N}}
$$

$$
s = \sqrt{\frac{\sum_{i=1}^{n} (X_i - \bar{X})^2}{n-1}}
$$

---

## Measures of Position

Percentiles:  

$$
l = \frac{(n+1)k}{100}
$$

Quartiles:  

\( Q_1 = 25\% \), \( Q_2 = 50\% \), \( Q_3 = 75\% \)

Standardized scores/z-scores:  

$$
z = \frac{x - \mu}{\sigma}
$$

---

## Effects of Changing Units on Summary Measures

| Summary Measure | \( Y_i = X_i + a \) | \( Y_i = bX_i \) |
|----------------|-------------------|------------------|
| Mean | \( +a \) | \( b \) |
| Median | \( +a \) | \( b \) |
| Range | Range unaffected | \( |b| \) |
| Standard Deviation | Std. Dev. unaffected | \( |b| \) |
| Quartiles | \( +a \) | \( b \) |
| Interquartile Range | IQR unaffected | \( |b| \) |

