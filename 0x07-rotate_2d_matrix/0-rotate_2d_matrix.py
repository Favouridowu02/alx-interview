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
    matrix.reverse()
    matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
