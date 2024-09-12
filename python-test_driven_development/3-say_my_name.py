#!/usr/bin/python3

"""
This contains the say_my_name function which prints a name and last name
"""

def say_my_name(first_name, last_name=""):


    """
    Parameters:
    First_name which is a string containing the first name
    Last_name which is a string containing the last name

    Raises:
    TypeError is first_name or last_name are not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
