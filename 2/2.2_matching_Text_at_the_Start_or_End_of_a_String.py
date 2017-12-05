#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 20:46:08 2017

@author: david
"""

import os
from urllib.request import urlopen
import re

"""
Problem
-------
You need to check the start or end of a string for specific text patterns,
such as filename extensions, URL schemes, and so on.
"""

filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))


filenames = os.listdir('.')
print(filenames)
print([name for name in filenames if name.endswith(('.py', '.h'))])
print(any(name.endswith('.py') for name in filenames))


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


choices = ['http:', 'ftp:']
url = 'http://www.python.org'
print(url.startswith(tuple(choices)))


filename = 'spam.txt'
print(filename[-4:] == '.txt')
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

url = 'http://www.python.org'
print(re.match('http:|https:|ftp:', url))
