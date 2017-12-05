#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 07:23:02 2017

@author: david
"""

from datetime import datetime

"""
Problem
-------
Your application receives temporal data in string format, but you want to
convert those strings into datetime objects in order to perform nonstring
operations on them.
"""

text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)
#nice_diff = datetime.strftime(diff, '%A %B %d, %Y')
#print(nice_diff)
nice_z = datetime.strftime(z, '%A %d %B, %Y')
print(nice_z)


def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
