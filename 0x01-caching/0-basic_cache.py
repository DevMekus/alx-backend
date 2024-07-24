#!/usr/bin/env python3
"""caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Function Represents an object that allows storing
    """
    def put(self, key, item):
        """Function Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Function Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
