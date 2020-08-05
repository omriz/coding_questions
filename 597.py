#!/usr/bin/env python3
"""
Given an array of integers, determine whether it contains a Pythagorean triplet.
Recall that a Pythogorean triplet (a, b, c) is defined by the equation a^2+ b^2= c^2.
"""

import sys
import typing


def has_p_tri(arr: typing.List[int]) -> bool:
    doubles = [a * a for a in arr]
    for i in range(len(doubles) - 2):
        for j in range(i + 1, len(doubles) - 1):
            for z in range(j + 1, len(doubles)):
                if (
                    doubles[i] + doubles[j] == doubles[z]
                    or doubles[i] + doubles[z] == doubles[j]
                    or doubles[j] + doubles[z] == doubles[i]
                ):
                    return True
    return False


if __name__ == "__main__":
    print(has_p_tri([int(a) for a in sys.argv[1:]]))

