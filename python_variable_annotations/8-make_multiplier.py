#!/usr/bin/env python3
from typing import Callable

"""
This module contains a function `make_multiplier`
which generates a multiplier function. The generated function
will multiply a float by a given multiplier.
"""

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that creates a multiplier function.

    Args:
        multiplier (float): The value by which to multiply the input.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns it multiplied by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        """Function that multiplies a float by the multiplier.

        Args:
            x (float): The value to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return x * multiplier

    return multiplier_function
