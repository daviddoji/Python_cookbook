#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 20:49:49 2017

@author: david
"""

import os

"""
Problem
-------
You want to write data to a file, but only if it doesn’t already exist on
the filesystem.
"""

if not os.path.exists('data/somefile'):
    with open('data/somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')

# x mode to open()
#with open('somefile', 'xt') as f:
#    f.write('Hello\n')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#FileExistsError: [Errno 17] File exists: 'somefile'
