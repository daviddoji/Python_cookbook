#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 21:54:07 2017

@author: david
"""

import sys

"""
Problem
-------
You have code that uses a while loop to iteratively process data because it
involves a function or some kind of unusual test condition that doesn’t fall
into the usual iteration pattern.
"""

CHUNKSIZE = 8192


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)


#def reader(s):
#    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
#        process_data(data)

f = open('/etc/passwd')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)
