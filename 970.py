#!/usr/bin/env python3
"""
You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.
"""

class OutOfRangeException(Exception):
    pass

class SparseArray(object):
    def __init__(self,size):
        self._size = size
        self._values = {}
    
    def set(self, i, val):
        self._values[i] = val
    
    def get(self,i):
        if i > self._size:
            raise OutOfRangeException("%d is larger than Array capacity %d", i, self._size)
        if i < 0:
            raise OutOfRangeException("%d is smaller than 0", i)
        return self._values.get(i, 0)

if __name__ == "__main__":
    a = SparseArray(5)
    assert 0 == a.get(2)
    a.set(2,7)
    assert 7 == a.get(2)
    assert 0 == a.get(4)
        