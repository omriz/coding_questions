#!/usr/bin/env python3
"""
A group of houses is connected to the main water plant by means of a set of pipes. A house can either be connected by a set of pipes extending directly to the plant, or indirectly by a pipe to a nearby house which is otherwise connected.

For example, here is a possible configuration, where A, B, and C are houses, and arrows represent pipes:

A <--> B <--> C <--> plant

Each pipe has an associated cost, which the utility company would like to minimize. Given an undirected graph of pipe connections, return the lowest cost configuration of pipes such that each house has access to water.

In the following setup, for example, we can remove all but the pipes from plant to A, plant to B, and B to C, for a total cost of 16.

pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}
"""

import copy
import typing


def reduce_costs(
    pipes: typing.Dict[str, typing.Dict[str, int]]
) -> typing.Dict[str, typing.Dict[str, int]]:
    # For each node - which is the lowest cost to reach it and from where
    minimal_paths = {}
    processing_paths = ["plant"]
    while processing_paths:
        current = processing_paths.pop(0)
        for k, v in pipes[current].items():
            if k not in minimal_paths or v < minimal_paths[k][1]:
                minimal_paths[k] = (current, v)
            processing_paths.append(k)
    new_pipes = copy.deepcopy(pipes)
    for k, v in pipes.items():
        for p in v.keys():
            if k in minimal_paths and minimal_paths[k][0] == p:
                continue
            if p in minimal_paths and minimal_paths[p][0] == k:
                continue
            new_pipes[k].pop(p)
    return new_pipes


if __name__ == "__main__":
    pipes = {
        "plant": {"A": 1, "B": 5, "C": 20},
        "A": {"C": 15},
        "B": {"C": 10},
        "C": {},
    }
    print(reduce_costs(pipes))
