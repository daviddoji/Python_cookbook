#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 23:18:01 2017

@author: david
"""

from collections import deque

"""
Problem
-------
You would like to define a generator function, but it involves extra state
that you would like to expose to the user somehow.
"""


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('somefile.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')

print()

f = open('somefile.txt')
lines = linehistory(f)
# Call iter() first, then start iterating
it = iter(lines)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
