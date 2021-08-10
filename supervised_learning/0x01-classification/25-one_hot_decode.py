#!/usr/bin/env python3
"""one_hot_decode module"""

import numpy as np


def one_hot_decode(one_hot):
    """converts a one-hot matrix into a vector of label

    Args:
        one_hot (numpy.ndarray):
            one-hot encoded numpy.ndarray with shape (classes, m)

    Returns:
        numpy.ndarray:
            numeric labels for each example, or None on failure
    """
    if not isinstance(one_hot, np.ndarray):
        return None
    if (one_hot.sum(axis=1) - np.ones(one_hot.shape[0])).sum() != 0:
        return None
    # returns the indices of the maximum values along an axis
    one_hot_decode = np.argmax(one_hot, axis=0)
    return one_hot_decode
