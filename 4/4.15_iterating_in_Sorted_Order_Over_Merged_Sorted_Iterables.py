#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 21:48:00 2017

@author: david
"""

import heapq

"""
Problem
-------
You have a collection of sorted sequences and you want to iterate over a
sorted sequence of them all merged together.
"""

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)


#with open('sorted_file_1', 'rt') as file1, \
#     open('sorted_file_2') 'rt' as file2, \
#     open('merged_file', 'wt') as outf:
#        for line in heapq.merge(file1, file2):
#             outf.write(line)
