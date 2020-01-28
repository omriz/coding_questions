#!/usr/env/bin python3
"""
Given a binary search tree, find the floor and ceiling of a given integer. The floor is the highest element in the tree less than or equal to an integer, while the ceiling is the lowest element in the tree greater than or equal to an integer.

If either value does not exist, return None.
"""

import sys


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_floor_and_ciel(num, tree):
    if not tree:
        return None, None
    p = tree
    floor = None
    ciel = None
    while p:
        if p.value < num:
            floor = p.value
            if p.right and p.right.value >= num:
                if p.right.value == num:
                    return num, num
                ciel = p.right.value
            p = p.right
        elif p.value > num:
            ciel = p.value
            if p.left and p.left.value <= num:
                if p.left.value == num:
                    return num, num
                floor = p.left.value
            p = p.left
        else:
            return num, num
    return floor, ciel


if __name__ == "__main__":
    tree = Node(3, Node(1), Node(7, Node(4), Node(8)))
    print(find_floor_and_ciel(int(sys.argv[1]), tree))
