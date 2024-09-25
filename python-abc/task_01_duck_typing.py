#!/usr/bin/python3
"""
This module will be used to try
duck typing about circles and rectangles
"""


from abc import ABC, abstractmethod


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


def shape_info(Shape):
    """
    A defined function which will print area
    and perimeter
    """
