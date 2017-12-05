#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 15:22:31 2017

@author: david
"""

from struct import Struct
import struct
from collections import namedtuple
import numpy as np

"""
Problem
-------
You want to read or write data encoded as a binary array of uniform structures
into Python tuples.
"""


def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures.
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))


# Examples
records = [(1, 2.3, 4.5),
           (6, 7.8, 9.0),
           (12, 13.4, 56.7)]

with open('data/data.b', 'wb') as f:
    write_records(records, '<idd', f)

with open('data/data.b', 'rb') as f:
    for rec in read_records('<idd', f):
        # Process rec
        print(rec)

print()

with open('data/data.b', 'rb') as f:
    data = f.read()
    for rec in unpack_records('<idd', data):
        # Process record
        print(rec)

print()

record_struct = Struct('<idd')
print(record_struct.size)
packed = record_struct.pack(1, 2.0, 3.0)
print(packed)
print(record_struct.unpack(packed))

print()

# Sometimes  pack() and unpack() operations are called as module-level
# functions
lit_end = struct.pack('<idd', 1, 2.0, 3.0)
print(lit_end)
unpack_lit_end = struct.unpack('<idd', lit_end)
print(unpack_lit_end)

print()

f = open('data/data.b', 'rb')
chunks = iter(lambda: f.read(20), b'')
print(chunks)

for chk in chunks:
    print(chk)

print()

Record = namedtuple('Record', ['kind', 'x', 'y'])
with open('data/data.b', 'rb') as f:
    records = (Record(*r) for r in read_records('<idd', f))
#for r in records:
#    print(r.kind, r.x, r.y)

print()

f = open('data/data.b', 'rb')
records = np.fromfile(f, dtype='<i,<d,<d')
print(records)
print(records[0])
