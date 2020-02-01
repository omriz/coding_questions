#!/usr/bin/env python3
"""
This problem was asked by Square.

Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""
import copy
import typing
import sys


def find_shortest_substring(word: str, chars: typing.Set[str]) -> str:
    found = None
    if not word:
        return ""
    for i in range(len(word)):
        if word[i] not in chars:
            continue
        i_chars = copy.deepcopy(chars)
        i_chars.remove(word[i])
        n = i + 1
        while n < len(word) and i_chars:
            if word[n] in i_chars:
                i_chars.remove(word[n])
            n += 1
        if not i_chars:
            if not found or len(found) > n - i:
                found = word[i : n + 1]
    return found


if __name__ == "__main__":
    print(find_shortest_substring(sys.argv[1], set(sys.argv[2:])))
