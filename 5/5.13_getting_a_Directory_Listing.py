#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:47:18 2017

@author: david
"""

import os
import os.path
import glob
from fnmatch import fnmatch

"""
Problem
-------
You want to get a list of the files contained in a directory on the filesystem.
"""

pyfiles = glob.glob('*.py')
# pyfiles = [name for name in os.listdir('.') if fnmatch(name, '*.py')]

# Get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]

for r in name_sz_date:
    print(r)

# Get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
