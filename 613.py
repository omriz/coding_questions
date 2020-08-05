#!/usr/bin/env python3
"""
Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map.
If the key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
For example, you should be able to run the following code:

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
"""

import typing

class PrefixMapSumBrute(object):
    def __init__(self):
        self.values = {}
    
    def insert(self, key, value):
        self.values[key] = value
    
    def sum(self, prefix):
        s = 0
        for k in self.values:
            if k.startswith(prefix):
                s += self.values[k]
        return s

class PrefixMapSumCascade(object):
    def __init__(self):
        self.values = {}
    
    def insert(self, key:str, value:int):
        if key in self.values:
            old_value = self.values[key][1]
        else:
            old_value = 0
        for i in range(1,len(key)):
            if key[:i] in self.values:
                self.values[key[:i]][0] += (value - old_value)
            else:
                self.values[key[:i]] = [self.values.get(key[:i-1],[value - old_value,0])[0], 0]
        self.values[key] = [self.values.get(key[:i-1],[value - old_value,0])[0], value]

    def sum(self, prefix:str) -> typing.Optional[int]:
        return self.values.get(prefix, None)[0]


if __name__ == "__main__":
    mapsum = PrefixMapSumBrute()
    mapsum.insert("columnar", 3)
    assert mapsum.sum("col") == 3

    mapsum.insert("column", 2)
    assert mapsum.sum("col") == 5

    mapsum = PrefixMapSumCascade()
    mapsum.insert("columnar", 3)
    assert mapsum.sum("col") == 3

    mapsum.insert("column", 2)
    assert mapsum.sum("col") == 5