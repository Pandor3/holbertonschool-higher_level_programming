#!/usr/bin/python3
"""
This module will contain a Square with its
various parameters
"""

Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """
    This class contains a Square
    """

    def __init__(self, size):
        """
        A constructor which will initialize the size of the
        square
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        A defined function which will print and return
        the area of a square
        """

        return self.__size * self.__size

    def __str__(self):
        """
        A defined function which will print and return 
        the area of a square
        """

        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
