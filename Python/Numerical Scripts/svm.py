__author__ = 'J Tas'

import numpy as np
import matplotlib.pyplot as plt
import sklearn.svm
from sklearn.datasets.samples_generator import make_blobs
import random


def generate():
    """
    Generate sample data
    """
    np.random.seed(0)
    c1 = [random.uniform(-2, 2), random.uniform(-2, 2)] # center 1 (random chosen)
    c2 = [random.uniform(-2, 2), random.uniform(-2, 2)] # center 2 (random chosen)
    centers = [c1, c2]
    return make_blobs(n_samples=3000, centers=centers, cluster_std=0.2)


def fit(xp, yp, **kwargs):
    """
    Fit using svm.SVS function
    """
    clf = sklearn.svm.SVC(**kwargs)
    clf.fit(xp, yp)
    return clf


def plot(x, y, clf):
    """
    Plot the maximum margin separating hyperplane within
    a two-class separable dataset using a Support Vector Machines
    linear classifier.
    """

    # get the separating hyperplane:
    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(-2, 2)
    yy = a * xx - (clf.intercept_[0]) / w[1]

    # plot the parallels to the separating hyperplane
    # that pass through the support vectors
    b = clf.support_vectors_[0]
    yy_down = a * xx + (b[1] - a * b[0])
    b = clf.support_vectors_[-1]
    yy_up = a * xx + (b[1] - a * b[0])

    # plot the line, the points, and the
    # nearest vectors to the plane
    plt.plot(xx, yy, 'k-')
    plt.plot(xx, yy_down, 'k--')
    plt.plot(xx, yy_up, 'k--')
    plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=5, facecolors='none')
    plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.Paired)
    plt.axis('tight')
    plt.show()


def main():
    x, y = generate()
    clf = fit(x, y, kernel='linear')
    plot(x, y, clf)


if __name__ == "__main__":
    main()
