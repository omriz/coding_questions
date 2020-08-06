#!/usr/bin/env python3
"""
You are given an array of integers, where each element represents the maximum number of steps that can be jumped going
forward from that element. Write a function to return the minimum number of jumps you must take in order to get from
the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the optimal solution involves jumping from 6 to 5,
and then from 5 to 9.
"""

import sys
import typing


def find_minimal_jumps(arr: typing.List[int]) -> int:
    jumps = [0]*len(arr)
    for i in range(len(arr)-2,-1,-1):
        if arr[i] <= 0:
            jumps[i] = len(arr)
        if arr[i] >= len(arr) - i:
            jumps[i] = 1
            continue
        minimal = len(arr) - i
        for j in range(i+1, i+arr[i]+1):
            if minimal > 1+jumps[j]:
                minimal = 1+jumps[j]
        jumps[i] = minimal
        print(jumps)
    return jumps[0]



if __name__ == "__main__":
    print(find_minimal_jumps([int(a) for a in sys.argv[1:]]))
