#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:55:44 2017

@author: david
"""

import os
import time

"""
Problem
-------
You need to test whether or not a file or directory exists.
"""

print(os.path.exists('/etc/passwd'))
print(os.path.exists('/tmp/spam'))

# Is a regular file
print(os.path.isfile('/etc/passwd'))

# Is a directory
print(os.path.isdir('/etc/passwd'))

# Is a symbolic link
print(os.path.islink('/usr/local/bin/python3'))

# Get the file linked to
print(os.path.realpath('/usr/local/bin/python3'))

print(os.path.getsize('/etc/passwd'))
print(os.path.getmtime('/etc/passwd'))
print(time.ctime(os.path.getmtime('/etc/passwd')))

#File testing is a straightforward operation using os.path . Probably the only
#thing to be aware of when writing scripts is that you might need to worry
#about permissions—especially for operations that get metadata
