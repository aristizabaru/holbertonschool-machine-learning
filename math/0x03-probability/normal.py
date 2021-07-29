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
        variables aleatorias normales"""
        # Z = (x - μ) / σ
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """docstring - Estandarización de
        variables aleatorias normales"""
        # X = σz + μ
        return (self.stddev * z) + self.mean
