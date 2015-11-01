__author__ = 'J Tas'

import random

import numpy as np


# =====================================================================

def in_random_order(data):
    """
    returns the elements of data in random order
    """
    idx = [i for i, _ in enumerate(data)]
    random.shuffle(idx)
    for i in idx:
        yield data[i]


def stochastic_gradient_descent(func, grad_func, x, y, theta_0, alpha_0=0.01, max_it=100):
    """
    Minimizes an unconstrained optimization problem using
    stochastic gradient descent method
    """
    data = zip(x, y)
    theta, alpha = theta_0, alpha_0
    min_theta, min_value, it = None, float("inf"), 0

    while it < max_it:

        value = sum(func(x_i, y_i, theta) for x_i, y_i in data)

        if value < min_value:
            min_theta = theta
            min_value = value
            it = 0
            alpha = alpha_0

        else:
            it += 1
            alpha *= 0.9

        for x_i, y_i in in_random_order(data):
            grad_i = grad_func(x_i, y_i, theta)
            theta = vector_subtract(theta, scalar_multiply(alpha, grad_i))

    return min_theta


def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def scalar_multiply(c, v):
    return [c * v_i for v_i in v]


# =====================================================================

def error(alpha, beta, x, y):
    return y - (beta * x + alpha)


def squared_error(x, y, theta):
    alpha, beta = theta
    return error(alpha, beta, x, y) ** 2


def squared_error_gradient(x, y, theta):
    alpha, beta = theta
    return [-2 * error(alpha, beta, x, y), -2 * error(alpha, beta, x, y) * x]


# =====================================================================

def main():
    random.seed(0)
    theta = [random.random(), random.random()]
    x = np.arange(0, 1, 0.1)
    y = np.arange(0, 1, 0.1)
    alpha, beta = stochastic_gradient_descent(squared_error, squared_error_gradient, x, y, theta)
    print alpha, beta


if __name__ == "__main__":
    main()
