#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 21:15:06 2017

@author: david
"""

import os.path

"""
Problem
-------
You want to read binary data directly into a mutable buffer without any
intermediate copying. Perhaps you want to mutate the data in-place and write
it back out to a file.
"""


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


# Write a sample file
with open('data/sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('data/sample.bin')
print(buf)

buf[0:5] = b'Hallo'
print(buf)

with open('data/newsample.bin', 'wb') as f:
    f.write(buf)


record_size = 32  # Size of each record (adjust value)
buf = bytearray(record_size)
with open('data/somefile', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break
        # Use the contents of buf

print(buf)
m1 = memoryview(buf)
m2 = m1[-5:]
print(m2)
m2[:] = b'WORLD'
print(buf)
