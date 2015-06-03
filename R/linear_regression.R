# load mtcars:
data(mtcars)

# Make factors:
mtcars$cyl = factor(mtcars$cyl)
mtcars$vs = factor(mtcars$vs)
mtcars$gear = factor(mtcars$gear)
mtcars$carb = factor(mtcars$carb)
mtcars$am = factor(mtcars$am,labels=c('Automatic','Manual'))

# Determine best model:
full.model = lm(mpg ~ ., data = mtcars)
best.model = step(full.model, direction = "backward")

# Residual plots of the best model as evaluated by the stepwise regression:
par(mfrow=c(2, 2))
plot(best.model)

# Evaluate collinearity:
library(car)
vif(best.model) # variance inflation factors 

# Boxplot of miles per gallon by transmission type:
boxplot(mpg ~ am, data = mtcars, col = "blue", ylab = "miles per gallon")

# Describes the transmission type (am) by the horsepower (hp) and weight (wt).
am.glm = glm(formula=am ~ hp + wt, data=mtcars, family=binomial)
summary(am.glm)

