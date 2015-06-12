#-----------------------------------------------------------------------------------------------
# Question 1
# Load the vowel.train and vowel.test data sets:
library(ElemStatLearn)
library(caret)
data(vowel.train)
data(vowel.test) 

# Set the variable y to be a factor variable in both the training and test set.
vowel.train$y=as.factor(vowel.train$y) 
vowel.test$y=as.factor(vowel.test$y) 
set.seed(33833)

# Fit (1) a random forest predictor relating the factor variable y to the remaining variables:
model1 = train(y~ ., data=vowel.train, method="rf", prox=TRUE, ntree=500) 
# predict outcome for test data set using the random forest model
pred1 = predict(model1, vowel.test)
# Results
confusionMatrix(vowel.test$y, pred1)

# Fit (2) a boosted predictor using the "gbm" method relating the factor variable y to the remaining variables:
model2= train(y~ ., data=vowel.train, method="gbm", verbose=F) 
pred2 = predict(model2, vowel.test)
# Results
confusionMatrix(vowel.test$y, pred2)

#-----------------------------------------------------------------------------------------------
#Question 2
#Load the Alzheimer's data using the following commands
library(caret)
library(gbm)
set.seed(3433)
library(AppliedPredictiveModeling)
data(AlzheimerDisease)
adData = data.frame(diagnosis,predictors)
inTrain = createDataPartition(adData$diagnosis, p = 3/4)[[1]]
training = adData[ inTrain,]
testing = adData[-inTrain,]

#Set the seed to 62433 and predict diagnosis with all the other variables using a random forest ("rf"), 
#boosted trees ("gbm") and linear discriminant analysis ("lda") model:
set.seed(62433)
model1 = train(diagnosis~ ., data=training, method="rf", trControl = trainControl(number = 4))
model2 = train(diagnosis~ ., data=training, method="gbm", verbose=F) 
model3 = train(diagnosis~ ., data=training, method="lda") 
pred1 = predict(model1, testing)
pred2 = predict(model2, testing)
pred3 = predict(model3, testing)

#Stack the predictions together using random forests ("rf"):
combo = data.frame(pred1, pred2, pred3, diagnosis=testing$diagnosis)
model4 = train(diagnosis~ .,data = combo, method="rf")
pred4 = predict(model4, testing)

# confusion matrixes:
confusionMatrix(pred1, testing$diagnosis)
confusionMatrix(pred2, testing$diagnosis)
confusionMatrix(pred3, testing$diagnosis)
confusionMatrix(pred4, testing$diagnosis)

#-----------------------------------------------------------------------------------------------
#Question 3
#Load the concrete data with the commands:
set.seed(3523)
library(AppliedPredictiveModeling)
data(concrete)
inTrain = createDataPartition(concrete$CompressiveStrength, p = 3/4)[[1]]
training = concrete[ inTrain,]
testing = concrete[-inTrain,]
#Set the seed to 233 and fit a lasso model to predict Compressive Strength
set.seed(233)
# load lars package
library(lars)
# perform lasso regression
set.seed(233)
lasso.model = train(CompressiveStrength~., data=training, method="lasso")
plot.enet(lasso.model$finalModel, xvar="penalty", use.color=TRUE)

#-----------------------------------------------------------------------------------------------
#Question 4
library(lubridate)  # For year() function below
dat = read.csv("~/Programming/R/Machine Learning/gaData.csv")
training = dat[year(dat$date) < 2012,]
testing = dat[(year(dat$date)) > 2011,]
tstrain = ts(training$visitsTumblr)
#Fit a model using the bats() function in the forecast package to the training time series:
model= bats(tstrain)
# forecast with a 95% ci
fcast = forecast(object = model, level = 95)
# test accuracy
accuracy(f = fcast, x = training$visitsTumblr)

#-----------------------------------------------------------------------------------------------
#Question 5
#Load the concrete data with the commands:
  
set.seed(3523)
library(AppliedPredictiveModeling)
data(concrete)
inTrain = createDataPartition(concrete$CompressiveStrength, p = 3/4)[[1]]
training = concrete[ inTrain,]
testing = concrete[-inTrain,]
#Set the seed to 325 and fit a support vector machine using the e1071 package to predict Compressive Strength using the default settings. Predict on the testing set. What is the RMSE?
require(e1071)
set.seed(325)
fit=svm(CompressiveStrength ~., data = training )
pred=predict(fit, testing)
library(forecast)
accuracy(f = pred, x = testing$CompressiveStrength)


