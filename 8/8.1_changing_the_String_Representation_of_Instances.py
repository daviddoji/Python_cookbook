#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 19:47:35 2017

@author: david
"""

"""
You want to change the output produced by printing or viewing instances to
something more sensible.
"""


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
#        return 'Pair(%r, %r)' % (self.x, self.y)
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x}, {0.y})'.format(self)


# Example of use
p = Pair(3, 4)
# p
# Pair(3, 4)  # __repr__() output
print(p)  # __repr__() output
print()
print('p is {0!r}'.format(p))
print('p is {0}'.format(p))
