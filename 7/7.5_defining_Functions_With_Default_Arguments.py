#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 07:32:33 2017

@author: david
"""

"""
You want to define a function or method where one or more of the arguments
are optional and have a default value.
"""


# (a) Dangers of using a mutable default argument
def spam(b=[]):
    return b


a = spam()
print(a)
a.append(1)
a.append(2)
b = spam()
print(b)       # Carefully observe result
print('-'*10)


# (b) Better alternative for mutable defaults
def spam(b=None):
    if b is None:
        b = []
    return b


a = spam()
print(a)
a.append(1)
a.append(2)
b = spam()
print(b)


def spam(a, b=None):
    if not b:
        # NO! Use 'b is None' instead
        b = []
    return b


c = spam(1)
print(c)
x = []
d = spam(1, x)  # Silent error. x value overwritten by default
print(d)
e = spam(1, 0)  # Silent error. 0 ignored
print(e)
f = spam(1, '')  # Silent error. '' ignored
print(f)
print('-'*10)


# (c) Example of testing if an argument was supplied or not
_no_value = object()


def spam(b=_no_value):
    if b is _no_value:
        print("No b value supplied")
    else:
        print("b =", b)


spam()
spam(None)
spam(0)
spam([])
print('-'*10)

# the values assigned as a default are bound only once at the time of function
# definition
x = 42


def spam(a, b=x):
    print(a, b)


spam(1)
x = 23
spam(1)  # Has no effect
