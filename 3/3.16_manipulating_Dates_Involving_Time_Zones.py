#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 07:31:22 2017

@author: david
"""

from datetime import datetime
from datetime import timedelta
from pytz import timezone
import pytz

"""
Problem
-------
You had a conference call scheduled for December 21, 2012, at 9:30 a.m. in
Chicago. At what local time did your friend in Bangalore, India, have to show
up to attend?
"""

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

# Localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

# Convert to Bangalore time
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

print()

# Be aware of daylight saving transitions
d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes=30)
print(later)  # WRONG! WRONG!
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)  # That's CORRECT!

print()

# Common way to deal with times is to convert to UTC time
print(loc_d)
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)
later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))

print()

# consult the pytz.country_timezones dictionary using the ISO 3166 country
# code as a key
print(pytz.country_timezones['IN'])
