#!/usr/bin/env python3
"""
Server class to paginate a database of popular baby names.
"""

import csv
import math
from typing import List, Dict, Union, Tuple

class Server:
    """Server class to paginate a database of popular baby names."""
    
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the Server class."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the dataset from a CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset.

        Args:
            page (int, optional): Page number. Defaults to 1.
            page_size (int, optional): Number of items per page. Defaults to 10.

        Returns:
            List[List]: List of rows corresponding to the requested page.
        """
        file_path = f'/alx-backend/0x00-pagination/{self.DATA_FILE}'
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"
        
        with open(file_path) as f:
            reader = csv.reader(f)
            dataset = [row for row in reader][1:]

        start, end = self.index_range(page, page_size)
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[int, List[List], None]]:
        """
        Get hypermedia pagination details.

        Args:
            page (int, optional): Page number. Defaults to 1.
            page_size (int, optional): Number of items per page. Defaults to 10.

        Returns:
            Dict[str, Union[int, List[List], None]]: Pagination details.
        """
        dataset_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(dataset_page),
            "page": page,
            "data": dataset_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        Return a tuple of start and end indices for pagination.

        Args:
            page (int): Page number.
            page_size (int): Number of items per page.

        Returns:
            Tuple[int, int]: Start and end indices.
        """
        start = (page - 1) * page_size
        end = start + page_size
        return start, end
