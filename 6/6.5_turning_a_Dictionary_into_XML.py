#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 23:01:49 2017

@author: david
"""

from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring
from xml.sax.saxutils import escape, unescape

"""
Problem
-------
You want to take the data in a Python dictionary and turn it into XML.
"""


def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


# An example
s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
e = dict_to_xml('stock', s)
print(e)

print()

print(tostring(e))

print()

e.set('_id', '1234')
print(tostring(e))

print()

print(escape('<spam>'))
print(unescape(_))
