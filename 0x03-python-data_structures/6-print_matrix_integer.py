#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers"""
    for i in len(maxtrix):
        for j in len(matrix[i]):
            print("{}".format(matrix[i][j]), end="")
            if j != (len(matrix[i]) - 1):
                print(" ", end="")
        print("")
