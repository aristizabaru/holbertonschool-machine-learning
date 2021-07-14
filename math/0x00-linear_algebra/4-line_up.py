#!/usr/bin/env python3
"""Adds two arrays element-wise"""


def add_arrays(arr1, arr2):
    """Adds two arrays element-wise

    Args:
        arr1 (list): list of integers/floats
        arr2 (list): list of integers/floats

    Returns:
        add array (list): arr1 + arr2
    """
    if not is_same_dimension(arr1, arr2):
        return
    num_elements = len(arr1)
    add_array = [arr1[i] + arr2[i] for i in range(num_elements)]
    return add_array


def is_same_dimension(arr1, arr2):
    """Check if two arrays has the same dimension

    Args:
        arr1 (list): list of integers/floats
        arr2 (list): list of integers/floats

    Returns:
        boolean: check arrays length
    """
    return len(arr1) == len(arr2)
