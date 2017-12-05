#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 15:18:59 2017

@author: david
"""

import base64

"""
Problem
-------
You need to decode or encode binary data using Base64 encoding.
"""

# Some byte data
s = b'hello'

# Encode as Base64
a = base64.b64encode(s)
print(a)

print()

# Decode from Base64
b = base64.b64decode(a)
print(b)

print()

# If mixing Base64-encoded data with Unicode text
a = base64.b64encode(s).decode('ascii')
print(a)
