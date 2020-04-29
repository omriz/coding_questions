#!/usr/bin/env python3
"""
Given an array of numbers, find the maximum sum of any contiguous
subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86],
the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0,
since we would not take any elements.

Do this in O(N) time.
"""

import typing
import sys


def max_array(m: typing.List[int]) -> typing.List[int]:
    # going right
    right_max = m[0]
    right_index = 0
    right_sum = m[0]
    for i in range(1, len(m)):
        right_sum += m[i]
        if right_sum > right_max:
            right_index = i
            right_max = right_sum
    # going left
    left_max = m[-1]
    left_index = len(m) - 1
    left_sum = m[-1]
    for i in range(len(m) - 2, -1, -1):
        left_sum += m[i]
        if left_sum > left_max:
            left_index = i
            left_max = left_sum
    # If no intersection then it means we don't want to return anything
    return m[left_index : right_index + 1]


if __name__ == "__main__":
    print(max_array([int(a) for a in sys.argv[1:]]))
