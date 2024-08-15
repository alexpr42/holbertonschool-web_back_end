#!/usr/bin/env python3
from typing import Union, Tuple

""" function that thake a string and float arguments"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    # return of the str and float at square
    return (k, float(v ** 2))
