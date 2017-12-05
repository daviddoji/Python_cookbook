#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 21:27:38 2017

@author: david
"""

from collections import Iterable

"""
Problem
-------
You have a nested sequence that you want to flatten into a single list of
values.
"""


def flatten(items):#, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable):# and not isinstance(x, ignore_types):
#            yield from flatten(x)
            for i in flatten(x):
                yield i
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]


for x in flatten(items):
    print(x)

print()

#items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
#for x in flatten(items):
#    print(x)
