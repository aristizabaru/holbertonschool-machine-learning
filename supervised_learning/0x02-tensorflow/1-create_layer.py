#!/usr/bin/env python3
"""creates a model"""
import tensorflow as tf


def create_layer(prev, n, activation):
    """creates a model

    Args:
        prev (tensorflow.python.framework.ops.Tensor):
            tensor output of the previous layer
        n (int):
            number of nodes in the layer to create
        activation (function):
            activation function that the layer should use

    Returns:
        tensorflow.python.framework.ops.Tensor:
            tensor output of the layer
    """
    he_et_al = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    model = tf.layers.Dense(units=n,
                            activation=activation,
                            kernel_initializer=he_et_al,
                            name='layer')
    return model(prev)
