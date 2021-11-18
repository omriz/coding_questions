#!/usr/bin/env python3
'''
You are given a list of data entries that represent entries and exits of groups of people into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building.
Return it as a pair of (start, end) timestamps. You can assume the building always starts off and ends up empty, i.e. with 0 people inside.
'''

def find_busy_time(entries):
    sorted_entries = sorted(entries,key=lambda x: x["timestamp"])
    start_time = 0
    count = 0
    max_start_time = 0
    max_end_time = 0
    max_count = 0
    for e in sorted_entries:
        if e["type"] == "enter":
            start_time = e["timestamp"]
            count += e["count"]
        if e["type"] == "exit":
            if count > max_count:
                max_start_time = start_time
                max_end_time = e["timestamp"]
                max_count = count
            start_time = e["timestamp"]
            count -= e["count"]
    return (max_start_time,max_end_time)

if __name__ == "__main__":
    e = [
        {"timestamp":1, "count":3, "type": "enter"},
        {"timestamp":2, "count":2, "type": "exit"},
        {"timestamp":3, "count":4, "type": "enter"},
        {"timestamp":4, "count":5, "type": "exit"},
    ]
    print(find_busy_time(e))
