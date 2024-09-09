#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Copier la liste via methode de slicing, : veux dire toute la liste
    new_list = my_list[:]
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list

    new_list[idx] = element
    return new_list
