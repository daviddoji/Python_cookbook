#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 06:51:05 2017

@author: david
"""

from decimal import Decimal
from decimal import localcontext
import math

"""
Problem
-------
You need to perform accurate calculations with decimal numbers, and don’t
want the small errors that naturally occur with floats.
"""

a = 4.2
b = 2.1
print(a + b)
print((a + b) == 6.3)

print()

a = Decimal('4.2')
b = Decimal('2.1')
print((a + b) == Decimal('6.3'))

print()

a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

print()

nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))  # Notice how 1 disappears
print(math.fsum(nums))

print()
