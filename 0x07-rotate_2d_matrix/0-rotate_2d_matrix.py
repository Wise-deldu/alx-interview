#!usr/bin/python3
"""Module for 2D Matrix rotation.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees counterclockwise in-place.

    Parameters:
        matrix (list[list[int]]): the 2D matrix to be rotated.

    Returns:
        None
    """
    # First, we transpose the matrix
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Then, we reverse each row
    for row in matrix:
        row.reverse()
