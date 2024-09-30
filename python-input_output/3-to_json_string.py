#!/usr/bin/python3
"""
This module will return a JSON represention of
an object/string
"""


import json

def to_json_string(my_obj):
    """
    This function whill return the JSON representations of
    an object/string
    """

    return json.dumps(my_obj)
