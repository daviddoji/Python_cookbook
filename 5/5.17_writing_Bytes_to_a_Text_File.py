#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:28:56 2017

@author: david
"""

import sys

"""
Problem
-------
You want to write raw bytes to a file opened in text mode.
"""

# A byte string
data = b'Hello World\n'

# Write onto the buffer attribute (bypassing text encoding)
print(sys.stdout.write(data))
