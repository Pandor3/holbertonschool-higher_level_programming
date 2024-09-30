#!/usr/bin/python3
"""
This module will contain a function which will return an object
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    This function will return an object represented by
    a JSON string
    """

    my_str = json.loads(my_str)
    return my_str
