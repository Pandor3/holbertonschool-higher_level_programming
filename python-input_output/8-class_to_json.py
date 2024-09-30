#!/usr/bin/python3
"""
This module will contain a function which returns the dictionary description
for JSON serialization of an object
"""

import json


def class_to_json(obj):
    return obj.__dict__
