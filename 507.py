#!/usr/bin/env python3
"""
On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file.
Write a program that reads this file as a stream and returns the top 3 candidates at any given time.
If you find a voter voting more than once, report this as fraud.
"""

import pprint


class FraudException(Exception):
    pass


def analyze_votes(voting_stream):
    voters = {}
    candidates = {}
    top3 = {}
    for line in voting_stream:
        voter, candidate = line.split(",")
        voter = voter.strip()
        candidate = candidate.strip()
        if voter in voters:
            raise FraudException(message="%s committed fraud" % voter)
        voters[voter] = True
        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1
        if candidate in top3:
            top3[candidate] += 1
        elif len(top3) < 3:
            top3[candidate] = candidates[candidate]
        else:
            for t in top3:
                if candidates[candidate] > top3[t]:
                    top3.pop(t)
                    top3[candidate] = candidates[candidate]
        pprint.pprint(top3)


if __name__ == "__main__":
    v = [
        "a,bibi",
        "b,bibi",
        "c,bibi",
        "d,bibi",
        "4,bibi",
        "f,bibi",
        "g,gantz",
        "h,gantz",
        "i,gantz",
        "j,peres",
        "k,gantz",
        "m,gantz",
        "n,shimi",
        "o,shimi",
        "p,gantz",
        "q,gantz",
        "s,david",
        "t,gantz",
        "u,gantz",
    ]
    analyze_votes(v)
