#!/usr/bin/env python3
"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

import typing


def is_intersecting(l1: typing.Tuple[int, int], l2: typing.Tuple[int, int]) -> bool:
    if l1[0] > l2[0] and l1[0] < l2[1]:
        return True
    if l1[1] > l2[0] and l1[1] < l2[1]:
        return True
    if l1[0] < l2[0] and l1[1] > l2[1]:
        return True
    if l1[0] > l2[0] and l1[1] < l2[1]:
        return True
    return False


def find_min_rooms(lectures: typing.List[typing.Tuple[int, int]]) -> int:
    parallel = {}
    for i, lecture in enumerate(lectures):
        if lecture not in parallel:
            parallel[lecture] = 0
        for j in range(i, len(lectures)):
            if is_intersecting(lecture, lectures[j]):
                parallel[lecture] += 1
                if lectures[j] not in parallel:
                    parallel[lectures[j]] = 1
                else:
                    parallel[lectures[j]] += 1
    return max(parallel.values())


if __name__ == "__main__":
    test_arr = [(30, 75), (0, 50), (60, 150)]
    print(find_min_rooms(test_arr))
