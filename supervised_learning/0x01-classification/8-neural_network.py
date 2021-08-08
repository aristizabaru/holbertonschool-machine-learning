#!/usr/bin/env python3
"""represents a neural network with one hidden layer
performing binary classification"""

import numpy as np


class NeuralNetwork:
    """represents a neural network with one hidden layer
    performing binary classification

    Attributes:
        W1 (numpy.ndarray): the weights vector for the hidden layer.
        b1 (numpy.ndarray): the bias for the hidden layer.
        A1 (int): the activated output for the hidden layer.
        W2 (numpy.ndarray): the weights vector for the output layer.
        b2 (int): the bias for the output layer.
        A2 (int): the activated output for the output layer (prediction).

    Methods:
        __init__(self, nx, nodes): constructor
    """

    def __init__(self, nx, nodes):
        """defines a neural network with one hidden layer
    performing binary classification

        Args:
            nx (int): number of input features.
            nodes (int): number of nodes found in the hidden layer.

        Raises:
            TypeError: nx must be an integer.
            ValueError: nx must be a positive integer.
            TypeError: nodes must be an integer.
            ValueError: nodes must be a positive integer.
        """
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        if not isinstance(nodes, int):
            raise TypeError('nodes must be an integer')
        if nodes < 1:
            raise ValueError('nodes must be a positive integer')
        self.W1 = np.random.randn(nodes, nx)
        self.b1 = np.zeros([nodes, 1], dtype=float)
        self.A1 = 0
        self.W2 = np.random.randn(1, nodes)
        self.b2 = 0
        self.A2 = 0
