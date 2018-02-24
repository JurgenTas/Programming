"""
Set-up: we model vibrations of a homogeneous bar of length L with constant wave speed c > 0. Dirichlet boundary conditions 
are imposed along with the usual initial conditions.

Similar to the numerical schemes for the heat equation, we can use an approximation of derivatives by difference 
quotients to arrive at a numerical scheme for the wave equation. We replace the second order derivatives by their 
standard finite difference approximations. This scheme is conditionally stable.

http://www-users.math.umn.edu/~olver/num_/lnp.pdf
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.sparse import diags

# Globals:
M = 100  # Number of grid points
N = 200  # Number of time steps
T = 1.0  # Number of seconds
L = 1.0  # Size of bar
C = 1  # Wave speed


def solve(dx, dt):
    """
    Solve using a (simple) explicit difference scheme. 
    """

    # init. sigma:
    sigma = ((C * dt) / dx) ** 2
    if sigma > 1:
        print("Warning: stability condition violated!")

    # init. matrices:
    mtrx1 = sigma * diags([-1, 2, -1], [1, 0, -1], shape=(M - 2, M - 2)).toarray()
    mtrx2 = diags([1], shape=(M - 2, M - 2)).toarray()
    mtrx3 = (2 * mtrx2 - mtrx1)

    # Calculate solution for t = 1, 2:
    u = [(i * dx) * (1 - i * dx) for i in range(M)]
    v = np.zeros(M, float)
    v[1:-1] = [u[i] + 0.5 * sigma * (u[i - 1] - 2 * u[i] + u[i + 1]) for i in range(1, M - 1)]

    # Apply scheme for t = 2, 3, 4,...
    x = np.linspace(0, L, M)
    y = np.linspace(0, T, N)
    z = np.zeros((len(y), len(x)))
    z[0], z[1] = u, v
    for i in range(1, N):
        sol = [0] * M  # Init. solution vector
        sol[1:-1] = mtrx3.dot(v[1:-1]) - u[1:-1]
        u, v = v, sol
        z[i] = sol
    return x, y, z


def plot(x, y, z):
    x, y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = Axes3D(fig)
    surf = ax.plot_surface(x, y, z, rstride=3, cstride=3, linewidth=0.3, cmap="coolwarm", vmax=abs(z).max(),
                           vmin=-abs(z).max())
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('u')
    ax.view_init(30, 45)

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
