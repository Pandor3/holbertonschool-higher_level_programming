#!/usr/bin/python3

def add_integer(a, b=98):
    result = a + b
    try:
        print("{}".format(result))
        if not isinstance(a(int, float)):
            raise TypeError ("a must be an integer")
        if not isinstance(b(int, float)):
            raise TypeError ("b must be an integer")
    except ValueError:
        return result
    finally:
        return result
