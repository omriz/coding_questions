#!/usr/bin/env python3
"""
Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0,
using only mathematical or bit operations. You can assume b can only be 1 or 0.
"""

import sys

if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    b = int(sys.argv[3])
    print(b*x -1 * (b-1)*y)
