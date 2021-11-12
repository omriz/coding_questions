#!/usr/bin/env python3
'''
The United States uses the imperial system of weights and measures,
which means that there are many different,
seemingly arbitrary units to measure distance.
There are 12 inches in a foot, 3 feet in a yard, 22 yards in a chain, and so on.

Create a data structure that can efficiently convert
a certain quantity of one unit to the correct amount of any other unit.
You should also allow for additional units to be added to the system.
'''

import logging

class Convertor(object):
    def __init__(self):
        self._inches = {
            "inch": 1.0,
            "foot": 12,
            "yard": 3*12,
            "chain": 22*36,
        }
    def convert(self,value, source_unit, target_unit):
        if source_unit not in self._inches:
            logging.error("%s - unknown unit" % source_unit)
            return None
        if target_unit not in self._inches:
            logging.error("%s - unknown unit" % target_unit)
            return None
        return value*self._inches[source_unit]/(1.0*self._inches[target_unit])
    def add_type(self,new_unit, value, current_unit):
        if current_unit not in self._inches:
            logging.error("%s - unknown unit" % current_unit)
            return None
        self._inches[new_unit] = value * self._inches[current_unit]

if __name__ == "__main__":
    c = Convertor()
    assert 66 == c.convert(1,"chain","foot")
    c.add_type("moshe", 0.5, "foot")
    assert 1 == c.convert(6, "inch", "moshe")