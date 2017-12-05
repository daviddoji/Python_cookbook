#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 16:37:32 2017

@author: david
"""

import pandas as pd
"""
You need to crunch through large datasets and generate summaries or other
kinds of statistics.
"""

# Read a CSV file, skipping last line
rats = pd.read_csv('data/rats.csv', skipfooter=1)

# Investigate range of values for a certain field
print(rats['Current Activity'].unique())

print()

# Filter the data
crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
print(len(crew_dispatched))

print()

# Find 10 most rat-infested ZIP codes in Chicago
print(crew_dispatched['ZIP Code'].value_counts().head(10))

print()

# Group by completion date
dates = crew_dispatched.groupby('Completion Date')
print(len(dates))

print()

# Determine counts on each day
date_counts = dates.size()
print(date_counts[0:10])

print()

# Sort the counts
print(sorted(date_counts)[-10:])
