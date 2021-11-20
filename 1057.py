#!/usr/bin/env python3
'''
This problem was asked by Amazon.

Given an integer N, construct all possible binary search trees with N nodes.
'''

import sys
import typing


class Node(object):
    def __init__(self, value: int, left: "Node" = None, right: "Node" = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "(%d,%s,%s)" % (self.value, self.left, self.right)


def generate_possible_trees(values: typing.List[int]) -> typing.List["Node"]:
    if len(values) == 0:
        return [None]
    if len(values) == 1:
        return [Node(values[0], None, None)]
    values.sort()
    possible_trees = []
    for i in range(len(values)):
        left_options = generate_possible_trees(values[:i])
        right_options = generate_possible_trees(values[i + 1 :])
        for l in left_options:
            for r in right_options:
                possible_trees.append(Node(values[i], l, r))
    return possible_trees


if __name__ == "__main__":
    print(
        [str(x) for x in generate_possible_trees([x for x in range(int(sys.argv[1]))])]
    )
