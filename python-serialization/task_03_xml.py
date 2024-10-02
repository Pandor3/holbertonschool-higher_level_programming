#!/usr/bin/python3
"""
This module will be used to contain 2 functions which will
- Take a python dictionary and a filename as parameters which
will serialize the dictionary into XML and save it.
- Take a filename as its parameter, read the XML data from that
and return a deserialized Python dictionary
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Defined function which will serialize a dictionary
    into XML and save it
    """

    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Defined function which will read a XML data and
    return a deserialized Python dictionary
    """

    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
