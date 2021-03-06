#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 21:32:57 2017

@author: david
"""

"""
You want to create a new kind of instance attribute type with some extra
functionality, such as type checking.
"""


# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
print(p.x)  # Calls Point.x.__get__(p,Point)
p.y = 5  # Calls Point.y.__set__(p, 5)
try:
    p.x = 2.3  # Calls Point.y.__set__(p, 2.3)
except TypeError as e:
    print(e)
# If a descriptor is accessed as a class variable, the instance argument is
# set to None
print(Point.x)  # Calls Point.x.__get__(None, Point)
print()


# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate


# Example use
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('ACME', 100, 490.1)
print(s.name, s.shares, s.price)
s.shares = 50
try:
    s.shares = 'a lot'
except TypeError as e:
    print(e)
