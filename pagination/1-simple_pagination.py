#!/usr/bin/env python3
"""takes two interger arguments with default values"""


import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a page of the dataset.
        """
        # Ensure page and page_size are valid integers greater than 0
        assert isinstance(page, int) and page > 0,
        assert isinstance(page_size, int) and page_size > 0,

        # Calculate the start and end indexes for the requested page
        start, end = index_range(page, page_size)

        # Return the slice of the dataset for the requested page
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]
