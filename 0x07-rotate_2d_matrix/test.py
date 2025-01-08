#!/usr/bin/python3
"""
    This Module is used to test the Rotattion of a 2 Dimenstional 
"""


def rotate(matrix):
    matrix.reverse()
    # return [[row[i] for row in matrix] for i in range(len(matrix) - 1, -1, -1)]
    # return [[row[i] for row in matrix.reverse()] for i in range(len(matrix) - 1, -1, -1)]
    matrix = [[row[i] for row in matrix] for i in range(len(matrix))]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix,"\n\n")
# matrix = rotate(matrix)
rotate(matrix)
print(matrix)