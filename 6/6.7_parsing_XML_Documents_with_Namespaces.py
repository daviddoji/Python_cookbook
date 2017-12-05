#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 23:17:16 2017

@author: david
"""

from xml.etree.ElementTree import parse
from xml.etree.ElementTree import iterparse

"""
Problem
-------
You need to parse an XML document, but it’s using XML namespaces.
"""


class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = '{'+uri+'}'

    def __call__(self, path):
        return path.format_map(self.namespaces)


doc = parse('data/sample.xml')
ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')

e = doc.find(ns('content/{html}html'))
print(e)

text = doc.findtext(ns('content/{html}html/{html}head/{html}title'))
print(text)

print()

# you can get a bit more information about the scope of namespace processing
# if you use the iterparse() function
for evt, elem in iterparse('data/sample.xml', ('end', 'start-ns', 'end-ns')):
    print(evt, elem)
