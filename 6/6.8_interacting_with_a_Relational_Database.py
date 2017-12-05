!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 23:25:13 2017

@author: david
"""

import sqlite3

"""
Problem
-------
You need to select, insert, or delete rows in a relational database.
"""

stocks = [
        ('GOOG', 100, 490.1),
        ('AAPL', 50, 545.75),
        ('FB', 150, 7.45),
        ('HPQ', 75, 33.2),
        ]

# Connect with the db
db = sqlite3.connect('database.db')
# First of all, you need to create a cursor
c = db.cursor()

# Do your stuff
c.execute('create table portfolio (symbol text, shares integer, price real)')
db.commit()

# Insert a sequence
c.executemany('insert into portfolio values (?,?,?)', stocks)
db.commit()

# Perform a query
for row in db.execute('select * from portfolio'):
    print(row)

# Query that accepts user input parameters
min_price = 100
for row in db.execute('select * from portfolio where price >= ?',
                      (min_price,)):
    print(row)
