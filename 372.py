#!/usr/bin/env python3
"""
Write a function that takes a natural number as input and returns the number of digits the input has.

Constraint: don't use any loops.
"""

import sys


def num_digits(n: int) -> int:
    return len(str(n))


if __name__ == "__main__":
    print(num_digits(int(sys.argv[1])))
