__author__ = 'J Tas'

import math as mt

import numpy as np


# =====================================================================

def solve(f, x, n_steps, tol_x=1e-6, tol_f=1e-6):
    """
    Given an initial guess x[0..n-1] for a root in n dimensions, take n_steps Newton-Raphson
    steps to improve the root.
    :param f: n-dimensional function
    :param x: n-dimensional vector
    :param n_steps: number of steps to take
    :param tol_x: tolerance for x
    :param tof_f: tolerance for function f
    :return:
    """

    n = len(x)
    p = np.empty(n)
    for k in range(0, n_steps):

        fvec = f(x)
        fjac = jacobian(f, x)
        errf = 0.0
        for i in range(0, n):
            errf += abs(fvec[i])
        if errf <= tol_f:
            return x
        for i in range(0, n):
            p[i] = -fvec[i]
        s = np.linalg.solve(fjac, p)
        errx = 0.0
        for i in range(0, n):
            errx += abs(s[i])
            x[i] += s[i]
        if errx <= tol_x:
            return x

    return x


def jacobian(func, x, eps=1.0e-8):
    """
    Computes forward-difference approximation to Jacobian.
    :param func: user-supplied function
    :param x: numpy array of size n
    :param eps: numerical precision
    :return: Jacobian matrix
    """

    n = len(x)
    xh = x
    f = func(x)
    df = np.empty((n, n))
    for j in range(0, n):

        temp = xh[j]
        h = eps * mt.fabs(temp)
        if h == 0.0:
            h = eps
        xh[j] = temp + h  # trick to reduce finite-precision error
        h = xh[j] - temp
        fh = func(xh)
        xh[j] = temp
        for i in range(0, n):
            df[i][j] = (fh[i] - f[i]) / h
            
    return df


# =====================================================================


def g(x):
    g1 = x[0] + 1
    g2 = x[1] + 2 * x[0]
    g3 = 4 * x[2] + 6 * x[1] + x[0] * x[1]
    return [g1, g2, g3]


def main():
    x = [1.0, 2.0, 3.0]
    s = solve(g, x, 100)
    print(s)
    print(g(s))


if __name__ == "__main__":
    main()
