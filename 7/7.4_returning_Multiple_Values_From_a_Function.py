#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 07:27:47 2017

@author: david
"""

"""
You want to return multiple values from a function.
"""


# To return multiple values from a function, simply return a tuple
def myfun():
    return 1, 2, 3


# Tuple unpacking
a, b, c = myfun()
print(a)
print(b)
print(c)

print()

# Tuple packed
x = myfun()
print(x)
