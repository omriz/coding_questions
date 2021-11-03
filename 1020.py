#!/usr/bin/env python3

'''
This problem was asked by Google.

Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.
'''
class Node():
    def __init__(self, value: int, parent: "Node" = None, left: "Node" = None, right: "Node" = None) -> "Node":
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value

def find_in_tree(tree,found, v):
    if tree == None:
        return None
    if tree.value == v and tree != found:
        return v
    if v > tree.value:
        return find_in_tree(tree.right,found, v)
    return find_in_tree(tree.left,found, v)

def search_coupl_in_tree(target, tree, sub_tree):
    if tree == None:
        return None
    if sub_tree == None:
        return None
    p = sub_tree
    if p.value > target:
        return search_coupl_in_tree(target, tree, p.left)
    resp = find_in_tree(tree,p, target - p.value)
    if resp != None:
        return (p.value, resp)
    op_a = search_coupl_in_tree(target, tree, p.right)
    op_b = search_coupl_in_tree(target, tree, p.left)
    if op_a != None:
        return op_a
    return op_b


def main():
    target = 20
    root = Node(10)
    root.left = Node(5,root)
    root.left.right = Node(9,root.left)
    root.right = Node(15,root)
    root.right.left = Node(11,root.right)
    root.right.right = Node(15,root.right)
    resp = search_coupl_in_tree(target,root,root)
    if resp:
        print(resp)
    else:
        print("No option found")

if __name__ == '__main__':
    main()