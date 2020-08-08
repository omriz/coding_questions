#!/usr/bin/env python3
"""
Given a start word, an end word, and a dictionary of valid words,
find the shortest transformation sequence from start to end such that
only one letter is changed at each step of the sequence,
and each transformed word exists in the dictionary.
If there is no possible transformation, return null.
Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and dictionary = {
    "dot", "dop", "dat", "cat"}, return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {
    "dot", "tod", "dat", "dar"},
return null as there is no possible transformation from dog to cat.
"""

import copy
import typing

def diff_word(start:str,end:str) -> int:
    assert len(start) == len(end)
    diff = 0
    for i in range(len(start)):
        if start[i] != end[i]:
            diff += 1
    return diff

def get_transformation(
    start: str, end: str, words: typing.List[str],
) -> typing.List[str]:
    if end not in words:
        return None
    if diff_word(start,end) == 0:
        return [end]
    if diff_word(start,end) == 1:
        return [start,end]
    transformation = None
    for word in words:
        if diff_word(start, word) == 1:
            nwords = copy.deepcopy(words)
            nwords.remove(word)
            new_transform = get_transformation(word, end, nwords)
            if new_transform and new_transform[-1] == end:
                if not transformation:
                    transformation = new_transform
                elif len(new_transform) < len(transformation):
                    transformation = new_transform
    if transformation:
        return [start] + transformation
    else:
        return None

    


if __name__ == "__main__":
    start = "dog"
    end = "cat"
    words = ["dot", "dop", "dat", "cat"]
    print(get_transformation(start, end, words))
