#!/usr/bin/python3

"""
This contains the tex_indentation function
"""


def text_indentation(text):

    """
Args:
    Text contains the string to print
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text.strip() == "":
        return
    pun = {".", "?", ":"}
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in pun:
            result += "\n\n"
        i += 1
    print(result.strip())
