#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 09:23:05 2017

@author: david
"""

from collections import defaultdict

"""
Problem
-------
You want to iterate over a sequence, but would like to keep track of which
element of the sequence is currently being processed.
"""

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

print()

# start the numbering at 1 instead of 0
for idx, val in enumerate(my_list, 1):
    print(idx, val)

print()


# Example of iterating over lines of a file with an extra lineno attribute
def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))


parse_data('data/sample.dat')

print()

# using enumerate() to map each word to the line offset in the file where it
# was found
word_summary = defaultdict(list)
with open('data/somefile.txt', 'r') as f:
    lines = f.readlines()
for idx, line in enumerate(lines):
    # Create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(word_summary)

print()

data = [(1, 2), (3, 4), (5, 6), (7, 8)]
# Correct!
for n, (x, y) in enumerate(data):
    print(n)

# Error!
# for n, x, y in enumerate(data):
#     print(n)
# Traceback (most recent call last):
# ValueError: not enough values to unpack (expected 3, got 2)
