#!/usr/bin/python3
"""
This module will be used to return the sounds of
various animals
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal class
    """

    @abstractmethod
    def sound(self):
        """
        A defined function which will produce
        a sound
        """

        pass


class Dog(Animal):
    """
    Dog class
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Cat class
    """
    def sound(self):
        return "Meow"
