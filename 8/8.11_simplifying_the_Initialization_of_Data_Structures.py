#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 22:00:28 2017

@author: david
"""

import math

"""
You are writing a lot of classes that serve as data structures, but you are
getting tired of writing highly repetitive and boilerplate __init__()
functions.
"""


class Structure:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


# Example class definitions
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    class Point(Structure):
        _fields = ['x', 'y']

    class Circle(Structure):
        _fields = ['radius']

        def area(self):
            return math.pi * self.radius ** 2


s = Stock('ACME', 50, 91.1)
print(s.name, s.shares, s.price)
p = Point(2, 3)
print(p.x, p.y)
c = Circle(4.5)
print(c.radius)
try:
    s2 = Stock('ACME', 50)
except TypeError as e:
    print(e)
print()


# map the keyword arguments so that they only correspond to the attribute
# names specified in _fields
class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


# Example use
class Stock(Structure):
    _fields = ['name', 'shares', 'price']


s1 = Stock('ACME', 50, 91.1)
s2 = Stock('ACME', 50, price=91.1)
s3 = Stock('ACME', shares=50, price=91.1)
print(s1.name, s1.shares, s1.price)
print(s2.name, s2.shares, s2.price)
print(s3.name, s3.shares, s3.price)
print()


# use keyword arguments as a means for adding additional
# attributes to the structure not specified in _fields
class Structure:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the additional arguments (if any)
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))


# Example use
class Stock(Structure):
    _fields = ['name', 'shares', 'price']


s1 = Stock('ACME', 50, 91.1)
s2 = Stock('ACME', 50, 91.1, date='8/2/2012')
print(s1.name, s1.shares, s1.price)
print(s2.name, s2.shares, s2.price, s2.date)
