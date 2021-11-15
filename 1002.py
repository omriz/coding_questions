#!/usr/bin/env python3
'''
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.

'''

import sys
def main(arr):
    res = 1
    for i in range(len(arr)):
        if arr[i] <= res:
            res += arr[i]
        else:
            break
    return res

if __name__== "__main__":
    print(main([int(x) for x in sys.argv[1:]]))