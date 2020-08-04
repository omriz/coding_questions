#!/usr/bin/env python3
"""
Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent"
cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true,
exists(board, "SEE") returns true,
exists(board, "ABCB") returns false.
"""

import typing


def attempt(
    board: typing.List[typing.List[str]],
    word: str,
    forbidden: typing.List[typing.Tuple[int, int]],
) -> bool:
    if len(word) == 0:
        return True
    i, j = forbidden[-1]
    if (
        i > 0
        and (i - 1, j) not in forbidden
        and word.startswith(board[i - 1][j])
        and attempt(board, word[1:], forbidden + [(i - 1, j)])
    ):
        return True
    if (
        j < len(board[i]) -1
        and (i, j + 1) not in forbidden
        and word.startswith(board[i][j + 1])
        and attempt(board, word[1:], forbidden + [(i, j + 1)])
    ):
        return True
    if (
        i < len(board) -1
        and (i + 1, j) not in forbidden
        and word.startswith(board[i + 1][j])
        and attempt(board, word[1:], forbidden + [(i + 1, j)])
    ):
        return True
    if (
        j > 0
        and (i, j - 1) not in forbidden
        and word.startswith(board[i][j - 1])
        and attempt(board, word[1:], forbidden + [(i, j - 1)])
    ):
        return True
    return False


def exists(board: typing.List[typing.List[str]], word: str) -> bool:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if word.startswith(board[i][j]):
                if attempt(board, word[1:], [(i, j)]):
                    return True
    return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

    print("ABCCED " + str(exists(board, "ABCCED")))
    print("SEE " + str(exists(board, "SEE")))
    print("ABCB " + str(exists(board, "ABCB")))
