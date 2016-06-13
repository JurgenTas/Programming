# -*- coding: utf-8 -*-
__author__ = 'J Tas'

import math
import random

import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from sklearn.datasets import load_iris


class Network:
    def __init__(self, input_size, hidden_size, output_size):
        """
        :param input_size: each input is a vector of length 'input_size'
        :param hidden_size: the number of neurons in the hidden layer
        :param output_size: we need 'output_size' outputs for each input
        Each hidden neuron has one weight per input, plus a bias weight
        Each output neuron has one weight per hidden neuron, plus a bias weight
        """
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.hidden_layer = [[random.random() for _ in range(input_size + 1)] for _ in range(hidden_size)]
        self.output_layer = [[random.random() for _ in range(hidden_size + 1)] for _ in range(output_size)]
        self.layers = [self.hidden_layer, self.output_layer]


# ======================================================================================================================


class NeuralNetwork:
    def __init__(self, network):
        self.network = network
        self.error = []

    def train(self, n, x_arr, y_arr):
        self.error = []
        for _ in range(n):
            err = 0
            for x, y in zip(x_arr, y_arr):
                err += self._backpropagate(x, y)
            self.error.append(err)

    def predict(self, x, round=True):
        return self._feed_forward(x)

    def _logistic(self, x):
        return 1.0 / (1 + math.exp(-x))

    def _neuron_output(self, w, x):
        return self._logistic(np.dot(w, x))

    def _feed_forward(self, x):
        """
        :param x: vector of input
        :return: the output from forward-propagating the input
        """

        outputs = []

        for layer in self.network.layers:
            x_bias = np.append(x, [1])  # add a bias input
            out = [self._neuron_output(neuron, x_bias) for neuron in layer]  # output for this layer
            outputs.append(out)  # remember output
            x = out  # the input to the next layer is the output of this one
        return outputs

    def _backpropagate(self, X, Y):

        hidden_outputs, outputs = self._feed_forward(X)
        output_deltas = [out * (1 - out) * (out - Y[i]) for i, out in enumerate(outputs)]

        diff = np.asarray(Y) - np.asarray(outputs)
        err = np.linalg.norm(diff)

        # adjust weights for output layer (network[-1])
        for i, output_neuron in enumerate(self.network.layers[-1]):
            for j, hidden_output in enumerate(hidden_outputs + [1]):
                output_neuron[j] -= output_deltas[i] * hidden_output

        # back-propagate errors to hidden layer
        hidden_deltas = []
        for i, hidden_output in enumerate(hidden_outputs):
            hidden_deltas.append(
                hidden_output * (1 - hidden_output) * np.dot(output_deltas, [n[i] for n in self.network.layers[-1]]))

        # adjust weights for hidden layer (network[0])
        for i, hidden_neuron in enumerate(self.network.layers[0]):
            for j, x in enumerate(X + [1]):
                hidden_neuron[j] -= hidden_deltas[i] * x

        return err


# ======================================================================================================================


def load():
    iris = load_iris()
    n_samples, n_features = iris.data.shape
    indices = np.arange(n_samples)
    np.random.shuffle(indices)
    X = iris.data[indices]
    Y = iris.target[indices]
    split = (n_samples * 4) / 5
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = Y[:split], Y[split:]
    X_train = preprocessing.normalize(X_train)
    X_test = preprocessing.normalize(X_test)

    Y_train = []
    for Y in y_train:
        if Y == 0: Y_train.append([1, 0, 0])
        if Y == 1: Y_train.append([0, 1, 0])
        if Y == 2: Y_train.append([0, 0, 1])

    Y_test = []
    for Y in y_test:
        if Y == 0: Y_test.append([1, 0, 0])
        if Y == 1: Y_test.append([0, 1, 0])
        if Y == 2: Y_test.append([0, 0, 1])

    return X_train, Y_train, X_test, Y_test


# ======================================================================================================================


def main():
    X_train, Y_train, X_test, Y_test = load()
    network = Network(4, 10, 3)
    model = NeuralNetwork(network)
    model.train(1000, X_train, Y_train)
    plt.plot(model.error)
    plt.ylabel('Errors')
    plt.show()
    for x, y in zip(X_test, Y_test):
        print("Input vector: ", x, "|| Target value: ", y, "|| Predicted value: ", model.predict(x)[-1])


if __name__ == "__main__":
    main()
