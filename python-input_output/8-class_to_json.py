#!/usr/bin/python3
"""
This module will be used to contain a function which will
return a dictionary description with simple data structure for
JSON serialization of an object
"""


import json


def class_to_json(obj):
    """
    This function will be used to return a dictionary description with simple
    data structure for JSON serialization of an object
    """

    return obj.__dict__
