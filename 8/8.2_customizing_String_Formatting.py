#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 19:56:09 2017

@author: david
"""

from datetime import date

"""
You want an object to support customized formatting through the format()
function and string method.
"""

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
    }


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


# Use case
d = Date(2012, 12, 21)
print(format(d))
print('The date is {:ymd}'.format(d))
print('The date is {:mdy}'.format(d))
print('The date is {:dmy}'.format(d))
print()

d = date(2012, 12, 21)
print(format(d))
print(format(d, '%A, %B %d, %Y'))
print('The end is {:%d %b %Y}. Goodbye'.format(d))

# https://docs.python.org/3/library/string.html
