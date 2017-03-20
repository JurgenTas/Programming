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
# Predict the house price in Boston from house details

data("BostonHousing")
df <- BostonHousing
head(df)
summary(df)

df.hex <- as.h2o(df)

# pick a response for the supervised problem
response <- "medv"

# use all other columns (except for the response) as predictors
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
# build model:

grid <-
  h2o.grid(
    "glm",
    grid_id = "grid",
    hyper_params = list(alpha = list(
      list(0), list(.25), list(.5), list(.75), list(1)
    )),
    y = response,
    x = predictors,
    training_frame = h2o.rbind(train, valid),
    family = "gaussian",
    nfolds = 5,
    seed = 1234
  )

################################################################################
################################################################################
# analyze results:

# sort by R2:
sorted_grid <- h2o.getGrid(grid_id = "grid", sort_by = "r2")
print(sorted_grid)

# get best model:
best_model <- h2o.getModel(sorted_grid@model_ids[[1]])
summary(best_model)

# out-of-sample:
perf <- h2o.performance(best_model, test)
print(perf)

################################################################################
################################################################################
# clear objects & shutdown of H2O:

rm(list = ls())
h2o.shutdown(prompt = FALSE)

################################################################################
################################################################################