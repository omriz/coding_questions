#!/usr/env/bin python3
"""
You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""
import typing


def get_min_moves(grid: typing.List[typing.Tuple[int, int]]) -> int:
    if len(grid) <= 1:
        return 0
    curr = grid[0]
    steps = 0
    for i in range(1, len(grid)):
        x_dist = abs(grid[i][0] - curr[0])
        y_dist = abs(grid[i][1] - curr[1])
        steps += max(x_dist, y_dist)
        curr = grid[i]
    return steps


if __name__ == "__main__":
    grid = [(0, 0), (1, 1), (1, 2)]
    print(get_min_moves(grid))
