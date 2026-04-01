---
layout: default
title: "Unit 2: Exploring Bivariate Data"
parent: AP Statistics
nav_order: 2
permalink: /notes/ap/stats/bivardata/
---

# Unit 2: Exploring Bivariate Data

When comparing distributions of two or more groups, use the following criteria:

- Compare the centers of the distributions  
- Compare the spread of the distributions. Consider the differences in the spread of data within each group as well as the differences between groups  
- Compare clusters of measurements and gaps in measurements  
- Compare outliers and any other unusual features  
- Compare the shapes of the distributions  
- Compare in the context of the question  

Many graphing techniques could be used to compare; just choose the right one and have the two or more things in parallel  

---

# Exploring Bivariate Data

Bivariate data is data on two different variables collected from each item in a study  

If two different quantitative variables have a linear relation, then we can measure the strength of the relationship with linear regression  

---

## Scatterplot

A scatterplot is used to describe the nature, degree, and direction of the relation between two variables \( x \) and \( y \), where \( (x,y) \) gives a pair of measurements.  

Draw an x-axis and a y-axis, and scale to accommodate all x and y values. Finally, plot the \( (x,y) \) pairs.  

---

### Shape

A scatterplot tells us whether the nature of the relation between two variables is linear or non-linear  

---

### Direction

The scatterplot will show the linear relationship between the x and y values (positive/negative/no correlation). Specifically, upward trend = positive correlation, downward trend = negative correlation  

---

### Strength of Relationship

If the trend of the data can be described to some degree with a line or a curve, then the spread of the data values around the line or curve describes the degree (or strength) of the relationship between the two  

---

## Pearson’s Correlation Coefficient

Pearson’s Correlation Coefficient (also known simply as “the correlation coefficient”) is a numeric measure of degree and direction of the linear relation between two quantitative variables.  

The correlation coefficient between two variables \( x \) and \( y \) computed from a population is denoted by \( \rho \), whereas the correlation coefficient computed from a sample is denoted by \( r \)  

$$
-1 \le r \le 1
$$

---

### Formula

$$
r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}
$$

---

### Direction

A positive \( r \)-value indicates positive correlation and a negative \( r \)-value indicates negative correlation  

---

### Strength

The numeric value of the correlation describes the strength of a correlation.  

If \( |r| = 1 \), that is a perfect correlation, and the further \( |r| \) gets to 0, the weaker the correlation.  

Usually:  

- no correlation is \( |r| < 0.1 \)  
- a weak correlation is \( 0.1 < |r| < 0.5 \)  
- a strong correlation is \( 0.5 < |r| < 0.85 \)  
- a very strong correlation is \( |r| > 0.85 \)  

---

# Least-Squares Regression Line

A linear regression model/equation is an equation that gives a straight line relationship between two variables, and is modeled by the equation  

$$
Y = \beta_0 + \beta_1 X + \epsilon
$$

- \( Y \) is the dependent variable  
- \( X \) is the independent/explanatory variable  
- \( \beta_0 \) is the y-intercept (value of \( Y \) when \( X = 0 \))  
- \( \beta_1 \) is the slope of the line  
- \( \epsilon \) is the random error  

This general term accounts for everything besides what is accounted for in the model without \( \epsilon \).  

\( \epsilon \) represents the distance from the actual point, and the goal of the model is to reduce this error  

---

## Predicted Values and Residuals

The predicted value of \( Y \) for a given value of \( X \) is denoted by \( \hat{y} \) and is computed using the regression line  

$$
\hat{y} = \beta_0 + \beta_1 x
$$

The error/residual (\( e \)) is calculated by  

$$
e = y - \hat{y}
$$

(actual - predicted)  

---

## Least-Squares Regression Line

A least-squares regression line is a line that minimizes the sum of the squares of the residuals (also known as line of best fit).  

The line of best fit will always pass through the point \( (\bar{X}, \bar{Y}) \) and will always have the slope  

$$
\beta_1 = r \left( \frac{s_y}{s_x} \right)
$$

(where \( s \) is the standard deviation)  

---

## Coefficient of Determination

The coefficient of determination measures the percent of variation in \( Y \)-values explained by the linear relation between \( X \)- and \( Y \)-values.  

It is denoted by  

$$
R^2
$$

(square of the coefficient of correlation, and is always between 0 and 1)  

---

## Influential Observations

An influential observation is an observation is an observation that strongly affects a statistic  

---

## Residual Plots

A residual plot is a plot of residuals versus the predicted values of \( Y \).  

This type of plot is used to assess the fit of the model (should look random).  

If the residual plot shows any patterns or trends, it indicates that the linear model is not appropriate  

---

## Transformations to Achieve Linearity

Sometimes, if a model is not linear, you can use a transformation to achieve linearity  

Example:  

$$
y = e^x \Rightarrow \ln(Y) = x
$$

where we substitute the LHS (the \( \ln(Y) \) in the example) with another variable \( Z \)  

---

### Common Transformations

Log Transformation:  

$$
Z = \ln(Y)
$$

Square Root Transformation:  

$$
Z = \sqrt{Y}
$$

Reciprocal Transformation:  

$$
Z = \frac{1}{Y}
$$

---

## Two-Way Tables

If data is classified into two criteria, we can create a contingency table with dimensions of \( r \times c \)  

(\( r \) categories of one criteria and \( c \) categories of the other criteria)  

Each box represents the intersection of a category in each criteria  

---

## Marginal Frequency

The frequency at which each category occurs  

---

## Conditional Relative Frequency

The relative frequency of one category given the other category has occurred (basically Bayes’ Theorem)  

---

## Association

The degree of relation between two categorical variables  

If there is no association, the number for each cell would be  

$$
\frac{(\text{row total})(\text{column total})}{\text{total number of measurements}}
$$

If actual \( > \) calculated, there is a positive correlation  

If actual \( < \) calculated, there is a negative correlation