#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 23:35:52 2017

@author: david
"""

import binascii
import base64

"""
Problem
-------
You need to decode a string of hexadecimal digits into a byte string or
encode a byte string as hex.
"""

# Initial byte string
s = b'hello'
# Encode as hex
h = binascii.b2a_hex(s)
print(h)
# Decode back to bytes
b = binascii.a2b_hex(h)
print(b)

print()

# Encode as base64
h = base64.b16encode(s)
print(h)
# Decode back to bytes
b = base64.b16decode(h)
print(b)
# To coerce it to Unicode for output
b = h.decode('ascii')
print(b)
