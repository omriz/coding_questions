#!/usr/bin/env python3
"""
Given a function that generates perfectly random numbers between 1 and k (inclusive),
where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""
import random
import typing

def perfect_random(k):
    return random.randint(1, k)

# The point is to pick random from the whole set
# Then repeatedly pick a random one from the remaining set.
# As the likelyhood remains the same all around for all permutations we get the same probablility.
def shuffle_array(arr: typing.List[str]) -> typing.List[str]:
    for i in range(len(arr), 0, -1):
        index = perfect_random(i) - 1
        t = arr[i-1]
        arr[i-1] = arr[index]
        arr[index] = t
    return arr

