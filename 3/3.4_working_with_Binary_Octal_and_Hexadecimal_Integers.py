#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 07:15:03 2017

@author: david
"""

"""
Problem
-------
You need to convert or output integers represented by binary, octal, or
hexadecimal digits.
"""

x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

# Values are signed
x = -1234
print(format(x, 'b'))
print(format(x, 'x'))

# Unsigned values
print(format(2**32 + x, 'b'))
print(format(2**32 + x, 'x'))

# Convert to different bases
print(int('4d2', 16))
print(int('10011010010', 2))

# Make sure you prefix the octal value with 0o
# os.chmod('script.py', 0o755)
