#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 20:35:28 2017

@author: david
"""

import re

"""
Problem
-------
You need to split a string into fields, but the delimiters (and spacing around
them) aren’t consistent throughout the string.
"""

line = 'asdf fjdk; afed, fjek,asdf,      foo'

# (a) Splitting on space, comma, and semicolon
parts = re.split(r'[\s,;]\s*', line)
print('\nparts: ', parts)

# (b) Splitting with a capture group
fields = re.split(r'(\s|,|;)\s*', line)
print('\nfields: ', fields)

# (c) Rebuilding a string using fields above
values = fields[::2]
delimiters = fields[1::2]
delimiters.append('')
print('\nvalue =', values)
print('\ndelimiters =', delimiters)
# Reform the line using the same delimiters
newline = ''.join(v+d for v, d in zip(values, delimiters))
print('\nnewline =', newline)

# (d) Splitting using a non-capture group
parts = re.split(r'(?:\s|,|;)\s*', line)
print('\nparts: ', parts)
