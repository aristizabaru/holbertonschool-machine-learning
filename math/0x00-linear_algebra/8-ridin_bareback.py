#!/usr/bin/env python3
"""Performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """Performs matrix multiplication

    Args:
        mat1 (list): matrix A
        mat2 (list): matrix B

    Returns:
        matrix_product (list): product of mat1 * mat2
    """
    if len(mat1[0]) != len(mat2):
        return

    # create empty matrix
    matrix_product = [[0 for _ in range(len(mat2[0]))]
                      for _ in range(len(mat1))]

    # iterate through rows of mat1
    for i in range(len(mat1)):
        # iterate through columns of mat2
        for j in range(len(mat2[0])):
            # iterate through rows of mat2
            for k in range(len(mat2)):
                matrix_product[i][j] += mat1[i][k] * mat2[k][j]

    return matrix_product
