#!/usr/bin/python3
"""
This module will contain a function which will read data
from one format CSV to convert it into JSON format
"""


import csv
import json


def convert_csv_to_json(csv_file, json_file='data.json'):
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)

        return True
    except FileNotFoundError:
        print("File not found")
        return False
