#!/usr/bin/python3
"""
This module will be used to:
    -define a square
    -define its size
    -define its errors
"""


class Square:
    """
    This class is used to define a square.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
