#!/usr/bin/env python3


def permute(arr, p):
    if len(arr) != len(p):
        return None
    to_ret = [0]*len(arr)
    for i, v in enumerate(p):
        to_ret[i] = arr[v]
    return to_ret


if __name__ == '__main__':
    print(permute(["a", "b", "c"], [2, 1, 0]))
