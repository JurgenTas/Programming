############################################################################################
############################################################################################
#libraries:

rm(list = ls())
library(mlbench)
library(caret)
library(kernlab)
library(pROC)

############################################################################################
#data handling:

data("BreastCancer")
df <- BreastCancer[, 2:11]
df <- na.omit(df)
df[, 1:9] <- sapply(df[, 1:9], as.numeric)
head(df)
summary(df)
table(df$Class)

############################################################################################
#create partitions:

set.seed(123)
id <- createDataPartition(df$Class, p = .75, list = FALSE)
training <- df[id,]
testing  <- df[-id,]

############################################################################################
#build models:

ctrl <-
  trainControl(
    method = "repeatedcv",
    number = 10,
    repeats = 3,
    classProbs = TRUE,
    summaryFunction = twoClassSummary
  )

svm <-
  train(
    x = training[, 1:9],
    y = training$Class,
    method = "svmRadial",
    preProc = c("center", "scale"),
    metric = "ROC",
    trControl = ctrl
  )

grid <-
  expand.grid(sigma = c(.005, .001, .015, 0.02),
              C = 2 ^ seq(-2, 1, length = 15))

svm.tune <-
  train(
    x = training[, 1:9],
    y = training$Class,
    method = "svmRadial",
    preProc = c("center", "scale"),
    metric = "ROC",
    tuneGrid = grid,
    trControl = ctrl
  )

############################################################################################
#display results:

summary(svm)
summary(svm.tune)

pred.svm <- predict(svm, newdata = testing[, 1:9])
pred.svm.tune <- predict(svm.tune, newdata = testing[, 1:9])

confusionMatrix(pred.svm, testing$Class)
confusionMatrix(pred.svm.tune, testing$Class)

resamps <- resamples(list(SVM = svm, SVM.TUNE = svm.tune))
summary(resamps)
trellis.par.set(theme1)
bwplot(resamps, layout = c(3, 1))

############################################################################################
############################################################################################
