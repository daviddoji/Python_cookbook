#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 07:51:17 2017

@author: david
"""

import array

"""
Problem
-------
You need to read or write binary data, such as that found in images, sound
files, and so on.
"""

# Text string
t = 'Hello World'
print(t[0])

print()

for c in t:
    print(c)

print()

# Byte string
b = b'Hello World'
print(b[0])

print()

for c in b:
    print(c)

print()

# make sure you remember to decode or encode text from a binary-mode file
#with open('somefile.bin', 'rb') as f:
#   data = f.read(16)
#   text = data.decode('utf-8')
#with open('somefile.bin', 'wb') as f:
#   text = 'Hello World'
#   f.write(text.encode('utf-8'))

nums = array.array('i', [1, 2, 3, 4])
with open('data/data.bin', 'wb') as f:
    f.write(nums)

a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data/data.bin', 'rb') as f:
    f.readinto(a)
print(a)
