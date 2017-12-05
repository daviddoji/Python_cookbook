#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 19:58:59 2017

@author: david
"""

from collections import namedtuple

"""
Problem
-------
You have code that accesses list or tuple elements by position, but this
makes the code somewhat difficult to read at times. You’d also like to be
less dependent on position in the structure, by accessing the elements by name.
"""

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

print(len(sub))
addr, joined = sub
print(addr)
print(joined)


Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


# Some Data
records = [('GOOG', 100, 490.1),
           ('ACME', 100, 123.45),
           ('IBM', 50, 91.15)
           ]

print(compute_cost(records))


s = Stock('ACME', 100, 123.45)
print(s)
s = s._replace(shares=75)
print(s)


Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)


# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))
