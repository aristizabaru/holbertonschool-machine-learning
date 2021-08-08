#!/usr/bin/env python3
"""represents a single neuron performing binary classification"""
import numpy as np


class Neuron:
    """represents a single neuron performing binary classification

    Attributes:
        W (numpy.ndarray): the weights vector for the neuron
        b (int): the bias for the neuron
        A (int): the activated output of the neuron (prediction)

    Methods:
        __init__(self, nx): constructor
    """

    def __init__(self, nx):
        """defines a single neuron performing binary classification

        Args:
            nx (int): number of input features to the neuron

        Raises:
            TypeError: nx must be an integer
            ValueError: nx must be a positive integer
        """
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """define public attribute W

        Returns:
            numpy.ndarray: the weights vector for the neuron
        """
        return self.__W

    @property
    def b(self):
        """define public attribute b

        Returns:
           int: the bias for the neuron
        """
        return self.__b

    @property
    def A(self):
        """define public attribute A

        Returns:
           int: the activated output of the neuron (prediction)
        """
        return self.__A
