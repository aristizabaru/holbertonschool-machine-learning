#!/usr/bin/env python3
"""calculates the accuracy of a prediction"""
import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """calculates the accuracy of a prediction

    Exp. 'y' and 'y_pred' are one hot encoded, tf.argmax()
    creates new vectors with the indexes of the correct
    asnwers (y) and predicted answers (y_pred).
    tf.equal() evaluates both vecotors and return true/false
    if there's a match and finally tf.reduce_mean() calculates
    the average of correct answers.

    Args:
        y (tensorflow.python.framework.ops.Tensor):
            placeholder for the labels of the input data
        y_pred (tensorflow.python.framework.ops.Tensor):
            tensor containing the network’s predictions

    Returns:
        tensorflow.python.framework.ops.Tensor:
             tensor containing the decimal accuracy of the prediction
    """
    # new vector with the indexes of the correct asnwers
    correct_answers = tf.argmax(y, 1)
    # new vector with the indexes of the predicted asnwers
    predicted_answers = tf.argmax(y, 1)
    # evaluate if both answers match (true/false)
    predictions = tf.equal(correct_answers, predicted_answers)
    # compute the mean of the predictions vector
    # casting bool values to floats
    accuracy_percentage = tf.reduce_mean(tf.cast(predictions, "float"))

    return accuracy_percentage
