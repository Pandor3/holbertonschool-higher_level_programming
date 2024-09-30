#!/usr/bin/python3
"""
This module will contain a function which will append a string
at the end of a text file and return the number of characters created
"""


def append_write(filename="", text=""):
    """
    Function which will append a string at the end of a
    defined text file and return the number of
    characters
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
