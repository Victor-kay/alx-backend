#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union

class Server:
    """Server class to paginate a database of popular baby names."""
    
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server class."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the dataset from a CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Union[int, List[List]]]:
        """
        Get hypermedia pagination details based on index.

        Args:
            index (int, optional): Index of the start item. Defaults to None.
            page_size (int, optional): Number of items per page. Defaults to 10.

        Returns:
            Dict[str, Union[int, List[List]]]: Pagination details.
        """
        indexed_dataset = self.indexed_dataset()
        total_items = len(indexed_dataset)
        assert index is None or 0 <= index < total_items, "Index out of range"

        data = [indexed_dataset[i] for i in range(index, min(index + page_size, total_items))]

        next_index = index + page_size if index + page_size < total_items else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
