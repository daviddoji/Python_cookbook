#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 20:36:08 2017

@author: david
"""

from operator import attrgetter

"""
Problem
-------
You want to sort objects of the same class, but they don’t natively support
comparison operations.
"""


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
print(users)

# Sort it by user-id
print(sorted(users, key=attrgetter('user_id')))

print(min(users, key=attrgetter('user_id')))

print(max(users, key=attrgetter('user_id')))
