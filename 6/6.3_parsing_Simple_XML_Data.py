#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 19:54:49 2017

@author: david
"""

from urllib.request import urlopen
#from xml.etree.ElementTree import parse
from lxml.etree import parse

"""
Problem
-------
You would like to extract data from a simple XML document.
"""

# Download the RSS feed and parse it
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)

# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)
    print()