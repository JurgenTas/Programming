# prevalance = 0.1%
# assume there are 100000 visits in total, i.e., population=100000
# sensitivity=99% => TP=99, FN=1
TP <- 99
FN <- 1

# population=100000 => FP+TN=99000
# specificity=99% => TN=0.99*99000=98901, therefore FP=999
TN <- 0.99 * 99900
FP <- 99900 - TN
FP

# what being asked is positive predictive value (PPV), which is, what is the
# probability of a click happens in a specific visit, given that the
# predicted outcome is positive.
# PPV=TP/(TP+FP)
PPV <- TP / (TP + FP)
PPV
