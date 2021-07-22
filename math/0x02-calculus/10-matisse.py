#!/usr/bin/env python3
"""calculates the derivative of a polynomial"""


def poly_derivative(poly):
    """calculates the derivative of a polynomial

    Args:
        poly (list): coefficients representing a polynomial

    Returns:
        derivative [list]: coefficients representing
                           the derivative of the polynomial
    """
    check = all([type(coefficient) is int
                 for coefficient in poly])
    if check is False:
        return
    derivative = [poly[coefficient] * coefficient
                  for coefficient in range(1, len(poly))]
    if sum(derivative) == 0:
        return [0]
    return derivative
