import numpy as np


class Perceptron(object):
    def __init__(self, eta=0.01, n=50):
        self.eta = eta
        self.n = n
        self.w = []

    def fit(self, xlist, ylist):
        """
        
        :type xlist: list of lists
        :type ylist: list
        """
        self.w = [0] * len(xlist[0])
        for _ in range(self.n):
            for x, y in zip(xlist, ylist):
                error = y - step_function(np.dot(self.w, x))
                if error != 0:
                    for i, xi in enumerate(x):
                        assert isinstance(xi, int)
                        self.w[i] += self.eta * error * xi


def step_function(z):
    return 0 if not z >= 0.5 else 1


def main():
    x = [[0, 0], [1, 0], [0, 1], [1, 1]]
    y = [0, 0, 0, 1]
    p = Perceptron()
    p.fit(x, y)
    print(p.w)


if __name__ == "__main__":
    main()
