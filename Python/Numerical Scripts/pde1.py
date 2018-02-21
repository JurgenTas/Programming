"""
Solves the Poisson equation (elliptic PDE): https://en.wikipedia.org/wiki/Poisson%27s_equation 

Set-up: two (rectangular-shaped) charges are placed in a two-dimensional box. The potential is zero on the walls and
the charges have opposite sized densities.
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Globals:
M = 500  # Number of grid points per side
OMEGA = 0.9  # Parameters to determine over-relaxation
ITER = 7500  # Maximum number of iterations
L = 1
TOL = 1e-4  # Target accuracy


def solve(x):
    """
    Solve using the Gauss-Seidel method (using 'overelaxation').
    """
    errs = []
    dx = L / M  # grid spacing
    c1 = (dx ** 2)
    c2 = (1 + OMEGA)
    for _ in range(ITER):
        err = 0
        for i in range(1, M):
            for j in range(1, M):
                diff = (x[i + 1, j] + x[i - 1, j] + x[i, j + 1] + x[i, j - 1] + c1 * f(i, j, dx)) / 4 - x[i, j]
                x[i, j] += c2 * diff
                err = max(err, abs(diff))
        errs.append(err)
        if errs[-1] < TOL:
            break
    print("Final error: {} ".format(errs[-1]))
    return x, errs


def f(i, j, dx):
    """
    Helper function to model the four (square) charges.
    """
    x, y = float(i * dx), float(j * dx)
    if 0.2 < x < 0.8 and 0.2 < y < 0.4:
        return 1
    elif 0.2 < x < 0.8 and 0.6 < y < 0.8:
        return -1
    else:
        return 0


def plot(x, y, z):
    x, y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = Axes3D(fig)
    surf = ax.plot_surface(x, y, z, rstride=3, cstride=3, linewidth=0.3, cmap="coolwarm")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('u')
    ax.view_init(30, 45)

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()


def main():
    z0 = np.zeros([M + 1, M + 1], float)
    z, errs = solve(z0)

    # plot results:
    x = np.linspace(0, 1, M + 1)
    y = np.linspace(0, 1, M + 1)
    plot(x, y, z)


if __name__ == "__main__":
    main()
