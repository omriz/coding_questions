#!/usr/bin/env python3
'''
This problem was asked by Facebook.

On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue.
One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |
'''

import sys
import typing

def get_next(a,b):
    if a == 'B':
        if b == 'G':
            return 'R'
        else:
            return 'G'
    elif a == 'G':
        if b == 'R':
            return 'B'
        else:
            return 'R'
    else: # a == 'R'
        if b == 'B':
            return 'G'
        else:
            return 'B'

def get_minimal(row: typing.List[str]) -> typing.List[str]:
    if len(row) == 0:
        return []
    if len(row) == 1:
        return row[:]
    if len(row) == 2:
        if row[0] == row[1]:
            return [row[0],row[1]]
        else:
            return [get_next(row[0],row[1])]
    op_a = [row[0]] + get_minimal(row[1:])
    if row[0] == row[1]:
        op_b = row[0:1] + get_minimal(row[2:])
    else:
        op_b = [get_next(row[0],row[1])] + get_minimal(row[2:])
    if op_a != row:
        op_a = get_minimal(op_a)
    if op_b != row:
        op_b = get_minimal(op_b)
    if len(op_a) < len(op_b):
        return op_a
    return op_b


def get_minimal_xor(row):
    if len(row) == 0:
        return []
    new_row = row[:]
    while len(set(new_row)) != 1:
        i = 0
        while i < len(new_row) -1:
            if new_row[i] != new_row[i+1]:
                break
            i += 1
        if i != len(new_row)-1:
            new_row = new_row[:i]  + [get_next(new_row[i],new_row[i+1])] + new_row[i+2:]
    return new_row
        
def main():
    #print(get_minimal(sys.argv[1:]))
    print(get_minimal_xor(sys.argv[1:]))

if __name__ == "__main__":
    main()