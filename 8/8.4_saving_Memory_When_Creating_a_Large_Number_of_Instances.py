#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 22:26:15 2017

@author: david
"""

"""
Your program creates a large number (e.g., millions) of instances and uses a
large amount of memory.
"""


# When you define __slots__ , Python uses a much more compact internal
# representation for instances
class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
