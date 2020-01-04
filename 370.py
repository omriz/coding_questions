#!/usr/bin/env python3
"""
The “active time” of a courier is the time between the pickup and dropoff of a delivery. Given a set of data formatted like the following:

(delivery id, timestamp, pickup/dropoff)

Calculate the total active time in seconds. A courier can pick up multiple orders before dropping them off. The timestamp is in unix epoch seconds.

For example, if the input is the following:

(1, 1573280047, 'pickup')
(1, 1570320725, 'dropoff')
(2, 1570321092, 'pickup')
(3, 1570321212, 'pickup')
(3, 1570322352, 'dropoff')
(2, 1570323012, 'dropoff')

The total active time would be 1260 seconds.
"""
import typing
import sys


def total_active_time(times: typing.List[typing.Tuple[int, int, str]]) -> int:
    hashed = {}
    for t in times:
        if t[0] not in hashed:
            hashed[t[0]] = {}
        hashed[t[0]][t[2]] = t[1]
    s = 0
    for t in hashed:
        s += (hashed[t]["dropoff"] - hashed[t]["pickup"])
    return s


# The input doesn't make sense but the solution is solid.
if __name__ == "__main__":
    times = [
        (1, 1573280047, "pickup"),
        (1, 1570320725, "dropoff"),
        (2, 1570321092, "pickup"),
        (3, 1570321212, "pickup"),
        (3, 1570322352, "dropoff"),
        (2, 1570323012, "dropoff"),
    ]
    print(total_active_time(times))
