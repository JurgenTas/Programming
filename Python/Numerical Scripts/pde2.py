"""
Solves the one-dimensional heat equation (parabolic PDE) using the Crank-Nicholson scheme: 

https://en.wikipedia.org/wiki/Heat_equation
https://en.wikipedia.org/wiki/Crank%E2%80%93Nicolson_method

This scheme is based on the idea that the forward-in-time approximation of the time derivative is estimating the derivative at the halfway point 
between times n and n+1. Set-up: The temperature (u) is initially distributed over a one-dimensional, one-unit-long interval.
"""

import math as mt

import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import diags

# Globals:
M = 1000  # Number of spatial slices
N = 1000  # Number of time steps
D = 1.0  # Thermal diffusivity
T = 1.0  # Number of seconds 
L = 1.0  # Size of grid


def solve(dx, dt):
    """
    Solve using the Crank-Nicholson scheme.
    """

    # init. lhs and rhs matrices:
    c = (D / 2.0) * (dt / (dx ** 2))
    mtrx1 = diags([-c, 2 * (1 + c), -c], [1, 0, -1], shape=(M - 2, M - 2)).toarray()
    mtrx2 = diags([c, 2 * (1 - c), c], [1, 0, -1], shape=(M - 2, M - 2)).toarray()

    # Init. initial temperature distribution:
    u = [mt.sin(i * dx * mt.pi) for i in range(M)]
    u[0], u[-1] = 0, 0  # Dirichlet boundary conditions
    res = [None] * N # init. result list
    res[0] = u

    # Solve linear system of equations and update rhs:
    rhs = mtrx2.dot(u[1:-1])
    for i in range(1, N):
        sol = [0] * M  # Init. solution vector
        sol[1:-1] = np.linalg.solve(mtrx1, rhs)
        rhs = mtrx2.dot(sol[1:-1])
        res[i] = sol
    return result


def main():
    # Init. spatial and time step:
    dx = L / (M - 1)  # grid spacing
    dt = T / N  # time spacing
    result = solve(dx, dt)

    # Plot 100 first timesteps:
    n = 100
    x = np.linspace(0, L, M)
    for i in range(n):
        f = result[i]
        plt.plot(x, f, str(i/n))
    plt.show()
  
if __name__ == "__main__":
    main()
