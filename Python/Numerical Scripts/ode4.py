"""
A thick cylinder (radius L) conveys a fluid with a temperature of 0 degrees Celsius. At the same time
the cylinder is immersed in a bath that is kept at 200 degrees Celsius. The differential equation
and the boundary conditions that govern steady-state heat conduction in the cylinder are

    T'' = (1/r) * T', T(L/2) = 0 and T(L) = 200.

where T is the temperature.

We solve this equation using a finite difference (FD) approach.
"""

import math as mt

import matplotlib.pyplot as plt
from scipy import optimize as opt

# Globals:
M = 15
L = 1.0
T1 = 0
T2 = 200


def f(x, y, y_prime):
    """
    Differential eqn. y’’ = f(x, y, y’)
    """
    return -(1 / x) * y_prime


def residual(yp):
    """
    Residual of FD eqs.
    """
    # Define step size, x-grid:
    h = (L / 2.0) / M
    xp = [(L / 2.0) + h * i for i in range(M + 1)]
    return _residual(yp, xp, h)


def _residual(yp, xp, h):
    """
    Helper function to compute residual.
    """
    res = [0] * (M + 1)
    res[0] = yp[0] - T1
    res[M] = yp[M] - T2
    for i in range(1, M):
        lhs = yp[i - 1] - 2 * yp[i] + yp[i + 1]  # FD approx. lhs equation
        rhs = h * h * f(xp[i], yp[i], (yp[i + 1] - yp[i - 1]) / (2.0 * h))  # FD approx. rhs equation
        res[i] = lhs - rhs
    return res


def solve(y0):
    sol = opt.root(residual, y0)
    print(sol.message)
    return sol.x


def main():
    # Define step size, x-grid:
    h = (L / 2.0) / M
    xp = [(L / 2.0) + h * i for i in range(M + 1)]

    # Numerical solution:
    y0 = [0] * (M + 1)  # initial solution
    y1 = solve(y0)

    # Exact solution:
    const1 = (T1 - T2) / mt.log(0.5)
    const2 = T2 - const1 * mt.log(L)
    y2 = [const1 * mt.log(x) + const2 for x in xp]

    # Plot results:
    plt.plot(xp, y1, 'r--o', label='Numerical')
    plt.plot(xp, y2, 'b-', label='Exact')
    plt.legend(framealpha=1, frameon=True)
    plt.xlabel('r')
    plt.ylabel('T')
    plt.title('Temperature profile through the thickness of the cylinder')
    plt.show()


if __name__ == "__main__":
    main()
