#!/usr/bin/env python3
"""calculates the accuracy of a prediction"""
import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """docstring"""
    loss = tf.losses.softmax_cross_entropy(y, y_pred)
    return loss
