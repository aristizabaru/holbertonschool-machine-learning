#!/usr/bin/env python3
"""creates the forward propagation graph for the neural network"""
import tensorflow as tf

create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """creates the forward propagation graph for the neural network

    Args:
        x (tensorflow.python.framework.ops.Tensor):
            placeholder for the input data
        layer_sizes (list, optional):
            number of nodes in each layer of the network. Defaults to [].
        activations (list, optional):
            activation functions for each layer of the networ. Defaults to [].

    Returns:
        tensorflow.python.framework.ops.Tensor:
            prediction of the network in tensor form
    """
    # first output
    output = create_layer(x, layer_sizes[0], activations[0])
    # get other layer's outputs
    for layer in range(1, len(layer_sizes)):
        output = create_layer(output,
                              layer_sizes[layer],
                              activations[layer])
    return output
