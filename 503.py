#!/usr/bin/env python3
"""
Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.

Solution:
    We're going to do merge sort on the linked list.
    We'll split it into two lists and then merge them.
    We don't create new nodes, just a couple of vars in every iteration.
    Merge sort is O(nlogn) in runtime so that works :-)
"""
import typing
import sys


class Node(object):
    def __init__(self, v: int, n: typing.Optional["Node"] = None):
        self.value = v
        self.next_node = n


def build_linked_list(arr: typing.List[str]) -> Node:
    if not arr:
        return None
    n = Node(int(arr[0]))
    if len(arr) == 1:
        return n
    c = n
    for a in arr[1:]:
        c.next_node = Node(int(a))
        c = c.next_node
    return n


def print_linked_list(ll: Node):
    if not ll:
        return
    a = ll
    s = "%d" % a.value
    a = a.next_node
    while a:
        s += "->%d" % a.value
        a = a.next_node
    print(s)


def split_linked_list(ll: Node) -> (Node, Node):
    a = ll
    b = ll
    c = ll
    prev = b
    while c and c.next_node:
        prev = b
        b = b.next_node
        c = c.next_node.next_node
    prev.next_node = None
    return (a, b)


def sort_linked_list(ll: Node) -> Node:
    if not ll.next_node:
        return ll
    ls, lr = split_linked_list(ll)
    ss = sort_linked_list(ls)
    sr = sort_linked_list(lr)
    merged = None
    c = None
    while ss and sr:
        if ss.value < sr.value:
            if merged:
                c.next_node = ss
                c = c.next_node
            else:
                merged = ss
                c = merged
            ss = ss.next_node
        else:
            if merged:
                c.next_node = sr
                c = c.next_node
            else:
                merged = sr
                c = merged
            sr = sr.next_node
    while ss:
        c.next_node = ss
        c = c.next_node
        ss = ss.next_node
    while sr:
        c.next_node = sr
        c = c.next_node
        sr = sr.next_node
    return merged


if __name__ == "__main__":
    ll = build_linked_list(sys.argv[1:])
    print_linked_list(ll)
    ll = sort_linked_list(ll)
    print_linked_list(ll)
