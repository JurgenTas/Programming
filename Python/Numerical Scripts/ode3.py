"""
We consider the van der Pol oscillator:
i.e. https://en.wikipedia.org/wiki/Van_der_Pol_oscillator

The van der Pol equation is an 2nd order ODE. This equation arises in the study of circuits
containing vacuum.
"""
import math

import matplotlib.pyplot as plt
import numpy as np

# Globals:
MU = 0.3


def f(x, y):
    # Right-hand side of first order system of equations. Returns 2D vector of functions.
    y1 = y[1]
    y2 = MU * (1 - y[0] * y[0]) * y[1] - y[0]
    return np.array([y1, y2], float)


def solve(func, x, y, xstop, h, tol=1.0e-6, iterstop=10000000):
    """
    Implements and adaptive Runge-Kutta method using Dormant-Price
    coefficients, i.e. see

    https://en.wikipedia.org/wiki/Dormand%E2%80%93Prince_method
    """
    a1 = 0.2
    a2 = 0.3
    a3 = 0.8
    a4 = 8 / 9
    a5 = 1.0
    a6 = 1.0

    c0 = 35 / 384
    c2 = 500 / 1113
    c3 = 125 / 192
    c4 = -2187 / 6784
    c5 = 11 / 84

    d0 = 5179 / 57600
    d2 = 7571 / 16695
    d3 = 393 / 640
    d4 = -92097 / 339200
    d5 = 187 / 2100
    d6 = 1 / 40

    b10 = 0.2
    b20 = 0.075
    b21 = 0.225
    b30 = 44 / 45
    b31 = -56 / 15
    b32 = 32 / 9
    b40 = 19372 / 6561
    b41 = -25360 / 2187
    b42 = 64448 / 6561
    b43 = -212 / 729
    b50 = 9017 / 3168
    b51 = -355 / 33
    b52 = 46732 / 5247
    b53 = 49 / 176
    b54 = -5103 / 18656
    b60 = 35 / 384
    b62 = 500 / 1113
    b63 = 125 / 192
    b64 = -2187 / 6784
    b65 = 11 / 84

    xlist = []
    ylist = []
    xlist.append(x)
    ylist.append(y)
    stopper = 0  # Integration stopper(0 = off, 1 = on)
    k0 = h * func(x, y)
    for i in range(iterstop):
        k1 = h * func(x + a1 * h, y + b10 * k0)
        k2 = h * func(x + a2 * h, y + b20 * k0 + b21 * k1)
        k3 = h * func(x + a3 * h, y + b30 * k0 + b31 * k1 + b32 * k2)
        k4 = h * func(x + a4 * h, y + b40 * k0 + b41 * k1 + b42 * k2 + b43 * k3)
        k5 = h * func(x + a5 * h, y + b50 * k0 + b51 * k1 + b52 * k2 + b53 * k3 + b54 * k4)
        k6 = h * func(x + a6 * h, y + b60 * k0 + b62 * k2 + b63 * k3 + b64 * k4 + b65 * k5)
        dy = c0 * k0 + c2 * k2 + c3 * k3 + c4 * k4 + c5 * k5

        diff = (c0 - d0) * k0 + (c2 - d2) * k2 + (c3 - d3) * k3 + (c4 - d4) * k4 + (c5 - d5) * k5 - d6 * k6
        err = math.sqrt(np.sum(diff ** 2) / len(y))
        h_next = 0.9 * h * (tol / err) ** 0.2

        # Accept integration step if error e is within tolerance
        if err <= tol:
            y = y + dy
            x = x + h
            xlist.append(x)
            ylist.append(y)
            if stopper == 1:
                break  # Reached end of x-range
            if abs(h_next) > 10.0 * abs(h):
                h_next = 10.0 * h

            # Check if next step is the last one; if so, adjust h
            if (h > 0.0) == ((x + h_next) >= xstop):
                h_next = xstop - x
                stopper = 1
            k0 = k6 * h_next / h
        else:
            if abs(h_next) < 0.1 * abs(h):
                h_next = 0.1 * h
            k0 = k0 * h_next / h
        h = h_next
    return np.array(xlist), np.array(ylist)


def plot(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y, color='red')
    ax.set_xlabel('y')
    ax.set_ylabel('dy/dt')
    ax.grid()
    plt.show()


def main():
    x = 0
    y = [0.01, 0]  # Initial conditions
    h = 1e-4  # Initial step size
    xlist, ylist = solve(f, x, y, 125, h)

    # Plot results:
    plot(ylist[:, 0], ylist[:, 1])


if __name__ == "__main__":
    main()
