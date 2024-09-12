#!/usr/bin/python3
""" 
This module adds the add_integer function
"""

def add_integer(a, b=98):
    """
    This function returns the addition of two numbers
    after checking their types of course

    a and b must be integers or floats, else a TypeError message will appear
    if they are floats then they'll be converted to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
