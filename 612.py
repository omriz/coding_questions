#!/usr/bin/env python3
"""
Given a collection of intervals, find the minimum number of intervals
you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8),
return 1 as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.
"""

import typing


def intersects(a: typing.Tuple[int], b: typing.Tuple[int]) -> bool:
    if a[0] > b[0] and a[0] < b[1]:
        return True
    if a[1] > b[0] and a[1] < b[1]:
        return True
    if a[0] > b[0] and a[1] < b[1]:
        return True
    if a[0] < b[0] and a[1] > b[1]:
        return True
    return False


def build_dict(
    intervals: typing.List[typing.Tuple[int]]
) -> typing.Dict[typing.Tuple[int], typing.Set[typing.Tuple[int]]]:
    intervals_dict = {}
    for i in intervals:
        intervals_dict[i] = set()
    for i in intervals_dict:
        for j in intervals:
            if i == j:
                continue
            if intersects(i, j):
                intervals_dict[i].add(j)
    return intervals_dict


def get_total_length(
    intervals_dict: typing.Dict[typing.Tuple[int], typing.Set[typing.Tuple[int]]]
):
    l = 0
    for i in intervals_dict:
        l += len(intervals_dict[i])
    return l


def remove_max_tile(
    intervals_dict: typing.Dict[typing.Tuple[int], typing.Set[typing.Tuple[int]]]
):
    m = 0
    k = None
    for i in intervals_dict:
        if len(intervals_dict[i]) > m:
            k = i
    if k is None:
        return
    print("Removing {}".format(k))
    max_set = intervals_dict.pop(k)
    for i in max_set:
        intervals_dict[i].discard(k)


def how_many_to_remove(intervals: typing.List[typing.Tuple[int]]) -> int:
    intervals_dict = build_dict(intervals)
    total_length = get_total_length(intervals_dict)
    num_removed = 0
    while total_length > 0:
        remove_max_tile(intervals_dict)
        num_removed += 1
        total_length = get_total_length(intervals_dict)
    return num_removed


if __name__ == "__main__":
    intervals = [(7, 9), (2, 4), (5, 8)]
    assert how_many_to_remove(intervals) == 1