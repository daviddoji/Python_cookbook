#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 20:15:35 2017

@author: david
"""

import csv
from collections import namedtuple
import re

"""
Problem
-------
You want to read or write data encoded as a CSV file.
"""

# (a) Reading as tuples
print('Reading as tuples:')
with open('data/stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # process row
        print('    ', row)
print()

# Example of reading tab-separated values
print('Reading a tsv file:')
with open('data/stocks.tsv') as f:
    f_tsv = csv.reader(f, delimiter='\t')
    for row in f_tsv:
        # Process row
        print('    ', row)
print()

# regex substitution on nonvalid identifier characters
print('Using regex for nonvalid characters:')
with open('data/stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        # Process row
        print('    ', row)
print()


# (b) Reading as namedtuples
print('Reading as namedtuples')
with open('data/stocks.csv') as f:
    f_csv = csv.reader(f)
    Row = namedtuple('Row', next(f_csv))
    for r in f_csv:
        row = Row(*r)
        # Process row
        print('    ', row)
print()


# (c) Reading as dictionaries
print('Reading as dicts')
with open('data/stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # process row
        print('    ', row)
print()


# (d) Reading into tuples with type conversion
print('Reading into named tuples with type conversion')
col_types = [str, float, str, str, float, int]
with open('data/stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Apply conversions to the row items
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        print(row)
print()


# (e) Converting selected dict fields
print('Reading as dicts with type conversion')
field_types = [('Price', float),
               ('Change', float),
               ('Volume', int)]

with open('data/stocks.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key]))
                   for key, conversion in field_types)
        print(row)
