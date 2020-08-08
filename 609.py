#!/usr/bin/env python3
r"""
Given a node in a binary search tree, return the next bigger element,
also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer.
"""

import typing

class Node(object):
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


def get_inorder_successor(node: Node) -> typing.Optional[Node]:
    # In order to get the next bigger element there are several options:
    # 1) If it has a right son, we need to get the leftmost node in the right subtree
    # 2) If there is no right son and it is a left son - then it is it's parent
    # 3) If there is no right son and it is a right son - then we need to go up till the point
    #    where we are the left son
    # 3) If it has no right son, and no parent (i.e. it is the root) it is the biggest
    if node.right:
        p = node.right
        while p.left:
            p = p.left
        return p
    if not node.parent:
        return None
    if node.parent.value > node.value: # i.e we are the left son.
        return node.parent
    # We are a right son and have no right son.
    p = node.parent
    # As long as we are a right son
    while p.parent and p.value > p.parent.value:
        p = p.parent
    if not p.parent: # we got to the top
        return None
    p = p.parent # The parent is bigger - we are in the left tree
    if p.right:
        p = p.right
        while p.left:
            p = p.left
    return p

if __name__ == "__main__":
    t = Node(10)
    t.left = Node(5,t)
    t.right = Node(30,t)
    t.right.left = Node(22,t.right)
    t.right.right = Node(35,t.right)
    print(get_inorder_successor(t.left).value)