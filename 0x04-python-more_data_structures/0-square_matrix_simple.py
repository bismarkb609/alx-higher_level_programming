#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    resultingMatrix = []

    for i in range(len(matrix)):
        resultingMatrix += [list(map(lambda x: x ** 2, matrix[i]))]
    return resultingMatrix
