#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:28:46 2017

@author: david
"""

"""
Problem
-------
You want to eliminate the duplicate values in a sequence, but preserve the
order of the remaining items.
"""


# If the values in the sequence are hashable
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(a)
# If you don't care about the order
print(set(a))
# If the order is important
print(list(dedupe(a)))

# If you want to read a file eliminating duplicate lines
# with open(somefile,'r') as f:
#     for line in dedupe(f):


# If the values in the sequence are NOT hashable
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


b = [{'x': 2, 'y': 3},
     {'x': 1, 'y': 4},
     {'x': 2, 'y': 3},
     {'x': 2, 'y': 3},
     {'x': 10, 'y': 15},
     ]
print(b)
print(list(dedupe2(b, key=lambda b: (b['x'], b['y']))))
