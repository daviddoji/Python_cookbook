#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 19:18:02 2017

@author: david
"""

import random

"""
Problem
-------
You want to pick random items out of a sequence or generate random numbers.
"""

values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))

print(random.sample(values, 3))
print(random.sample(values, 3))

random.shuffle(values)
print(values)
random.shuffle(values)
print(values)

print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))

print(random.random())
print(random.random())

print(random.getrandbits(200))
