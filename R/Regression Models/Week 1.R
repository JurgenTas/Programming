#-------------------------------------
# Question 1:
# Give the value of ?? that minimizes the least squares equation ???ni=1wi(xi?????)2
f1 = function(y) {
  x = c(0.18, -1.54, 0.42, 0.95)
  w = c(2, 1, 3, 1)
  sum(w*(x-y)^2)
} 

f1(0.300)
f1(1.077)
f1(0.0025)
f1(0.1471)

#-------------------------------------
# Question 2:
#Fit the regression through the origin and get the slope treating y as the 
# outcome and x as the regressor. 
# (Hint, do not center the data since we want regression through the origin, 
# not through the means of the data.)
x = c(0.8, 0.47, 0.51, 0.73, 0.36, 0.58, 0.57, 0.85, 0.44, 0.42)
y = c(1.39, 0.72, 1.55, 0.48, 1.19, -1.59, 1.23, -0.65, 1.49, 0.05)
lm(formula = y ~ 0 + x)

#-------------------------------------
# Question 3:
# Do data(mtcars) from the datasets package and fit the regression model with 
# mpg as the outcome and weight as the predictor. Give the slope coefficient
data(mtcars)
lm(mpg ~ wt, data = mtcars)

#-------------------------------------
# Question 4:
# Consider data with an outcome (Y) and a predictor (X). 
# The standard deviation of the predictor is one half that of the outcome. 
# The correlation between the two variables is .5. 
# What value would the slope coefficient for the regression model 
# with Y as the outcome and X as the predictor?
st_x = 1
st_y = 2
corr_xy = 0.5
slope = corr_xy * (st_y / st_x)

#-------------------------------------
# Question 6:
# What is the value of the first measurement 
# if x were normalized (to have mean 0 and variance 1)?
x = c(8.58, 10.46, 9.01, 9.64, 8.86)
xn = (x-mean(x))/sd(x)
xn

#-------------------------------------
# Question 7:
# Consider the following data set (used above as well). 
# What is the intercept for fitting the model with x as the predictor and y as the outcome?
x = c(0.8, 0.47, 0.51, 0.73, 0.36, 0.58, 0.57, 0.85, 0.44, 0.42)
y = c(1.39, 0.72, 1.55, 0.48, 1.19, -1.59, 1.23, -0.65, 1.49, 0.05)
lm(formula = y ~ x)

#-------------------------------------
# Question 9:
# What value minimizes the sum of the squared distances between these points and itself?
f2= function(y) {
  x = c(0.8, 0.47, 0.51, 0.73, 0.36, 0.58, 0.57, 0.85, 0.44, 0.42)
  sum((x-y)^2)
} 

f2(0.573)
f2(0.8)
f2(0.36)
f2(0.44)

#-------------------------------------
# Question 10:

x = c(0.8, 0.47, 0.51, 0.73, 0.36, 0.58, 0.57, 0.85, 0.44, 0.42)
y = c(1.39, 0.72, 1.55, 0.48, 1.19, -1.59, 1.23, -0.65, 1.49, 0.05)
a1 = cor(y, x) * sd(y) / sd(x)
a2 = cor(x, y) * sd(x) / sd(y)
a1/a2
(sd(y) * sd(y))/(sd(x) * sd(x))






