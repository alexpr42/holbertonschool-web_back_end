#!/usr/bin/env python3
from typing import List, Union

"""function that works with mixed list of int and float"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return of the sum as a float"""
    return sum(mxd_lst)
