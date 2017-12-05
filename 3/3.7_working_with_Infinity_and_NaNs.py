#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 07:38:12 2017

@author: david
"""

import math

"""
Problem
-------
You need to create or test for the floating-point values of infinity,
negative infinity, or NaN (not a number).
"""

a = float('inf')
b = float('-inf')
c = float('nan')
print(a)
print(b)
print(c)

print(math.isinf(a))
print(math.isnan(c))

# Infinite values will propagate in calculations in a mathematical manner
print(a + 45)
print(a * 10)
print(10 / a)

# However, certain operations are undefined
print(a / a)
print(a + b)

# NaN values propagate through all operations without raising an exception
print(c + 23)
print(c / 2)
print(c * 2)
print(math.sqrt(c))

# NaN values never compare as equal
d = float('nan')
print(c == d)
print(c is d)
