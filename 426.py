#!/usr/bin/env python3
"""
Given a binary tree, return the level of the tree with minimum sum.
"""

import typing


class Node(object):
    def __init__(
        self,
        value: int,
        right: typing.Optional["Node"] = None,
        left: typing.Optional["Node"] = None,
    ):
        self.value = value
        self.right = right
        self.left = left


def find_minimal_sum(root: Node) -> int:
    levels = {}
    if not root:
        return 0
    running = [(0, root)]
    while running:
        l, p = running.pop()
        if l not in levels:
            levels[l] = 0
        levels[l] += p.value
        if p.right:
            running = [(l + 1, p.right)] + running
        if p.left:
            running = [(l + 1, p.left)] + running
    max_level = 0
    max_value = root.value
    for k, v in levels.items():
        if v > max_value:
            max_level = k
            max_value = v
    return max_level


if __name__ == "__main__":
    print(find_minimal_sum(Node(5, Node(3), Node(4, None, Node(6)))))
