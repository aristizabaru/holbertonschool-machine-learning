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
        W2 (numpy.ndarray): the weights vector for the output layer
        b2 (int): the bias for the output layer.
        A2 (int): the activated output for the output layer (prediction).

    Methods:
        __init__(self, nx, nodes): constructor
        forward_prop(self, X):
            calculates the forward propagation of the NN

    Static Methods
        sigmoid(x):
            calculates sigmoid function to 'x' value.
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
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros([nodes, 1], dtype=float)
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """defines public attribute W1"""
        return self.__W1

    @property
    def b1(self):
        """defines public attribute b1"""
        return self.__b1

    @property
    def A1(self):
        """defines public attribute A1"""
        return self.__A1

    @property
    def W2(self):
        """defines public attribute W2"""
        return self.__W2

    @property
    def b2(self):
        """defines public attribute b2"""
        return self.__b2

    @property
    def A2(self):
        """defines public attribute A2"""
        return self.__A2

    def forward_prop(self, X):
        """calculates the forward propagation of the NN

        Formulas:
            Y = Σ (weight * input) + bias → get the input value to
            the sigmoid activation function

        Args:
            X (numpy.ndarray):
                with shape (nx, m), X contains the input data.
                'nx' is the number of input features to the neuron.
                'm' is the number of examples.

        Returns:
            int: the activated output of the NN (prediction)
        """
        # pass hidden layer
        Y1 = np.dot(self.W1, X) + self.b1
        self.__A1 = type(self).sigmoid(Y1)
        # pass output layer
        Y2 = np.dot(self.W2, self.A1) + self.b2
        self.__A2 = type(self).sigmoid(Y2)

        return self.A1, self.A2

    @staticmethod
    def sigmoid(x):
        """calculates sigmoid function to 'x' value

        Formula:
            S(x) = 1 / (1 + e^-x)
            e → 2.7182818285 (Euler's number)

        Args:
            x (numpy.ndarray): contains the dot product
                               of the input data and weights
                               plus the bias

        Returns:
            numpy.ndarray: the activation values
        """
        # S(x) = 1 / (1 + e^-x)
        return 1/(1 + np.exp(-x))
