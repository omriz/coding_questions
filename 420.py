#!/usr/bin/env python3
"""
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.  
"""

import sys


def nth_perfect_number(n: int) -> int:
    if n < = 0:
        return -1
    rh_side = 10 - (n/10) -1



if __name__ == "__main__":
    print(nth_perfect_number(int(sys.argv[1])))
