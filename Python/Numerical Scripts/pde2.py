"""
Solves the one-dimensional heat equation (parabolic PDE) using the Crank-Nicholson scheme: 

https://en.wikipedia.org/wiki/Heat_equation
https://en.wikipedia.org/wiki/Crank%E2%80%93Nicolson_method

This scheme is based on the idea that the forward-in-time approximation of the time derivative is estimating the 
derivative at the halfway point between times n and n+1. Set-up: The temperature (u) is initially distributed over a 
one-dimensional, one-unit-long interval.
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.sparse import diags

# Globals:
M = 25  # Number of spatial slices
N = 50  # Number of time steps
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
    u = [(i * dx) * (1 - i * dx) for i in range(M)]
    u[0], u[-1] = 0, 0  # Dirichlet boundary conditions

    # Apply scheme for t = 1, 2, 3,...
    x = np.linspace(0, L, M)
    y = np.linspace(0, T, N)
    z = np.zeros((len(y), len(x)))
    z[0] = u
    rhs = mtrx2.dot(u[1:-1])
    for i in range(1, N):
        sol = [0] * M  # Init. solution vector
        sol[1:-1] = np.linalg.solve(mtrx1, rhs)
        rhs = mtrx2.dot(sol[1:-1])
        z[i] = sol
    return x, y, z


def plot(x, y, z):
    x, y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = Axes3D(fig)
    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap="hot")

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()


def main():
    # Init. spatial and time step:
    dx = L / (M - 1)  # grid spacing
    dt = T / N  # time spacing
    x, y, z = solve(dx, dt)

    # plot result:
    plot(x, y, z)


if __name__ == "__main__":
    main()
