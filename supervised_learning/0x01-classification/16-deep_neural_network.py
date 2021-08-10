#!/usr/bin/env python3
"""represents a deep neural network performing
binary classification"""

import numpy as np


class DeepNeuralNetwork:
    """represents a deep neural network
    performing binary classification

    Attributes:
        L (int): the number of layers in the neural network.
        cache (dict): hold all intermediary values of the network.
        weights (dict): hold all weights and biased of the network.

    Methods:
        __init__(self, nx, nodes): constructor
    """

    def __init__(self, nx, layers):
        """defines a deep neural network performing
        binary classification.

        Exp. The layers weights are initialized using He et al. method
        and the bias to 0's. To use He et al. method W1 and b1 must be
        initialized beforehand.

        Numpy implementation He et al. method:
            weight = np.random.randn(layer_size[l],layer_size[l-1])
                    *np.sqrt(2/layer_size[l-1])

        Args:
            nx (int): number of input features.
            layers (list):
                represents the number of nodes in each
                layer of the network

        Raises:
            TypeError: nx must be an integer.
            ValueError: nx must be a positive integer.
            TypeError: layers must be a list of positive integers.
        """
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        if not isinstance(layers, list) or len(layers) == 0\
                or np.argmin(layers) < 0:
            raise TypeError('layers must be a list of positive integers')

        self.L = len(layers)
        self.cache = dict()
        self.weights = dict()
        # initialize L1
        # weights (neurons x input features)
        self.weights["W1"] = np.random.randn(layers[0], nx)*np.sqrt(2/nx)
        # bias (float of zero's x # neurons of the layer)
        self.weights["b1"] = np.zeros([layers[0], 1], dtype=float)
        # initialize L2 and L3
        for layer in range(1, self.L):
            # check if layer is int
            if not isinstance(layers[layer], int):
                raise TypeError('layers must be a list of positive integers')
            # He et al method
            # weight = np.random.randn(layer_size[l],layer_size[l-1])
            # *np.sqrt(2/layer_size[l-1])
            self.weights["W{}".format(
                layer + 1)] = np.random.randn(layers[layer],
                                              layers[layer-1])*np.sqrt(
                                                  2/layers[layer-1])
            # bias (float of zero's x # neurons of the layer)
            self.weights["b{}".format(
                layer + 1)] = np.zeros([layers[layer], 1], dtype=float)
