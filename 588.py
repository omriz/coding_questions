#!/usr/bin/env python3
"""
You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.
"""


class SparseArray(object):
    def __init__(self, size: int):
        self._max_size = size
        self._values = {}

    def Set(self, i: int, val: int):
        if i > self._max_size:
            raise OverflowError("Index %d is out of bounds" % i)
        else:
            if val == 0:
                if i in self._values:
                    self._values.pop(i)
            else:
                self._values[i] = val

    def Get(self, i: int):
        self._values.get(i, 0)

