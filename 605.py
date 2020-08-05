#!/usr/bin/env python3
"""
In academia, the h-index is a metric used to calculate the impact of a researcher's papers.
It is calculated as follows:

A researcher has index h if at least h of her N papers have h citations each.
If there are multiple h satisfying this formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5].
Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.
"""

import typing
import sys


def get_h_index(papers: typing.List[int]) -> int:
    papers.sort()
    i = len(papers) - 1
    while i > 0:
        if len(papers) - i >= papers[i]:
            return i + 1
        i -= 1
    return 0



if __name__ == "__main__":
    print(get_h_index([int(x) for x in sys.argv[1:]]))
