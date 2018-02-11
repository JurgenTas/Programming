"""
Find a solution of the Poisson equation. Set-up: two (square) charges are 
placed in a two-dimensional box. The potential is zero on the walls and
the charges have opposite equally sized densities.
"""

import matplotlib.pyplot as plt
import numpy as np

# Globals:
M = 100  # Number of grid points per side
OMEGA = 0.5  # Parameters to determine over-relaxation
ITER = 5000  # Maximum number of iterations
CONST1 = 0.01  # Step size (1 cm)
CONST2 = 8.854187817e-12  # Vacuum permittivity
TOL = 1e-6  # Target accuracy


def init(n):
    """
    Init. phi to zeros.
    """
    phi = np.zeros([n + 1, n + 1], float)
    return phi


def f(i, j):
    """
    Helper function to model the (square) charges.
    """
    x, y = float(i * CONST1), float(j * CONST1)
    if 0.6 < x < 0.8 and 0.6 < y < 0.8:
        return 1
    elif 0.2 < x < 0.4 and 0.2 < y < 0.4:
        return -1
    else:
        return 0


def solve(x):
    """
    Solve using the Gauss-Seidel method (using 'overelaxation').
    """
    errs = []
    c1 = (CONST1 ** 2) / CONST2
    c2 = (1 + OMEGA)
    for _ in range(ITER):
        err = 0
        for i in range(1, M):
            for j in range(1, M):
                diff = (x[i + 1, j] + x[i - 1, j] + x[i, j + 1] + x[i, j - 1] + c1 * f(i, j)) / 4 - x[i, j]
                x[i, j] += c2 * diff
                err = max(err, abs(diff))
        errs.append(err)
        if err < TOL:
            break
    print("Final error: {} ".format(errs[-1]))
    return x, errs


def main():
    phi0 = init(M)
    result, errs = solve(phi0)
    plt.imshow(result, interpolation='bilinear', origin='lower', extent=[0, 1, 0, 1], vmax=abs(result).max(),
               vmin=-abs(result).max())
    plt.show()


if __name__ == "__main__":
    main()
