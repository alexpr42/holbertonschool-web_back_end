#!/usr/bin/env python3
from typing import Callable

"""
This module provides a function `make_multiplier`.
The `make_multiplier` function takes a float as an argument
and returns another function that multiplies a given float by
the specified multiplier.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The value by which to multiply input floats.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns the product of the float and the multiplier.
    """
    def multiplier_function(x: float) -> float:
        """Multiplies a float by the pre-defined multiplier.

        Args:
            x (float): The float to be multiplied.

        Returns:
            float: The result of multiplying `x` by the multiplier.
        """
        return x * multiplier

    return multiplier_function
