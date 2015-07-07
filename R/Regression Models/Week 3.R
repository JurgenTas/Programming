#-------------------------------------
# Question 1:
# Consider the mtcars data set. Fit a model with mpg as the outcome that includes number 
# of cylinders as a factor variable and weight as confounder. 
# Give the adjusted estimate for the expected change in mpg comparing 8 cylinders to 4.
data(mtcars)
mtcars$cyl = factor(mtcars$cyl)
model = lm(mpg ~ cyl + wt, data = mtcars)
summary(model)

#-------------------------------------
# Question 2:
# Consider the mtcars data set. Fit a model with mpg as the outcome that includes number 
# of cylinders as a factor variable and weight as a possible confounding variable. Compare 
# the effect of 8 versus 4 cylinders on mpg for the adjusted and unadjusted by weight models. 
# Here, adjusted means including the weight variable as a term in the regression model and 
# unadjusted means the model without weight included. What can be said about the effect 
# comparing 8 and 4 cylinders after looking at models with and without weight included?.
data(mtcars)
mtcars$cyl = factor(mtcars$cyl)
model1 = lm(mpg ~ cyl + wt, data = mtcars)
summary(model1)
model2 = lm(mpg ~ cyl, data = mtcars)
summary(model2)

#-------------------------------------
# Question 3:
# Consider the mtcars data set. Fit a model with mpg as the 
# outcome that considers number of cylinders as a factor variable and weight as 
# confounder. Now fit a second model with mpg as the outcome model that considers the interaction 
# between number of cylinders (as a factor variable) and weight. 
# Give the P-value for the likelihood ratio test comparing the two models and suggest 
# a model using 0.05 as a type I error rate significance benchmark.
data(mtcars)
mtcars$cyl = factor(mtcars$cyl)
model1 = lm(mpg ~ cyl + wt, data = mtcars)
model1$coef
model2 = lm(mpg ~ cyl*wt, data = mtcars)
model2$coef
anova(model1, model2)

#-------------------------------------
# Question 5:
# Give the hat diagonal for the most influential point
x = c(0.586, 0.166, -0.042, -0.614, 11.72)
y = c(0.549, -0.026, -0.127, -0.751, 1.344)
model = lm(y ~ x)
max(hatvalues(model))
plot(hatvalues(model), type = "h")

#-------------------------------------
# Question 6:
# Give the slope dfbeta for the point with the highest hat value.
library(car)
x = c(0.586, 0.166, -0.042, -0.614, 11.72)
y = c(0.549, -0.026, -0.127, -0.751, 1.344)
dfbetasPlots( model <- lm(y ~ x) )


