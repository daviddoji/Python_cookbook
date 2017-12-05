#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 07:10:35 2017

@author: david
"""

"""
You want a function to only accept certain arguments by keyword.
"""


# A simple keyword-only argument
def recv(maxsize, *, block=True):
    print(maxsize, block)


print(recv(8192, block=False))        # Works
try:
    print(recv(8192, False))          # Fails
except TypeError as e:
    print(e)


# Adding keyword-only args to *args functions
def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


print(minimum(1, 5, 2, -5, 10))
print(minimum(1, 5, 2, -5, 10, clip=0))
