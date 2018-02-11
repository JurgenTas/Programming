"""
Find a solution of the Poisson equation. Set-up: two (square) charges are 
placed in a two-dimensional box. The potential is zero on the walls and
the charges have opposite equally sized densities.
"""

import matplotlib.pyplot as plt
import numpy as np

# Globals:
M = 100  # Grid squares on a side
OMEGA = 0.75  # Overelaxation coefficient
ITER = 5000  # Maximum number of iterations
CONST1 = 0.01  # Step size (1 cm)
CONST2 = 8.854187817e-12  # Vacuum permittivity


def init(n):
    """Init. phi."""
    phi = np.zeros([n + 1, n + 1], float)
    return phi


def f(i, j, c):
    """
    Helper function to model the (square) charges.
    """
    x, y = float(i * CONST1), float(j * CONST1)
    if 0.6 < x < 0.8 and 0.6 < y < 0.8:
        return c
    elif 0.2 < x < 0.4 and 0.2 < y < 0.4:
        return -c
    else:
        return 0


def solve(phi):
    """
    Solve using the Gauss-Seidel method (using 'overelaxation')
    """
    errs = []
    c = ((CONST1 ** 2) / (4 * CONST2))
    for _ in range(ITER):
        err = 0
        for i in range(1, M):
            for j in range(1, M):
                diff = (phi[i + 1, j] + phi[i - 1, j] + phi[i, j + 1] + phi[i, j - 1]) / 4 + f(i, j, c) - phi[i, j]
                phi[i, j] += (1 + OMEGA) * diff
                err = max(err, abs(diff))
        errs.append(err)
    print("Final error: {} ".format(errs[-1]))
    return phi, errs


def main():
    phi0 = init(M)
    result, errs, = solve(phi0)
    plt.imshow(result, interpolation='bilinear', origin='lower', extent=[0, 1, 0, 1], vmax=abs(result).max(),
               vmin=-abs(result).max())
    plt.show()


if __name__ == "__main__":
    main()
