#!/usr/bin/env python3

"""
This problem was asked by Jane Street.

Given integers M and N, write a program that counts how many positive integer pairs
(a, b) satisfy the following conditions:

a + b = M
a XOR b = N
"""

import sys

# There's probably some linear algebra trick here.
def count_condition(m: int, n:int) -> int:
    count = 0
    for a in range(1,m/2 + 1):
        b = m - a
        if a ^ b == n:
            count += 1
    return count


if __name__ == "__main__":
    print(count_condition(int(sys.argv[1]), int(sys.argv[2])))