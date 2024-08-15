#!/usr/bin/env python3
from typing import Callable

""" Annotated function that takes float multiplier as arg"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
