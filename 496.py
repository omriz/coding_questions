#!/usr/bin/env python3
"""
Write an algorithm that finds the total number of set bits in all integers between 1 and N.
"""

import sys

# This is pretty brute force - but works
# There may be a better way to do this

def calculate_total_set_bits(n: int) -> int:
    count = 0
    for i in range(n+1):
        a = i
        while a:
            if a % 2:
                count += 1
            a = a // 2
    return count

if __name__ == "__main__":
    print(calculate_total_set_bits(int(sys.argv[1])))
