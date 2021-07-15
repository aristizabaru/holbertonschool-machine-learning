#!/usr/bin/env python3
"""Concatenates two matrices along a specific axis"""


def np_cat(mat1, mat2, axis=0):
    """Concatenates twi matrices along a specific axis

    Args:
        mat1 (numpy.ndarray): matrix A
        mat2 (numpy.ndarray): matrix B
        axis (int, optional): axis to perform concatenation. Defaults to 0.

    Returns:
        numpy.ndarray: mat1 concatenated with mat2
    """
    import numpy as np
    return np.concatenate((mat1, mat2), axis=axis)
