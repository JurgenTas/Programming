"""
A thick cylinder (radius R) conveys a fluid with a temperature of 0 degrees
Celsius. At the same time the cylinder is immersed in a bath that is kept at
200 degrees Celsius. The  differential equation
and the boundary conditions that govern steady-state heat conduction in the
cylinder are

    T'' = (1/r) * T', T(R/2) = 0 and T(R) = 200.

where T is the temperature. We solve this equation using a finite
difference (FD) approach.
"""

import math as mt

import matplotlib.pyplot as plt
import numpy as np

# Globals:
M = 32  # Number of grid steps
R = 1  # Radius of the cylinder
T1 = 0.0  # Temperature at r = R/2
T2 = 200.0  # Temperature at r = R


def solve():
    """
    Solve using FD method.

    :return: x-points, y-points
    :rtype: tuple
    """
    # Define step size, x-grid:
    h = (R / 2.0) / M
    xp = [(R / 2.0) + h * i for i in range(M + 1)]

    # Define FD matrix:
    a = matrix(xp, h)

    # Define FD rhs:
    b = [0] * (M + 1)
    b[0], b[M] = T1, T2

    # Solve and return solution:
    yp = np.linalg.solve(a, b)
    return xp, yp


def matrix(xp, h):
    """
    Helper function to construct LHS matrix.

    :param xp: x-points
    :type xp: lst
    :param h: step size
    :type h: float
    :return: matrix
    :rtype: numpy.array
    """
    a = np.zeros((M + 1, M + 1))
    a[0, 0], a[M, M] = 1, 1
    for i in range(1, M):
        a[i, i - 1] = 1.0 - 0.5 * (h / xp[i])
        a[i, i] = -2.0
        a[i, i + 1] = 1.0 + 0.5 * (h / xp[i])
    return mt


def plot(xp, yp1, yp2):
    """
    Plot results.

    :param xp: x-points
    :type xp: list
    :param yp1: numerical solution
    :type yp1: list
    :param yp2: analytical solution
    :type yp2: list
    """
    plt.subplot(2, 1, 1)
    plt.grid(True)
    plt.plot(xp, yp1, '-o', markersize=4)
    plt.grid(True)
    plt.title('Temperature profile through the thickness of the cylinder')

    # calculate absolute error:
    yp3 = np.absolute(yp1 - yp2)
    plt.subplot(2, 1, 2)
    plt.grid(True)
    plt.plot(xp, yp3, '-o', markersize=4)
    plt.grid(True)
    plt.title('Approximation error')
    plt.show()


def main():
    # Numerical solution:
    yp1, xp = solve()

    # Exact solution:
    c1 = (T1 - T2) / mt.log(0.5)
    c2 = T2 - c1 * mt.log(R)
    yp2 = [c1 * mt.log(x) + c2 for x in xp]

    # Plot results:
    plot(xp, yp1, yp2)


if __name__ == "__main__":
    main()
