__author__ = 'J Tas'

import matplotlib.pyplot as plt
import numpy as np

# Globals:
CONST1 = 10.0
CONST2 = 28.0
CONST3 = 8.0 / 3.0


class Ode3:
    """Solve dr/dt = f(r,t). With r is a 3D vector, f is a 3D vector of functions."""

    def __init__(self, a, b, n=10):
        self.h = (b - a) / n
        self.tp = np.arange(a, b, self.h)

    def rkn4(self, f, start):
        """
        Implements 4th order Runge-Kutta method.
        See: https://en.wikipedia.org/wiki/Runge-Kutta_methods
        """
        r = np.array(start, float)
        self.xp = []
        self.yp = []
        self.zp = []
        for t in self.tp:
            self.xp.append(r[0])
            self.yp.append(r[1])
            self.zp.append(r[2])
            r += self._rkn4_step(r, t, f)

    def _rkn4_step(self, r, t, f):
        k1 = self.h * f(r, t)
        k2 = self.h * f(r + 0.5 * k1, t + 0.5 * self.h)
        k3 = self.h * f(r + 0.5 * k2, t + 0.5 * self.h)
        k4 = self.h * f(r + k3, t + self.h)
        return (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0


def f(r, t):
    """
    Right-hand side of Lorenz equations. Returns 3D vector of functions.
    """
    x = r[0]
    y = r[1]
    z = r[2]
    fx = CONST1 * (y - x)
    fy = CONST2 * x - y - x * z
    fz = x * y - CONST3 * z
    return np.array([fx, fy, fz], float)


def ode3():
    a = 0.0
    b = 50
    s = Ode3(a, b, 5000)
    s.rkn4(f, [1, 0, 0])
    plt.plot(s.zp, s.xp)
    plt.show()


def main():
    ode3()


if __name__ == "__main__":
    main()
