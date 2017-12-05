#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 19:23:40 2017

@author: david
"""

"""
Problem
-------
You need to format text with some sort of alignment applied.
"""

text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

print(text.rjust(20, '='))
print(text.center(20, '*'))

# More general and powerful
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))

print(format(text, '=>20s'))
print(format(text, '*^20s'))

print('{:>10s} {:>10s}'.format('Hello', 'World'))

x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))

# Old code style
print('%-20s' % text)
print('%20s' % text)
