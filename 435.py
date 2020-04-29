#!/usr/bin/env python3
"""
Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
"""

import typing


class Node(object):
    def __init__(
        self,
        value: str,
        back: typing.Optional["Node"] = None,
        left: typing.Optional["Node"] = None,
        right: typing.Optional["Node"] = None,
    ):
        self.value = value
        self.back = back
        self.left = left
        self.right = right

    def __str__(self):
        rep = "(" + self.value
        if self.right:
            rep += "," + str(self.left) + "," + str(self.right)
        elif self.left:
            rep += "," + str(self.left)
        rep += ")"
        return rep


def reorder_tree(preorder: typing.List[str], inorder: typing.List[str]) -> Node:
    "ALMOST GOT IT WORKING"
    p = 1
    i = 0
    root = Node(preorder[0])
    curr = root
    while p < len(preorder) and i < len(inorder):
        print(root)
        did_left = False
        while p < len(preorder) and i < len(inorder) and preorder[p] != inorder[i]:
            did_left = True
            curr.left = Node(preorder[p], curr)
            curr = curr.left
            p += 1
        if p >= len(preorder):
            break
        if did_left:
            curr.left = Node(preorder[p], curr)
            curr = curr.left
        i += 1
        while curr and i < len(inorder) and inorder[i] != curr.value:
            curr = curr.back
        p += 1
        if curr is None:
            curr = root
        else:
            i+=1
        if p < len(preorder):
            curr.right = Node(preorder[p],curr)
            curr = curr.right
    return root


if __name__ == "__main__":
    preorder = ["a", "b", "d", "e", "c", "f", "g"]
    inorder = ["d", "b", "e", "a", "f", "c", "g"]
    print(reorder_tree(preorder, inorder))
