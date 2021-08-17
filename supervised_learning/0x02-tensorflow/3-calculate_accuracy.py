#!/usr/bin/env python3
"""calculates the accuracy of a prediction"""
import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """calculates the accuracy of a prediction

    Args:
        y (tensorflow.python.framework.ops.Tensor):
            placeholder for the labels of the input data
        y_pred (tensorflow.python.framework.ops.Tensor):
            tensor containing the network’s predictions

    Returns:
        tensorflow.python.framework.ops.Tensor:
             tensor containing the decimal accuracy of the prediction
    """
    equality = tf.equal(y, y_pred),
    # Computes the mean of elements across dimensions of a tensor
    mean = tf.reduce_mean(tf.cast(equality, 'float32'))
    return mean
