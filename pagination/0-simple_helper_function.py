#!/usr/bin/env python3
"""function that takes two integer arguments"""


def index_range(page: int, page_size: int) -> tuple:
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
