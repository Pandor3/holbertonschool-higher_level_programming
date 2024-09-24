#!/usr/bin/python3
"""
This module will contain a class BaseGeometry
with a public instance method about its area
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class rectangle which inherits from another
    class called BaseGeometry
    """

    def __init__(self, width, height):
        """
        A constructor which contains width and height
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        print("[TypeError] height must be an integer")
