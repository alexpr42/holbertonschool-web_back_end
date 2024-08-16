#!/usr/bin/env python3
from typing import Callable

""" Annotated function that takes float multiplier as arg"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(x: float) -> float:
        """ function that multiplies a foat
        by multiplier. annotated function
        """
        return x * multiplier
    """return a multipler function"""
    return multiplier_function
