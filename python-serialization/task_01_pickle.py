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
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print("an Error occured", e)

    @classmethod
    def deserialize(cls, filename):
        """
        deserialize method
        """

        if not os.path.exists(filename):
            print("File not found.")
            return None

        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except pickle.UnpicklingError:
            print("Error occurred while unpickling.")
            return None
        except Exception as e:
            print("Error occurred:", e)
            return None
