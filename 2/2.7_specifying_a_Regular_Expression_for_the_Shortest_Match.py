#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 18:29:37 2017

@author: david
"""

import re

"""
Problem
-------
You’re trying to match a text pattern using regular expressions, but it is
identifying the longest possible matches of a pattern. Instead, you would like
to change it to find the shortest possible match.
"""

# Sample text
text1 = 'Computer says "no."'

# Another sample text
text2 = 'Computer says "no." Phone says "yes."'

# (a) Regex that finds quoted strings - longest match (greedy)
str_pat = re.compile(r'\"(.*)\"')
print(str_pat.findall(text1))
print(str_pat.findall(text2))

# (b) Regex that finds quoted strings - shortest match (nongreedy)
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))
