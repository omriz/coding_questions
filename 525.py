#!/usr/env/bin python3
"""
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
"""

import typing


def print_spiral(m: typing.List[typing.List[int]]):
    i_start = 0
    i_end = len(m)
    j_start = 0
    j_end = len(m[0])
    while j_start < j_end and i_start < i_end:
        for j in range(j_start, j_end):
            print(m[i_start][j])
        i_start += 1
        for i in range(i_start, i_end):
            print(m[i][j_end - 1])
        j_end -= 1
        for j in range(j_end - 1, j_start - 1, -1):
            print(m[i_end - 1][j])
        i_end -= 1
        for i in range(i_end - 1, i_start - 1, -1):
            print(m[i][j_start])
        j_start += 1

    pass


if __name__ == "__main__":
    m = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    print_spiral(m)
