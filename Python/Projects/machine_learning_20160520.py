# coding=utf-8
__author__ = 'J Tas'

import numpy as np
import matplotlib.pyplot as plt


# =====================================================================


class Perceptron(object):
    """
    This class implements an algorithm for supervised learning of 
    binary classifiers. 
    """
    def __init__(self, eta=0.01, n=10):
        self.eta = eta
        self.n = n
        self.w = []
        self.error = []
    
    def train(self, xlist, ylist):
        """
        :type xlist: list of lists (i.e 2D list)
        :type ylist: list
        """
        self.w = [0]*len(xlist[0]) # init. weights
        for _ in range(self.n):
            cnt = 0
            print(self.w)
            for x, y in zip(xlist, ylist):
                delta = y - self.predict(x) # missclassification: != 0
                if delta != 0:
                    cnt += 1
                    for i, xi in enumerate(x):
                        self.w[i] += self.eta * delta * xi
            self.error.append(cnt)
    

    def predict(self, x):
        return 0 if np.dot(self.w, x) < 0.0 else 1
    
 
    def plot_classification_error(self):
        plt.plot(range(1, len(self.error)+1), self.error, marker='o')
        plt.xlabel('Iterations')
        plt.ylabel('Missclassifications')
        plt.show()

    
# =====================================================================


def main():
    x = [[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]] 
    y = [1, 1, 1, 0] 
    p = Perceptron()
    p.train(x, y)
    p.plot_classification_error()
    print(p.w)


if __name__ == "__main__":
    main()
