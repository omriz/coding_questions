#!/usr/bin/env python3
"""
You are given an string representing the initial conditions of some dominoes.
Each element can take one of three values:

L, meaning the domino has just been pushed to the left,
R, meaning the domino has just been pushed to the right, or
., meaning the domino is standing still.
Determine the orientation of each tile when the dominoes stop falling.
Note that if a domino receives a force from the left and right side simultaneously,
it will remain upright.

For example, given the string .L.R....L, you should return LL.RRRLLL.

Given the string ..R...L.L, you should return ..RR.LLLL.
"""

import sys
import typing


def next_state(state: str) -> str:
    n = ""
    for i in range(len(state)):
        d = state[i]
        L = False
        R = False
        if d == ".":
            if i > 0 and state[i - 1] == "R":
                R = True
            if i < len(state) and state[i + 1] == "L":
                L = True
            if R and L:
                n += "."
            elif R:
                n += "R"
            elif L:
                n += "L"
            else:
                n += "."
        else:
            n += d
    return n


def get_final_state(state: str) -> str:
    old_state = state
    state = next_state(state)
    while old_state != state:
        old_state = state
        state = next_state(state)
    return state


if __name__ == "__main__":
    print(get_final_state(sys.argv[1]))
