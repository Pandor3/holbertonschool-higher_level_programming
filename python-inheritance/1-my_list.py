#!/usr/bin/python3
"""
This module will contain a class
which inherits from another class
"""


class MyList(list):
    """
    This class will inherit for the
    list class
    """

    def print_sorted(self):
        """
        This defined function will print
        the list in a sorted order
        """

        print(sorted(self))
