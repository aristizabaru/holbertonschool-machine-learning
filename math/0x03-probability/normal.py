#!/usr/bin/env python3
"""This module represents Normal distribution"""


class Normal:
    """docstring"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """docstring"""

        if data is None:
            self.mean = float(mean)
            self.stddev = float(stddev)
            if stddev <= 0:
                raise ValueError('stddev must be a positive value')
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')

            n = len(data)
            # μ = Σ xᵢ / n
            self.mean = sum(data) / n
            # variance → σ² = Σ (x - μ)² / n
            variance = sum([(x - self.mean) ** 2 / n for x in data])
            # σ = √σ²
            self.stddev = variance ** (1/2)

    def z_score(self, x):
        """docstring - Estandarización de
        variables aleatorias normales

        Return the desviación normalizada
        para validar tabla estandarizada
        """
        # Z = (x - μ) / σ
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """docstring - Estandarización de
        variables aleatorias normales

        Return desviación normal tiπficada
        """
        # X = σz + μ
        return (self.stddev * z) + self.mean

    def pdf(self, x):
        """docstring"""
        e = 2.7182818285  # Euler's number
        π = 3.1415926535
        μ = self.mean
        σ = self.stddev
        variance = σ ** 2

        # f(x) = e^−((x−μ)² / (2σ²)) / σ√2π
        exp = -((x - μ) ** 2) / (2 * variance)
        divisor = σ * ((2 * π) ** (1/2))
        return (e ** exp) / divisor

    def cdf(self, x):
        """docstring"""
        π = 3.1415926535
        μ = self.mean
        σ = self.stddev
        quotient = (x - μ) / (σ * (2 ** 0.5))
        erf = (2 / (π ** 0.5)) * (quotient - ((quotient ** 3) / 3)
                                  + ((quotient ** 5) / 10)
                                  - ((quotient ** 7) / 42)
                                  + ((quotient ** 9) / 216))
        return ((1/2) * (1 + erf))
