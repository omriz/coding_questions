#!/usr/bin/env python3
"""
Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less than k
come before nodes greater than or equal to k.
For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3,
the solution could be 1 -> 0 -> 5 -> 8 -> 3.
"""

import typing
import sys

class Node(object):
    def __init__(self, value:int, next_node:typing.Optional["Node"] = None):
        self.value = value
        self.next_node = next_node

def partition_list(l: Node, k:int) -> Node:
    before = None
    l_before = None
    after = None
    curr = l
    while curr:
        next_node = curr.next_node
        if curr.value < k:
            if not before:
                before = curr
                l_before = curr
                before.next_node = None
            else:
                curr.next_node = before
                before = curr
        else:
            if not after:
                after = curr
                after.next_node = None
            else:
                curr.next_node = after
                after = curr
        curr = next_node
    if not before:
        return after
    l_before.next_node = after
    return before


def make_list(l):
    a = Node(int(l[0]))
    it = a
    for i in l[1:]:
        it.next_node = Node(int(i))
        it = it.next_node
    return a


def print_list(l):
    a = l
    while a:
        print(a.value)
        a = a.next_node


if __name__ == "__main__":
    l = make_list(sys.argv[2:])
    print_list(partition_list(l,int(sys.argv[1])))
