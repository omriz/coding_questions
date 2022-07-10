#!/usr/env/bin python3
r"""
Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""


class Node(object):
    def __init__(self, v, left=None, right=None):
        self.value = v
        self.left = left
        self.right = right


def minimal_sum(t):
    if t == None:
        return 0
    else:
        return t.value + min(minimal_sum(t.left), minimal_sum(t.right))


if __name__ == "__main__":
    t = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1, Node(-1), None)))
    print(minimal_sum(t))