#!/usr/bin/env python3

import sys


def sort_by_frequency(s: str) -> str:
    frequency = {}
    for i in s:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    rev_frequency = {}
    for v, i in frequency.items():
        if i in rev_frequency:
            rev_frequency[i].append(v)
        else:
            rev_frequency[i] = [v]
    to_ret = ""
    for i in reversed(sorted(rev_frequency.keys())):
        for z in rev_frequency[i]:
            to_ret += z * i
    return to_ret


if __name__ == "__main__":
    print(sort_by_frequency(sys.argv[1]))
