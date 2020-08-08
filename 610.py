#!/usr/bin/env python3
"""
Implement division of two positive integers without using the division,
multiplication, or modulus operators. Return the quotient as an integer,
ignoring the remainder.
"""

import sys


def divide(a:int, b:int) -> int:
    if a < b:
        return 0
    c = 0
    while a >= b:
        a -= b
        c += 1
    return c

if __name__ == "__main__":
    print(divide(int(sys.argv[1]), int(sys.argv[2])))