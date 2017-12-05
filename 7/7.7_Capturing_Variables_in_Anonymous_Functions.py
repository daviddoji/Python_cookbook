#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 22:48:10 2017

@author: david
"""

"""
You’ve defined an anonymous function using lambda , but you also need to
capture the values of certain variables at the time of definition.
"""

# the value of x used in the lambda expression is a free variable that gets
# bound at runtime, not definition time
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y

print(a(10))
print(b(10))

print()

# More examples
x = 15
print(a(10))
x = 3
print(a(10))

print()

# If you want an anonymous function to capture a value at the point of
# definition and keep it, include the value as a default value
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y

print(a(10))
print(b(10))

print()

# It will not remember the iteration variable at the time of definition
funcs = [lambda x: x+n for n in range(5)]
for f in funcs:
    print(f(0))

print()

# It will remember
funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0))
