#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 07:33:35 2017

@author: david
"""

"""
Problem
-------
You want to redirect the output of the print() function to a file.
"""

with open('data/sample2.txt', 'wt') as f:
    print('Hello World!', file=f)
