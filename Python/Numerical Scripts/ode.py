__author__ = 'J Tas'

import numpy as np
from scipy.optimize import newton
import matplotlib.pyplot as plt
import math


class Ode1:
    # Solve dx/dt = f(x,t)

    def __init__(self, a, b, n=10):
        self.h = (b - a) / n
        self.tp = np.arange(a, b, self.h)
        self.xp = []

    def euler_fwd(self, f, x):
        self.xp = []
        for t in self.tp:
            self.xp.append(x)
            x += self.h * f(x, t)
        return self.tp, self.xp

    def euler_bwd(self, f, x, tol, max_iter):
        self.xp = []
        for t in self.tp:
            self.xp.append(x)
            func = lambda y: y - self.h * f(y, t + self.h) - x
            x = newton(func, x, tol=tol, maxiter=max_iter)
        return self.tp, self.xp

    def rkn2(self, f, x):
        self.xp = []
        for t in self.tp:
            self.xp.append(x)
            k1 = self.h * f(x, t)
            k2 = self.h * f(x + 0.5 * k1, t + 0.5 * self.h)
            x += k2
        return self.tp, self.xp

    def rkn4(self, f, x):
        self.xp = []
        for t in self.tp:
            self.xp.append(x)
            k1 = self.h * f(x, t)
            k2 = self.h * f(x + 0.5 * k1, t + 0.5 * self.h)
            k3 = self.h * f(x + 0.5 * k2, t + 0.5 * self.h)
            k4 = self.h * f(x + k3, t + self.h)
            x += (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        return self.tp, self.xp


def g(p, q):
    return p * math.sin(q)


def main():
    a = 0.0
    b = 2.0 * math.pi
    s = Ode1(a, b, 100)
    x, y = s.euler_bwd(g, 1, 1.0e-12, 10)
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    main()
