#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 11:58:17 2017

@author: david
"""

"""
Problem
-------
You want to perform various calculations (e.g., minimum value, maximum value,
sorting, etc.) on a dictionary of data.
"""

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Find min and max price
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

# Be aware that zip() creates an iterator that can only be consumed once
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # (10.75, 'FB')
# print(max(prices_and_names))  # ValueError: max() arg is an empty sequence

print('min price:', min_price)
print('max price:', max_price)

print('sorted prices:')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
for price, name in prices_sorted:
    print('    ', name, price)

# Not what I want
print(min(prices))
print(max(prices))

# Getting closer, but not exactly what I want
print(min(prices.values()))
print(max(prices.values()))

# Almost there!
print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))

# Combining all together
min_value = prices[min(prices, key=lambda k: prices[k])]
max_value = prices[max(prices, key=lambda k: prices[k])]
print(min_value)
print(max_value)


prices = {'AAA': 45.23, 'ZZZ': 45.23}
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))
