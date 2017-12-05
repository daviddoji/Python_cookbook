#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 07:02:59 2017

@author: david
"""

"""
Problem
-------
You need to format a number for output, controlling the number of digits,
alignment, inclusion of a thousands separator, and other details.
"""

x = 1234.56789

# Two decimal places of accuracy
print(format(x, '0.2f'))

# Right justified in 10 chars, one-digit accuracy
print(format(x, '>10.1f'))

# Left justified
print(format(x, '<10.1f'))

# Centered
print(format(x, '^10.1f'))

# Inclusion of thousands separator
print(format(x, ','))
print(format(x, '0,.1f'))

# Use of exponential notation
print(format(x, 'e'))
print(format(x, '0.2E'))

# Same notation as format method
print('The value is {:0,.2f}'.format(x))

# Values are also rounded as usual
print(format(x, '0.1f'))
print(format(-x, '0.1f'))

# Dealing with a thousands separator (see also locale module)
swap_separators = {ord('.'): ',', ord(','): '.'}
print(format(x, ',').translate(swap_separators))

# Formatting with the % operator
print('%0.2f' % x)
print('%10.1f' % x)
print('%-10.1f' % x)
