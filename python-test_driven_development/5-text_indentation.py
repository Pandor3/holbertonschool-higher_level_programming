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

    text = text.strip()
    if text.strip() == "":
        return
    punctuations = {".", "?", ":"}
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in punctuations:
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
