#!/usr/bin/python3
"""
This module will show how to create a dragon
"""


from abc import ABC, abstractmethod


class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def swim(self):
        print("The creature swims!")

    def fly(self):
        print("The creature flies!")

    def roar(self):
        print("The dragon roars!")
