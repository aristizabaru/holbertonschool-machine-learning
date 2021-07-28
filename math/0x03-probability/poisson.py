#!/usr/bin/env python3
"""This module represents Poisson distribution"""


class Poisson:
    """Represents poisson distribution.

    Def. A discrete frequency distribution which gives
    the probability of a number of 'independent events'
    occurring in a fixed time.

    Probability Mass Function (PMF):
        This function gives the probability of observing 'k'
        events in defined interval, the average of the
        events in the same interval.

        Formula → f(k,λ) = P(X = k) = (e^-λ * λᴷ) / k!
        k → # of events in a interval
        λ → avarage of events in a interval.
            Must always be positive
        e → 2.7182818285 (Euler's number)

    Cumulative Distribution Function (CDF)
        This functions gives the probability from a variable
        to be less or equal than a given value

        General Formula → F(x) = P(X ≤ x)

        Probability Distribution Formula:
        F(x) = Σ pmf(i) from i=0 to x
        x → upper limit
    """

    def __init__(self, data=None, lambtha=1.):
        """Init Poisson instance with a lambtha
        public attribute

        Expl:
            lambtha is the expected number of events
            in a interval (mean). λ has to be always > 0

            Formula → λ = Σ xᵢ / N
            Σ xᵢ → Sum of events in a interval
            N → # of events in a interval

        Args:
            data (list, optional): events. Defaults to None.

            lambtha (float, optional): average of events. Defaults to 1.0
        """
        if data is None:
            self.lambtha = float(lambtha)
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        else:
            # λ = Σ xᵢ / N
            self.lambtha = float(sum(data) / len(data))
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

    @staticmethod
    def factorial(num):
        """Computes a factorial number recursively

        Args:
            num (int): factorial number

        Returns:
            int: computed factorial number
        """
        return num * Poisson.factorial(num - 1) if num > 1 else 1

    def pmf(self, k):
        """Probability Mass Function:
        Computes the probability of observing 'k'
        events in defined interval, the average of the
        events in the same interval.

        Args:
            k (int/float): # of events in a interval

        Returns:
            float: probability of k's event success
        """
        e = 2.7182818285  # Euler's number
        k = int(k)
        λ = self.lambtha

        if k < 0:
            return 0
        # P(X = k) = (e^-λ * λᴷ) / k!
        return (e ** -λ * λ ** k) / Poisson.factorial(k)

    def cdf(self, x):
        """Cumulative Distribution Function:
        This functions gives the probability from a variable
        to be less or equal than a given value

        General Formula → F(x) = P(X ≤ x)

        Probability Distribution Formula:
        F(x) = Σ pmf(i) from i=0 to x

        Args:
            x (int/float): x → upper limit

        Returns:
            float: cumulative probability
        """
        x = int(x)

        if x < 0:
            return 0
        # Σ pmf(i) from i=0 to x
        return sum([self.pmf(i) for i in range(x + 1)])
