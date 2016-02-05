# Start up a parallel cluster
parallelCluster = parallel::makeCluster(parallel::detectCores())
print(parallelCluster)

# Single argument function we are
# going to pass to parallel
mkWorker = function(yName,vars,d) {
  force(yName)
  force(vars)
  force(d)
  
  # define any and every function our worker function
  # needs in this environment
  fitOneTargetModel = function(yName,yLevel,vars,data) {
    formula <-
      paste('(',yName,'=="',yLevel,'") ~ ',paste(vars,collapse = ' + '),sep = '')
    glm(as.formula(formula),family = binomial,data = data)
  }
  
  # Finally: define and return our worker function.
  # The function worker's "lexical closure"
  # (where it looks for unbound variables)
  # is mkWorker's activation/execution environment
  # and not the usual Global environment.
  # The parallel library is willing to transport
  # this environment (which it does not
  # do for the Global environment).
  worker = function(yLevel) {
    fitOneTargetModel(yName,yLevel,vars,d)
  }
  return(worker)
}

d = iris 
vars = c('Sepal.Length','Sepal.Width','Petal.Length')
yName = 'Species'
yLevels = sort(unique(as.character(d[[yName]])))
print(yLevels)
models = parallel::parLapply(parallelCluster,yLevels,mkWorker(yName,vars,d))
names(models) = yLevels
print(models)





