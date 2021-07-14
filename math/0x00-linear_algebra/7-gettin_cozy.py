#!/usr/bin/env python3
"""Concatenates two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two matrices along a specific axis

    Args:
        mat1 (list): matrix of integer/floats
        mat2 (list): matrix of integer/floats
        axis (int, optional): axis to perform concatenation. Defaults to 0.

    Returns:
        list: mat1 concatenated with mat2
    """
    # check if columns are equals
    if not axis and len(mat1[0]) == len(mat2[0]):
        return mat1 + mat2
    # check if rows are equals
    elif axis == 1 and len(mat1) == len(mat2):
        return [mat1[row] + mat2[row] for row in range(len(mat1))]
