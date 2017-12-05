#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:22:41 2017

@author: david
"""

import urllib.request
import io
import sys

"""
Problem
-------
You want to add or change the Unicode encoding of an already open file
without closing it first.
"""

# add Unicode encoding/decoding to an already existing file object
u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()

print(text)


# change the encoding of an already open text-mode file
print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(sys.stdout.encoding)
