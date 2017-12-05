#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 09:15:10 2017

@author: david
"""

from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

"""
Problem
-------
You want to iterate over all of the possible combinations or permutations of
a collection of items.
"""

items = ['a', 'b', 'c']
for p in permutations(items):
    print(p)

print()

for p in permutations(items, 2):
    print(p)

print()

for c in combinations(items, 3):
    print(c)

print()

for c in combinations(items, 2):
    print(c)

print()

for c in combinations(items, 1):
    print(c)

print()

for c in combinations_with_replacement(items, 3):
    print(c)
