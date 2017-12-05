#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 20:15:43 2017

@author: david
"""

from collections import Counter

"""
Problem
-------
You have a sequence of items, and you’d like to determine the most
frequently occurring items in the sequence.
"""


words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
         'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
         'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
         'my', 'eyes', "you're", 'under'
         ]

word_counts = Counter(words)
print(word_counts['not'])
print(word_counts['eyes'])
top_three = word_counts.most_common(3)
print(top_three)


morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
word_counts.update(morewords)
print(word_counts.most_common(3))


a = Counter(words)
b = Counter(morewords)
c = a + b
print(c)
d = a - b
print(d)
