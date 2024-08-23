#!/usr/bin/env python3


""" function that thake a string and float arguments"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return the string and the float at square"""
    return (k, float(v ** 2))
