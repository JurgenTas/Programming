# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 09:16:54 2015

@author: J Tas
"""

import itertools

import matplotlib.pyplot as plt
import numpy as np

# =====================================================================
# Globals

items = 5
score = []  # scores (to be defined in main)
alpha = [1, 1, 1, 1, 1]  # alpha's
delta = [-1.9, -0.6, -0.25, 0.30, 0.45]  # deltas's


# =====================================================================

def logistic(x, alpha, delta):
    """
    One parameter logistic (1PL) model
    """
    arg = np.exp(alpha * (x - delta))
    return arg / (1 + arg)


def f(x):
    """
    Log likelihood function
    """
    i, res = 0, 0.0
    while i < items:
        arg = logistic(x, alpha[i], delta[i])
        p = score[i] * np.log(arg) + (1.0 - score[i]) * np.log(1.0 - arg)
        res += p
        i += 1
    return res


def d1f(x, h=1.e-6):
    """
    First derivative: based on central diff. approx.
    See: https://en.wikipedia.org/wiki/Finite_difference
    """
    arg = f(x + h) - f(x - h)
    return arg / (2 * h)


def d2f(x, h=1.e-6):
    """
    Second derivative: based on central diff. approx.
    See: https://en.wikipedia.org/wiki/Finite_difference
    """
    arg = f(x + h) - 2.0 * f(x) + f(x - h)
    return arg / (h * h)


# =====================================================================

def plot():
    x0 = -3
    x1 = 3
    xp = np.linspace(x0, x1, 100)
    yp = f(xp)
    plt.plot(xp, yp, 'r')
    plt.show()


# =====================================================================

def newton(func, dfunc, x0=1, tol=1E-6, n=20, debug=False):
    """
    Newton's algorithm
    """
    i = 1
    while i <= n:
        x1 = x0 - (func(x0) / dfunc(x0))
        if debug:
            print("iteration: ", i, " value: ", x1)
        if abs(x1 - x0) < tol:
            return x1
        else:
            x0 = x1
            i += 1
    return False


# =====================================================================

def main():
    scores = itertools.product(range(2), repeat=5)  # create score combinations
    global score
    for s in scores:
        score = s
        res = newton(d1f, d2f, x0=0.0)
        print("Score vector:", score, "; result:", res)


if __name__ == "__main__":
    main()
