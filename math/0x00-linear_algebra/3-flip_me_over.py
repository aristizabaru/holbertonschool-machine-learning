#!/usr/bin/env python3
"""Transpose a 2D matrix"""


def matrix_transpose(matrix):
    """Transpose a 2D matrix

    Args:
        matrix (list): 2D

    Returns:
        transpose (list): transposed list
    """
    num_colums = len(matrix[0])
    transpose = [[row[i] for row in matrix] for i in range(num_colums)]
    return transpose
