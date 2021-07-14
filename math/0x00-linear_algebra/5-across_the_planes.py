#!/usr/bin/env python3
"""Adds two matrices element-wise"""


def add_matrices2D(mat1, mat2):
    """Adds two matrices element-wise

    Args:
        mat1 (list): matrix of integers/floats
        mat2 (list): matrix of integers/floats

    Returns:
        add_matrix (list): mat1 + mat2
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return
    num_rows = len(mat1)
    num_colums = len(mat1[0])
    add_matrix = [[mat1[i][j] + mat2[i][j]
                  for j in range(num_colums)] for i in range(num_rows)]

    return add_matrix
