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
    # accuracy = correct_predictions / all_predictions
    accuracy = tf.divide(y, y_pred)
    # Computes the mean of elements across dimensions of a tensor
    mean = tf.reduce_mean(tf.cast(accuracy, tf.float32))
    return mean
