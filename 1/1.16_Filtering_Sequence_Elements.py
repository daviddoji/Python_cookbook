#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 20:53:07 2017

@author: david
"""

from itertools import compress
import math

"""
Problem
-------
You have data inside of a sequence, and need to extract values or reduce the
sequence using some criteria.
"""


mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# All positive values
pos = [n for n in mylist if n > 0]
print(pos)

# All negative values
neg = [n for n in mylist if n < 0]
print(neg)

# transform the data at the same time
print([math.sqrt(n) for n in mylist if n > 0])

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)


# Negative values clipped to 0
neg_clip = [n if n > 0 else 0 for n in mylist]
print(neg_clip)

# Positive values clipped to 0
pos_clip = [n if n < 0 else 0 for n in mylist]
print(pos_clip)

# you can use generator expressions to produce the filtered values iteratively
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)


# Compressing example
addresses = ['5412 N CLARK',
             '5148 N CLARK',
             '5800 E 58TH',
             '2122 N CLARK',
             '5645 N RAVENSWOOD',
             '1060 W ADDISON',
             '4801 N BROADWAY',
             '1039 W GRANVILLE',
             ]

counts = [0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n > 5 for n in counts]
a = list(compress(addresses, more5))
print(a)
