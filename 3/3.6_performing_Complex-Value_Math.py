#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 07:31:44 2017

@author: david
"""

import cmath
import numpy as np
import math

"""
Problem
-------
Your code for interacting with the latest web authentication scheme has
encountered a singularity and your only solution is to go around it in the
complex plane. Or maybe you just need to perform some calculations using
complex numbers.
"""

a = complex(2, 4)
b = 3 - 5j
print(a)
print(b)

print(a.real)
print(a.imag)
print(a.conjugate)

print(a + b)
print(a * b)
print(a / b)
print(abs(a))

print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
print(a + 2)
print(np.sin(a))

#print(math.sqrt(-1))  # ValueError: math domain error
print(cmath.sqrt(-1))
