#!/usr/bin/env python3
"""
Given a string and a number of lines k, print the string in zigzag form.
In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line,
then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

t     a     g
 h   s z   a
  i i   i z
   s     g
"""

import sys

def zizag_string(s: str, k: int) -> str:
    z = []
    for i in range(k):
        z.append("")
    c = 0
    inc = 1
    for a in s:
        for i in range(k):
            if i == c:
                z[i] += a
            else:
                z[i] += " "
        c += inc
        if c == k-1 or c == 0:
            inc *= -1
    return "\n".join(z)



if __name__ == "__main__":
    print(zizag_string(sys.argv[1], int(sys.argv[2])))
