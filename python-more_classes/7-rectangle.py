#!/usr/bin/python3
"""
This module will help us to create a rectangle which:
    -have its own width and height
    -can print its own area and perimeter
    -can print its own shape
    -return accurately its shape in int
"""


class Rectangle:
    """
    This class will be used to define a rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0:
            return 0
        if self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0:
            return ""
        if self.__height == 0:
            return ""
        lines = []
        for _ in range(self.height):
            if isinstance(self.print_symbol, list):
                row = ''.join("{}".format(self.print_symbol)
                              for _ in range(self.width))
            else:
                row = str(self.print_symbol) * self.__width
            lines.append(row)
        return '\n'.join(lines)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
