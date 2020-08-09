#!/usr/bin/env python3
r"""
This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
"""

import typing


class Node(object):
    def __init__(
        self,
        value: str,
        left: typing.Optional["Node"] = None,
        right: typing.Optional["Node"] = None,
    ):
        self.value = value
        self.left = left
        self.right = right


def invert_tree(tree:Node) -> Node:
    if not tree:
        return None
    new_right = invert_tree(tree.left)
    new_left = invert_tree(tree.right)
    tree.left = new_left
    tree.right = new_right
    return tree
