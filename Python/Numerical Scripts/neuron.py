# coding=utf-8
__author__ = 'J Tas'

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# =====================================================================


class Perceptron(object):
    """
    This class implements an algorithm (based on perceptron learning rule)
    for supervised learning of binary classifiers.
    """

    def __init__(self, eta=0.01, n=15):
        self.eta = eta
        self.n = n
        self.w = []
        self.error = []

    def train(self, xlist, ylist):
        """
        :type xlist: list of lists (i.e 2D list)
        :type ylist: list
        """
        self.w = [0] * len(xlist[0])  # init. weights
        for k in range(self.n):
            cnt = 0
            for x, y in zip(xlist, ylist):
                delta = y - self.predict(x)  # misclassification: != 0
                if delta != 0:
                    cnt += 1
                    for i, xi in enumerate(x):
                        self.w[i] += self.eta * delta * xi
            self.error.append(cnt)

    def predict(self, x):
        return 0 if np.dot(self.w, x) < 0.0 else 1

    def plot_classification_error(self):
        plt.plot(range(1, len(self.error) + 1), self.error, marker='o')
        plt.xlabel('Iterations')
        plt.ylabel('Missclassifications')
        plt.show()


class Adaline(object):
    """
    This class implements an algorithm (based on adaline learning rule)
    for supervised learning of binary classifiers.
    """

    def __init__(self, eta=0.01, n=15):
        self.eta = eta
        self.n = n

    def train(self, xlist, ylist):
        """
        :type xlist: list of lists (i.e 2D list)
        :type ylist: list
        """
        x = np.asarray(xlist)
        y = np.asarray(ylist)
        self.w = np.zeros(x.shape[1])
        for k in range(self.n):
            delta = y - self.predict(x)  # calculate delta
            print(np.sum(delta))
            self.w += self.eta * x.T.dot(delta)

    def predict(self, x):
        return np.where(np.dot(self.w, x.T) < 0.0, 0, 1)


# =====================================================================


def load():
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
    y = df.iloc[:, 4].values
    y = np.where(y == 'Iris-setosa', 0, 1)
    x = df.iloc[:, [0, 1, 2, 3]].values
    return (x - x.mean(axis=0) / x.std(axis=0)), y


def main():
    x, y = load()
    p = Perceptron()
    p.train(x, y)
    p.plot_classification_error()
    print(p.w)


if __name__ == "__main__":
    main()
