#!/usr/bin/python3

def safe_print_integer(value):
    count = 0
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            count = 1
    except (TypeError, ValueError):
        pass
    return count
