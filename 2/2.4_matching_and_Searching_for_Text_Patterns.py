#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 17:28:33 2017

@author: david
"""

import re

"""
Problem
-------
You want to match or search text for a specific pattern.
"""

# Some sample text
text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
print(text == 'yeah')
# Match at start or end
print(text.startswith('yeah'))
print(text.endswith('no'))
# Search for the location of the first occurrence
print(text.find('no'))

# Using re module
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

# Simple matching: \d+ means match one or more digits at the start of a string
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

# Another sample text
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

# (a) Find all matching dates for all occurrences of a pattern
datepat = re.compile(r'\d+/\d+/\d+')
print(datepat.findall(text))

# (b) Find all matching dates with capture groups
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# (c) Iterative search
for m in datepat.finditer(text):
    print(m.groups())


# the match() will match things you aren’t expecting
m = datepat.match('11/27/2012abcdef')
print(m.group())

# For an exact match, make sure the pattern includes the end-marker ($)
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat.match('11/27/2012abcdef'))
print(datepat.match('11/27/2012'))

# Skipping the compilation step for a quick matching/searching
print(re.findall(r'(\d+)/(\d+)/(\d+)', text))
