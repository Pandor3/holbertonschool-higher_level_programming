#!/usr/bin/python3
"""
This module will be used to try
duck typing about circles and rectangles
"""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Shape class
    """

    @abstractmethod
    def area(self):
        """
        A defined function which will define
        the area of a shape
        """

        pass

    @abstractmethod
    def perimeter(self):
        """
        A defined function which will define
        the perimeter of a shape
        """

        pass


class Circle(Shape):
    """
    Circle class
    """
    def __init__(self, radius):
        """
        Constructor
        """
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * pi

    def perimeter(self):
        return (self.radius * 2) * pi


class Rectangle(Shape):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        """
        Constructor
        """
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


def shape_info(Shape):
    """
    A defined function which will print area
    and perimeter
    """

    print("Area: {}".format(Shape.area()))
    print("Perimeter: {}".format(Shape.perimeter()))
