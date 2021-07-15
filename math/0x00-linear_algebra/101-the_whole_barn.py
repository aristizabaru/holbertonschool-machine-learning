#!/usr/bin/env python3
"""Adds two matrices"""


def add_matrices(mat1, mat2):
    """Adds two matrices

    Args:
        mat1 (list): matrix A
        mat2 (list): matrix B

    Returns:
        new_matrix (list): addition of matrix A and B
    """
    mat1_shape = matrix_shape(mat1)
    mat2_shape = matrix_shape(mat2)
    steps = len(mat1_shape)

    if mat1_shape != mat2_shape:
        return
    new_matrix = get_add_matrix(mat1, mat2, steps)
    return new_matrix


def get_add_matrix(mat1, mat2, steps):
    """Adds two matrices. Does not validate shape

    Args:
        mat1 (list): matrix A
        mat2 (list): matrix B
        steps (int): axes of the matrix

    Returns:
        add_matrix (list): addition of matrix A and B
    """
    # base case
    if steps == 1:
        new_matrix = add_arrays(mat1, mat2)
        return new_matrix

    add_matrix = list()
    for i in range(len(mat1)):
        new_matrix = get_add_matrix(mat1[i], mat2[i], steps - 1)
        add_matrix.append(new_matrix)
    return add_matrix


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


def add_arrays(arr1, arr2):
    """Adds two arrays element-wise

    Args:
        arr1 (list): list of integers/floats
        arr2 (list): list of integers/floats

    Returns:
        add array (list): arr1 + arr2
    """
    num_elements = len(arr1)
    add_array = [arr1[i] + arr2[i] for i in range(num_elements)]
    return add_array
