#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 18:47:58 2017

@author: david
"""

from queue import Queue
from functools import wraps
import multiprocessing

"""
You’re writing code that uses callback functions, but you’re concerned about
the proliferation of small functions and mind boggling control flow. You
would like some way to make the code look more like a normal sequence of
procedural steps.
"""


# Sample function to illustrate callback control flow
def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)
    # Invoke the callback with the result
    callback(result)


# Inlined callback implementation
class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper


# Sample use
def add(x, y):
    return x + y


@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')


# Simple test
print('# --- Simple test')
test()
print()
print('# --- Multiprocessing test')
pool = multiprocessing.Pool()
apply_async = pool.apply_async
test()
