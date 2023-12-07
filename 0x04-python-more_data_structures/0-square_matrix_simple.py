#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    columns = len(matrix[0]) if matrix else 0

    square_matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            square_matrix[i][j] = matrix[i][j] ** 2

    return square_matrix
