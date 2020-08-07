#!/usr/bin/env python3
r"""
This problem was asked by Google.

Given the root of a binary tree, return a deepest node.
For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
"""

import typing

class Node(object):
    def __init__(self, value: str, left: typing.Optional["Node"] = None, right: typing.Optional["Node"]= None):
        self.value = value
        self.left = left
        self.right = right


def find_deepest_node(tree:Node) -> typing.Optional[str]:
    if not tree:
        return None
    q = []
    q.insert(0, tree)
    last = tree
    while len(q) > 0:
        last = q.pop(-1)
        if last.left:
            q.insert(0,last.left)
        if last.right:
            q.insert(0, last.right)
    return last.value

if __name__ == "__main__":
    t = Node('a',Node('b',Node('d'),None),Node('c'))
    assert find_deepest_node(t) == 'd'