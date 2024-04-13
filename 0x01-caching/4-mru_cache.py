#!/usr/bin/python3
""" MRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict

class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and implements MRU caching strategy
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.mru_cache = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache using MRU algorithm
        """
        if key is None or item is None:
            return

        # Check if key already exists in cache
        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # Remove most recently used item
            mru_key = next(reversed(self.mru_cache))
            print(f"DISCARD: {mru_key}")
            del self.cache_data[mru_key]
            del self.mru_cache[mru_key]

        # Add new item
        self.cache_data[key] = item
        self.mru_cache[key] = None

    def get(self, key):
        """ Get an item by key and move it to the beginning of the OrderedDict
        """
        if key not in self.cache_data:
            return None

        # Move the key to the beginning to mark it as most recently used
        del self.mru_cache[key]
        self.mru_cache[key] = None

        return self.cache_data[key]

# Testing the MRUCache class
if __name__ == '__main__':
    my_cache = MRUCache()

    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
