#!/usr/bin/env python3
"""
Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1],
return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
"""

import typing
import sys

def longest_sub_array(arr: typing.List[int]) -> int:
    m = 0
    for i in range(len(arr)):
        restricted = {arr[i]:True}
        c = 1
        for j in range(i+1,len(arr)):
            if arr[j] in restricted:
                if c > m:
                    m = c
                break
            else:
                c += 1
                restricted[arr[j]] = True
        if c > m:
            m = c
    return m




if __name__ == "__main__":
    print(longest_sub_array([int(x) for x in sys.argv[1:]]))
