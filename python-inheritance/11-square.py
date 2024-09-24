#!/usr/bin/python3
"""
Module which will print a Square
"""


Rectangle = __import__('10-square').Rectangle


class Square(Rectangle):
    """
    Class which will print a Square
    """

    def __init__(self, size):
        """
        Constructor of the Square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        a defined function which will print the area
        """

        return self.__size ** 2
