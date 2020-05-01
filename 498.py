#!/usr/bin/env python3
"""
Given an array of integers out of order, determine the bounds of the
smallest window that must be sorted in order for the entire array to be sorted.
For example, given [3, 7, 5, 6, 9], you should return (1, 3).
"""

import sys
import typing


def minimal_sort_index(arr: typing.List[int]) -> typing.Tuple[int, int]:
    if len(arr) <= 1:
        return (0, 0)
    start_index = -1
    stop_index = 0
    curr_max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < curr_max:
            if start_index == -1:
                start_index = i - 1
            stop_index = i
        else:
            curr_max = arr[i]
    return (start_index, stop_index)


if __name__ == "__main__":
    print(minimal_sort_index([int(x) for x in sys.argv[1:]]))
