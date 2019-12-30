#!/usr/bin/env python3

import typing


class Node(object):
    def __init__(self, value: int, next_node: typing.Optional["Node"] = None):
        self.value = value
        self.next_node = next_node


def remove_kth_node(linked_list: Node, k: int) -> Node:
    # Cheking the list is ok
    if linked_list is None:
        return None
    # Checking k is positive
    if k < 0:
        return linked_list
    ender = linked_list
    # Checking k is not longer then the list
    for i in range(k):
        if ender.next_node is None:
            return None
        ender = ender.next_node
    # If we are removing the first element, simply remove it
    if ender.next_node == None:
        p = linked_list.next_node
        del linked_list
        return p
    # Iterating till we get to the end of the list and removing the kth element
    to_remove = linked_list
    while ender.next_node is not None:
        ender = ender.next_node
        prev = to_remove
        to_remove = to_remove.next_node
    prev.next_node = to_remove.next_node
    del to_remove
    return linked_list


if __name__ == "__main__":
    n = Node(1, Node(2, Node(3, Node(4))))
    n = remove_kth_node(n, 3)
    while n is not None:
        print(n.value)
        n = n.next_node
