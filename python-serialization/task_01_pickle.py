#!/usr/bin/python3
"""
This module will be used to serialize and deserialize
custom Python objects with Python
"""

import os
import pickle


class CustomObject:
    """
    Custom Object class
    """

    def __init__(self, name, age, is_student):
        """
        Constructor method
        """

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display method
        """

        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize method
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        deserialize method
        """

        if not os.path.exists(filename):
            print("File not found.")
            return None

        with open(filename, 'rb') as file:
            return pickle.load(file)
