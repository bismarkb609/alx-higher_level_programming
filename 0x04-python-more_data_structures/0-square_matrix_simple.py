#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix)

    for n in range(rows):
        for m in range(cols):
            print(matrix[n][m] * matrix[n][m], end=" ")
