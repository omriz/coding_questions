#!/usr/bin/env python3
'''
This problem was asked by Google.

In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.

Here is an example:

1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2
Write a program to determine whether a given input is a Toeplitz matrix.
'''

def is_square(mat):
    s = len(mat)
    for l in mat:
        if s != len(l):
            return False
    return True

def is_topelitz(matrix):
    x = 0
    while x < len(matrix):
        i = x
        j = 0
        prev = matrix[x][0]
        while i < len(matrix) and j < len(matrix[i]):
            if matrix[i][j] != prev:
                return False
            i += 1
            j += 1
        x += 1
    y = 1
    while y < len(matrix[0]):
        i = 0
        j = y
        prev = matrix[0][y]
        while i < len(matrix) and j < len(matrix[i]):
            if matrix[i][j] != prev:
                return False
            i += 1
            j += 1
        y += 1
    return True

def main():
    matrix = [
    [1,2,3,4,8],
    [5,1,2,3,4],
    [4,5,1,2,3],
    [7,4,5,1,2],      
    ]
    if len(matrix) == 0:
        print("Null matrix")
        return
    if len(matrix) == 1 and type(matrix[0]) == int:
        print ("Toeplitz matrix")
        return
    if  is_topelitz(matrix):
        print ("Toeplitz matrix")
        return
    print ("not Toeplitz matrix")
        

if __name__ == '__main__':
    main()