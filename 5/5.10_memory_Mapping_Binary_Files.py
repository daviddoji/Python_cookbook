#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:37:55 2017

@author: david
"""

import os
import mmap

"""
Problem
-------
You want to memory map a binary file into a mutable byte array, possibly for
random access to its contents or to make in-place modifications.
"""


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


# initially create a file and expand it to a desired size:
size = 1000000
with open('data/data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

# example of memory mapping
m = memory_map('data/data')
print(len(m))
print(m[0:10])
print(m[0])
# Reassign a slice
m[0:11] = b'Hello World'
m.close()

# Verify that changes were made
with open('data/data', 'rb') as f:
    print(f.read(11))


with memory_map('data/data') as m:
    print(len(m))
    print(m[0:11])

print(m.closed)

#If read-only access is needed
#m = memory_map(filename, mmap.ACCESS_READ)
# If you intend to modify the data locally, but don’t want those changes
# written back to the original file
#m = memory_map(filename, mmap.ACCESS_COPY)

m = memory_map('data/data')
# Memoryview of unsigned integers
v = memoryview(m).cast('I')
v[0] = 7
print(m[0:4])
m[0:4] = b'\x07\x01\x00\x00'
print(v[0])
