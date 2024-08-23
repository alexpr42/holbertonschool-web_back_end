#!/usr/bin/env python3


"""function that works with mixed list of int and float"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return of the sum as a float"""
    return sum(mxd_lst)
