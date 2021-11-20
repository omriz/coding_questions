#!/usr/bin/env python3
"""
This problem was asked by Twitter.

A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.
"""

import sys
import typing


def find_strobogrammatic(digits: int) -> typing.Optional[typing.List[int]]:
    if digits == 0:
        return None
    if digits == 1:
        return [0, 1, 8]
    if digits == 2:
        return [11, 69, 88, 96]
    nums = []
    if digits > 2:
        for a in find_strobogrammatic(digits - 2):
            nums += [
                int("1" + str(a) + "1"),
                int("6" + str(a) + "9"),
                int("8" + str(a) + "8"),
                int("9" + str(a) + "6"),
            ]
    return nums


if __name__ == "__main__":
    print(find_strobogrammatic(int(sys.argv[1])))
