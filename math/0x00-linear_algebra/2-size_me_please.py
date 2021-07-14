#!/usr/bin/env python3
"""Calculates the shape of a matrix"""


def matrix_shape(matrix):
    """Calculates the shape of a matrix with the same dimension

    Args:
        matrix (list): matrix to be evaluated

    Returns:
        result (list): list of integers desribing the matrix shape
    """
    # base case
    if type(matrix) is int:
        return []

    result = matrix_shape(matrix[0])
    result.insert(0, len(matrix))
    return result
