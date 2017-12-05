#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:23:17 2017

@author: david
"""

import html
from xml.sax.saxutils import unescape

"""
Problem
-------
You want to replace HTML or XML entities such as &entity; or &#code; with
their corresponding text. Alternatively, you need to produce text, but escape
certain characters (e.g., < , > , or &).
"""

s = 'Elements are written as "<tag>text</tag>".'
print(s)
print(html.escape(s))

# Disable escaping of quotes
print(html.escape(s, quote=False))

s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

s = 'Spicy &quot;Jalape&#241;o&quot.'
print(html.unescape(s))

t = 'The prompt is &gt;&gt;&gt;'
print(unescape(t))
