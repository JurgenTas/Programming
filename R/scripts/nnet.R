############################################################################################
############################################################################################
#libraries:

rm(list = ls())
library(mlbench)
library(caret)
library(nnet)
library(randomForest)
library(pROC)
library(doMC)
registerDoMC(cores = detectCores())

############################################################################################
############################################################################################
#data handling:

data("PimaIndiansDiabetes")
df <- PimaIndiansDiabetes[, 1:9]
df <- na.omit(df)
df[, 1:8] <- sapply(df[, 1:8], as.numeric)
head(df)
summary(df)
table(df$diabetes)

############################################################################################
############################################################################################
#create partitions:

set.seed(123)
id <- createDataPartition(df$diabetes, p = 0.75, list = FALSE)
training <- df[id,]
testing  <- df[-id,]
x.train <- training[, 1:8]
y.train <- training$diabetes
x.test <- testing[, 1:8]
y.test <- testing$diabetes

############################################################################################
############################################################################################
#build models:

stats <- function(...)
  c(twoClassSummary(...), defaultSummary(...)) #wrapper function

ctrl <-
  trainControl(
    method = "repeatedcv",
    number = 10,
    repeats = 10,
    classProbs = TRUE,
    summaryFunction = stats
  )

metric <- "Kappa"
grid <- expand.grid(.decay = c(0.5, 0.75, 1), .size = c(1:15))

model <-
  train(
    x = x.train,
    y = y.train,
    method = "nnet",
    preProc = c("center", "scale"),
    metric = metric,
    tuneGrid = grid,
    trace = FALSE,
    trControl = ctrl
  )

model.ref <-
  train(
    x = x.train,
    y = y.train,
    method = "rf",
    preProc = c("center", "scale"),
    metric = metric,
    trace = FALSE,
    trControl = ctrl
  )

############################################################################################
############################################################################################
#display results:

summary(model)
plot(model)
pred <- predict(model, newdata = x.test)
confusionMatrix(pred, y.test)

pred.probs <- predict(model, x.test, type = "prob")
x <- as.numeric((y.test == "pos") * 1)
obj.roc <- roc(x,  y.test)
plot.roc(
  obj.roc,
  type = "l",
  print.thres = c(0.5, 0.6, 0.7),
  grid = TRUE,
  print.auc = TRUE
)

resamps <- resamples(list(NNET = model, RF = model.ref))
summary(resamps)
dotplot(resamps, layout = c(1, 4))

############################################################################################
############################################################################################
