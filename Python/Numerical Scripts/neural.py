# -*- coding: utf-8 -*-
__author__ = 'J Tas'

import math

import numpy as np
import pandas as pd


class NeuralNetwork:
    def __init__(self, input_size, num_hidden, output_size):
        """
        :param input_size: each input is a vector of length 'input_size'
        :param num_hidden: we have 'num_hidden' neurons in the hidden layer
        :param output_size: we need 'output_size' outputs for each input
        :return:
        """
        self.input_size = input_size
        self.num_hidden = num_hidden
        self.output_size = output_size
        # each hidden neuron has one weight per input, plus a bias weight
        self.hidden_layer = [[0 for _ in range(input_size + 1)] for _ in range(num_hidden)]

        # each output neuron has one weight per hidden neuron, plus a bias weight
        self.output_layer = [[0 for _ in range(num_hidden + 1)] for _ in range(output_size)]
        self.layers = [self.hidden_layer, self.output_layer]


class MultilayerPerceptron:
    def __init__(self, network):
        self.network = network

    def train(self, n, x_arr, y_arr):
        for _ in range(n):
            for x, y in zip(x_arr, y_arr):
                self._backpropagate(x, y)

    def predict(self, x):
        return self._feed_forward(x)

    def _logistic(self, x):
        return 1.0 / (1 + math.exp(-x))

    def _logistic_deriv(self, x):
        return self._logistic(x) * (1 - self._logistic(x))

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
            output = [self._neuron_output(neuron, x_bias) for neuron in layer]  # output for this layer
            outputs.append(output)  # remember output
            x = output  # the input to the next layer is the output of this one
        return outputs

    def _backpropagate(self, x, y):

        hidden_outputs, outputs = self._feed_forward(x)
        output_deltas = [output * (1 - output) * (output - y[i]) for i, output in enumerate(outputs)]

        # adjust weights for output layer (network[-1])
        for i, output_neuron in enumerate(self.network.layers[-1]):
            for j, hidden_output in enumerate(hidden_outputs + [1]):
                output_neuron[j] -= output_deltas[i] * hidden_output

        # back-propagate errors to hidden layer
        hidden_deltas = []
        for i, hidden_output in enumerate(hidden_outputs):
            hidden_deltas.append(hidden_output * (1 - hidden_output) * np.dot(output_deltas,
                                                                              [n[i] for n in self.network.layers[-1]]))

        # adjust weights for hidden layer (network[0])
        for i, hidden_neuron in enumerate(self.network.layers[0]):
            for j, x in enumerate(x + [1]):
                hidden_neuron[j] -= hidden_deltas[i] * x


# =====================================================================


def load():
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
    y = df.iloc[:, 4].values
    y = np.where(y == 'Iris-setosa', 0, 1)
    ybin = [tobin(_, 1) for _ in y]
    x = df.iloc[:, [0, 1, 2, 3]].values
    return (x - x.mean(axis=0) / x.std(axis=0)), ybin


def tobin(x, s):
    return [(x >> k) & 1 for k in range(0, s)]


# =====================================================================


def main():
    x_arr, y_arr = load()
    input_size = 4
    num_hidden = 5
    output_size = 1
    network = NeuralNetwork(input_size, num_hidden, output_size)
    mlp = MultilayerPerceptron(network)
    mlp.train(10, x_arr, y_arr)


if __name__ == "__main__":
    main()
