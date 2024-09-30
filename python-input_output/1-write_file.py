#!/usr/bin/python3
"""
This module will contain a function which will
write a string to a text file and return the numbers
of characters
"""


def write_file(filename="", text=""):
    """
    This function will allow us to write a string to as text file
    and return the numbers of characters
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
