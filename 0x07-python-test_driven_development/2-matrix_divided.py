#!/usr/bin/python3

def matrix_divided(matrix, div):
    # Check if matrix is a list of lists and each sublist has the same length
    if (
        not isinstance(matrix, list)
        or not all(isinstance(i, list) for i in matrix)
        or len(set(len(i) for i in matrix)) != 1
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if div is a number and not zero
    if not isinstance(div, (int, float)) or div == 0:
        raise TypeError("div must be a number")

    # Create a new matrix and divide each element by div
    new_matrix = []
    for row in matrix:
        new_row = [round(i / div, 2) for i in row]
        new_matrix.append(new_row)

    return new_matrix
