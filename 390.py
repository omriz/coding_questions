#!/usr/bin/env python3
import typing


def find_missing(num_list: typing.List[int]) -> typing.List[int]:
    # O(nlog(n)) - in place, but we can sacrafice space for not in place
    num_list.sort()
    missing = []
    if num_list[0] != 1:
        i = 1
        while i < num_list[0]:
            missing.append(i)
            i += 1
    # O(n)
    for i in range(1, len(num_list)):
        if num_list[i] - num_list[i - 1] == 1:
            continue
        x = num_list[i - 1] + 1
        while x < num_list[i]:
            missing.append(x)
            x += 1
    return missing
