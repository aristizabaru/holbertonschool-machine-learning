#!/usr/bin/env python3
"""calculates the derivative of a polynomial"""


def poly_derivative(poly):
    """calculates the derivative of a polynomial

    Explanation: A variable is something that gives a certain
          value when equated to a constant.

          We know that anything raised to the power zero
          gives us the value 1, which is undoubtedly a constant.

          That means x^0 is a constant as well, and hence
          DOES NOT qualify as a polynomial.

    Args:
        poly (list): coefficients representing a polynomial

    Returns:
        derivative [list]: coefficients representing
                           the derivative of the polynomial
    """
    check = all([type(coefficient) is int
                 for coefficient in poly])
    if type(poly) is not list\
            or len(poly) == 0\
            or check is False:
        return
    if len(poly) == 1:
        return [0]
    derivative = [poly[coefficient] * coefficient
                  for coefficient in range(1, len(poly))]
    if sum(derivative) == 0:
        return [0]
    return derivative
