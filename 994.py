#!/usr/bin/env python3
r'''
Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
'''

class Node(object):
    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right

# This is basically BFS
def print_tree(t):
    q = [t]
    while q:
        if q[-1].left:
            q = [q[-1].left] + q
        if q[-1].right:
            q = [q[-1].right] + q
        print(q.pop().value)

if __name__ == "__main__":
    t = Node(1,Node(2,None,None),Node(3,Node(4,None,None),Node(5,None,None)))
    print_tree(t)
