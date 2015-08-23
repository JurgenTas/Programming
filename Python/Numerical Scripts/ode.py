__author__ = 'J Tas'

import math

import numpy as np
from scipy.optimize import newton
import matplotlib.pyplot as plt


# =====================================================================


class Ode1:
    """
    Solve dx/dt = f(x,t)
    """

    def __init__(self, a, b, n=10):
        self.h = (b - a) / n
        self.tp = np.arange(a, b, self.h)
        self.xp = []

    def euler_fwd(self, f, x):
        """
        Implements the standard Euler method.
        See: https://en.wikipedia.org/wiki/Euler_method
        """
        self.xp = []
        for t in self.tp:
            self.xp.append(x)
            x += self.h * f(x, t)
        return self.tp, self.xp

    def euler_bwd(self, f, x, **kwargs):
        """
        Implements the implicit Euler method.
        See: https://en.wikipedia.org/wiki/Backward_Euler_method
        """
        self.xp = []
        for t in self.tp:
            self.xp.append(x)
            func = lambda y: y - self.h * f(y, t + self.h) - x
            x = newton(func, x, **kwargs)
        return self.tp, self.xp

    def rkn2(self, f, x):
        """
        Implements 2nd order Runge-Kutta method.
        See: https://en.wikipedia.org/wiki/Runge-Kutta_methods
        """
        self.xp = []
        for t in self.tp:
            self.xp.append(x)
            k1 = self.h * f(x, t)
            k2 = self.h * f(x + 0.5 * k1, t + 0.5 * self.h)
            x += k2
        return self.tp, self.xp

    def rkn4(self, f, x):
        """
        Implements 4th order Runge-Kutta method.
        See: https://en.wikipedia.org/wiki/Runge-Kutta_methods
        """
        self.xp = []
        for t in self.tp:
            self.xp.append(x)
            k1 = self.h * f(x, t)
            k2 = self.h * f(x + 0.5 * k1, t + 0.5 * self.h)
            k3 = self.h * f(x + 0.5 * k2, t + 0.5 * self.h)
            k4 = self.h * f(x + k3, t + self.h)
            x += (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        return self.tp, self.xp


# =====================================================================

def g(x, t):
    return x * math.sin(t)


def ode1():
    a = 0.0
    b = 6.0 * math.pi
    s = Ode1(a, b, 100)
    x, y = s.euler_bwd(g, 1, tol=1.0e-12, maxiter=10)
    plt.plot(x, y)
    plt.show()


def main():
    ode1()


if __name__ == "__main__":
    main()
