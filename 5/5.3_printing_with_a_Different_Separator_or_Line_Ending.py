#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 07:41:35 2017

@author: david
"""

"""
Problem
-------
You want to output data using print() , but you also want to change the
separator character or line ending.
"""

print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')

print()

for i in range(5):
    print(i)

print()

for i in range(5):
    print(i, end=' ')

print()
print()

# Only works with strings
print(','.join(('ACME', '50', '91.5')))

# Needed of acrobatics to get it work
row = ('ACME', 50, 91.5)
print(','.join(str(x) for x in row))

# Or simply
print(*row, sep=',')
