#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 19:52:51 2017

@author: david
"""

import sys

"""
Problem
-------
You want to create a string in which embedded variable names are substituted
with a string representation of a variable’s value.
"""

s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))

name = 'Guido'
n = 37
print(s.format_map(vars()))


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


# (a) Simple substitution
a = Info('Guido', 37)
print(s.format_map(vars(a)))


# print(s.format(name='Guido'))
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# KeyError: 'n'

class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


# (b) Safe substitution with missing values
del n
print(s.format_map(safesub(vars())))


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


# (c) Safe substitution + frame hack
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))
