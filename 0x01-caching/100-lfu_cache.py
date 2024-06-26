#!/usr/bin/python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict

class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and implements LFU caching strategy
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.frequency = {}  # Dictionary to store frequency of each key
        self.lru_cache = OrderedDict()  # For LRU when LFU has more than one item to discard

    def update_frequency(self, key):
        """ Update the frequency of the given key
        """
        self.frequency[key] = self.frequency.get(key, 0) + 1

    def put(self, key, item):
        """ Add an item in the cache using LFU algorithm
        """
        if key is None or item is None:
            return

        # Update frequency of the key
        self.update_frequency(key)

        # Check if key already exists in cache
        if key in self.cache_data:
            del self.cache_data[key]
            self.lru_cache[key] = None
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # Remove least frequency used item
            min_freq = min(self.frequency.values())
            items_with_min_freq = [k for k, v in self.frequency.items() if v == min_freq]

            # If more than one item has the same min frequency, use LRU to decide
            if len(items_with_min_freq) > 1:
                lru_key = next(iter(self.lru_cache))
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.lru_cache[lru_key]
                print(f"DISCARD: {lru_key}")
            else:
                discard_key = items_with_min_freq[0]
                del self.cache_data[discard_key]
                del self.frequency[discard_key]
                print(f"DISCARD: {discard_key}")

        # Add new item
        self.cache_data[key] = item
        self.lru_cache[key] = None

    def get(self, key):
        """ Get an item by key and move it to the beginning of the OrderedDict
        """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and move the key to the beginning of LRU OrderedDict
        self.update_frequency(key)
        del self.lru_cache[key]
        self.lru_cache[key] = None

        return self.cache_data[key]


# Testing the LFUCache class
if __name__ == '__main__':
    my_cache = LFUCache()

    # Testing Empty cache
    my_cache.print_cache()

    # Testing Cache with one element
    my_cache.put("A", "Hello")
    my_cache.print_cache()
    print(my_cache.get("A"))

    # Testing put method with key or item as None
    my_cache.put(None, "test")
    my_cache.put("test_key", None)
    my_cache.print_cache()

    # Testing BaseCaching.MAX_ITEMS = 1 add 5 items
    BaseCaching.MAX_ITEMS = 1
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.print_cache()

    # Reset MAX_ITEMS for next tests
    BaseCaching.MAX_ITEMS = 2

    # Testing BaseCaching.MAX_ITEMS = 2 add 10 items
    for i in range(1, 11):
        my_cache.put(f"Key{i}", f"Value{i}")
    my_cache.print_cache()

    # Reset MAX_ITEMS for next tests
    BaseCaching.MAX_ITEMS = 5

    # Testing BaseCaching.MAX_ITEMS = 5 add 10 items
    for i in range(1, 11):
        my_cache.put(f"Key{i}", f"Value{i}")
    my_cache.print_cache()
