# coding=utf-8
__author__ = 'J Tas'

import math as mt

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize as opt


# =====================================================================

def jacobian(x, func, eps=1.e-8):
    """
    Computes forward-difference approximation to Jacobian.
    :param x: numpy array of size n
    :return: Jacobian matrix
    """
    n = len(x)
    xh = x
    fx = func(x)
    ans = np.empty((n, n))
    for j in range(0, n):

        temp = xh[j]
        h = eps * mt.fabs(temp)
        if h == 0.0:
            h = eps
        xh[j] = temp + h  # trick to reduce finite-precision error
        h = xh[j] - temp
        fh = func(xh)
        xh[j] = temp
        for i in range(0, n):
            ans[i][j] = (fh[i] - fx[i]) / h

    return ans


# =====================================================================

def f(x):
    """
    Multivariate vector function f
    :param x: argument vector
    :return: vector of function values
    """
    return [x[1] - 3 * x[0] * (x[0] + 1) * (x[0] - 1), .25 * x[0] ** 2 + x[1] ** 2 - 1]


def df(x):
    return jacobian(x, f)


def solve(func, x0, **kwargs):
    """
    Find a root of a vector function. Methods that can be used are:
    ‘hybr’, ‘lm’, ‘broyden1’, ‘broyden2’, ‘anderson’, ‘linearmixing’, ‘diagbroyden’,
    ‘excitingmixing’, ‘krylov’.
    :param f: multivariate vector function
    :param x0: initial guess
    :param kwargs: args=(), method='hybr', jac=None, tol=None, callback=None, options=None
    :return: The solution represented as a OptimizeResult object.
    """
    return opt.root(func, x0, **kwargs)


# =====================================================================

def power_series(x, *params):
    ans = 0
    for i, p in enumerate(params):
        ans += p * (x ** i)
    return ans


def g(x, a, b, c):
    return power_series(x, a, b, c)


def fit(func, x_data, y_data, **kwargs):
    """
    Use non-linear least squares to fit a function, f, to data.
    :param func: The model function, f(x, ...).
    :param x_data: The independent data
    :param y_data: The dependent data
    :param kwargs: p0=None, sigma=None, absolute_sigma=False, check_finite=True
    :return popt : array Optimal values for the parameters so that the sum of the squared error
    of f(xdata, *popt) - ydata is minimized
    :return pcov : 2d arrayThe estimated covariance of popt.
    """
    return opt.curve_fit(func, x_data, y_data, **kwargs)


# =====================================================================


def find_root():
    print(solve(f, (0.5, 0.5), jac=df))


def fit_curve():
    # create data (incl. random noise):
    x0 = 0.0
    x1 = 1.0
    n = 100
    xp = np.linspace(x0, x1, n)
    yp = np.exp(xp) * (1 + np.random.normal(0, 0.1, n))

    # fit curve
    p0 = (0, 0, 0)
    p_opt, p_cov = fit(g, xp, yp, p0=p0)

    # plot results:
    plt.scatter(xp, yp)
    model = g(xp, p_opt[0], p_opt[1], p_opt[2])
    plt.plot(xp, model, 'r')
    plt.show()


def main():
    find_root()
    fit_curve()


if __name__ == "__main__":
    main()
