__author__ = 'J Tas'

import math as mt


def cdf(z, n):
    """ Calculates the normal cum. distr. function."""
    return 0.5 * erfc(-z / mt.sqrt(2), n)


def erf(z, n):
    """ Calculates the error function.

    See: Abramowitz and Stegun: Handbook of Mathematical Functions (7.1.15).
    """
    s = 0
    for i in range(0, n + 1):
        m = 2*i + 1
        sign = (-1.0 ) ** i
        s += sign * (z ** m) / (mt.factorial(i) * m)
    return (2.0 / mt.sqrt(mt.pi)) * s


def erfc(z, n):
    """ Calculates the complementary error function. """
    return 1 - erf(z, n)

# -------------------------------------------------------------------------------


def inv_cdf(p):
    """ Calculates the inverse of the normal cum. distr. function."""

    if p <= 0.0 or p >= 1.0:
        raise Exception("Invalid input argument!")

    if p < 0.5:
        return -1.0 * approx(mt.sqrt(-2.0*mt.log(p)))
    else:
        return approx(mt.sqrt(-2.0*mt.log(1-p)))


def approx(t):
    """ See: Abramowitz and Stegun: Handbook of Mathematical Functions (26.2.23)."""

    c = [2.515517, 0.802853, 0.010328]
    d = [1.432788, 0.189269, 0.001308]
    return t - ((c[2]*t + c[1])*t + c[0]) / (((d[2]*t + d[1])*t + d[0])*t + 1.0)

# -------------------------------------------------------------------------------


def main():

    n = 100
    z = 3
    print(cdf(z, n))
    print(inv_cdf())

if __name__ == "__main__":
    main()