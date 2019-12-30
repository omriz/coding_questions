#!/usr/bin/env python3
import typing


def is_compaible(
    job: typing.Tuple[int, int], job_list: typing.List[typing.Tuple[int, int]]
) -> bool:
    for pair in job_list:
        if job[0] > pair[0] and job[0] < pair[1]:
            return False
        if job[1] > pair[0] and job[1] < pair[1]:
            return False
        if job[0] <= pair[0] and job[1] >= pair[1]:
            return False
    return True


def brute_force_find(
    job_list: typing.List[typing.Tuple[int, int]],
    on_going: typing.Optional[typing.List[typing.Tuple[int, int]]] = None,
) -> typing.List[typing.Tuple[int, int]]:
    if not job_list:
        return on_going[:]
    if not on_going:
        current = []
    else:
        current = on_going[:]
    without = brute_force_find(job_list[1:], current[:])
    if is_compaible(job_list[0], current):
        within = brute_force_find(job_list[1:], current[:] + [job_list[0]])
    else:
        within = []
    if len(within) > len(without):
        return within
    else:
        return without


if __name__ == "__main__":
    jobs = [(0, 6), (1, 4), (3, 5), (3, 8), (4, 7), (5, 9), (6, 10), (8, 11)]
    print(brute_force_find(jobs))
