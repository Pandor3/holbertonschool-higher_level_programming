#!/usr/bin/python3
"""
This module adds the matrix_divided function
"""

def matrix_divided(matrix, div):
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
    return new_matrix
