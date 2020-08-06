#!/usr/bin/env python3
"""
This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.
"""

import typing


class Node(object):
    def __init__(self, v, left, right):
        self.v = v
        self.left = left
        self.right = right


def find_second_largest(root: Node) -> int:
    if not root:
        return None
    if not root.left and not root.right:
        return None
    if root.right:
        n = root
        p = root.right
        while p.right:
            n = p
            p = p.right
        return n.v
    if not root.left.right:
        return root.left.v
    n = root.left
    p = root.left.right
    while p.right:
        n = p
        p = p.right
    return p.v


if __name__ == "__main__":
    assert 2 == find_second_largest(Node(1, None, Node(2, None, Node(3, None, None))))
    assert 2 == find_second_largest(Node(2, Node(1, None, None), Node(3, None, None)))
    assert 2 == find_second_largest(
        Node(2, Node(1, None, Node(1.5, None, None)), Node(3, None, None))
    )
    assert 2 == find_second_largest(Node(3, Node(1, None, Node(2, None, None)), None))
