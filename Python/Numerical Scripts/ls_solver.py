__author__ = 'J Tas'

from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt


class Parameter:
    def __init__(self, value):
        self.value = value

    def set(self, value):
        self.value = value

    def __call__(self):
        return self.value

    def __repr__(self):
        msg = "{}(value={value})"
        return msg.format(self.__class__.__name__, **vars(self))


def fit(func, parameters, y, x=None):
    def f(params):
        i = 0
        for p in parameters:
            p.set(params[i])
            i += 1
        return y - func(x)

    if x is None: x = np.arange(y.shape[0])
    p = [param() for param in parameters]
    optimize.leastsq(f, p)


def g(x):
    ans = 0
    for i in range(0, 4):
        ans += param_list[i]() * (x ** i)
    return ans


def main():
    # create data (incl. random noise):
    x0 = 0.0
    x1 = 1.0
    n = 100
    xp = np.linspace(x0, x1, n)
    yp = np.exp(xp) * (1 + np.random.normal(0, 0.1, n))

    # fit data to model:
    global param_list  # global parameter list
    param_list = [Parameter(1), Parameter(2), Parameter(3), Parameter(4)]
    fit(g, param_list, yp, xp)

    # plot results:
    plt.scatter(xp, yp)
    plt.plot(xp, g(xp), 'r')
    plt.show()


if __name__ == "__main__":
    main()
