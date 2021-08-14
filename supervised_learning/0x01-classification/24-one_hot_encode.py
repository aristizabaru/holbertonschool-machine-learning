#!/usr/bin/env python3
"""one_hot_encode module"""

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
    if not isinstance(Y, np.ndarray):
        return None
    if not isinstance(classes, int):
        return None

    one_hot_encode = np.eye(classes)[Y].T
    return one_hot_encode
