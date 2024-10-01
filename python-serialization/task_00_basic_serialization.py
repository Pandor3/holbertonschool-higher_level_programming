#!/usr/bin/python3
"""
This module will be used to contain a basic serialization which will
add the functionality to serialize a Python dictionary to a JSON file
aswell as deserialize a JSON file to recreate a Python dictionary
"""


import pickle


def serialize_and_save_to_file(data, filename):
    """
    Defined function which will serialize
    and save a Python dictionary to a JSON file
    """

    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """
    Defined function which will deserialize a JSON file
    to recreate a Python dictionary
    """

    with open(filename, 'rb') as file:
        data = pickle.load(file)
    return data
