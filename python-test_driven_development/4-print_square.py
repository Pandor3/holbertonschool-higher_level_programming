#!/usr/bin/python3


"""
This contains the print_size function
"""


def print_square(size):

    """
Prints:
    Size Square
Size:
    Value of the print
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
