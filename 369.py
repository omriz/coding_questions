#!/usr/bin/env python3
"""
You’re tracking stock price at a given instance of time. Implement an API with the following functions: add(), update(), remove(), which adds/updates/removes a datapoint for the stock price you are tracking. The data is given as (timestamp, price), where timestamp is specified in unix epoch time.

Also, provide max(), min(), and average() functions that give the max/min/average of all values seen thus far.
"""
import typing
import sys


class StockTracker(object):
    def __init__(self, name: str):
        self.name = name
        self._history = {}
        self._average = 0
        self._max = 0
        self._min = 0

    def _internal_update(self, data: typing.Tuple[int, int]):
        timestamp = data[0]
        value = data[1]
        if not self._max or value > self._max:
            self._max = value
        if not self._min or value < self._min:
            self._min = value
        if not self._average:
            self._average = value
        else:
            if timestamp in self._history:
                old_value = self._history[timestamp]
                self._average = (
                    self._average * len(self._history) - old_value + value
                ) / float(len(self._history))
            else:
                self._average = (self._average * len(self._history) + value) / float(
                    len(self._history) + 1
                )
        self._history[timestamp] = value

    def update(self, data: typing.Tuple[int, int]):
        self._internal_update(data)

    def add(self, data: typing.Tuple[int, int]):
        self._internal_update(data)

    def remove(self, timestamp: int):
        if timestamp not in self._history:
            return
        value = self._history[timestamp]
        self._history.pop(timestamp)
        if len(self._history):
            self._average = (self._average * (len(self._history) + 1) - value) / float(
                len(self._history)
            )
            if value == self._min:
                self._min = min(self._history.values())
            if value == self._max:
                self._max = max(self._history.values())
        else:
            self._average = 0
            self._max = 0
            self._min = 0

    def max(self):
        return self._max

    def min(self):
        return self._min

    def average(self):
        return self._average


if __name__ == "__main__":
    pass
