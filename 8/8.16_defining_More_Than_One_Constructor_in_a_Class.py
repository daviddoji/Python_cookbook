#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 20:18:28 2018

@author: david
"""

import time

"""
You’re writing a class, but you want users to be able to create instances in
more than the one way provided by __init__().
"""


class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(2012, 12, 21)
b = Date.today()
print(a.year, a.month, a.day)
print(b.year, b.month, b.day)


# It is extremely subtle, but this aspect of class methods makes them work
# correctly with features such as inheritance
class NewDate(Date):
    pass


c = Date.today()  # Creates an instance of Date (cls=Date)
d = NewDate.today()  # Creates an instance of NewDate (cls=NewDate)
print('Should be Date instance:', Date)
print('Should be NewDate instance:', NewDate)
