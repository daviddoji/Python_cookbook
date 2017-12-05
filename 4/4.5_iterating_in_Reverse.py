#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 20:00:51 2017

@author: david
"""

"""
Problem
-------
You want to iterate in reverse over a sequence.
"""

a = [1, 2, 3, 4]
# Built-in reversed()
for x in reversed(a):
    print(x)

print()

# Print a file backwards
# Be aware that turning an iterable into a list as shown could consume a lot
# of memory if it’s large.
#f = open('somefile')
#for line in reversed(list(f)):
#    print(line, end='')


# Defining a reversed iterator makes the code much more efficient, as it’s no
# longer necessary to pull the data into a list and iterate in reverse on the
# list.
class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


c = Countdown(5)
print("Forward:")
for x in c:
    print(x)

print("Reverse:")
for x in reversed(c):
    print(x)
