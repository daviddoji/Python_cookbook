#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 22:39:25 2017

@author: david
"""

from xml.etree.ElementTree import iterparse
from xml.etree.ElementTree import parse
from collections import Counter

"""
Problem
-------
You need to extract data from a huge XML document using as little memory
as possible.
"""

# The file 'data/potholes.xml' is a greatly condensed version of a larger
# file available for download at
#
# https://data.cityofchicago.org/api/views/7as2-ds3y/rows.xml?accessType=DOWNLOAD


# a simple function that can be used to incrementally process huge XML
# files using a very small memory footprint
def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
#               makes this recipe save memory
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


# it takes about 450 MB of memory
potholes_by_zip = Counter()
doc = parse('data/potholes.xml')
for pothole in doc.iterfind('row/row'):
    potholes_by_zip[pothole.findtext('zip')] += 1
for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)

print()

# it takes about 7 MB of memory but it is much slower
potholes_by_zip = Counter()
data = parse_and_remove('data/potholes.xml', 'row/row')
for pothole in data:
    potholes_by_zip[pothole.findtext('zip')] += 1
for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)

print()

data = iterparse('data/potholes.xml', ('start', 'end'))
print(next(data))
print(next(data))
