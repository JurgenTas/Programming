################################################################################
################################################################################
############################## author: Jurgen Tas ##############################
################################################################################
################################################################################
# load libraries, set path etc.

rm(list = ls())

library(mlbench)
library(h2o)

path <- dirname(rstudioapi::getActiveDocumentContext()$path)
setwd(path)

################################################################################
################################################################################
# connect to H2O cluster:

h2o.init(
  nthreads = -1,
  max_mem_size = "8g",
  ip = "localhost",
  startH2O = TRUE
)
h2o.removeAll() # clean slate - just in case the cluster was already running

################################################################################
################################################################################
# Wisconsin Breast Cancer Database
# The objective is to identify each of a number of benign or malignant classes.

data("BreastCancer")
df <- BreastCancer[, 2:11]
df <- na.omit(df)
df[, 1:9] <- sapply(df[, 1:9], as.numeric)
head(df)
summary(df)
table(df$Class)
df.hex <- as.h2o(df)

# pick a response for the supervised problem
response <- "Class"

# IMPORTANT: encode the (binary) repsonse as a factor
df.hex[[response]] <- as.factor(df.hex[[response]])

# use all other columns (except for the name) as predictors
predictors <- setdiff(names(df.hex), c(response))

# data splits:
splits <- h2o.splitFrame(
  data = df.hex,
  ratios = c(0.8, 0.1),
  ## only need to specify 2 fractions, the 3rd is implied
  destination_frames = c("train.hex", "valid.hex", "test.hex"),
  seed = 1234
)
train <- splits[[1]]
valid <- splits[[2]]
test  <- splits[[3]]

################################################################################
################################################################################
# build model

# number of trees to grow
ntrees <- c(250, 500, 100)

# number of variables randomly sampled as candidates
# at each split
mtries <- c(2, 3, 4)

rf_grid <- h2o.grid(
  "randomForest",
  grid_id = "rf_grid",
  x = predictors,
  y = response,
  training_frame = h2o.rbind(train, valid),
  nfolds = 4,
  seed = 1234,
  hyper_params = list(ntrees = ntrees, mtries = mtries)
)

# get the grid results, sorted by AUC
rf_perf <- h2o.getGrid(grid_id = "rf_grid",
                       sort_by = "auc",
                       decreasing = TRUE)

# get the best performing model and evaluate on test set:
best_model <- h2o.getModel(rf_perf@model_ids[[1]])
summary(best_model)
perf <- h2o.performance(model = best_model, newdata = test)
h2o.confusionMatrix(perf)

################################################################################
################################################################################
# clear objects & shutdown of H2O:

rm(list = ls())
h2o.shutdown(prompt = FALSE)

################################################################################
################################################################################








