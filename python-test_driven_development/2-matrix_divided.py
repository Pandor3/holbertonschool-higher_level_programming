#!/usr/bin/python3

"""
This module adds the matrix_divided function
"""


def matrix_divided(matrix, div):

    """
    The function divides numbers in a matrix before putting them in a new matrix
    Parameters :
    Matrix and Div
    Return:
    it will return the matrix with the divided numbers
    Raises:
    TypeError in case if the matrix is not in a list of lists with integers or floats
    TypeError in case the rows of the matrixes are not at the same size
    TypeError in case if div is not an integer
    ZerodivisionError in case if div is equal to 0
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
    return new_matrix
