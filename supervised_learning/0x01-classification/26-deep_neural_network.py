#!/usr/bin/env python3
"""represents a deep neural network performing
binary classification"""

import numpy as np
import matplotlib.pyplot as plt
import pickle


class DeepNeuralNetwork:
    """represents a deep neural network
    performing binary classification

    Attributes:
        L (int): the number of layers in the neural network.
        cache (dict): hold all intermediary values of the network.
        weights (dict): hold all weights and biased of the network.

    Methods:
        __init__(self, nx, nodes): constructor.
        forward_prop(self, X):
            calculates the forward propagation of the deep NN.
        cost(self, Y, A):
            calculates the cost of the model.
        evaluate(self, X, Y):
            Evaluates the neural network’s predictions.
        gradient_descent(self, Y, cache, alpha=0.05):
            calculates one pass of gradient descent on
            the neural network.
        train(self, X, Y, iterations=5000, alpha=0.05, verbose=True,
              graph=True, step=100):
            Trains the model by doing a forward propagation
            and a gradient descent 'iterations' number of times

    Static Methods:
        sigmoid(x):
            calculates sigmoid function to 'x' value.
        loss(Y, A):
            calculates the loss in multiple training examples
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
        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError('layers must be a list of positive integers')
        # check if layer[0] in list is integer
        if layers[0] < 1 or not isinstance(layers[0], int):
            raise TypeError('layers must be a list of positive integers')

        self.__L = len(layers)
        self.__cache = dict()
        self.__weights = dict()
        # initialize L1
        # weights (neurons x input features)
        self.__weights['W1'] = np.random.randn(layers[0], nx)*np.sqrt(2/nx)
        # bias (float of zero's x # neurons of the layer)
        self.__weights['b1'] = np.zeros([layers[0], 1], dtype=float)
        # initialize L2 and L3
        for layer in range(1, self.L):
            # check if layer[layer] in list is integer
            if layers[layer] < 1 or not isinstance(layers[layer], int):
                raise TypeError('layers must be a list of positive integers')
            # He et al method
            # weight = np.random.randn(layer_size[l],layer_size[l-1])
            # *np.sqrt(2/layer_size[l-1])
            self.__weights['W{}'.format(
                layer + 1)] = np.random.randn(layers[layer],
                                              layers[layer-1])*np.sqrt(
                2/layers[layer-1])
            # bias (float of zero's x # neurons of the layer)
            self.__weights['b{}'.format(
                layer + 1)] = np.zeros([layers[layer], 1], dtype=float)

    @property
    def L(self):
        """defines public attribute L"""
        return self.__L

    @property
    def cache(self):
        """defines public attribute cache"""
        return self.__cache

    @property
    def weights(self):
        """defines public attribute weights"""
        return self.__weights

    def forward_prop(self, X):
        """calculates the forward propagation of the deep NN

        Formulas:
            Y = Σ (weight * input) + bias → get the input value to
            the sigmoid activation function

        Args:
            X (numpy.ndarray):
                with shape (nx, m), X contains the input data.
                'nx' is the number of input features to the neuron.
                'm' is the number of examples.

        Returns:
            tuple: the output of the neural network and the cache, respectively
        """
        # calculate A0
        self.__cache['A0'] = X
        # calculate An (i == layer)
        for i in range(1, self.L + 1):
            Y = np.dot(self.weights['W{}'.format(i)], self.cache['A{}'.format(
                i - 1)]) + self.weights['b{}'.format(i)]
            self.__cache['A{}'.format(i)] = type(self).sigmoid(Y)
        # (output deep NN, cache all layers)
        return self.cache['A{}'.format(self.L)], self.cache

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
        # output layer
        A = self.cache['A{}'.format(self.L)]
        cost = self.cost(Y, A)
        prediction = np.where(A <= 0.5, 0, 1)

        return prediction, cost

    def gradient_descent(self, Y, cache, alpha=0.05):
        """calculates one pass of gradient descent on the neural network.

        The derivates are calculated using the vecorization technique.

        Args:
            Y (numpy.ndarray): contains the correct labels for the
                               input data. Shape (1, m)
            cache (dict): contains all the intermediary values of the network
            alpha (float, optional): learning rate. Defaults to 0.05.
        """
        # vectorized logistic regression's gradient descent
        m = Y.shape[1]
        A = cache['A{}'.format(self.__L)]
        dZ = A - Y
        for i in range(self.__L, 0, -1):
            # output value
            A = cache['A{}'.format(i - 1)]
            # weights
            w = self.weights['W{}'.format(i)]
            # bias
            b = self.weights["b{}".format(i)]

            db = np.sum(dZ, axis=1, keepdims=True) / m
            dw = np.matmul(A, dZ.T) / m
            dZ = np.matmul(w.T, dZ) * (A * (1 - A))
            self.__weights['W{}'.format(i)] = w - (alpha * dw).T
            self.__weights['b{}'.format(i)] = b - (alpha * db)

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
            A, _ = self.forward_prop(X)
            # gradient descent
            self.gradient_descent(Y, self.cache, alpha)
            # add values to print
            if i % step == 0:
                cost = self.cost(Y, A)
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

        prediction, cost = self.evaluate(X, Y)
        return prediction, cost

    def save(self, filename):
        """saves the instance object to a file in pickle format

        Args:
            filename (str): file to which the object should be saved
        """
        if filename[-4:] != '.pkl':
            filename += '.pkl'
        # open to write bytes
        with open(filename, 'wb') as file:
            pickle.dump(self.__dict__, file)

    @staticmethod
    def load(filename):
        """loads a pickled DeepNeuralNetwork object

        Args:
            filename (str): the file from which the object should be loaded

        Returns:
            DeepNeuralNetwork: loaded object
        """
        try:
            # opent to read bytes
            with open(filename, 'rb') as file:
                deep_attributes = pickle.load(file)
            # <class 'dict'> -> <class 'DeepNeuralNetwork'>
            dummy_layers = [5, 3, 1]
            deep_NN = DeepNeuralNetwork(1, dummy_layers)
            for key in deep_NN.__dict__:
                deep_NN.__dict__[key] = deep_attributes[key]
            return deep_NN
        except FileNotFoundError:
            return None

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
