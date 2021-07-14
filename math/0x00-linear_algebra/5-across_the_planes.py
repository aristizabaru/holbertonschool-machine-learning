#!/usr/bin/env python3
"""Adds two matrices element-wise:"""


def add_matrices2D(mat1, mat2):
    """Adds two matrices element-wise

    Args:
        mat1 (list): matrix of integers/floats
        mat2 (list): matrix of integers/floats

    Returns:
        add_matrix (list): mat1 + mat2
    """
    if not is_same_dimension(mat1, mat2):
        return
    num_rows = len(mat1)
    num_colums = len(mat1[0])
    add_matrix = [[mat1[i][j] + mat2[i][j]
                  for j in range(num_colums)] for i in range(num_rows)]

    return add_matrix


def is_same_dimension(mat1, mat2):
    """Check if two matrix has the same dimension

    Args:
        mat1 (list): matrix of integers/floats
        mat2 (list): matrix of integers/floats

    Returns:
        boolean: check arrays length
    """
    shape1 = matrix_shape(mat1)
    shape2 = matrix_shape(mat2)
    return shape1 == shape2


def matrix_shape(matrix):
    """Calculates the shape of a matrix

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
