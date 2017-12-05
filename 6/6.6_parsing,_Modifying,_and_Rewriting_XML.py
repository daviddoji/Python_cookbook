#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 23:10:04 2017

@author: david
"""

from xml.etree.ElementTree import parse, Element

"""
Problem
-------
You want to read an XML document, make changes to it, and then write it back
out as XML.
"""

doc = parse('data/pred.xml')
root = doc.getroot()
print(root)
print()

# Remove a few elements
root.remove(root.find('sri'))
root.remove(root.find('cr'))

# Insert a new element after <nm>...</nm>
nm_index = root.getchildren().index(root.find('nm'))
print(nm_index)
print()

e = Element('spam')
e.text = 'This is a test'
root.insert(nm_index + 1, e)

# Write back to a file
doc.write('data/newpred.xml', xml_declaration=True)
