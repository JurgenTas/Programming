__author__ = 'J Tas'


import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm


def generate():
    n = 1000
    xp = np.random.random((n, 2))
    yp = []

    for x in xp:
        if x[0] / x[1] <= 1:
            yp.append(-1)
        else:
            yp.append(1)
    return xp, np.asarray(yp)


def fit(xp, yp, **kwargs):
    clf = svm.SVC(**kwargs)
    clf.fit(xp, yp)
    return clf


def plot(x, y, clf):
    """
    Plot the maximum margin separating hyperplane within
    a two-class separable dataset using a Support Vector Machines
    classifier with linear kernel.
    """

    # get the separating hyperplane:
    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(0, 1)
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
    xp, yp = generate()
    clf = fit(xp, yp, kernel='linear')
    plot(xp, yp, clf)


if __name__ == "__main__":
    main()
