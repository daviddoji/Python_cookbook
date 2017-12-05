#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 08:52:10 2017

@author: david
"""

import itertools

"""
Problem
-------
You want to take a slice of data produced by an iterator, but the normal
slicing operator doesn’t work.
"""


def count(n):
    while True:
        yield n
        n += 1


c = count(0)
# print(c[10:20])
# Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
# TypeError: 'generator' object is not subscriptable


# Now using islice()
for x in itertools.islice(c, 10, 20):
    print(x)
