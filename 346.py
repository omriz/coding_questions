#!/usr/bin/env python3
"""
You are given a huge list of airline ticket prices between different cities around the world on a given day. These are all direct flights. Each element in the list has the format (source_city, destination, price).

Consider a user who is willing to take up to k connections from their origin city A to their destination B. Find the cheapest fare possible for this journey and print the itinerary for that journey.

For example, our traveler wants to go from JFK to LAX with up to 3 connections, and our input flights are as follows:

[
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]
Due to some improbably low flight prices, the cheapest itinerary would be JFK -> ATL -> ORD -> LAX, costing $440.
"""
def pre_process(costs_list):
    to_ret = {}
    for k in costs_list:
        if k[0] not in to_ret:
            to_ret[k[0]] = {}
        to_ret[k[0]][k[1]] = k[2]
    return to_ret

def find_cheapest(source,dest,k,costs):
    options = []

    

if __name__ == "__main__":
    costs_list = [
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]
    costs = pre_process(costs_list)
    path,cost = find_cheapest(source,dest,k,costs)
    print(path)
    print(cost)
