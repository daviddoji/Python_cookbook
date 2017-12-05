#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 22:41:18 2017

@author: david
"""

"""
You need to supply a short callback function for use with an operation such
as sort(), but you don’t want to write a separate one-line function using
the def statement. Instead, you’d like a shortcut that allows you to specify
the function “in line.”
"""

add = lambda x, y: x + y
print(add(2, 3))
print(add("hello", "world"))


# the "lambda" expression is the same as having typed this
def add(x, y):
    return x + y


print(add(3, 4))


# Typically, lambda is used in the context of some other operation, such as
# sorting or a data reduction
names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))
