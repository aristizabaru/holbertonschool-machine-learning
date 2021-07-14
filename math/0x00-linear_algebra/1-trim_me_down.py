#!/usr/bin/env python3
"""Trim a matrix creating a new one with the 3rd and 4th columns"""
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
the_middle = []
the_middle = [colum[2:4] for colum in matrix]
print("The middle columns of the matrix are: {}".format(the_middle))
