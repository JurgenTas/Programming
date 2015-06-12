#-------------------------------------------------------------------------------------------------------
# Question 1:
# Load the Alzheimer's disease data using the commands:
library(AppliedPredictiveModeling)
library(caret)
data(AlzheimerDisease)

# The following commands will create training and test sets with 
# about 50% of the observations assigned to each:
adData = data.frame(diagnosis,predictors)
trainIndex = createDataPartition(diagnosis,p=0.5,list=FALSE)
training = adData[trainIndex,]
testing = adData[-trainIndex,]

#-------------------------------------------------------------------------------------------------------
# Question 2:
# Load the cement data using the commands:
library(AppliedPredictiveModeling)
data(concrete)
library(caret)
set.seed(1000)
inTrain = createDataPartition(mixtures$CompressiveStrength, p = 3/4)[[1]]
training = mixtures[ inTrain,]
testing = mixtures[-inTrain,]

# There are a large number of values that are the same and even if you took the log(SuperPlasticizer + 1) 
# they would still all be identical so the distribution would not be symmetric.
x = training$Superplasticizer + 1
x = log(x)
hist(x)

#-------------------------------------------------------------------------------------------------------
# Question 3:
# Load the Alzheimer's disease data using the commands:
library(caret)
library(AppliedPredictiveModeling)
set.seed(3433)
data(AlzheimerDisease)
adData = data.frame(diagnosis,predictors)
inTrain = createDataPartition(adData$diagnosis, p = 3/4)[[1]]
training = adData[ inTrain,]
testing = adData[-inTrain,]

# Find all the predictor variables in the training set that begin with IL:
sub_set = adData[ , grepl( '^IL' , names( adData ) )]

# Calculates the number of principal components needed to capture 90% of the variance:
pp = preProcess(sub_set, method="pca",thres=.9)
pp

#-------------------------------------------------------------------------------------------------------
# Question 4
# Load the Alzheimer's disease data using the commands:
library(caret)
library(AppliedPredictiveModeling)
set.seed(3433)
data(AlzheimerDisease)
adData = data.frame(diagnosis,predictors)
inTrain = createDataPartition(adData$diagnosis, p = 3/4)[[1]]
training = adData[ inTrain,]
testing = adData[-inTrain,]

# Create a training/testing data set consisting of only the predictors with variable names beginning 
# with IL and the diagnosis.
training_sub = data.frame(training$diagnosis, training[, grepl( '^IL' , names( adData ) ) ])
testing_sub = data.frame(testing$diagnosis, testing[, grepl( '^IL' , names( adData ) ) ])

# Build two predictive models, one using the predictors as they are and one using PCA 
# with principal components explaining 80% of the variance in the predictors. 
# Use method="glm" in the train function.

# model 1:
pp1 = preProcess(training_sub [,-1], method=c("center","scale"))
train1 = predict(pp1,training_sub [,-1]) 
model1 = train(training$diagnosis ~ .,method="glm",data=train1)
# make predictions:
pred_model1 = predict(pp1, testing_sub[,-1])
# compare results: 
confusionMatrix(testing$diagnosis,predict(model1, pred_model1))

# model 2:
pp2 = preProcess(training_sub [,-1], method="pca",thres=.8)
train2 = predict(pp2,training_sub [,-1])
model2 = train(training$diagnosis ~ .,method="glm",data=train2)
# make predictions:
pred_model2 = predict(pp2, testing_sub[,-1])
# compare results:
confusionMatrix(testing$diagnosis,predict(model2, pred_model2))




