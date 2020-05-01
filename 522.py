#!/usr/bin/env python3
"""
Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string.
For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
"""

import typing
import sys


def find_pattern(s: str, ptr: str) -> typing.List[int]:
    # This assumes the pattern can repeat within itself i.e.
    # pattern abab in string ababab should return 0,2
    occr = []
    for i in range(len(s)):
        if s[i : i + len(ptr)] == ptr:
            occr.append(i)
    return occr


if __name__ == "__main__":
    print(find_pattern(sys.argv[1], sys.argv[2]))
