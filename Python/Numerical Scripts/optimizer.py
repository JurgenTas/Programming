# coding=utf-8
__author__ = 'J Tas'

import scipy.optimize as opt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np


# =====================================================================


# The Rosenbrock function
def g(x):
    a = 1
    b = 100
    return (a - x[0]) ** 2 + b * (x[1] - x[0] ** 2) ** 2


def h(x):
    return -(2 * x[0] * x[1] + 2 * x[0] - x[0] ** 2 - 2 * x[1] ** 2)


# =====================================================================


def optimize_uncnstr(f, x0, n, **kwargs):
    """
    Unconstrained minimization of scalar function of one or more variables
    :param f: Objective function to be minimized.
    :param x0: Initial guess.
    :param fprime: Gradient of f.
    :return: The optimization result represented as a OptimizeResult object
    """
    if n == 1:  # Minimize a function using the Nelder-Mead algorithm.
        return opt.minimize(f, x0, method="Nelder-Mead", **kwargs)
    if n == 2:  # Minimize a function using modified Powell’s method.
        return opt.minimize(f, x0, method="Powell", **kwargs)
    if n == 3:  # Minimize a function using a nonlinear conjugate gradient algorithm.
        return opt.minimize(f, x0, method="CG", **kwargs)
    if n == 4:  # Minimize a function using the BFGS algorithm.
        return opt.minimize(f, x0, method="BFGS", **kwargs)
    if n == 5:  # Minimize a function using the Newton-CG method.
        return opt.minimize(f, x0, method="Newton-CG", **kwargs)
    return


def optimize_cnstr(f, x0, **kwargs):
    """
    Constrained minimization of scalar function of one or more variables. Uses Sequential Least Squares Programming
    to minimize a function of several variables with any combination of bounds, equality and inequality constraints.
    :param f: Objective function to be minimized.
    :param x0: Initial guess.
    :param fprime: Gradient of f.
    :return: The optimization result represented as a OptimizeResult object
    """
    return opt.minimize(f, x0, method="SLSQP", **kwargs)


# =====================================================================


def plot():
    x = np.outer(np.linspace(-1, 1, 50), np.ones(50))
    y = x.copy().T
    z = g([x, y])
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, z, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0)
    fig.add_axes(ax)
    plt.show()


def optimize1():
    """ Unconstrained optimization """
    x0 = [0, 2.5]
    ux = optimize_uncnstr(g, x0, 1)
    print(ux)


def optimize2():
    """ Constrained optimization """
    cons = ({'type': 'eq', 'fun': lambda x: np.array([x[0] ** 3 - x[1]]),
             'jac': lambda x: np.array([3.0 * (x[0] ** 2.0), -1.0])},
            {'type': 'ineq',
             'fun': lambda x: np.array([x[1] - (x[0] - 1) ** 4 - 2])})
    bnds = ((0.5, 1.5), (1.5, 2.5))
    x0 = [0, 2.5]
    cx = optimize_cnstr(h, x0, bounds=bnds, constraints=cons)
    print(cx)


# =====================================================================


def main():
    plot()
    optimize1()
    optimize2()


if __name__ == "__main__":
    main()
