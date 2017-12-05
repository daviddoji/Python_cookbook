#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 19:32:13 2017

@author: david
"""

import sys

"""
Problem
-------
You want to combine many small strings together into a larger string.
"""

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

# For only a few strings
a = 'Is Chicago'
b = 'Not Chicago?'
c = 'Of course!'
print(a + ' ' + b)

print('{} {}'.format(a, b))

# to combine string literals together in source code
a = 'Hello' 'World'
print(a)


# This should be avoided due to the memory copies and garbage collection
s = ''
for p in parts:
    s += p
print(s)

# A trick is the conversion of data to strings and concatenation at the same
# time using a generator expresion
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

a = 'Is Chicago'
b = 'Not Chicago?'
c = 'Of course!'
print(a + ':' + b + ':' + c)  # Ugly
print(':'.join([a, b, c]))  # Still ugly
print(a, b, c, sep=':')  # Better


# Version 1 (string concatenation) for small strings
sys.stdout.write(a + b)
sys.stdout.write('\n')
# Version 2 (separate I/O operations) for large strings
sys.stdout.write(a)
sys.stdout.write(b)
sys.stdout.write('\n')


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


# (a) Simple join operator
text = ''.join(sample())
print(text)


# (b) Redirection of parts to I/O
for part in sample():
    sys.stdout.write(part)
sys.stdout.write('\n')


# (c) Combination of parts into buffers and larger I/O operations
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)


for part in combine(sample(), 32768):
    sys.stdout.write(part)
sys.stdout.write('\n')
