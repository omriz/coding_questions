#!/usr/bin/env python3
"""
A competitive runner would like to create a route that starts and ends at his house, with the condition that the route goes entirely uphill at first, and then entirely downhill.

Given a dictionary of places of the form {location: elevation}, and a dictionary mapping paths between some of these locations to their corresponding distances, find the length of the shortest route satisfying the condition above. Assume the runner's home is location 0.

For example, suppose you are given the following input:

elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}
In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a distance of 28.
"""

import typing


def _check_path(
    current: typing.List[int], paths: typing.Dict[typing.Tuple[int, int], int]
) -> typing.List[typing.List[int]]:
    to_ret = []
    for p in paths.keys():
        if p[0] == current[-1]:
            if p[1] == 0:
                to_ret.append(current[:] + [0])
            else:
                optional_paths = _check_path(current[:] + [p[1]], paths)
                if optional_paths:
                    to_ret.extend(optional_paths)
    return to_ret


def _valid_loop(loop: typing.List[int], elevations: typing.Dict[int, int]) -> bool:
    if len(loop) <= 1:
        return False
    going_up = True
    for i in range(1, len(loop)):
        if elevations[loop[i]] > elevations[loop[i - 1]]:
            if not going_up:
                return False
        elif elevations[loop[i]] < elevations[loop[i - 1]]:
            if going_up:
                going_up = False
    return True


def _calculate_distance(
    loop: typing.List[int], paths: typing.Dict[typing.Tuple[int, int], int]
) -> int:
    if len(loop) <= 1:
        return 0
    length = 0
    for i in range(1, len(loop)):
        for p in paths:
            if p[0] == loop[i - 1] and p[1] == loop[i]:
                length += paths[p]
                break
    return length


def find_shortest_path(
    elevations: typing.Dict[int, int], paths: typing.Dict[typing.Tuple[int, int], int]
) -> int:
    # First - find all possible loops
    loops = _check_path([0], paths)
    # Second - filter according to elevation
    valid_loops = []
    for l in loops:
        if _valid_loop(l, elevations):
            valid_loops.append(l)
    # Third calculate distance for each
    loops_with_distance = []
    for loop in valid_loops:
        loops_with_distance.append((loop, _calculate_distance(loop, paths)))
    min_loop, min_distance = loops_with_distance[0]
    for loop, d in loops_with_distance:
        if d < min_distance:
            min_distance = d
            min_loop = loop
    print(min_loop)
    print(min_distance)
    return min_distance


if __name__ == "__main__":
    elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
    paths = {
        (0, 1): 10,
        (0, 2): 8,
        (0, 3): 15,
        (1, 3): 12,
        (2, 4): 10,
        (3, 4): 5,
        (3, 0): 17,
        (4, 0): 10,
    }
    find_shortest_path(elevations, paths)
