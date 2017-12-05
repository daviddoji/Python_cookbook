#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 11:11:35 2017

@author: david
"""

import heapq

"""
Problem
-------
You want to implement a queue that sorts items by a given priority and always
returns the item with the highest priority on each pop operation.
"""


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # to get the queue to sort items from highest to lowest
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# Example use
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print("Should be bar:", q.pop())
print("Should be spam:", q.pop())
print("Should be foo:", q.pop())
print("Should be grok:", q.pop())


a = Item('foo')
b = Item('bar')
# print(a < b)
# TypeError: '<' not supported between instances of 'Item' and 'Item'

a = (1, Item('foo'))
b = (5, Item('bar'))
print(a < b)  # True

a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
print(a < b)  # True
print(a < c)  # True
