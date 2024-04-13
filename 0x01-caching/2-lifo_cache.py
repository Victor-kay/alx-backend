#!/usr/bin/python3
""" LIFOCache module
"""

# Importing BaseCaching class from base_caching module
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and implements LIFO caching strategy
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache using LIFO algorithm
        """
        if key is None or item is None:
            return

        # Check if cache is full
        if len(self.cache_data) >= self.MAX_ITEMS:
            # Get the last key inserted in cache (LIFO)
            last_key = list(self.cache_data.keys())[-1]
            print(f"DISCARD: {last_key}")
            del self.cache_data[last_key]
        
        # Add new item
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)

# Exporting LIFOCache for import
LIFOCache = LIFOCache

# Testing the LIFOCache class
if __name__ == '__main__':
    my_cache = LIFOCache()

    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()

    my_cache.put("E", "Battery")
    my_cache.print_cache()

    my_cache.put("C", "Street")
    my_cache.print_cache()

    my_cache.put("F", "Mission")
    my_cache.print_cache()

    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
