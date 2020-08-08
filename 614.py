#!/usr/bin/env python3
"""
A network consists of nodes labeled 0 to N. You are given a list of edges (a, b, t),
describing the time t it takes for a message to be sent from node a to node b.
Whenever a node receives a message, it immediately passes the message on to a neighboring node,
if possible.

Assuming all nodes are connected,
determine how long it will take for every node to receive a message that begins at node 0.

For example, given N = 5, and the following edges:

edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
You should return 9, because propagating the message from 0 -> 2 -> 3 -> 4 will
take that much time.
"""

import typing

def preprocess_graph(edges: typing.List[typing.Tuple[int,int,int]]) -> typing.Dict[int,typing.Dict[int,int]]:
    graph = {}
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = {}
        graph[edge[0]][edge[1]] = edge[2]
    return graph


def message_time(graph:typing.Dict[int,typing.Dict[int,int]], num_nodes:int) -> int:
    timing = [-1] * num_nodes
    timing[0] = 0
    to_process = []
    for k in graph[0]:
        to_process.append((graph[0][k],0,k))
    while to_process:
        to_process.sort()
        current = to_process[0]
        if timing[current[2]] == -1 or timing[current[2]] > current[0]:
            timing[current[2]] = current[0]
            if current[2] in graph:
                for k in graph[current[2]]:
                    to_process.append((timing[current[2]] + graph[current[2]][k],current[2],k))
        to_process = to_process[1:]
    message_t = timing[0]
    for t in timing:
        if t > message_t:
            message_t = t
    return message_t




if __name__ == "__main__":
    edges = [
        (0, 1, 5),
        (0, 2, 3),
        (0, 5, 4),
        (1, 3, 8),
        (2, 3, 1),
        (3, 5, 10),
        (3, 4, 5)
    ]
    print(message_time(preprocess_graph(edges), 6))