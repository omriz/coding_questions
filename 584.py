#!/usr/bin/env python3
"""
Given a string with repeated characters,
rearrange the string so that no two adjacent characters are the same.
If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
"""

import sys


def reorder_no_adjacent(origin: str) -> str:
    reordered = list(origin)
    if len(reordered) <= 1:
        return reordered
    if len(reordered) == 2:
        if reordered[0] == reordered[1]:
            return None
        else: 
            return reordered
    for i in range(1,len(reordered)-1):
        if reordered[i] != reordered[i-1] and reordered[i] != reordered[i+1]:
            continue
        for j in range(i+2, len(reordered)):
            if reordered[j] != reordered[i-1] and reordered[j] != reordered[i+1]:
                a = reordered[j]
                reordered[j] = reordered[i]
                reordered[i] = a
                break
        else:
            return None
    return "".join(reordered)

if __name__ == "__main__":
    print(reorder_no_adjacent(sys.argv[1]))