#!/usr/bin/python3
"""
This module will be used to contain a function which will
write an object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Function which will write an object to a text file in JSON
    """

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(my_obj)
        return json.dumps(my_obj)
