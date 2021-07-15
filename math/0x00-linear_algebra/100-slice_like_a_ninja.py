#!/usr/bin/env python3
"""Slices a matrix along specific axes"""


def np_slice(matrix, axes={}):
    """Slices a matrix along specific axes
    The if no axe is passed along the dictonary
    the default value will be `None`

    Args:
        matrix (numpy.ndarray): matrix to be sliced
        axes (dict, optional): slices. Defaults to {}.

    Returns:
        numpy.ndarray: sliced matrix
    """
    slices = []
    # find all available axes
    for i in range(len(matrix.shape)):
        if i in axes:
            # unpack elements to slice function
            slices.append(slice(*axes[i]))
        else:
            slices.append(slice(None, None, None))
    # Using a non-tuple sequence for multidimensional indexing is deprecated
    return matrix[tuple(slices)]
