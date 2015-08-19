# coding=utf-8
__author__ = 'J Tas'

import scipy.optimize as opt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np


# The Rosenbrock function
def f(params):
    x, y = params
    return .5 * (1 - x) ** 2 + (y - x ** 2) ** 2


def optimize(f, x0, n, **kwargs):
    """
    Minimization of scalar function of one or more variables
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
        return opt.minimize(f, x0, method="BFGS", **kwargs)
    return None


def plot():
    x = np.outer(np.linspace(-1, 1, 50), np.ones(50))
    y = x.copy().T
    z = f([x, y])
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, z, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0)
    fig.add_axes(ax)
    plt.show()


def main():
    plot()
    x0 = [2, 2]
    s = optimize(g, x0, 1)
    print(s.message)
    print(s.x)


if __name__ == "__main__":
    main()
