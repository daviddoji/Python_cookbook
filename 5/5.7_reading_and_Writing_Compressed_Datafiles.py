#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 21:03:59 2017

@author: david
"""

import gzip
import bz2

"""
Problem
-------
You need to read or write data in a file with gzip or bz2 compression.
"""

# to read compressed files as text
# gzip compression
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

# bz2 compression
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()


# to write compressed data
# gzip compression
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

# bz2 compression
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)


# specify the compression level, default is 9(highest level of compression)
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)


# they can be layered on top of an existing file opened in binary mode
f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()

# If you want to work with binary data instead, use a file mode of rb or wb
