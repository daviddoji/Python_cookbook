#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 07:44:16 2017

@author: david
"""

"""
Problem
-------
You need to process items in an iterable, but for whatever reason, you can’t
or don’t want to use a for loop.
"""

# manually reads lines from a file
with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass

print()

# Another way to do it
with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

print()

# Basic mechanics of what happens during iteration:
items = [1, 2, 3]
# Get the iterator
it = iter(items)  # Invokes items.__iter__()
# Run the iterator
print(next(it))  # Invokes it.__next__()
print(next(it))
print(next(it))
#print(next(it))
#Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
#StopIteration