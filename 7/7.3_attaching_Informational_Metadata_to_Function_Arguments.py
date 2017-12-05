#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 07:20:33 2017

@author: david
"""

"""
You’ve written a function, but would like to attach some additional information
to the arguments so that others know more about how a function is supposed to
be used.
"""


def add(x: int, y: int) -> int:
    return x + y


help(add)

print(add.__annotations__)
