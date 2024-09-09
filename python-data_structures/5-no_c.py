#!/usr/bin/python3

def no_c(my_string):

    n_string = ''.join([char for char in my_string if char not in ('c', 'C')])
    return n_string
