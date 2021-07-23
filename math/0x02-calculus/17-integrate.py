#!/usr/bin/env python3
"""calculates the integral of a polynomial"""


def poly_integral(poly, C=0):
    """calculates the derivative of a polynomial

    Explanation: A variable is something that gives a certain
          value when equated to a constant.

          We know that anything raised to the power zero
          gives us the value 1, which is undoubtedly a constant.

          That means x^0 is a constant as well, and hence
          DOES NOT qualify as a polynomial.

    Args:
        poly (list): coefficients representing a polynomial
        C (int): integration constant

    Returns:
        integral [list]: coefficients representing
                         the integral of the polynomial
    """
    if type(poly) is not list or len(poly) == 0:
        return
    integral = [div(coefficient, i + 1) for i, coefficient in enumerate(poly)]

    return [C] + integral


def div(x, y):
    """divide x and y representing as an integer
    the coefficient if it is a whole number

    Args:
        x (int): dividend
        y (int): divider

    Returns:
        int/float: result of divition
    """
    if y == 0:
        return 0
    if x % y == 0:
        return x // y
    else:
        return x / y
