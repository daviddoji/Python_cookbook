#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 20:20:17 2017

@author: david
"""

from collections import ChainMap

"""
Problem
-------
You have multiple dictionaries or mappings that you want to logically combine
into a single mapping to perform certain operations, such as looking up values
or checking for the existence of keys.
"""

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# Simple example of combining
c = ChainMap(a, b)
print(c['x'])      # Outputs 1  (from a)
print(c['y'])      # Outputs 2  (from b)
print(c['z'])      # Outputs 3  (from a)

# Output some common values
print('len(c):', len(c))
print('c.keys():', list(c.keys()))
print('c.values():', list(c.values()))


# Modify some values will affect the first mapping listed
c['z'] = 10
c['w'] = 40
del c['x']
print("a:", a)


# Example of stacking mappings (like scopes)
values = ChainMap()
values['x'] = 1

# Add a new mapping
values = values.new_child()
values['x'] = 2

# Add a new mapping
values = values.new_child()
values['x'] = 3

print(values)
print(values['x'])

# Discard last mapping
values = values.parents
print(values)
print(values['x'])

# Discard last mapping
values = values.parents
print(values)
print(values['x'])


# Alternative to ChainMap: merging dictionaries together using update()
print('\nUsing update()')
a = {'x': 100, 'z': 300}
b = {'y': 200, 'z': 400}
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])

a['x'] = 130
print(merged['x'])

print('\nUsing ChainMap')
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
print(merged['x'])
a['x'] = 42
print(merged['x'])
