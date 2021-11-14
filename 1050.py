#!/usr/bin/env python3
'''
A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation.
For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array.
For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].
'''

# O(n) complexity + O(n) Memory
def permute_new_array(arr,perm):
    new_arr = [0]*len(arr)
    for i,v in enumerate(perm):
        new_arr[i] = arr[v]
    return new_arr

# O(n^2) complexity + O(1) Memory
def permute_in_place(arr,perm):
    for i in range(len(arr)):
        if perm[i] == i:
            continue
        for j in range(i,len(arr)):
            if perm[j] == i:
                x = arr[j]
                arr[j] = arr[i]
                arr[i] = x
                perm[j] = j
    return arr

if __name__ == "__main__":
    arr = ["a","b","c"]
    perm = [2,1,0]
    print(permute_new_array(arr, perm))
    print(permute_in_place(arr, perm))