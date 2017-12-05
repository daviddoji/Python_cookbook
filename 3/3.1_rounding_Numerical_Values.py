#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:21:52 2017

@author: david
"""

"""
Problem
-------
You want to round a floating-point number to a fixed number of decimal places.
"""

print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25361, 3))

print()

a = 1627731
print(round(a, -1))
print(round(a, -2))
print(round(a, -3))

print()

x = 1.23456
print(format(x, '0.2f'))
print(format(x, '0.3f'))
print('value is {:0.3f}'.format(x))

print()

a = 2.1
b = 4.2
c = a + b
print(c)
c = round(c, 2)  # "Fix" result (???)
print(c)
