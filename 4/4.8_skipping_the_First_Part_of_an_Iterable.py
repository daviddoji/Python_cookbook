#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 08:57:54 2017

@author: david
"""

from itertools import dropwhile
from itertools import islice

"""
Problem
-------
You want to iterate over items in an iterable, but the first few items aren’t
of interest and you just want to discard them.
"""

with open('/etc/passwd') as f:
    for line in f:
        print(line, end='')

print()

with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

print()

items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

print()

for x in islice(items, 3, 5):
    print(x)

# dropwhile() and islice() equilents
with open('/etc/passwd') as f:
    # Skip over initial comments
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break

    # Process remaining lines
    while line:
        # Replace with useful processing
        print(line, end='')
        line = next(f, None)

with open('/etc/passwd') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')
