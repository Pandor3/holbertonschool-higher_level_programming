#!/usr/bin/python3
"""
This module will contain a function which
will be used to determine if the object is
an instance.
"""


def is_kind_of_class(obj, a_class):
    """
    Function which will determine if
    the object is an instance.
    """

    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
