#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 10:53:04 2017

@author: david
"""

from collections import deque

"""
Problem
-------
You want to keep a limited history of the last few items seen during iteration
or during some other kind of processing.
"""

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)

q.append(4)
print(q)

q.append(5)
print(q)


q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)

q.appendleft(4)
print(q)

q.pop()
print(q)

q.popleft()
print(q)
