# -*- coding: utf-8 -*-
__author__ = 'J Tas'

import math
import numpy as np

# =====================================================================

def logistic(t):
    """
    Return logistic(t)
    """
    return 1.0 / (1 + math.exp(-t))

def tanh(t):
    """
    Return the hyperbolic tangent of t
    """
    return math.tanh(t)
    
# =====================================================================

def neuron(func, w, x):
    return func(np.dot(w, x))
    
def feed_forward(network, x, func):
    """
    Network represented as a list of lists
    """
    res = []
    for layer in network:
        x = x + [1] #add bias
        y = [neuron(func, w, x) for w in layer]
        res.append(y)
        x = y  
    return res
   
# =====================================================================

def main():
    hidden_layer = [[20, 20, -30], [20, 20, -10]]
    output_layer = [[-60, 60, -30]]
    network = [hidden_layer,output_layer]
    for x in [0, 1]:
        for y in [0, 1]:
            print(x, y , feed_forward(network, [x, y], tanh)[-1])

# =====================================================================

if __name__ == "__main__":
    main()
