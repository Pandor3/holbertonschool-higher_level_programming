#!/usr/bin/python3
"""
This module will contain a function which will read a text file
and print it
"""


def read_file(filename=""):
    """
    Function which will read and print
    a text file
    """

    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
