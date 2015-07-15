#-------------------------------------
# Question 1
# Consider the space shuttle data ?shuttle in the MASS library. 
# Consider modeling the use of the autolander as the outcome (variable name use). 
# Fit a logistic regression model with autolander (variable auto) use (labeled as "auto" 1) versus not (0) 
# as predicted by wind sign (variable wind). Give the estimated odds ratio for autolander use 
# comparing head winds, labeled as "head" in the variable headwind (numerator) to tail winds (denominator).
library(MASS)
data(shuttle)
shuttle$useD = 0
shuttle$useD[shuttle$use=="auto"] = 1
shuttle$wind = factor(shuttle$wind)
# model with omitted intercept
logit = glm(useD ~ wind - 1, data=shuttle, family='binomial')
summary(logit)$coef
## odds ratios only
exp(coef(logit))

#-------------------------------------
# Question 2
# Consider the previous problem. Give the estimated odds ratio for autolander 
# use comparing head winds (numerator) to tail winds (denominator) adjusting for 
# wind strength from the variable magn.
library(MASS)
data(shuttle)
shuttle$useD = 0
shuttle$useD[shuttle$use=="auto"] = 1
shuttle$wind = factor(shuttle$wind)
shuttle$magn = factor(shuttle$mag)
# model with omitted intercept
logit = glm(useD~ wind + magn - 1, data=shuttle, family='binomial')
summary(logit)
## odds ratios only
exp(coef(logit))

#-------------------------------------
# Question 3
library(MASS)
data(shuttle)
shuttle$useD = 0
shuttle$useD[shuttle$use=="auto"] = 1
shuttle$wind = factor(shuttle$wind)

logit1 = glm(useD ~ wind - 1, data=shuttle, family='binomial')
summary(logit1)$coef

logit2 = glm(1-useD~ wind - 1, data=shuttle, family='binomial')
summary(logit2)$coef

#-------------------------------------
# Question 4
library(MASS)
data(InsectSprays)
InsectSprays$spray = factor(InsectSprays$spray)
model = glm(count ~ spray - 1, data = InsectSprays, family = poisson)
summary(model)
exp(model$coefficients)

#-------------------------------------
# Question 6
# Using a knot point at 0, fit a linear model that 
# looks like a hockey stick with two lines meeting at x=0. 
# Include an intercept term, x and the knot point term. What is the estimated slope of the line after 0?
x = -5:5
y = c(5.12, 3.93, 2.67, 1.87, 0.52, 0.08, 0.93, 2.05, 2.54, 3.87, 4.97)
# define knot point
knots = 0
# define the ()+ function to only take the values that are positive after the knot pt 
splineTerms <- sapply(knots, function(knot) (x > knot) * (x - knot))
# define the predictors as X and spline term
xMat <- cbind(x, splineTerms)
# fit linear models for y vs predictors
yhat <- predict(lm(y ~ xMat))
# plot data points (x, y)
plot(x, y, frame = FALSE, pch = 21, bg = "lightblue") # plot fitted values
lines(x, yhat, col = "red", lwd = 2)