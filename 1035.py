#! /usr/bin/env python3
"""
MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written.
They would like to give the smallest positive amount to each worker consistent with the constraint that if a developer has written more lines of code than their neighbor,
they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.

For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].
"""

import sys
import typing

def get_bonus(seats: typing.List[int]) -> typing.List[int]:
    if len(seats) == 0:
        return []
    if len (seats) == 1:
        return [1]
    bonuses = [1]
    for i in range(1,len(seats)):
        if seats[i] == seats[i-1]:
            bonuses.append(bonuses[i-1])
        elif seats[i] > seats[i-1]:
            bonuses.append(bonuses[i-1] + 1)
        else: #seats[i] < seats[i-1]:
            bonuses.append(1)
            j = i
            while j > 0 and seats[j] < seats[j-1] and bonuses[j] == bonuses[j-1]:
                bonuses[j-1] += 1
                j -= 1
    return bonuses

def main():
    print(get_bonus([int(x) for x in sys.argv[1:]]))

if __name__ == "__main__":
    main()