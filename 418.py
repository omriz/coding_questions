#!/usr/bin/env python3
"""
MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written. They would like to give the smallest positive amount to each worker consistent with the constraint that if a developer has written more lines of code than their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.

For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].
"""

import sys
import typing

def give_bonus(employees: typing.List[int]) -> typing.List[int]:
    if not employees:
        return None
    bonuses = [0]
    if len(employees) == 1:
        return [1]
    if employees[0] > employees[1]:
        bonuses = [1,0]
    elif employees[0] == employees[1]:
    for i in range(1,len(employees)):
        if 


if __name__ == "__main__":
    employees = [int(a) for a in sys.argv[1:]]
    print(give_bonus(employees))
