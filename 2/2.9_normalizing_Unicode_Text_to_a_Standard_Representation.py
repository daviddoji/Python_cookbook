#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 18:49:30 2017

@author: david
"""

import unicodedata

"""
Problem
-------
You’re working with Unicode strings, but need to make sure that all of the
strings have the same underlying representation.
"""

# Two strings
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

# (a) Print them out (usually looks identical)
print(s1)
print(s2)


# (b) Examine equality and length
print('s1 == s2', s1 == s2)
print(len(s1), len(s2))


# (c) Normalize and try the same experiment
# NFC means that characters should be fully composed
n_s1 = unicodedata.normalize('NFC', s1)
n_s2 = unicodedata.normalize('NFC', s2)

print('n_s1 == n_s2', n_s1 == n_s2)
print(len(n_s1), len(n_s2))
print(ascii(n_s1))

# NFD means that characters should be fully decomposed with the use of
# combining characters
n_s3 = unicodedata.normalize('NFD', s1)
n_s4 = unicodedata.normalize('NFD', s2)

print('n_s3 == n_s4', n_s3 == n_s4)
print(len(n_s3), len(n_s4))
print(ascii(n_s3))


s = '\ufb01'  # A single character
print(s)
print(unicodedata.normalize('NFD', s))
# Notice how the combined letters are broken apart here
print(unicodedata.normalize('NFKD', s))
print(unicodedata.normalize('NFKC', s))


# (d) Example of normalizing to a decomposed form and stripping accents
t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))
