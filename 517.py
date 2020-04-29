#!/usr/bin/env python3
"""
Given two singly linked lists that intersect at some point,
find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and
constant space.
"""

import typing

def find_intersection(a: typing.List[int], b: typing.List[int]) -> int:
    if not a or not b:
        return None
    ai = len(a) - 1
    bi = len(b) - 1
    while a[ai] == b[bi] and ai >= 0 and bi >= 0:
        ai -= 1
        bi -= 1
    # Reached the end
    if ai < 0:
        return a[0]
    if bi < 0:
        return b[0]
    # Never started
    if ai == len(a) - 1:
        return None
    return a[ai+1]

if __name__ == "__main__":
    a =[3,7,8,10]
    b =[99,1,8,10]
    print(find_intersection(a,b))