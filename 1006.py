#!/usr/bin/env python3
'''
Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0
and the other list q1, q2, ..., qn on the line y = 1.
Imagine a set of n line segments connecting each point pi to qi.
Write an algorithm to determine how many pairs of the line segments intersect.
'''

def how_many_intersect(p,q):
    # We'll make a tuple of every pair.
    # We'll have two arrays, one sorted by q and one by p
    # then we'll find the location
    tuples = []
    for i in range(len(p)):
        tuples.append((p[i],q[i]))
    p_sorted = sorted(tuples, key=lambda x: x[0],reverse=False)
    q_sorted = sorted(tuples, key=lambda x: x[1],reverse=False)
    print(p_sorted)
    print(q_sorted)
    arcs = 0
    for i in range(len(tuples)):
        for j in range(len(tuples)):
            if p_sorted[i][0] == q_sorted[j][0] and p_sorted[i][1] == q_sorted[j][1]:
                if i> j:
                    arcs += (i-j) 
                continue
    return arcs

if __name__ == "__main__":
    p =[1,2,3,5,7]
    q = [3,2,10,1,2]
    print(how_many_intersect(p,q))