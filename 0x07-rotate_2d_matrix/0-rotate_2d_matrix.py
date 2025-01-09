#!/usr/bin/python3
"""
    This Module is used to test the Rotattion of a 2 Dimenstional
"""


def rotate_2d_matrix(matrix):
    """
        This Method is used to Rotate a 2D
        Matrix by 90 degree clockwise

        Arguments:
            matrix: the 2-Dimensional Matrix to be rotated
    """
    if not isinstance(matrix, list):
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: isinstance(x, list), matrix)):
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if not all(map(lambda x: len(x) == cols, matrix)):
        return
    c, r = 0, rows - 1
    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if r == -1:
            r = rows - 1
            c += 1
        matrix[-1].append(matrix[r][c])
        if c == cols - 1 and r >= -1:
            matrix.pop(r)
        r -= 1
