#!/usr/bin/env python3
"""
The sequence [0, 1, ..., N] has been jumbled,
and the only clue you have for its order is an array representing
whether each number is larger or smaller than the last.
Given this information, reconstruct an array that is consistent with it.
For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4]
"""

import typing

def array_reconstruction(arr: typing.List[typing.Optional[str]]) -> typing.List[int]:
    # the trick is this: We find how many ups we have and how many downs we have.
    # We take the ups as the upper range of the array and the downs as the lower
    # every time we take an up we pop the smallest upper range. Every time we take
    # a down we take the largest from the lower range.
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [0]
    num_negatives = arr.count("-")
    negatives = [x for x in range(num_negatives)]
    positives = [x for x in range(num_negatives,len(arr))]
    to_ret = []
    for i in arr:
        if i == "+" or i is None:
            to_ret.append(positives.pop(0))
        else:
            to_ret.append(negatives.pop())
    return to_ret


if __name__ == "__main__":
    arr = [None, "-", "+", "-", "+"]
    print(array_reconstruction(arr))
