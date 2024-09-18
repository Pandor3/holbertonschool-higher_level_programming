#!/usr/bin/python3
"""
This module will help us to create a rectangle which:
    -have its own width and height
    -can print its own area and perimeter
    -can print its own shape
    -return accurately its shape in int
    -can add and delete its instances
    -can count its instances
    -can use various symbols for its shape
    -can create and compare other shapes
    -can return its shape with its details
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
                row.elements = [
                    "{}".format(self.print_symbol) for _ in range(self.width)
                ]
                row = ''.join(row_elements)
            else:
                row = str(self.print_symbol) * self.__width
            lines.append(row)
        return '\n'.join(lines)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
