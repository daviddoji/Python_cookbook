#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 09:39:26 2017

@author: david
"""

"""
Problem
-------
You have an N-element tuple or sequence that you would like to unpack into a
collection of N variables.
"""


p = (4, 5)
x, y = p
print(x)
print(y)
# x, y, z = p
#  Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
#  ValueError: not enough values to unpack (expected 3, got 2)


s = 'Hello'
a, b, c, d, e = s
print(a)
print(b)
print(e)


data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(date)

name, shares, price, (year, mon, day) = data
print(name)
print(year)
print(mon)
print(day)

_, shares, price, _ = data
print(shares)
print(price)
