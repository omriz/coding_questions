#!/usr/bin/env python3
"""
Huffman coding is a method of encoding characters based on their frequency.
Each letter is assigned a variable-length binary string, such as 0101 or 111110,
where shorter lengths correspond to more common letters.
To accomplish this, a binary tree is built such that the path from the root to any leaf uniquely maps to a character.
When traversing the path, descending to a left child corresponds to a 0 in the prefix,
while descending right corresponds to 1.

Here is an example tree (note that only the leaf nodes have letters):

        *
      /   \
    *       *
   / \     / \
  *   a   t   *
 /             \
c               s
With this encoding, cats would be represented as 0000110111.

Given a dictionary of character frequencies, build a Huffman tree,
and use it to determine a mapping between characters and their encoded binary strings.
"""

import typing


class Node(object):
    def __init__(self, v=None, weight=None, left=None, right=None):
        self.v = v
        self.weight = weight
        self.left = left
        self.right = right

    def __str__(self):
        return "(%s, (%s, %s))" % (self.v, self.left, self.right)


def minimize(t: typing.List[Node]) -> typing.List[Node]:
    minimals = []
    for _ in range(2):
        minimal_index = 0
        minimal_weight = t[0].weight
        for i, a in enumerate(t):
            if a.weight < minimal_weight:
                minimal_index = i
                minimal_weight = a.weight
        minimals.append(t[i])
        t = t[0:i] + t[i + 1 :]
    n = Node("*", minimals[0].weight + minimals[1].weight, minimals[0], minimals[1])
    t.append(n)
    return t


def generate_h_tree(freq: typing.Dict[str, int]) -> Node:
    # Generate a node from each letter
    trees = []
    for c, w in freq.items():
        trees.append(Node(c, w, None, None))
    while len(trees) > 1:
        trees = minimize(trees)
    return trees[0]


if __name__ == "__main__":
    freq = {"a": 2, "t": 3, "c": 1, "s": 1}
    print(generate_h_tree(freq))
