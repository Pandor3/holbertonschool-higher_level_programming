#!/usr/bin/python3
"""
This module will be used to:
    -define a square
    -define its size
    -define its errors
    -define its area
    -put a setter - getter
    -print the shape of the square
"""


class Square:
    """
    This class is used to define a square.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
