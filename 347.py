#!/usr/bin/env python3
"""
You are given a string of length N and a parameter k. The string can be manipulated by taking one of the first k letters and moving it to the end.

Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.

For example, suppose we are given the string daily and k = 1. The best we can create in this case is ailyd.
"""

import sys


def smallest_word(word: str, k: int) -> str:
    if k >= len(word):
        return "".join(list(word).sort())
    check = True
    while check:
        check = False
        for i in range(k):
            if word[i] > word[i+1]:
                word = word[:i] + word[i+1:] + word[i]
                check = True
                break
    return word


if __name__ == "__main__":
    print(smallest_word(sys.argv[1], int(sys.argv[2])))
