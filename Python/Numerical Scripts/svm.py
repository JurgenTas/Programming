__author__ = 'J Tas'

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.svm


def load():
    """
    Load default data
    """
    df = pd.read_csv('https://d1pqsl2386xqi9.cloudfront.net/notebooks/Default.csv', index_col=0)
    df.info()
    df1 = df[(df.default == "Yes")]
    df2 = df[(df.default == "No")].sample(n=len(df1.index))
    df3 = df1.append(df2)
    d = {'Yes': 1, 'No': 0}
    x1 = df3.ix[:, 'balance'].values.tolist()
    x1_max = max(x1)
    x1_norm = [float(z) / x1_max for z in x1]
    x2 = df3.ix[:, 'income'].values.tolist()
    x2_max = max(x2)
    x2_norm = [float(z) / x2_max for z in x2]
    x = list(zip(x1_norm, x2_norm))
    print(x)
    y = df3.ix[:, 'default'].map(d).values.tolist()
    return x, y


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
    x1 = [row[0] for row in x]
    x2 = [row[1] for row in x]
    plt.scatter(x1, x2, c=y, cmap=plt.cm.Paired)
    plt.axis('tight')
    plt.ylim(0, 1)
    plt.show()


def main():
    x, y = load()
    clf = fit(x, y, kernel='linear')
    print(clf)
    plot(x, y, clf)


if __name__ == "__main__":
    main()
