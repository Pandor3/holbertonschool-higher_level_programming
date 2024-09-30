#!/usr/bin/python3
"""
This module will be used to contain a function which will define
a class named Student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            return getattr(attrs, list)
        else:
            return self.__dict__
