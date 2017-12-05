#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:54:09 2017

@author: david
"""

import sys
import os

"""
Problem
-------
You want to perform file I/O operations using raw filenames that have not
been decoded or encoded according to the default filename encoding.
"""

print(sys.getfilesystemencoding())

print()

# Wrte a file using a unicode filename
with open('data/jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')

# Directory listing (decoded)
print(os.listdir('data'))

# Directory listing (raw)
print(os.listdir(b'data'))  # Note: byte string

# Open file with raw filename
#with open(b'data/jalapen\xcc\x83o.txt') as f:
#    print(f.read())
