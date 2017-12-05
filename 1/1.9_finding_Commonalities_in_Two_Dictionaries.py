#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:17:05 2017

@author: david
"""

"""
Problem
-------
You have two dictionaries and want to find out what they might have in common
(same keys, same values, etc.).
"""

a = {'x': 1,
     'y': 2,
     'z': 3,
     }

b = {'w': 10,
     'x': 11,
     'y': 2,
     }

print('Common keys:', a.keys() & b.keys())
print('Keys in a not in b:', a.keys() - b.keys())
print('(key,value) pairs in common:', a.items() & b.items())

# Make a new dictionary with certain keys removed
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)
