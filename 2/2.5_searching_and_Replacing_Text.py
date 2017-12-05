#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 17:46:21 2017

@author: david
"""

import re
from calendar import month_abbr

"""
Problem
-------
You want to search for and replace a text pattern in a string.
"""

text = 'yeah, but no, but yeah, but no, but yeah'
# For literal patterns
print(text.replace('yeah', 'yep'))

# Some sample text
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

# (a) Simple substitution
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))


# (b) For repeated substitutions of the same pattern (better performance)
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))


# (c) Replacement function
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


print(datepat.sub(change_date, text))

# how many substitutions were made?
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)
