#!/usr/bin/python3
"""
This module will contain a class BaseGeometry
with a public instance method about its area
"""


class BaseGeometry:
    """
    A class called BaseGeometry
    """

    def area(self):
        """
        A defined function which will raise
        an error message
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A defined function which will validate
        value or return an error message
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
