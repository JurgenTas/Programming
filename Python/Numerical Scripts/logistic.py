# coding=utf-8
__author__ = 'J Tas'

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score

# =====================================================================


def fit(x, y):
    # evaluate the model by splitting into train and test sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    model = LogisticRegression()
    model.fit(x_train, y_train)

    # predict class labels for the test set
    predicted = model.predict(x_test)
    print(predicted)

    # generate class probabilities
    pr = model.predict_proba(x_test)
    print(pr)

    # generate evaluation metrics
    print(metrics.accuracy_score(y_test, predicted))
    print(metrics.roc_auc_score(y_test, pr[:, 1]))
    print(metrics.confusion_matrix(y_test, predicted))
    print(metrics.classification_report(y_test, predicted))

    # evaluate the model using 10-fold cross-validation
    scores = cross_val_score(LogisticRegression(), x, y, scoring='accuracy', cv=10)
    print(scores)
    print(scores.mean())


# =====================================================================


def load():
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
    y = df.iloc[:, 4].values
    y = np.where(y == 'Iris-setosa', -1, 1)
    x = df.iloc[:, 0:1].values
    return (x - x.mean(axis=0) / x.std(axis=0)), y


# =====================================================================


def main():
    x, y = load()
    fit(x, y)


if __name__ == "__main__":
    main()
