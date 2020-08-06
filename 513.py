#!/usr/bin/env python3
"""
Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""

import typing
import sys


def find_cont_elements(l: typing.List[int], k: int) -> typing.List[int]:
    # This only works for positive numbers
    # When working with negatives it's either O(n^2) or maybe there's some other way...
    s = 0
    e = 0
    total = 0
    while s < len(l) and e < len(l):
        if total == k:
            return l[s : e]
        elif total < k:
            total += l[e]
            e += 1
        else:
            total -= l[s]
            s += 1
    return []


if __name__ == "__main__":
    k = int(sys.argv[1])
    l = [int(x) for x in sys.argv[2:]]
    print(find_cont_elements(l, k))
