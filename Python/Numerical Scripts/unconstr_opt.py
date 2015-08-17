__author__ = 'J Tas'

import scipy.optimize as opt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np


def optimize(func, x0, name, **kwargs):
    """
    :param f: a callable function
    :param x0: initial value used to start the algorithm
    :param name: algorithm type
    :param kwargs: see http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
    """

    if name == "fmin_bfgs":
        print("Minimization of scalar function of one or more variables using the BFGS algorithm.")
        return opt.fmin(func, x0, **kwargs)
    if name == "fmin_cg":
        print("Minimization of scalar function of one or more variables using the Conjugate Gradient algorithm.")
        return opt.fmin_cg(func, x0, **kwargs)
    if name == "fmin_ncg":
        print("Minimization of scalar function of one or more variables using the Newton-CG algorithm.")
        return opt.fmin_ncg(func, x0, **kwargs)
    if name == "fmin_powell":
        print("Minimization of scalar function of one or more variables using the Powell algorithm.")
        return opt.fmin_powell(func, x0, **kwargs)
    print("Skipping optimization")

    return


def f(params):
    """
    Rosenbrock's banana function
    :param params: x, y values
    :return: function value
    """
    a = 1
    b = 100
    x, y = params
    return ((a - x) ** 2) + b * ((y - x ** 2) ** 2)


def main():
    # plot:
    x = np.outer(np.linspace(-1, 1, 30), np.ones(30))
    y = x.copy().T
    z = f([x, y])
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, z, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0)
    fig.add_axes(ax)
    plt.show()

    # optimize:
    arr = np.array([-1, 1])
    ans = optimize(f, arr, "fmin_bfgs", disp=True)
    print(ans)


if __name__ == "__main__":
    main()
