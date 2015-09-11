__author__ = 'J Tas'

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def generate(a, b, n):
    """
    :param a: lower endpoint
    :param b: upper endpoint
    :param n: number of points
    :return: return 2D uniformly distr. points
    """
    return np.random.uniform(a, b, (n, 2))


def cluster(x, **kwargs):
    """
    :param x: 2D data points
    :return: use KMeans to cluster data
    """
    return KMeans(**kwargs).fit(x)


def plot(x, y):
    """
    :param x: 2D data points
    :param y: cluster
    :return: show clustered data
    """
    plt.scatter(x[:, 0], x[:, 1], c=y)
    plt.show()


def main():
    x = generate(-1, 1, 30000)
    y = cluster(x, n_clusters=10)
    plot(x, y.labels_)


if __name__ == "__main__":
    main()
