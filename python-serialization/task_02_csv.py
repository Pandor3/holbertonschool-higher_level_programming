#!/usr/bin/python3
"""
This module will contain a function which will read data
from one format CSV to convert it into JSON format
"""


import csv
import json


def convert_csv_to_json(self):
    with open(csv, 'r') as file:
        reader = csv.DictReader(file)
    for rown in reader:
        print(row)
    with open(csv, 'r') as file:
        json.dump(file)
