#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 09:54:33 2017

@author: david
"""

from statistics import mean

"""
Problem
-------
You need to unpack N elements from an iterable, but the iterable may be longer
than N elements, causing a “too many values to unpack” exception.
"""


def drop_first_last(grades):
    first, *middle, last = grades
    return mean(middle)


user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
print(name)
print(phone_numbers)


*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)
trailing_avg = sum(trailing) / len(trailing)
print(trailing_avg)


records = [('foo', 1, 2),
           ('bar', 'hello'),
           ('foo', 3, 4, 5, 6, 'hi'),
           ]


def do_foo(*x):
    print('foo', x)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)


record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)


items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)


# clever recursive algorithm
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


print(sum(items))
