#!/usr/bin/env python3
"""This module represents Exponential distribution"""


class Exponential:
    """Time til next event

        formula mean  λ = 1 / (Σ xᵢ / N)
    """

    def __init__(self, data=None, lambtha=1.):
        """Init Poisson instance with a lambtha
        public attribute

        Expl:
            lambtha is the expected number of events
            in a interval (mean). λ has to be always > 0

            Formula → λ = 1 / (Σ xᵢ / N)
            Σ xᵢ → Sum of events in a interval
            N → # of events in a interval

        Args:
            data (list, optional): events. Defaults to None.

            lambtha (float, optional): average of events. Defaults to 1.0
        """
        if data is None:
            self.lambtha = float(lambtha)
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            # λ = 1 / (Σ xᵢ / N)
            self.lambtha = float(1 / (sum(data) / len(data)))

    def pdf(self, x):
        """docstring"""
        e = 2.7182818285  # Euler's number
        λ = self.lambtha

        if x < 0:
            return 0
        # f(x) = λe^-λx
        return λ * e ** (-λ * x)

    def cdf(self, x):
        """docstring"""
        e = 2.7182818285  # Euler's number
        λ = self.lambtha

        if x < 0:
            return 0
        # F(x) = Σ 1 - e^-λx
        return 1 - e ** -λ * x
