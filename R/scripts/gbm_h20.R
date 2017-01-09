############################################################################################
############################################################################################
#libraries:

rm(list = ls())
library(mlbench)

############################################################################################
#connect to h20 cluster:

h2o.init(nthreads = -1, max_mem_size = "2G")
h2o.removeAll() ## clean slate - just in case the cluster was already running

############################################################################################
#data handling:

data("BreastCancer")
df <- BreastCancer[, 2:11]
df <- na.omit(df)
df[, 1:9] <- sapply(df[, 1:9], as.numeric)
head(df)
summary(df)
table(df$Class)
df.hex <- as.h2o(df)

## pick a response for the supervised problem
response <- "Class"

## the response variable is an integer, we will turn it into a categorical/factor 
# for binary classification
df.hex[[response]] <- as.factor(df.hex[[response]])

## use all other columns (except for the name) as predictors
predictors <- setdiff(names(df.hex), c(response))

############################################################################################
#build model:

splits <- h2o.splitFrame(
  data = df.hex, 
  ratios = c(0.6,0.2),   ## only need to specify 2 fractions, the 3rd is implied
  destination_frames = c("train.hex", "valid.hex", "test.hex"), seed = 1234
)
train <- splits[[1]]
valid <- splits[[2]]
test  <- splits[[3]]
############################################################################################

gbm <-
  h2o.gbm(
    x = predictors,
    y = response,
    training_frame = h2o.rbind(train, valid),
    nfolds = 4,
    seed = 1234
  )

gbm@model$cross_validation_metrics_summary
h2o.auc(h2o.performance(gbm, xval = TRUE))

############################################################################################
############################################################################################



