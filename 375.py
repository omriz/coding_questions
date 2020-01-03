#!/usr/bin/env python3
"""
The h-index is a metric used to measure the impact and productivity of a scientist or researcher.

A scientist has index _h_ if _h_ of their _N_ papers have at least _h_ citations each, and the other N - h papers have no more than _h_ citations each. If there are multiple possible values for _h_, the maximum value is used.

Given an array of natural numbers, with each value representing the number of citations of a researcher's paper, return the h-index of that researcher.

For example, if the array was:

[4, 0, 0, 2, 3]

This means the researcher has 5 papers with 4, 1, 0, 2, and 3 citations respectively. The h-index for this researcher is 2, since they have 2 papers with at least 2 citations and the remaining 3 papers have no more than 2 citations.
"""

import typing
import sys

# Complexity is O(nlog(n)) due to the sort.
def find_h_number(arr: typing.List[int]) -> int:
    arr.sort()
    if not arr:
        return 0
    if arr[0] > len(arr):
        return len(arr)
    for i, a in enumerate(reversed(arr)):
        if a <= i + 1:
            return a
    return 0


if __name__ == "__main__":
    print(find_h_number([int(a) for a in sys.argv[1:]]))
