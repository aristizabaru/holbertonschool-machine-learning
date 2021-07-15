#!/usr/bin/env python3
"""Performs element-wise addition,
subtraction, multiplication, and division"""


def np_elementwise(mat1, mat2):
    """Performs element-wise addition, subtraction,
    multiplication, and division

    Args:
        mat1 (numpy.ndarray): matrix A
        mat2 (numpy.ndarray): matrix B

    Returns:
        tuple: element-wise sum, difference, product,
                and quotient, respectively
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
