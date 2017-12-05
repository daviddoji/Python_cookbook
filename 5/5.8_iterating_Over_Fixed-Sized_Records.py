#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 21:10:32 2017

@author: david
"""

from functools import partial

"""
Problem
-------
Instead of iterating over a file by lines, you want to iterate over a
collection of fixed-sized records or chunks.
"""

# The file 'data.bin' contains 32-byte fixed size records
# that consist of a 4-digit number followed by a 28-byte string.

RECORD_SIZE = 32

with open('data/data2.bin', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)
