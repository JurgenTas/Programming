################################################################################
################################################################################
############################## author: Jurgen Tas ##############################
################################################################################
################################################################################
# load libraries, set path etc.

rm(list = ls())

library(mlbench)
library(h2o)
library(plotly)
library(ggplot2)
library(reshape)
library(data.table)

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
# The database consists of the multi-spectral values of pixels in 3x3
# neighbourhoods in a satellite image, and the classification associated with
# the central pixel in each neighbourhood. The aim is to predict this 
# classification, given the multi-spectral values.

data(Satellite)
df <- Satellite[, 1:37]
df <- na.omit(df)
df[, 1:36] <- sapply(df[, 1:36], as.numeric)
head(df)
summary(df)
df$classes <- as.factor(df$classes)
table(df$classes)

t1 <- Sys.time()
df.hex <- as.h2o(df)
t2 <- Sys.time()
t2 - t1

## pick a response variable
response <- "classes"

## use all other columns (except for the response variable) as predictors
predictors <- setdiff(names(df.hex), c(response))
summary(df.hex)

################################################################################
################################################################################
# 'hockeystick' method to determine optimal number of columns:
# https://en.wikipedia.org/wiki/Elbow_method_(clustering)

# determine k
df.res <- data.frame(
  No_Cluster = numeric(),
  TotWithinSS = numeric(),
  # the percentage of variance explained by clusters
  stringsAsFactors = FALSE
)

max.iter = 15
t1 <- Sys.time()
for (i in 2:max.iter) {
  km.model <- h2o.kmeans(
    training_frame = df.hex,
    k = i,
    x = predictors,
    init = "Random",
    seed = 123,
    max_iterations = 1000,
    nfolds = 10
  )
  df.res[i - 1, 1] <- i
  df.res[i - 1, 2] <-
    getTotWithinSS(km.model) # sum of squared distances within each cluster mean
}
t2 <- Sys.time()
difftime(t2, t1, units = "secs")

# plot the "hockeystick":
df.res <- melt(df.res, id = c("No_Cluster"))
p <- ggplot(data = df.res , aes(x = No_Cluster, y = value)) +
  geom_point(aes(text = paste("SS:", variable)), size = 1) +
  geom_smooth(aes(colour = variable, fill = variable))
(gg <- ggplotly(p))

################################################################################
################################################################################
# single kmeans:

nrcluster <- 6
km.model.single <-
  h2o.kmeans(
    training_frame = df.hex,
    x = predictors,
    init = "Random",
    k = nrcluster,
    seed = 123,
    nfolds = 10,
    max_iterations = 1000
  )

summary(km.model.single)
single_pred.hex = h2o.predict(object = km.model.single, newdata = df.hex)

# bind clusters with data:
dt.result = as.data.table(h2o.cbind(df.hex, single_pred.hex))
dt.centers = as.data.table(km.model.single@model$centers)

# # write output:
# write.csv(dt.result,
#           file = "result.csv",
#           append = TRUE,
#           sep = ",")
# 
# # write output:
# write.csv(dt.centers,
#           file = "result_centers.csv",
#           append = TRUE,
#           sep = ",")

################################################################################
################################################################################
# visualization (3D PCA plot):

data <- as.matrix(scale(dt.result[,-c("classes", "predict")]))
pca <- princomp(data, cor = T)
print(pca)
summary(pca)
df.pca <-
  as.data.frame(cbind(pca$scores[, 1:3], as.character(dt.result$predict)))

p <- plot_ly(
  df.pca,
  x = ~ Comp.1,
  y = ~ Comp.2,
  z = ~ Comp.3,
  color = ~ V4,
  mode = "markers",
  marker = list(size = 3.5, opacity = 0.7),
  showlegend = TRUE,
  colors = c(
    "#874bc6",
    "#b44f40",
    "#b34d8a",
    "#6f7fb0",
    "#609c57",
    "#b79046"
  )
  # see: http://tools.medialab.sciences-po.fr/iwanthue/
) %>%
  add_markers() %>%
  layout(scene = list(
    xaxis = list(title = 'PCA1'),
    yaxis = list(title = 'PCA2'),
    zaxis = list(title = 'PCA3')
  ))
p

################################################################################
################################################################################
# clear objects & shutdown of H2O:

rm(list = ls())
h2o.shutdown(prompt = FALSE)

################################################################################
################################################################################



