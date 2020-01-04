#!/usr/bin/env python3
"""
Given two sorted iterators, merge it into one iterator.

For example, given these two iterators:

foo = iter([5, 10, 15])
bar = iter([3, 8, 9])

You should be able to do:

for num in merge_iterators(foo, bar):
    print(num)

# 3
# 5
# 8
# 9
# 10
# 15

Bonus: Make it work without pulling in the contents of the iterators in memory.
"""
import typing
import sys


class merge_iterators(object):
    def __init__(self, foo: typing.Iterator, bar: typing.Iterator):
        self._foo = foo
        self._bar = bar
        self._load_foo = True
        self._next = None
        self._next = self._get_next()

    def __iter__(self):
        return self

    def _get_next(self):
        to_ret = None
        if self._load_foo and self._foo:
            try:
                loaded = self._foo.__next__()
            except StopIteration:
                self._foo = None
                loaded = None
        elif self._bar:
            try:
                loaded = self._bar.__next__()
            except StopIteration:
                self._bar = None
                loaded = None
        else:
            return None
        if loaded > self._next:
            to_ret = self._next
            self._next = loaded
            self._load_foo = not self._load_foo
        else:
            to_ret = loaded
        return to_ret

    def __next__(self):
        if self._next is None:
            raise StopIteration
        n = self._next
        self._next = self._get_next()
        return n


if __name__ == "__main__":
    #TODO: Incomplete!!!!!
    foo = iter([5, 10, 15])
    bar = iter([3, 8, 9])
    for num in merge_iterators(foo, bar):
        print("d: %d" %num)
