#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:45:56 2017

@author: david
"""

from tempfile import TemporaryFile
from tempfile import NamedTemporaryFile
from tempfile import TemporaryDirectory
import tempfile

"""
Problem
-------
You need to create a temporary file or directory for use when your program
executes. Afterward, you possibly want the file or directory to be destroyed.
"""

with TemporaryFile('w+t') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')

    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()

    # Temporary file is destroyed


with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)
# Avoid file to be deleted when it's closed
#with NamedTemporaryFile('w+t', delete=False) as f:
#    print('filename is:', f.name)


with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)
    # Use the directory

# Directory and all contents destroyed

# At a lower level, use this
print(tempfile.mkstemp())
print(tempfile.mkdtemp())
# Where are temp files/directories created?
print(tempfile.gettempdir())

# Naming conventions
f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')
print(f.name)
