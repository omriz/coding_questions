#!/usr/bin/env python3
"""
There are N prisoners standing in a circle, waiting to be executed.
The executions are carried out starting with the kth person,
and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.
"""

import sys


def find_last_survivor(n: int, k: int) -> int:
    ak = k - 1
    a = [x+1 for x in range(n)]
    while len(a) > k:
        a = a[ak+1:] + a[0:ak]
    while len(a) > 1:
        i = ak % len(a)
        a = a[i+1:] + a[0:i]
    return a[0]


if __name__ == "__main__":
    print(find_last_survivor(int(sys.argv[1]), int(sys.argv[2])))
