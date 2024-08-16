#!/usr/bin/env python3

""" annotate functions paprameters"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a
        sequence from the input and its length.
    """

    return [(i, len(i)) for i in lst]
