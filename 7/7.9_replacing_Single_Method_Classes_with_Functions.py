#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 18:21:17 2017

@author: david
"""

from urllib.request import urlopen

"""
You have a class that only defines a single method besides __init__().
However, to simplify your code, you would much rather just have a simple
function.
"""

# In many cases, single-method classes can be turned into functions using
# closures


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


# Example use. Download stock data from yahoo
url = 'http://finance.yahoo.com/quote/{names}&p={fields}'
yahoo = UrlTemplate(url)
for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))


# It could be replaced by the following function
def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener


# Example use
url = 'http://finance.yahoo.com/quote/{names}&p={fields}'
yahoo = urltemplate(url)
for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))

# Whenever you’re writing code and you encounter the problem of attaching 
# additional state to a function, think closures. They are often a more
# minimal and elegant solution than the alternative of turning your function
# into a full-fledged class.
