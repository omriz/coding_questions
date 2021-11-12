#!/usr/bin/env python3
'''
Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
'''

def search(board,i,j,word,restricted):
    if not word:
        return True
    if i > 0:
        if board[i-1][j] == word[0] and (i-1,j) not in restricted:
            restricted.add((i-1,j))
            if search(board,i-1,j,word[1:],restricted):
                return True
            restricted.remove((i-1,j))
    if i < len(board)-1:
        if board[i+1][j] == word[0] and (i+1,j) not in restricted:
            restricted.add((i+1,j))
            if search(board,i+1,j,word[1:],restricted):
                return True
            restricted.remove((i+1,j))
    if j > 0:
        if board[i][j-1] == word[0] and (i,j-1) not in restricted:
            restricted.add((i,j-1))
            if search(board,i,j-1,word[1:],restricted):
                return True
            restricted.remove((i,j-1))
    if j < len(board[i])-1:
        if board[i][j+1] == word[0] and (i,j+1) not in restricted:
            restricted.add((i,j+1))
            if search(board,i,j+1,word[1:],restricted):
                return True
            restricted.remove((i,j+1))
    return False



def exists(board, word):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0] and search(board,i,j,word[1:],set([(i,j)])):
                return True
    return False

if __name__ == "__main__":
    board = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    assert exists(board, "ABCCED")
    assert exists(board, "SEE")
    assert not exists(board, "ABCB")
