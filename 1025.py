#!/usr/bin/env python3
'''
Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.
'''
import sys 
import typing


def get_minimal_list(nums: typing.List[int]) -> typing.List[int]:
    if len(nums) == 0:
        return []
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum == 0:
            return get_minimal_list(nums[i+1:])
    return [nums[0]] + get_minimal_list(nums[1:])

def main():
    nums = [int(x) for x in sys.argv[1:]]
    print(get_minimal_list(nums))

if __name__ == "__main__":
    main()