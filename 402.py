#!/usr/bin/env python3
import sys

# 0
# 1
# 6 - 9
# 8
# 9 -6


def findStrobogrammatic(n):
    odd_reversables = ["0", "1", "8"]
    if n == 0:
        return []
    if n == 1:
        return odd_reversables
    odd = n % 2 == 1
    half_size = int(n / 2)
    half_num = ["1"] + ["0"] * (half_size - 1)
    final_half_num = ["0"] + ["0"] * (half_size - 1)
    nums = []
    while "".join(half_num) != "".join(final_half_num):
        reverse_half_num = half_num[::-1]
        for i in range(len(reverse_half_num)):
            if reverse_half_num[i] == "6":
                reverse_half_num[i] = "9"
            elif reverse_half_num[i] == "9":
                reverse_half_num[i] = "6"
        if odd:
            for a in odd_reversables:
                nums.append(int("".join(half_num + [a] + reverse_half_num)))
        else:
            nums.append(int("".join(half_num + reverse_half_num)))
        for i in reversed(range(len(half_num))):
            if half_num[i] == "0":
                half_num[i] = "1"
                break
            elif half_num[i] == "1":
                half_num[i] = "6"
                break
            elif half_num[i] == "6":
                half_num[i] = "8"
                break
            elif half_num[i] == "8":
                half_num[i] = "9"
                break
            elif half_num[i] == "9":
                half_num[i] = "0"
    return nums


if __name__ == "__main__":
    print(findStrobogrammatic(int(sys.argv[1])))
