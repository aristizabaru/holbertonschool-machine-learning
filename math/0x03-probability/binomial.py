#!/usr/bin/env python3
"""This module represents Binomial distribution"""


class Binomial:
    """docstring"""

    def __init__(self, data=None, n=1, p=0.5):
        """docstring"""

        if data is None:
            if n < 0:
                raise ValueError("n must be a positive value")
            if p < 0 or p > 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')

            n = len(data)
            # μ = Σ xᵢ / n
            μ = sum(data) / n
            # variance → σ² = Σ (x - μ)² / n
            variance = sum([(x - μ) ** 2 / n for x in data])
            self.p = 1 - (variance / μ)
            self.n = int(round(μ / self.p))
            self.p = μ / self.n
