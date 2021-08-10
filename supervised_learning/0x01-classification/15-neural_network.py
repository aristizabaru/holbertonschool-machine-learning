#!/usr/bin/env python3
"""represents a neural network with one hidden layer
performing binary classification"""

import numpy as np
import matplotlib.pyplot as plt


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
        cost(self, Y, A):
            calculates the cost of the model using logistic
            regression by quantifing the error between predicted
            values and expected values
        evaluate(self, X, Y):
            Evaluates the neural network’s predictions.

    Static Methods
        sigmoid(x):
            calculates sigmoid function to 'x' value.
        loss(Y, A):
            calculates the loss in multiple training example using
            logistic regression by quantifing the error between
            predicted values and expected values.
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
        """Evaluates the neural network’s predictions.

        The label values would be 1 if the output of the
        network is >= 0.5 and 0 otherwise.

        Args:
            X (numpy.ndarray): contains the input data. Shape (nx, m)
                               'nx' is the number of input features
                               to the neuron
                               'm' is the number of examples
            Y (numpy.ndarray): contains the correct labels for the
                               input data. Shape (1, m)

        Returns:
            tuple: tuple[0] → numpy.ndarray with shape (1, m)
                   containing the predicted labels for each example

                   tuple[1] → float representing the cost of the model
        """
        self.forward_prop(X)
        cost = self.cost(Y, self.A2)
        prediction = np.where(self.A2 <= 0.5, 0, 1)

        return prediction, cost

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """calculates one pass of gradient descent on the neural network.

        The derivates are calculated using the vecorization technique.

        Args:
            X (numpy.ndarray): contains the input data. Shape (nx, m)
                               nx → the number of input features to the neuron
                               m → number of examples
            Y (numpy.ndarray): contains the correct labels for the
                               input data. Shape (1, m)
            A1 (numpy.ndarray): output of the hidden layer.
            A2 (numpy.ndarray): predicted output.
            alpha (float, optional): learning rate. Defaults to 0.05.
        """
        m = Y.shape[1]
        # vectorized logistic regression's gradient descent
        # output layer
        dZ2 = A2 - Y
        db2 = np.sum(dZ2, keepdims=True, axis=1) / m
        dw2 = np.matmul(A1, dZ2.T) / m
        # hidden layer
        dZ1 = np.matmul(self.__W2.T, dZ2) * (A1 * (1 - A1))
        db1 = np.sum(dZ1, keepdims=True, axis=1) / m
        dw1 = np.matmul(X, dZ1.T) / m
        # update weigths and bias with gradient decent values
        self.__W2 = self.W2 - (alpha * dw2).T
        self.__b2 = self.b2 - (alpha * db2)
        self.__W1 = self.W1 - (alpha * dw1).T
        self.__b1 = self.b1 - (alpha * db1)

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True,
              graph=True, step=100):
        """Trains the model by doing a forward propagation
        and a gradient descent 'iterations' number of times

        Args:
            X (numpy.ndarray): contains the input data. Shape (nx, m)
                               nx → the number of input features to the neuron
                               m → number of examples
            Y (numpy.ndarray): contains the correct labels for the
                               input data. Shape (1, m)
            iterations (int, optional): the number of iterations to train over.
                                        Defaults to 5000.
            alpha (float, optional): learning rate. Defaults to 0.05.
            verbose (bool, optional): defines whether or not to print
                information about the training.
            graph (bool, optional): defines whether or not to graph information
                                    about the training once the training
                                    has completed
            step (int, optional): step to collect data from training loop

        Raises:
            TypeError: iterations must be an integer
            ValueError: iterations must be a positive integer
            TypeError: alpha must be a float
            ValueError: alpha must be positive

        Returns:
            tuple: tuple[0] → numpy.ndarray with shape (1, m)
                   containing the predicted labels for each example

                   tuple[1] → float representing the cost of the model
        """
        axis_cost = []
        axis_iteration = []

        if not isinstance(iterations, int):
            raise TypeError('iterations must be an integer')
        if iterations < 0:
            raise ValueError('iterations must be a positive integer')
        if not isinstance(alpha, float):
            raise TypeError('alpha must be a float')
        if alpha < 0:
            raise ValueError('alpha must be positive')
        if verbose or graph:
            if not isinstance(step, int):
                raise TypeError('step must be an integer')
            if step < 0 or step > iterations:
                raise ValueError('step must be positive and <= iterations')

        for i in range(iterations + 1):
            # forward propagation
            self.forward_prop(X)
            # gradient descent
            self.gradient_descent(X, Y, self.A1, self.A2, alpha)
            # add values to print
            if i % step == 0:
                cost = self.cost(Y, self.A2)
                axis_cost.append(cost)
                axis_iteration.append(i)
                # print verbose
                if verbose:
                    print("Cost after {} iterations: {}".format(i, cost))

        # print graph
        if graph:
            plt.plot(axis_iteration, axis_cost)
            plt.title('Training Cost')
            plt.xlabel('iteration')
            plt.ylabel('cost')
            plt.show()

        # get output value from evaluation
        prediction, cost = self.evaluate(X, Y)
        return prediction, cost

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
