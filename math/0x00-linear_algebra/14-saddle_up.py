#!/usr/bin/env python3
"""Performs matrix multiplication"""

import numpy as np


def np_matmul(mat1, mat2):
    """Performs matrix multiplication

    Args:
        mat1 (numpy.ndarray): matrix A
        mat2 (numpy.ndarray): matrix B

    Returns:
        numpy.ndarray: product of matrix multiplication
    """
    return np.matmul(mat1, mat2)
