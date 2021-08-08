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
        forward_prop(self, X): calculates the forward propagation
                               of the neuron
        cost(self, Y, A): calculates the cost of the model using
                          logistic regression by quantifing the error
                          between predicted values and expected values
        evaluate(self, X, Y): Evaluates the neuron’s predictions

    Static Methods:
        loss(Y, A): calculates the loss in multiple training example
                    using logistic regression by quantifing the error
                    between predicted values and expected values.
        sigmoid(x): calculates sigmoid function to 'x' value
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

    def forward_prop(self, X):
        """calculates the forward propagation of the neuron

        Formulas:
            Y = Σ (weight * input) + bias → get the input value to
            the sigmoid activation function

        Args:
            X (numpy.ndarray): with shape (nx, m), X contains
                               the input data
                               'nx' is the number of input features
                               to the neuron
                               'm' is the number of examples

        Returns:
            int: the activated output of the neuron (prediction)
        """
        # Y = Σ (weight * input) + bias
        Y = np.dot(self.W, X) + self.b
        # apply Sigmoid activation function
        self.__A = type(self).sigmoid(Y)

        return self.A

    def cost(self, Y, A):
        """calculates the cost of the model using logistic regression
        by quantifing the error between predicted values and expected values

        Cost Function
            This function gives the messaure how well
            the model is doing in the entire training set

            J(ŷ, y) = -(1/m) * Σ L(ŷ^(i), y^(i))
            ŷ → the predicted value of y
            y → correct values
            m → # of examples of the training set
            L(ŷ^(i), y^(i) → loss function

        Args:
            Y (numpy.ndarray): contains the correct labels for the
                               input data. Shape (1, m)
            A (numpy.ndarray): contains the activated output of the
                               neuron for each example. Shape (1, m)

        Returns:
            float: cost of the model
        """
        m = Y.shape[1]

        # J(ŷ, y) = -(1/m) * Σ L(ŷ^(i), y^(i))
        J = -(1/m) * np.sum(type(self).loss(Y, A))
        return J

    def evaluate(self, X, Y):
        """Evaluates the neuron’s predictions.

        The label values would be 1 if the output of the
        network is >= 0.5 and 0 otherwise.

        Args:
            X (numpy.ndarray): contains the input data. Shape (nx, m)
                               'nx' is the number of input features to
                               the neuron
                               'm' is the number of examples
            Y (numpy.ndarray): contains the correct labels for the
                               input data. Shape (1, m)

        Returns:
            tuple: tuple[0] → numpy.ndarray with shape (1, m)
                   containing the predicted labels for each example

                   tuple[1] → float representing the cost of the model
        """
        self.__A = self.forward_prop(X)
        cost = self.cost(Y, self.A)
        prediction = np.where(self.A <= 0.5, 0, 1)

        return prediction, cost

    @staticmethod
    def loss(Y, A):
        """calculates the loss in multiple training example using
        logistic regression by quantifing the error between
        predicted values and expected values.

        Loss Function:
            This is the one used in logistic regression to messaure how well
            the model is doing in a single training example

            L(ŷ, y) = y^(i) * log(ŷ^(i)) + (1 - y^(i)) * log(1 - ŷ^(i)
            ŷ → the predicted value of y
            y → correct values

        To avoid division by zero errors, it will be used 1.0000001 - A
        instead of 1 - A

        Args:
            Y (numpy.ndarray): contains the correct labels for the
                               input data. Shape (1, m)
            A (numpy.ndarray): contains the activated output of the
                               neuron for each example. Shape (1, m)

        Returns:
            numpy.ndarray: loss of every training example
        """
        # L(ŷ, y) = y^(i) * log(ŷ^(i)) + (1 - y^(i)) * log(1 - ŷ^(i)
        L = Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)
        return L

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
