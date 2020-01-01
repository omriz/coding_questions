#!/usr/bin/env python3
"""
Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
"""
import sys
import typing


def bought(buy_price: int, nums: typing.List[int], k:int) -> int:
    values = []
    for i, a in enumerate(nums):
        values.append(a - buy_price + max_profit(nums[i + 1 :], k))
    return max(values)


def max_profit(nums: typing.List[int], k:int) -> int:
    if k==0:
        return 0
    if len(nums) == 2:
        return nums[1] - nums[0]
    if len(nums) < 2:
        return 0
    return max(max_profit(nums[1:],k), bought(nums[0], nums[1:], k-1))


if __name__ == "__main__":
    nums = [int(a) for a in sys.argv[2:]]
    print(max_profit(nums,int(sys.argv[1])))
