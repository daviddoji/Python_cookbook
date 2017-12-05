#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 22:02:10 2017

@author: david
"""

import sys

"""
Problem
-------
Your program received a directory listing, but when it tried to print the
filenames, it crashed with a UnicodeEncodeError exception and a cryptic
message about “surrogates not allowed.
"""


# When printing filenames of unknown origin
def bad_filename(filename):
    return repr(filename)[1:-1]
    try:
        print(filename)
    except UnicodeEncodeError:
        print(bad_filename(filename))


def bad_filename(filename):
    temp = filename.encode(sys.getfilesystemencoding(), 
                           errors='surrogateescape')
    return temp.decode('latin-1')


for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))
