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
    if not_list(poly) or is_empty(poly) or not_number(poly) or C < 0:
        return
    if poly == [0]:
        return [C]
    integral = [div(coefficient, i + 1) for i, coefficient in enumerate(poly)]

    return [C] + integral


def not_number(poly):
    """checks if poly has numbers

    Args:
        poly (list): coefficients representing a polynomial

    Returns:
        bool: True/False
    """
    for item in poly:
        if type(item) is not int:
            return True
    return False


def is_empty(poly):
    """check if list is empty

    Args:
        poly (list): coefficients representing a polynomial

    Returns:
        bool: True/False
    """
    return len(poly) == 0


def not_list(poly):
    """check if list is type list

    Args:
        poly (list): coefficients representing a polynomial

    Returns:
        bool: True/False
    """
    return type(poly) is not list


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
