#!/usr/bin/env python3
"""
The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term. The first few terms are as follows:

1
11
21
1211
111221
As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.
"""

import sys
import typing

def calculate_term(n: int) -> typing.List[int]:
    "Brute force - we're going to calculate everything"
    if n <= 0:
        return 0
    if n == 1:
        return 1
    curr = [1]
    for i in range(1, n):
        seq = []
        count = 0
        num = 0
        for v in curr:
            if v == num:
                count += 1
            elif num != 0:
                seq.append(count)
                seq.append(num)
                count = 1
                num =v
            else:
                num = v
                count = 1
        seq.append(count)
        seq.append(num)
        curr = seq
    return curr

if __name__ == "__main__":
    print(calculate_term(int(sys.argv[1])))
