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
# Predict high-energy structures in the atmosphere from antenna data.

data(Ionosphere)
df <- Ionosphere[, 1:35]
df <- na.omit(df)
df[, 1:34] <- sapply(df[, 1:34], as.numeric)
head(df)
summary(df)
table(df$Class)
df.hex <- as.h2o(df)

# pick a response for the supervised problem
response <- "Class"

# IMPORTANT: encode the (binary) repsonse as a factor
df.hex[[response]] <- as.factor(df.hex[[response]])

# use all other columns (except for the response) as predictors
predictors <- setdiff(names(df.hex), c(response))

# data splits:
splits <- h2o.splitFrame(
  data = df.hex,
  ratios = c(0.7, 0.1),
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

hyper_params <-
  list(
    balance_classes = c(TRUE, FALSE),
    hidden = list(c(100, 100), c(200, 200)),
    activation = c("RectifierWithDropout", "RectifierWithDropout", "Tanh"),
    l1 = c(0, 1e-5),
    l2 = c(0, 1e-5)
  )

search_grid <- h2o.grid(
  "deeplearning",
  grid_id = "grid",
  x = predictors,
  y = response,
  training_frame = h2o.rbind(train, valid),
  nfolds = 5,
  seed = 1234,
  hyper_params = hyper_params
)

# get the grid results, sorted by auc:
search_grid <- h2o.getGrid(grid_id = "grid",
                           sort_by = "auc",
                           decreasing = TRUE)

# get the best performing model and evaluate on test set:
best_model <- h2o.getModel(search_grid@model_ids[[1]])
summary(best_model)

# out-of-sample
perf <- h2o.performance(model = best_model, newdata = test)
h2o.confusionMatrix(perf)

################################################################################
################################################################################
# clear objects & shutdown of H2O:

rm(list = ls())
h2o.shutdown(prompt = FALSE)

################################################################################
################################################################################


