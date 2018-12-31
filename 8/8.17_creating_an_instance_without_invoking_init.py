#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 16:25:20 2018

@author: david
"""

from time import localtime

"""
You need to create an instance, but want to bypass the execution of the
__init__() method for some reason.
"""


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Class method that bypasses __init__
    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


# Here’s how you can create a Date instance without invoking __init__():
d = Date.__new__(Date)
print(d)
# the resulting instance is uninitialized
print(hasattr(d, 'year'))


data = {
        'year': 2012,
        'month': 8,
        'day': 29
        }
# to set the appropriate instance variables
d.__dict__.update(data)
print(d.year)
print(d.month)

d = Date.today()
print(d.year, d.month, d.day)
