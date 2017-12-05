#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 16:53:34 2017

@author: david
"""

import html

"""
You want to write a function that accepts any number of input arguments.
"""


# function that accepts any number of positional arguments
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


# Sample use
print(avg(1, 2))
print(avg(1, 2, 3, 4))

print()


# function that accepts any number of keyword arguments
def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                  name=name,
                  attrs=attr_str,
                  value=html.escape(value))
    return element


# Sample use
# Creates '<item size="large" quantity="6">Albatross</item>'
print(make_element('item', 'Albatross', size='large', quantity=6))
# Creates '<p>&lt;spam&gt;</p>'
print(make_element('p', '<spam>'))


# function that accepts any number of arguments
def anyargs(*args, **kwargs):
    print(args)  # A tuple
    print(kwargs)  # A dict


# Arguments don't need to be at the end
def a(x, *args, y):
    pass


def b(x, *args, y, **kwargs):
    pass
