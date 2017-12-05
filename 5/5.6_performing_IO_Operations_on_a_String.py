#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 20:57:16 2017

@author: david
"""

import io

"""
Problem
-------
You want to feed a text or binary string to code that’s been written to
operate on file-like objects instead.
"""

s = io.StringIO()
print(s.write('Hello World\n'))
print('This is a test', file=s)

# Get all of the data written so far
print(s.getvalue())

# Wrap a file interface around an existing string
s = io.StringIO('Hello\nWorld\n')
print(s.read(4))
print(s.read())

# Usage with binary data
s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())
