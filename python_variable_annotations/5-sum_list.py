#!/usr/bin/env python3
from typing import List

"""
This module contains a function called `sum_list` that takes a list of floats
and returns the sum of those floats.
"""


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of floats.
    Args:
    input_list (List[float]): A list of numbers of type float.

    Returns:
    float: The sum of all elements in `input_list`.
    """
    return sum(input_list)
