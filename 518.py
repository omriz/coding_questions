#!/usr/bin/env python3

import sys
import typing

"""
Given an array of numbers and a number k, determine if
there are three entries in the array which add up to the specified number k.
For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.


A better solution can be done by sorting the array and then running from both sides
towards the middle.
"""


def does_it_fit(k: int, numbers: typing.List[int], it: int) -> bool:
    if it == 0:
        return k == 0
    for i, n in enumerate(numbers):
        if does_it_fit(k - n, numbers[:i] + numbers[i + 1 :], it - 1):
            return True
    return False


def does_it_fit_optimized(k: int, numbers: typing.List[int]) -> bool:
    for i,c in enumerate(numbers):
        for j,a in enumerate(numbers):
            if j == i:
                continue
            for z, b in enumerate(numbers):
                if z == j or z == i:
                    continue
                if b + a + c == k:
                    return True
    return False


if __name__ == "__main__":
    print(does_it_fit(int(sys.argv[1]), [int(x) for x in sys.argv[2:]], 3))
    print(does_it_fit_optimized(int(sys.argv[1]), [int(x) for x in sys.argv[2:]]))
