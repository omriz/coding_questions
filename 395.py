#!/usr/bin/env python3

import sys
import typing


def generate_anagrams(words: typing.Iterable[str]) -> typing.List[typing.List[str]]:
    sources = {}
    for word in words:
        # Frozenset is immutable and therefore can be used as dict keys
        k = frozenset(word)
        if k in sources:
            sources[k].append(word)
        else:
            sources[k] = [word]
    return list(sources.values())


if __name__ == "__main__":
    print(generate_anagrams(sys.argv[1:]))
