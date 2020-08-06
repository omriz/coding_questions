#!/usr/bin/env python3
"""
Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible reconstruction,
return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""


import sys
import typing


_WORDS = ["bed", "bath", "bedbath", "and", "beyond"]


def split_to_words(w: str) -> (bool, typing.List[str]):
    # We're going to make this recursive/ somewhat dynamic
    # Find the first word. Find the rest of the words in what's left.
    # If that works, great. If not, bummer.
    if not w:
        return True, []
    if w in _WORDS:
        return True, [w]
    for i in range(len(w)):
        if w[:i] in _WORDS:
            success, words = split_to_words(w[i:])
            if success:
                return True, [w[:i]] + words
    return False, []


if __name__ == "__main__":
    success, words = split_to_words(sys.argv[1])
    if success:
        print(words)
    else:
        print("ERROR: could not split: %s" % sys.argv[1])
