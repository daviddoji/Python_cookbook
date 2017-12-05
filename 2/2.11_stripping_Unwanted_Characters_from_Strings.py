#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 19:13:54 2017

@author: david
"""

import re

"""
Problem
-------
You want to strip unwanted characters, such as whitespace, from the beginning,
end, or middle of a text string.
"""

# Whitespace stripping
s = 'hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# Character stripping
t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))

s = ' hello      world   \n'
print(s.strip())

print(s.replace(' ', ''))
print(re.sub('\s+', ' ', s))


# combine string stripping operations with some other kind of iterative
# processing
#with open(filename) as f:
#    lines = (line.strip() for line in f)
#    for line in lines:
