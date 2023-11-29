#!/usr/bin/python3
"""strting the file"""

def matrix_divided(matrix, div):
    """divide all matrix element by div"""
    mx = []
    if not div:
        raise ZeroDivisionError("division by zero")
    check = 0
    for row in matrix:
        res_row = []
        if check != len(row) and check:
            raise TypeError("Each row of the mx must have the same size")
        check = len(row)
        for i in range(0, check):
            if not type(row[i]) in [float, int]:
                raise TypeError("mx must be a matrix (list of lists) of integers/floats")
            res_row.append(round(row[i] / div, 2))
        mx.append(res_row)
    return mx

