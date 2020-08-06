#!/usr/bin/env python3
"""
The edit distance between two strings refers to the minimum number of character insertions,
deletions, and substitutions required to change one string to the other.
For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

import sys

def edit_distance(a:str, b:str) -> int:
    if a == b:
        return 0
    if len(a) > len(b):
        ss = b
        ls = a
    else:
        ss = a
        ls = b
    dist = len(ls) - len(ss)
    min_change = len(ss)
    for i in range(dist+1):
        curr_change = 0
        for j in range(len(ss)):
            if ss[j] != ls[i+j]:
                curr_change += 1
        if curr_change < min_change:
            min_change = curr_change
    return dist + min_change


if __name__ == "__main__":
    print(edit_distance(sys.argv[1], sys.argv[2]))
