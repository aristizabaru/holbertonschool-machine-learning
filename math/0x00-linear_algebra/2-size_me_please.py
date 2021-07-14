#!/usr/bin/env python3
"""Calculates the shape of a matrix"""


def matrix_shape(matrix):
    """Calculates the shape of a matrix with the same dimension

    Args:
        matrix (list): matrix to be evaluated

    Returns:
        shape_matrix (list): list of integers desribing the matrix shape
    """
    # base case
    if type(matrix) is int:
        return []

    shape_matrix = matrix_shape(matrix[0])
    shape_matrix.insert(0, len(matrix))
    return shape_matrix
