#!/usr/bin/env python3
"""
This problem was asked by Microsoft.

Given a string, generate all possible subsequences of the string.

For example, given the string xyz, return an array or set with the following strings:


x
y
z
xy
xz
yz
xyz

Note that zx is not a valid subsequence since it is not in the order of the given string.
"""

import typing
import sys


def generate_sub_sequence(s: str) -> typing.List[str]:
    if not s:
        return [""]
    to_ret = []
    res = generate_sub_sequence(s[1:])
    for a in res:
        to_ret.append(s[0] + a)
    return to_ret + res


if __name__ == "__main__":
    print(generate_sub_sequence(sys.argv[1]))
