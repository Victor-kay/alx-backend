#!/usr/bin/env python3
"""
Module for simple pagination of a dataset.
"""

import csv
import os
from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return the start and end indexes for pagination.

    Args:
        page (int): Current page number.
        page_size (int): Number of items per page.

    Returns:
        Tuple[int, int]: Start and end indexes for pagination.
    """
    assert isinstance(page, int) and page > 0, "page must be a positive integer"
    assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index

class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """
        Retrieve the dataset from CSV file.

        Returns:
            List[List[str]]: Parsed dataset from CSV.
        """
        if self.__dataset is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, self.DATA_FILE)
            
            with open(file_path) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skipping header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Return the appropriate page of the dataset based on pagination parameters.

        Args:
            page (int, optional): Current page number. Defaults to 1.
            page_size (int, optional): Number of items per page. Defaults to 10.

        Returns:
            List[List[str]]: Paginated dataset.
        """
        start_index, end_index = index_range(page, page_size)
        
        dataset = self.dataset()
        
        if start_index >= len(dataset):
            return []
        
        return dataset[start_index:end_index]

# Testing the Server class
if __name__ == "__main__":
    server = Server()

    try:
        should_err = server.get_page(-10, 2)
    except AssertionError:
        print("AssertionError raised with negative values")

    try:
        should_err = server.get_page(0, 0)
    except AssertionError:
        print("AssertionError raised with 0")

    try:
        should_err = server.get_page(2, 'Bob')
    except AssertionError:
        print("AssertionError raised when page and/or page_size are not ints")

    print(server.get_page(1, 3))
    print(server.get_page(3, 2))
    print(server.get_page(3000, 100))
