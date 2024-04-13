#!/usr/bin/python3
""" LRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict

class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and implements LRU caching strategy
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.lru_cache = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache using LRU algorithm
        """
        if key is None or item is None:
            return

        # Check if key already exists in cache
        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # Remove least recently used item
            lru_key = next(iter(self.lru_cache))
            print(f"DISCARD: {lru_key}")
            del self.lru_cache[lru_key]

        # Add new item
        self.cache_data[key] = item
        self.lru_cache[key] = None

    def get(self, key):
        """ Get an item by key and move it to the end of the OrderedDict
        """
        if key not in self.cache_data:
            return None

        # Move the key to the end to mark it as most recently used
        if key in self.lru_cache:
            del self.lru_cache[key]
        self.lru_cache[key] = None

        return self.cache_data[key]

# Testing the LRUCache class
if __name__ == '__main__':
    my_cache = LRUCache()

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
