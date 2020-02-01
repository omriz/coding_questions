#!/usr/bin/env python3
"""
A ternary search tree is a trie-like data structure where each node may have up to three children. Here is an example which represents the words code, cob, be, ax, war, and we.

       c
    /  |  \
   b   o   w
 / |   |   |
a  e   d   a
|    / |   | \ 
x   b  e   r  e  
The tree is structured according to the following rules:

left child nodes link to words lexicographically earlier than the parent prefix
right child nodes link to words lexicographically later than the parent prefix
middle child nodes continue the current word
For instance, since code is the first word inserted in the tree, and cob lexicographically precedes cod, cob is represented as a left child extending from cod.

Implement insertion and search functions for a ternary search tree.
"""

import typing


class Node(object):
    def __init__(
        self,
        value: str,
        left: typing.Optional["Node"] = None,
        middle: typing.Optional["Node"] = None,
        right: typing.Optional["Node"] = None,
    ):
        self.value = value
        self.left = left
        self.middle = middle
        self.right = right


class TernarySearchTree(object):
    def __init__(self):
        self._root = None

    def search(self, word: str) -> bool:
        curr = self._root
        for i in word:
            if curr == None:
                return False
            while curr != None:
                if curr.value == i:
                    curr = curr.middle
                    break
                elif curr.value < i:
                    curr = curr.right
                else:
                    curr = curr.left
        return True

    def insert(self, word: str):
        if self._root is None:
            self._root = Node(word[0])
            curr = self._root
            for i in word[1:]:
                curr.middle = Node(i)
                curr = curr.middle
            return
        curr = self._root
        previous = self._root
        p = 0
        while curr is not None and p < len(word):
            previous = curr
            if curr.value == word[p]:
                curr = curr.middle
                p += 1
            elif curr.value > word[p]:
                curr = curr.left
            else:
                curr = curr.right
        curr = previous
        if p == len(word):
            return
        if word[p] < curr.value:
            curr.left = Node(word[p])
            curr = curr.left
        if word[p] > curr.value:
            curr.right = Node(word[p])
            curr = curr.right
        p += 1
        for i in range(p, len(word)):
            curr.middle = Node(word[i])
            curr = curr.middle


if __name__ == "__main__":
    t = TernarySearchTree()
    t.insert("cbz")
    print(t.search("cbz"))
    print(t.search("abc"))
    t.insert("abc")
    print(t.search("cbz"))
    print(t.search("abc"))
