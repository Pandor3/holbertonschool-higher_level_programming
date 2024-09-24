#!/usr/bin/python3
"""
This module will be used to define a class Rectangle
which inherits from another class aswell as its
various settings.
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
        if not isinstance(height, int):
            raise TypeError("{} must be an integer".format(height))
        elif not isinstance(width, int):
            raise TypeError("{} must be an integer".format(width))

    def area(self):
        """
        A defined function which will print and return
        the area of the Rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """
        A defined function which will print the parameters used
        to calculate the area of a rectangle
        """

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
