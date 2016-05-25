__author__ = 'J Tas'

import numpy as np


class Matrix:
    def __init__(self, data):
        self.m = data

    def set_value(self, i, j, value):
        self.m[(i, j)] = value

    def get_value(self, i, j):
        return self.m[(i, j)]

    def show(self):
        print(self.m)

    def add(self, a):
        x = self.m + a.m
        return Matrix(x)

    def subtract(self, a):
        x = self.m - a.m
        return Matrix(x)

    def scalar_multiply(self, s):
        x = self.m * s
        return Matrix(x)

    def matrix_multiply(self, a):
        x = np.dot(self.m, a.m)
        return Matrix(x)

    def transpose(self):
        x = self.m.T
        return Matrix(x)

    def determinant(self):
        return np.linalg.det(self.m)

    def cond(self):
        return np.linalg.cond(self.m)

    def inverse(self):
        x = np.linalg.inv(self.m)
        return Matrix(x)

    def solve(self, b):
        return np.linalg.solve(self.m, b)

    def eigenvalue(self):
        x, v = np.linalg.eigh(self.m)
        return x, v

    def svd(self):
        u, s, v = np.linalg.svd(self.m)
        return u, s, v


if __name__ == "__main__":
    A = np.random.randint(5, size=(3, 3))
    m1 = Matrix(A)
    m2 = m1.inverse()
    m3 = m1.matrix_multiply(m2)
