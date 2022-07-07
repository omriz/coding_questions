#!/usr/bin/env python3
'''
This problem was asked by Dropbox.

What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
'''

# Original code will print a series of 9s

import functools

def f(a):
    return a

functions = []
for i in range(10):
    functions.append(functools.partial(f,i))

for f in functions:
    print(f())
