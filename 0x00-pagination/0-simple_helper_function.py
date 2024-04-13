#!/usr/bin/env python3

"""
Simple Helper Function Module

This module provides a function to calculate the start and end index
for pagination based on given page and page size.
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for pagination.

    Args:
    - page (int): Current page number (1-indexed).
    - page_size (int): Number of items per page.

    Returns:
    tuple: A tuple containing start and end index.
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    return (start_index, end_index)
