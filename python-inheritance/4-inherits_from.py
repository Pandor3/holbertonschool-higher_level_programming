#!/usr/bin/python3
"""
This module will be used to contain a function
which will return True if the object is an instance
of a class which inherited from another class
"""


def inherits_from(obj, a_class):
    """
    This defined function is used to
    return True if an object is an instance
    of a class or inherited from a class
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return (True)
    else:
        return (False)
