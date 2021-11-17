#!/usr/bin/env python3
'''
Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same.
If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
'''

import sys

def rearrange(word:str)->str:
    if len(word) < 2:
        return word
    new_word = word[:]
    for i in range(1, len(word)):
        if new_word[i] != new_word[i-1]:
           continue
        fixed = False
        for j in range(i+1,len(word)):
            if new_word[j] != new_word[i]:
                new_word = new_word[:i] + new_word[j] + new_word[i:j] + new_word[j+1:]
                fixed = True
                continue
        if not fixed:
            return None
    return new_word


if __name__ == "__main__":
    print(rearrange(sys.argv[1]))