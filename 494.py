#!/usr/bin/env python3
"""
Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
"""

import typing
import sys


def max_sub_array(arr: typing.List[int]) -> int:
    # We're going to do it this way.
    # We're going to iterate over the array and find the subsection with the most negative attribution.
    multi_array = arr * 2
    max_size = len(arr)
    max_max = 0
    start_max = 0
    running_max = 0
    for i in range(len(multi_array)):
        print("%d %d" % (start_max, i))
        running_max = running_max + multi_array[i]
        if i - start_max >= max_size - 1:
            running_max -= multi_array[start_max]
            start_max += 1
        if running_max <= 0:
            start_max = i + 1
            running_max = 0
        if running_max > max_max:
            max_max = running_max
    return max_max


if __name__ == "__main__":
    print(max_sub_array([int(x) for x in sys.argv[1:]]))
