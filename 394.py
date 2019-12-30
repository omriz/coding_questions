#!/usr/bin/env python3
import typing


class Node(object):
    def __init__(
        self,
        value: int,
        left: typing.Optional["Node"] = None,
        right: typing.Optional["Node"] = None,
    ):
        self.value = value
        self.right = right
        self.left = left


def is_total_in_tree(tree: Node, total: int) -> bool:
    if tree is None:
        if total == 0:
            return True
        else:
            return False
    return is_total_in_tree(tree.left, total - tree.value) or is_total_in_tree(
        tree.right, total - tree.value
    )


if __name__ == "__main__":
    t = Node(8, Node(4, Node(2), Node(6)), Node(13, None, Node(19)))
    print(is_total_in_tree(t, 18))
