#!/usr/bin/env python3
"""
You have n fair coins and you flip them all at the same time. Any that come up tails you set aside. The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.
"""

import math
import sys

def main(n):
    print (math.ceil(math.log2(n)))

if __name__ == "__main__":
    main(int(sys.argv[1]))