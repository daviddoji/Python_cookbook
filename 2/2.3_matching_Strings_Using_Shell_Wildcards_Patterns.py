#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 21:01:01 2017

@author: david
"""

from fnmatch import fnmatch, fnmatchcase

"""
Problem
-------
You want to match text using the same wildcard patterns as are commonly used
when working in Unix shells (e.g., *.py , Dat[0-9]*.csv , etc.).
"""

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])


print(fnmatchcase('foo.txt', '*.TXT'))

addresses = ['5412 N CLARK ST',
             '1060 W ADDISON ST',
             '1039 W GRANVILLE AVE',
             '2122 N CLARK ST',
             '4802 N BROADWAY',
             ]

a = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(a)

b = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(b)
