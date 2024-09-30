#!/usr/bin/python3
"""
This module will be used to contain a function which will create
an Object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    This function will be used to create an Object from a JSON file"
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
