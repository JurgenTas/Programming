#-------------------------------------
# Question 1, 2:
# Give a P-value for the two sided hypothesis test of whether ??1 from a linear regression model is 0 or not.
# Consider the previous problem, give the estimate of the residual standard deviation.
x = c(0.61, 0.93, 0.83, 0.35, 0.54, 0.16, 0.91, 0.62, 0.62)
y = c(0.67, 0.84, 0.6, 0.18, 0.85, 0.47, 1.1, 0.65, 0.36)
model = lm(formula = y ~ x)
summary(model)

#-------------------------------------
# Question 3, 5:
# In the mtcars data set, fit a linear regression model of weight (predictor) on mpg (outcome). 
# Get a 95% confidence interval for the expected mpg at the average weight. What is the lower endpoint?
# Consider again the mtcars data set and a linear regression model with mpg as predicted by weight (1,000 lbs). 
# A new car is coming weighing 3000 pounds. 
# Construct a 95% prediction interval for its mpg. What is the upper endpoint?
data(mtcars)
x=mtcars$wt
y=mtcars$mpg
model=lm(y ~ x)
predict(model,data.frame(x=mean(x)), interval="confidence")
predict(model,data.frame(x=3), interval="prediction")

#-------------------------------------
# Question 6:
# Consider again the mtcars data set and a linear regression model with mpg as predicted by weight (in 1,000 lbs).
# A ???short??? ton is defined as 2,000 lbs. Construct a 95% confidence interval 
# for the expected change in mpg per 1 short ton increase in weight. Give the lower endpoint.
data(mtcars)
x=mtcars$wt 
y=mtcars$mpg
model=lm( y ~ I(x/2) )
summary(model)

#-------------------------------------
# Question 8:
# I have an outcome, Y, and a predictor, X and fit a linear regression model with Y=??0+??1X+?? 
# to obtain ??^0 and ??^1. What would be the consequence to the subsequent 
# slope and intercept if I were to refit the model with a new regressor, X+c for some constant, c?
x1 = c(0.61, 0.93, 0.83, 0.35, 0.54, 0.16, 0.91, 0.62, 0.62)
x2 = x1 + 1
y = c(0.67, 0.84, 0.6, 0.18, 0.85, 0.47, 1.1, 0.65, 0.36)
model1 = lm(formula = y ~ x1)
summary(model1)
model2 = lm(formula = y ~ x2)
summary(model2)

#-------------------------------------
# Question 9:
#Refer back to the mtcars data set with mpg as an outcome and weight (wt) as the predictor. 
# About what is the ratio of the the sum of the squared errors, ???ni=1(Yi???Y^i)2 when comparing a model 
# with just an intercept (denominator) to the model with the intercept and slope (numerator)?
data(mtcars)
x=mtcars$wt 
y=mtcars$mpg
model1=lm( y ~ 1 )
model2=lm( y ~ x )
anova(model1)
anova(model2)

278.32 / 1126 



