#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 19:42:51 2017

@author: david
"""

"""
Problem
-------
You want to implement a custom iteration pattern that’s different than the
usual built-in functions (e.g., range() , reversed() , etc.).
"""


# Iteration using a generator
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 1, 0.125)))


# underlying mechanics of a generator
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')


# Create the generator, notice no output appears
c = countdown(3)
print(c)

# Run to first yield and emit a value
print(next(c))

# Run to the next yield
print(next(c))

# Run to the next yield
print(next(c))

# Run to the next yield (iteration stops)
print(next(c))
