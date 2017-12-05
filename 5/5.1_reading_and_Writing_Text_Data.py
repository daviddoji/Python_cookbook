#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 21:58:52 2017

@author: david
"""

"""
Problem
-------
You need to read or write text data, possibly in different text encodings
such as ASCII, UTF-8, or UTF-16.
"""

# The file sample.txt is a UTF-8 encoded text file with Windows
# line-endings (\r\n).

# (a) Reading a basic text file (UTF-8 default encoding)

print("Reading a simple text file (UTF-8)")
with open('data/sample.txt', 'rt') as f:
    for line in f:
        print(repr(line))

# (b) Reading a text file with universal newlines turned off
print("Reading text file with universal newlines off")
with open('data/sample.txt', 'rt', newline='') as f:
    for line in f:
        print(repr(line))

# (c) Reading text file as ASCII with replacement error handling
print("Reading text as ASCII with replacement error handling")
with open('data/sample.txt', 'rt', encoding='ascii', errors='replace') as f:
    for line in f:
        print(repr(line))

# (d) Reading text file as ASCII with ignore error handling
print("Reading text as ASCII with ignore error handling")
with open('data/sample.txt', 'rt', encoding='ascii', errors='ignore') as f:
    for line in f:
        print(repr(line))
