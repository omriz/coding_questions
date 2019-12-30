#!/usr/bin/env python3

import random


def rand5():
    return random.randint(1, 5)


def rand7():
    return ((rand5() + rand5()) % 7) + 1

def uniform_rand7():
    x = rand5() + rand5()
    if x == 2 or x == 10:
        return uniform_rand7()
    return x


if __name__ == "__main__":
    print(rand7())
