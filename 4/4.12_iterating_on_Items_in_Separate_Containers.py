#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 09:50:56 2017

@author: david
"""

from itertools import chain

"""
Problem
-------
You need to perform the same operation on many objects, but the objects are
contained in different containers, and you’d like to avoid nested loops
without losing the readability of your code.
"""

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)
