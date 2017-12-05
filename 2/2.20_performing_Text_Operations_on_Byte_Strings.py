#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:09:54 2017

@author: david
"""

import re
import os

"""
Problem
-------
You want to perform common text operations (e.g., stripping, searching, and
replacement) on byte strings.
"""

data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

print()

data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

print()

data = b'FOO:BAR,SPAM'
print(re.split(b'[:,]', data))  # Notice: pattern as bytes

print()

a = 'Hello World'  # Text string
print(a[0])
print(a[1])
b = b'Hello World'  # Byte string
print(b[0])
print(b[1])

print()

s = b'Hello World'
print(s)  # Observe b'...'
print(s.decode('ascii'))

print()

print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))

# Write a UTF-8 filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')

# Get a directory listing
os.listdir('.')  # Text string (names are decoded)
os.listdir(b'.')  # Byte string (names left as bytes)
