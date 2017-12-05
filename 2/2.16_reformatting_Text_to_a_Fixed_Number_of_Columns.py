#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:13:11 2017

@author: david
"""

import textwrap
import os

"""
Problem
-------
You have long strings that you want to reformat so that they fill a
user-specified number of columns.
"""

# A long string
s = "Look into my eyes, look into my eyes, the eyes, the eyes, the eyes, \
not around the eyes, don't look around the eyes, look into my eyes, \
you're under."

print(textwrap.fill(s, 70))
print()

print(textwrap.fill(s, 40))
print()

print(textwrap.fill(s, 40, initial_indent='    '))
print()

print(textwrap.fill(s, 40, subsequent_indent='    '))
print()

print(os.get_terminal_size().columns)
