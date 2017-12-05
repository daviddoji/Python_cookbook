#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:59:47 2017

@author: david
"""

import pickle
import math
import time
import threading


"""
Problem
-------
You need to serialize a Python object into a byte stream so that you can do
things such as save it to a file, store it in a database, or transmit it
over a network connection.
"""


#data = ... # Some Python object
#f = open('somefile', 'wb')
#pickle.dump(data, f)
#
## To dump an object to a string
#s = pickle.dumps(data)
#
## Restore from a file
#f = open('somefile', 'rb')
#data = pickle.load(f)
## Restore from a string
#data = pickle.loads(s)

# An example
f = open('data/somedata', 'wb')
pickle.dump([1, 2, 3, 4], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()
f = open('data/somedata', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))

# You can pickle functions, classes, and instances, but the resulting data
# only encodes name references to the associated code objects
print(pickle.dumps(math.cos))


# countdown.py
class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)


c = Countdown(30)

# After a few moments
f = open('data/cstate.p', 'wb')
pickle.dump(c, f)
f.close()

# Now quit Python and try this after restart:
f = open('data/cstate.p', 'rb')
pickle.load(f)
