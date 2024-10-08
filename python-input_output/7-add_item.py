#!/usr/bin/python3
"""
This module will be used to contain a function which will add
all arguments to a Python list and then save them in a file
"""


import os
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []
items.extend(sys.argv[1:])
save_to_json_file(items, filename)
