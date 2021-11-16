#!/usr/bin/env python3
'''
Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right,
and satisfies the constraint that the key in the left child must be less than or equal to the root
and the key in the right child must be greater than or equal to the root.
'''

class Node(object):
    def __init__(self,value:int,left:"Node" = None,right:"Node" = None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_bi_tree(root:"Node") -> bool:
    if root == None:
        return True
    if (root.left == None or root.value > root.left.value) and (root.right == None or root.value < root.right.value):
        return is_valid_bi_tree(root.left) and is_valid_bi_tree(root.right)
    return False

if __name__ == "__main__":
    t_good = Node(4,Node(2,Node(1),Node(3)),Node(6,Node(5),Node(7)))
    assert is_valid_bi_tree(t_good)
    t_bad = Node(4,Node(2,Node(1),Node(3)),Node(5,Node(6),Node(7)))
    assert not is_valid_bi_tree(t_bad)
