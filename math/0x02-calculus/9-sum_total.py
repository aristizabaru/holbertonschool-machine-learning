#!/usr/bin/env python3
"""calculates summation"""


def summation_i_squared(n):
    """calculates summation of `i=1`
    to `n` where `i` is power of `2`

    Args:
        n (int): upper limit

    Returns:
        summation [int]: summation of n
    """
    if n is None or type(n) is not int or n < 1:
        return
    if n == 1:
        return 1
    summation = round(n*(n+1) * (2*n+1) / 6)
    return summation
