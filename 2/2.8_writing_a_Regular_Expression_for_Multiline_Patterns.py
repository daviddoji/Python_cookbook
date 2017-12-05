#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 18:41:23 2017

@author: david
"""

import re

"""
Problem
-------
You’re trying to match a block of text using a regular expression, but you
need the match to span multiple lines.
"""

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
            multiline comment */
        '''

print(comment.findall(text1))
print(comment.findall(text2))

# Support for newlines, (?:.|\n) specifies a noncapture group
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

# Works fine for simple cases
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))
