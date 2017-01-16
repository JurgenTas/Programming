############################################################################################
############################################################################################
#libraries:

rm(list = ls())
library(mlbench)
library(h2oEnsemble)
library(devtools)

############################################################################################
#connect to h20 cluster:

h2o.init(nthreads = -1)
h2o.removeAll() ## clean slate - just in case the cluster was already running

############################################################################################
#data handling:

data("PimaIndiansDiabetes")
df <- PimaIndiansDiabetes[, 1:9]
df <- na.omit(df)
df[, 1:8] <- sapply(df[, 1:8], as.numeric)
head(df)
summary(df)
table(df$diabetes)
df.hex <- as.h2o(df)

## pick a response for the supervised problem
response <- "diabetes"

## the response variable is an integer, we will turn it into a categorical/factor 
# for binary classification
df.hex[[response]] <- as.factor(df.hex[[response]])

## use all other columns (except for the name) as predictors
predictors <- setdiff(names(df.hex), c(response))

############################################################################################
#build model:

splits <- h2o.splitFrame(df.hex, c(0.6,0.2), seed=1234)
train  <- h2o.assign(splits[[1]], "train.hex") # 60%
valid  <- h2o.assign(splits[[2]], "valid.hex") # 20%
test   <- h2o.assign(splits[[3]], "test.hex")  # 20%

m1 <- h2o.deeplearning(
  model_id="dl_model_tuned", 
  training_frame=train, 
  validation_frame=valid, 
  x=predictors, 
  y=response, 
  overwrite_with_best_model=F,    ## Return the final model after 10 epochs, even if not the best
  hidden=c(128,128,128),          ## more hidden layers -> more complex interactions
  epochs=10,                      ## to keep it short enough
  score_validation_samples=10000, ## downsample validation set for faster scoring
  score_duty_cycle=0.025,         ## don't score more than 2.5% of the wall time
  adaptive_rate=F,                ## manually tuned learning rate
  rate=0.01, 
  rate_annealing=2e-6,            
  momentum_start=0.2,             ## manually tuned momentum
  momentum_stable=0.4, 
  momentum_ramp=1e7, 
  l1=1e-5,                        ## add some L1/L2 regularization
  l2=1e-5,
  max_w2=10                       ## helps stability for Rectifier
) 
summary(m1)

h2o.performance(m1, train=T)          ## sampled training data (from model building)
h2o.performance(m1, valid=T)          ## sampled validation data (from model building)
h2o.performance(m1, newdata=train)    ## full training data
h2o.performance(m1, newdata=valid)    ## full validation data
h2o.performance(m1, newdata=test)     ## full test data

pred <- h2o.predict(m1, test)
pred
test$Accuracy <- pred$predict == test$Class
1-mean(test$Accuracy)

h2o.shutdown(prompt=FALSE)
############################################################################################
############################################################################################

