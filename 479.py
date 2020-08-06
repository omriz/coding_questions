#!/usr/bin/env python3
"""
Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""

import sys
import typing


def permutations(arr: typing.List[int]) -> typing.List[typing.List[int]]:
    # We're going to do half recursive and half iterative.
    # We're going to recursivly discover permutations of each sub array without the first
    # array memeber.
    # We then going to insert the first member in every place in the array to generate all permutations
    # There is some question regarding repeated numbers. If we want we can make a set instead of a list in to_ret
    # The solution bellow does conversions between sets and tuples to make a unique. We can remove those if we know each
    # number is unique
    if len(arr) < 2:
        return [arr]
    if len(arr) == 2:
        return [arr, [arr[1],arr[0]]]
    perms = permutations(arr[1:])
    to_ret = set()
    for p in perms:
        for i in range(len(arr)):
            to_ret.add(tuple(p[:i] + [arr[0]] + p[i:]))
    return [list(x) for x in to_ret]



if __name__ == "__main__":
    print(permutations([int(x) for x in sys.argv[1:]]))
