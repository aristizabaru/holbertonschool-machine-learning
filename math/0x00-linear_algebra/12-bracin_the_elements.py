#!/usr/bin/env python3
"""Performs element-wise addition, subtraction, multiplication, and division"""

import numpy as np


def np_elementwise(mat1, mat2):
    """Performs element-wise addition, subtraction, multiplication, and division

    Args:
        mat1 (numpy.ndarray): matrix A
        mat2 (numpy.ndarray): matrix B

    Returns:
        tuple: element-wise sum, difference, product, and quotient, respectively
    """
    return (np.add(mat1, mat2), np.subtract(mat1, mat2),
            np.multiply(mat1, mat2), np.divide(mat1, mat2))
