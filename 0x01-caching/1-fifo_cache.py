#!/usr/bin/python3
""" FIFOCache module
"""

# Importing BaseCaching class from base_caching module
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and implements FIFO caching strategy
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm
        """
        if key is None or item is None:
            return
        
        # Check if cache is full
        if len(self.cache_data) >= self.MAX_ITEMS:
            # Get the first key inserted in cache (FIFO)
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            del self.cache_data[first_key]
        
        # Add new item
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)

# Testing the FIFOCache class
if __name__ == '__main__':
    my_cache = FIFOCache()

    # Test empty cache
    print("Testing empty cache:")
    my_cache.print_cache()

    # Test cache with one element
    print("\nTesting cache with one element:")
    my_cache.put("A", "Hello")
    my_cache.print_cache()
    print(my_cache.get("A"))

    # Test put and get methods with None values
    print("\nTesting put and get with None values:")
    my_cache.put(None, "World")
    my_cache.put("B", None)
    my_cache.print_cache()

    # Test get method with non-existent key
    print("\nTesting get with non-existent key:")
    print(my_cache.get("C"))

    # Test different cache sizes
    for max_items in [1, 2, 5]:
        BaseCaching.MAX_ITEMS = max_items
        print(f"\nTesting with BaseCaching.MAX_ITEMS = {max_items}:")
        for i in range(10):
            my_cache.put(f"Key_{i}", f"Value_{i}")
        my_cache.print_cache()

    # Test PEP8 validation (manually check or use tools like flake8)
