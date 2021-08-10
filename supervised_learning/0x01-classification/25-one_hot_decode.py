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
    if np.sum(one_hot) > len(one_hot):
        return None
    # returns the indices of the maximum values along an axis
    try:
        one_hot_decode = np.argmax(one_hot, axis=0)
        return one_hot_decode
    except Exception:
        return None
