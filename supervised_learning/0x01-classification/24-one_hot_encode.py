#!/usr/bin/env python3
"""one_hot_encode module"""

from matplotlib.pyplot import cla
import numpy as np


def one_hot_encode(Y, classes):
    """converts a numeric label vector into
    a one-hot matrix

    Args:
        Y (numpy.ndarray):
            shape (m,) containing numeric class labels
        classes (int): maximum number of classes found in Y

    Returns:
        numpy.ndarray:
            one-hot encoding of Y with shape (classes, m),
            or None on failure
    """
    # if len(Y) == 0 or not isinstance(classes, int) or classes < 1:
    #     return None
    one_hot_encode = np.eye(classes)[Y]
    return one_hot_encode.T
