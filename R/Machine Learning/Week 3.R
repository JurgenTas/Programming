#-----------------------------------------------------------------------------------------------
# Question 1
# Load the cell segmentation data from the AppliedPredictiveModeling package using the commands:
library(AppliedPredictiveModeling)
data(segmentationOriginal)
library(caret)

# Subset the data to a training set and testing set based on the Case variable in the data set: 
inTrain = grep("Train",segmentationOriginal$Case)
train = segmentationOriginal[inTrain,]
test= segmentationOriginal[-inTrain,]

# Set the seed to 125 and fit a CART model with the rpart 
# method using all predictor variables and default caret settings: 
set.seed(125)
modFit = train(Class ~ ., data=train[, 3:119], method="rpart")
# print the classification tree
print(modFit$finalModel)
# plot the classification tree
library(rattle)
fancyRpartPlot(modFit$finalModel)

# In the final model what would be the final model prediction for cases with the following variable values:
# a. TotalIntench2 = 23,000; FiberWidthCh1 = 10; PerimStatusCh1=2  => PS
# b. TotalIntench2 = 50,000; FiberWidthCh1 = 10;VarIntenCh4 = 100  => WS
# c. TotalIntench2 = 57,000; FiberWidthCh1 = 8;VarIntenCh4 = 100  => PS
# d. FiberWidthCh1 = 8;VarIntenCh4 = 100; PerimStatusCh1=2 => ?

#-----------------------------------------------------------------------------------------------
# Question 3
# Load the olive oil data using the commands:
library(pgmm)
data(olive)
olive = olive[,-1]
# fit classification tree as a model
modFit <- train(Area ~ .,method="rpart",data=olive)
# print the classification tree
print(modFit$finalModel)
# plot the classification tree
library(rattle)
fancyRpartPlot(modFit$finalModel)
newdata = as.data.frame(t(colMeans(olive)))
predict(modFit,newdata=newdata[-1])

#-----------------------------------------------------------------------------------------------
# Question 4
# Load the South Africa Heart Disease Data and create training and test sets with the following code:
library(ElemStatLearn)
data(SAheart)
set.seed(8484)
train = sample(1:dim(SAheart)[1],size=dim(SAheart)[1]/2,replace=F)
trainSA = SAheart[train,]
testSA = SAheart[-train,]

#set the seed to 13234 and fit a logistic regression model (method="glm", be sure to specify family="binomial") 
# with Coronary Heart Disease (chd) as the outcome and age at onset, current alcohol consumption, 
# obesity levels, cumulative tabacco, type-A behavior, and low density lipoprotein cholesterol as predictors. 
set.seed(13234)
modFit = train(chd ~ age + alcohol + obesity +tobacco + typea + ldl, method="glm", family="binomial", data=trainSA) 
missClass = function(values,prediction){sum(((prediction > 0.5)*1) != values)/length(values)}

missClass_train = missClass(trainSA$chd,predict(modFit,trainSA))
missClass_test = missClass(testSA$chd,predict(modFit,testSA))

#-----------------------------------------------------------------------------------------------
# Question 5
#Load the vowel.train and vowel.test data sets:
library(ElemStatLearn)
data(vowel.train)
data(vowel.test) 

#Set the variable y to be a factor variable in both the training and test set.
vowel.train$y=as.factor(vowel.train$y) 
vowel.test$y=as.factor(vowel.test$y) 
set.seed(33833)

#Fit a random forest predictor relating the factor variable y to the remaining variables.
rforrest = train(y ~ ., data=vowel.train, method="rf", prox=TRUE, ntree=500)
varImp(rforrest$finalModel)



