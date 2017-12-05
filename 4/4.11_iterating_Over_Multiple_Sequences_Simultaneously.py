#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 09:39:26 2017

@author: david
"""

from itertools import zip_longest

"""
Problem
-------
You want to iterate over the items contained in more than one sequence at a
time.
"""

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)

print()

# the length of the iteration is the same as the length of the shortest input
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a, b):
    print(i)

print()

for i in zip_longest(a, b):
    print(i)

print()

for i in zip_longest(a, b, fillvalue=0):
    print(i)

print()

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers, values))
print(s)
# Alternatively
for name, val in zip(headers, values):
    print(name, '=', val)

print()

# zip() can be passed more than two sequences as input
a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
for i in zip(a, b, c):
    print(i)

print()

# zip() creates an iterator
print(zip(a, b))
print(list(zip(a, b)))
