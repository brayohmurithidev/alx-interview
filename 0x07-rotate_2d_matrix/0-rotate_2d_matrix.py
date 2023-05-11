#!/usr/bin/python3

'''
Rotating the 2d matrix
'''


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise in place.

    The matrix is rotated in place, meaning the original matrix is modified.

    Args:
        matrix: A list of lists representing the 2D matrix.

    Returns:
        None.
    """
    n = len(matrix[0])
    for i in range(n - 1, -1, -1):
        for j in range(0, n):
            matrix[j].append(matrix[i].pop(0))
