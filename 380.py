#!/usr/bin/env python3
"""
Implement integer division without using the division operator. Your function should return a tuple of (dividend, remainder) and it should take two numbers, the product and divisor.

For example, calling divide(10, 3) should return (3, 1) since the divisor is 3 and the remainder is 1.

Bonus: Can you do it in O(log n) time?
"""
import typing
import sys


def divide_on(product: int, divisor: int) -> typing.Tuple[int, int]:
    c = 0
    while product >= divisor:
        product -= divisor
        c += 1
    return (c, product)


def divide_ologn(product: int, divisor: int) -> typing.Tuple[int, int]:
    accumolator = 0
    res = 0
    while product > 0:
        print("%d %d %d" % (product, accumolator, res))
        if accumolator - divisor < 0:
            product = product >> 1
            accumolator = accumolator << 1
            accumolator += 1
            res = res << 1
        else:
            res += 1
            accumolator -= divisor
    if accumolator >= divisor:
        res += 1
        accumolator -= divisor
    return (res, accumolator)


if __name__ == "__main__":
    print(divide_on(int(sys.argv[1]), int(sys.argv[2])))
    print(divide_ologn(int(sys.argv[1]), int(sys.argv[2])))
