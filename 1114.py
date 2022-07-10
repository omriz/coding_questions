#!/usr/bin/env python3
"""
On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file.
Write a program that reads this file as a stream and returns the top 3 candidates at any given time.
If you find a voter voting more than once, report this as fraud.
"""

class FraudException(Exception):pass

class VoteCounter(object):
    def __init__(self):
        self.voters = {}
        self.candidates = {}
        self.top_candidates = []
    
    def count_vote(self,voter,candidate):
        if voter in self.voters:
            raise FraudException("Voter %s voted multiple times!" % voter)
        self.voters[voter] = True
        if candidate in self.candidates:
            self.candidates[candidate] += 1
        else:
            self.candidates[candidate] = 1
        if candidate not in self.top_candidates:
            if len(self.top_candidates) < 3:
                self.top_candidates.append(candidate)
            else:
                if self.candidates[candidate] > self.candidates[self.top_candidates[-1]]:
                    self.top_candidates[-1] = candidate
        if len(self.top_candidates) > 2 and self.candidates[self.top_candidates[1]] < self.candidates[self.top_candidates[2]]:
            a = self.top_candidates[1]
            self.top_candidates[1] = self.top_candidates[2]
            self.top_candidates[2] = a
        if len(self.top_candidates) > 1 and self.candidates[self.top_candidates[0]] < self.candidates[self.top_candidates[1]]:
            a = self.top_candidates[0]
            self.top_candidates[0] = self.top_candidates[1]
            self.top_candidates[1] = a
    def print_top(self):
        print("******************")
        for c in self.top_candidates:
            print("* %s" % c)

if __name__ == "__main__":
    vc = VoteCounter()
    vc.count_vote("a","bb")
    vc.print_top()
    vc.count_vote("c","cc")
    vc.print_top()
    vc.count_vote("d","aa")
    vc.print_top()
    vc.count_vote("e","aa")
    vc.print_top()
    vc.count_vote("h","cc")
    vc.print_top()
    vc.count_vote("f","bb")
    vc.print_top()
    vc.count_vote("g","ff")
    vc.print_top()
    vc.count_vote("b","bb")
    vc.print_top()
