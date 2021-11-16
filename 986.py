#!/usr/bin/env python3
'''
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
'''

import sys

def longest_ones(num:int)->int:
    n = num
    current = 0
    last = 0
    while n:
        x = n % 2
        if x:
            current += 1
        else:
            if current > last:
                last = current
                current = 0
        n = n // 2 # Integer division python3
    if current > last:
        return current
    return last

if __name__ == "__main__":
    print(longest_ones(int(sys.argv[1])))