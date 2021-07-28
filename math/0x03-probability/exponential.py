#!/usr/bin/env python3
"""This module represents Exponential distribution"""


class Exponential:
    """Represents an Exponential distribution

    Def. One of the widely used continuous distributions.
    It is often used to model the time elapsed between events

    Probability Mass Function (PMF):
        This function gives the probability of the next
        event to happend before given value 'x'

        Formula → f(x) = λe^-λx
        x → value of the event
        λ → avarage of events in a interval.
            Must always be positive
        e → 2.7182818285 (Euler's number)

        formula mean  λ = 1 / (Σ xᵢ / N)

    Cumulative Distribution Function (CDF):
        This functions gives the probability from a variable
        to be less or equal than a given value

        General Formula → F(x) = P(X ≤ x)

        Probability Distribution Formula:
        F(x) = 1 - e^-λx
        x → value of the event
        λ → avarage of events in a interval.
            Must always be positive
        e → 2.7182818285 (Euler's number)

        formula mean  λ = 1 / (Σ xᵢ / N)
    """

    def __init__(self, data=None, lambtha=1.):
        """Init Exponential instance with a lambtha
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
        """Probability Mass Function (PMF):
        This function gives the probability of the next
        event to happend before given value 'x'

        Formula → f(x) = λe^-λx
        x → value of the event
        λ → avarage of events in a interval.
            Must always be positive
        e → 2.7182818285 (Euler's number)

        formula mean  λ = 1 / (Σ xᵢ / N)

        Args:
            x (int/float): value of the event

        Returns:
            int/float: probability of an event to happen
                       before 'x'
        """
        e = 2.7182818285  # Euler's number
        λ = self.lambtha

        if x < 0:
            return 0
        # f(x) = λe^-λx
        return λ * e ** (-λ * x)

    def cdf(self, x):
        """Cumulative Distribution Function (CDF):
        This functions gives the probability from a variable
        to be less or equal than a given value

        General Formula → F(x) = P(X ≤ x)

        Probability Distribution Formula:
        F(x) = 1 - e^-λx
        x → value of the event
        λ → avarage of events in a interval.
            Must always be positive
        e → 2.7182818285 (Euler's number)

        formula mean  λ = 1 / (Σ xᵢ / N)

        Args:
            x (int/float): value of the event

        Returns:
            int/float: cumulative probability'
        """
        e = 2.7182818285  # Euler's number
        λ = self.lambtha

        if x < 0:
            return 0
        # F(x) = 1 - e^-λx
        return 1 - e ** (-λ * x)
