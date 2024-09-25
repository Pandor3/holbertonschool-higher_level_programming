#!/usr/bin/python3
"""
This module will be used to iterate a counter
for each items
"""

from abc import ABC, abstractmethod


class CountedIterator:
    """
    CountedIterator class
    """

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.count

    def __iter__(self):
        return self
