#!/usr/bin/env python3
"""
Let's define a "sevenish" number to be one which is either a power of 7,
or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on.
Create an algorithm to find the nth sevenish number.
"""

import sys

# This is actually funky. The nth number is sort of a binary encoding:
# 1 = 7^0 (1)
# 7 = 7^1 (10)
# 8 = 7^1 + 7^0 (11)
# 49 = 7^2 (100)
# 50 = 7^2 + 7^0 (101)

def get_nth_sevenish(n: int) -> int:
    count = 0
    sum = 0
    while n > 0:
        if n % 2:
            sum += 7**count
        n = n // 2
        count +=1
    return sum

if __name__ == "__main__":
    print(get_nth_sevenish(int(sys.argv[1])))
