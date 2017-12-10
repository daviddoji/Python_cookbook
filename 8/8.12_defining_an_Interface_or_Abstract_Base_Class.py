#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 23:26:47 2017

@author: david
"""

from abc import ABCMeta, abstractmethod
import sys
import io
import collections

"""
You want to define a class that serves as an interface or abstract base class
from which you can perform type checking and ensure that certain methods are
implemented in subclasses.
"""


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


# Example implementation
class SocketStream(IStream):
    def read(self, maxbytes=-1):
        print('reading')

    def write(self, data):
        print('writing')


# Example of type checking
def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    print('serializing')


# Examples
# Attempt to instantiate ABC directly (doesn't work)
try:
    a = IStream()
except TypeError as e:
    print(e)

# Instantiation of a concrete implementation
a = SocketStream()
a.read()
a.write('data')

# Passing to type-check function
serialize(None, a)


# Attempt to pass a file-like object to serialize (fails)
try:
    serialize(None, sys.stdout)
except TypeError as e:
    print(e)

# Register file streams and retry
IStream.register(io.IOBase)
serialize(None, sys.stdout)
print()


class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass


x = list([1, 2, 3])
# Check if x is a sequence
print(isinstance(x, collections.Sequence))
# Check if x is iterable
print(isinstance(x, collections.Iterable))
# Check if x has a size
print(isinstance(x, collections.Sized))
# Check if x is a mapping
print(isinstance(x, collections.Mapping))
