#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 19:49:16 2017

@author: david
"""

"""
Problem
-------
Your program has become an unreadable mess of hardcoded slice indices and
you want to clean it up.
"""

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])
items[a] = [10, 11]
print(items)
del items[a]
print(items)

a = slice(5, 10, 2)
print(a.start)
print(a.stop)
print(a.step)

s = 'HelloWorld'
print(a.indices(len(s)))

for i in range(*a.indices(len(s))):
    print(s[i])
