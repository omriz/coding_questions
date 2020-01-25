#!/usr/bin/env python3
"""
Write a program to merge two binary trees. Each node in the new tree should hold a value equal to the sum of the values of the corresponding nodes of the input trees.

If only one input tree has a node in a given position, the corresponding node in the new tree should match that input node.
"""


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left == None and self.right == None:
            return "({})".format(self.value)
        else:
            return "({},{},{})".format(self.value, self.left, self.right)


# In an array implementation we could in theory just summed the array.
def sum_trees(t1, t2):
    if t1 == None and t2 == None:
        return None
    if t1 == None:
        return Node(t2.value, sum_trees(t2.left, None), sum_trees(t2.right, None))
    if t2 == None:
        return Node(t1.value, sum_trees(t1.left, None), sum_trees(t1.right, None))
    return Node(
        t1.value + t2.value, sum_trees(t1.left, t2.left), sum_trees(t1.right, t2.right)
    )


if __name__ == "__main__":
    a = Node(5, Node(6), Node(7, Node(8)))
    b = Node(5, Node(6), Node(7, Node(1), Node(0)))
    print(sum_trees(a, b))
