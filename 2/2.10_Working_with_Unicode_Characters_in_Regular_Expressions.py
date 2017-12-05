#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 19:06:29 2017

@author: david
"""

import re

"""
Problem
-------
You are using regular expressions to process text, but are concerned about
the handling of Unicode characters.
"""

num = re.compile('\d+')
# ASCII digits
print(num.match('123'))
# Arabic digits
print(num.match('\u0661\u0662\u0663'))
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
print(arabic)

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s))  # Matches
print(pat.match(s.upper()))  # Doesn't match
print(s.upper())  # Case folds
