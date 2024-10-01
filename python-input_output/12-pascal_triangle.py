#!/usr/bin/python3
"""
This module will be used to contain a function which will
return a list of list of integers representing a Pascal Triangle
"""


def pascal_triangle(n):
    """
    This function define Pascal's triangle which returns a list of
    lists of integers
    """

    n_list = []
    if n <= 0:
        return n_list

    for x in range(n):
        list_added = [1] * (x + 1)
        if x > 1:
            for y in range(1, x):
                list_added[y] = n_list[x - 1][y - 1] + n_list[x - 1][y]
        n_list.append(list_added)

    return n_list
