#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 19:23:16 2017

@author: david
"""

import unicodedata
import sys

"""
Problem
-------
Some bored script kiddie has entered the text “pýtĥöñ” into a form on your
web page and you’d like to clean it up somehow.
"""

# A tricky string
s = 'p\xfdt\u0125\xf6\xf1\x0cis\tawesome\r\n'
print(s)

# (a) Remapping whitespace
remap = {ord('\t'): ' ',
         ord('\f'): ' ',
         ord('\r'): None      # Deleted
         }

a = s.translate(remap)
print('whitespace remapped:', a)

# (b) Remove all combining characters/marks
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
c = b.translate(cmb_chrs)
print('accents removed:', c)


digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}
print(len(digitmap))
# Arabic digits
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))


# (c) Accent removal using I/O decoding
d = b.encode('ascii', 'ignore').decode('ascii')
print('accents removed via I/O:', d)


# Clean up white spaces
def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s
