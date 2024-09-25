#!usr/bin/python3
"""
This module will be used to define notifications
messages whenever a command is used.
"""


from abc import ABC, abstractmethod


class VerboseList(list):
    """
    VerboseList class
    """

    def append(self, element):
        print("Added {} to the list.".format(element))
        super().append(element)

    def extend(self, element):
        print("Extended the list with {} items.".format(element))
        super().extend(element)

    def remove(self, element):
        print("Removed {} from the list.".format(element))
        super().remove(element)

    def pop(self, element=-1):
        item = super().pop(element)
        print("Popped {} from the list.".format(item))
        return item
