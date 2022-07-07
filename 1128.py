#!/usr/bin/env python3
'''
This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
'''

import typing
import sys

def permutations(arr: typing.List[int]) -> typing.List[typing.List[int]]:
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [[arr[0]]]
    elem = arr[0]
    perms = permutations(arr[1:])
    to_ret = []
    for p in perms:
        for i in range(len(p)):
            to_ret.append(p[:i] + [elem] + p[i:])
        to_ret.append(p[:] + [elem])
    return to_ret


if __name__ == '__main__':
    nums = [int(a) for a in sys.argv[1:]]
    print(permutations(nums))