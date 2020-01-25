#!/usr/bin/env python3

"""
Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.
"""

import typing
import sys


def remove_zero_sums(origin: typing.List[int]) -> typing.List[int]:
    if not origin:
        return []
    to_ret = origin[:]
    start_index = 0
    while start_index < len(to_ret):
        stop_index = 0
        current_sum = to_ret[start_index]
        for i in range(start_index + 1, len(to_ret)):
            current_sum += to_ret[i]
            if current_sum == 0:
                stop_index = i
                break
        if current_sum == 0:
            to_ret = to_ret[0:start_index] + to_ret[stop_index + 1 :]
        else:
            start_index += 1
    return to_ret


if __name__ == "__main__":
    print(remove_zero_sums([int(a) for a in sys.argv[1:]]))
