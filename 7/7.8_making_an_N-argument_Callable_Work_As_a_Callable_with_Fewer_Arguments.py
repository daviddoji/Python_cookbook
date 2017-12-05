#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 22:58:29 2017

@author: david
"""

from functools import partial
import math
import logging
from multiprocessing import Pool
from socketserver import StreamRequestHandler, TCPServer

"""
You have a callable that you would like to use with some other Python code,
possibly as a callback function or handler, but it takes too many arguments
and causes an exception when called.
"""


def spam(a, b, c, d):
    print(a, b, c, d)


s1 = partial(spam, 1)  # a = 1
s1(2, 3, 4)
s1(4, 5, 6)
s2 = partial(spam, d=42)  # d = 42
s2(1, 2, 3)
s2(4, 5, 5)
s3 = partial(spam, 1, 2, d=42)  # a= 1, b = 2, d = 42
s3(3)
s3(4)
s3(5)

print()

# Example of using partial() with sorting a list of (x,y) coordinates
points = [(1, 2), (3, 4), (5, 6), (7, 8)]


# suppose you want to sort all of the points according to their distance from
# some other point. The sort() method of lists accepts a key argument that
# can be used to customize sorting, but it only works with functions that
# take a single argument (thus, distance() is not suitable)
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


pt = (4, 3)
points.sort(key=partial(distance, pt))
print(points)

print()


# Using partial to supply extra arguments to a callback function
def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)


# A sample function
def add(x, y):
    return x + y


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('test')

p = Pool()
p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
p.close()
p.join()


print()


# Using partial to supply extra arguments to a class constructor
class EchoHandler(StreamRequestHandler):
    # ack is added keyword-only argument. *args, **kwargs are
    # any normal parameters supplied (which are passed on)
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)


serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
print('Echo server running on port 15000')
serv.serve_forever()
