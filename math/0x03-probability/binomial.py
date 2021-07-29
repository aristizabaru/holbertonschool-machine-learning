#!/usr/bin/env python3
"""This module represents Binomial distribution"""


class Binomial:
    """docstring"""

    def __init__(self, data=None, n=1, p=0.5):
        """docstring"""

        if data is None:
            if n <= 0:
                raise ValueError('n must be a positive value')
            if p <= 0 or p >= 1:
                raise ValueError('p must be greater than 0 and less than 1')
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) <= 2:
                raise ValueError('data must contain multiple values')

            n = len(data)
            # μ = Σ xᵢ / n
            μ = sum(data) / n
            # variance → σ² = Σ (x - μ)² / n
            variance = sum([(x - μ) ** 2 / n for x in data])
            self.p = 1 - (variance / μ)
            self.n = int(round(μ / self.p))
            self.p = float(μ / self.n)

    def pmf(self, k):
        """docstring"""
        k = int(k)

        if k < 0:
            return 0
        n_fac = Binomial.factorial(self.n)
        k_fac = Binomial.factorial(k)
        # (n! / (k! * (n - k)!)) * p^x * q^n-x
        return (n_fac / (k_fac * Binomial.factorial(self.n - k))) \
            * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    @staticmethod
    def factorial(num):
        """Computes a factorial number recursively

        Args:
            num (int): factorial number

        Returns:
            int: computed factorial number
        """
        return num * Binomial.factorial(num - 1) if num > 1 else 1
