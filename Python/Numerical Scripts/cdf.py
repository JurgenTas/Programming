__author__ = 'J Tas'

import math as mt


def cdf(z, n):
    """ Calculates the normal cum. distr. function. """
    return 0.5 * erfc(-z / mt.sqrt(2), n)


def erf(z, n):
    """ Calculates the error function.

    See: Abramowitz and Stegun: Handbook of Mathematical Functions (7.1.15).
    """
    ans = 0
    for i in range(0, n + 1):
        m = 2 * i + 1
        sign = (-1.0) ** i
        ans += sign * (z ** m) / (mt.factorial(i) * m)
    return (2.0 / mt.sqrt(mt.pi)) * ans


def erfc(z, n):
    """ Calculates the complementary error function. """
    return 1 - erf(z, n)


# -------------------------------------------------------------------------------


def invcdf(p, n):
    """ Calculates the inverse of the normal cum. distr. function. """

    if p <= 0.0 or p >= 1.0:
        raise Exception("Invalid input argument!")

    return -1.0 * mt.sqrt(2.0) * inverfc(2.0 * p, n)


def inverf(p, n):
    """ Calculates inverse of error function.

    See: Numerical Recipes, 3th edition (6.2).
    """
    return inverfc(1.0 - p, n)


def inverfc(p, n):
    """ Calculates inverse of complementary error function.

    See: Numerical Recipes, 3th edition (6.2).
    """
    if p >= 2.0:
        return -100
    if p <= 0.0:
        return 100

    if p < 1.0:
        pp = p
    else:
        pp = 2.0 - p

    t = mt.sqrt(-2.0 * mt.log(pp / 2.0))
    ans = -0.70711 * ((2.30753 + t * 0.27061) / (1 + t * (0.99229 + t * 0.04481)) - t)
    for i in range(0, 2):
        err = erfc(ans, n) - pp
        ans += err / (1.12837916709551257 * mt.exp(-ans * ans) - ans * err)  # Halley

    if p < 1.0:
        return ans
    else:
        return -ans


# -------------------------------------------------------------------------------


def main():

    n = 6
    xp = [0.1,0.25,0.5,0.75,0.9]
    for x in xp:
        print(invcdf(x, n))


if __name__ == "__main__":
    main()
