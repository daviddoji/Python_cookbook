#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 19:51:32 2018

@author: david
"""

"""
You want an instance to delegate attribute access to an internally held
instance possibly as an alternative to inheritance or in order to implement
a proxy.
"""


# delegation is a programming pattern where the responsibility for
# implementing a particular operation is handed off (i.e., delegated) to a
# different object
class A:
    def spam(self, x):
        print('A.spam')

    def foo(self):
        print('A.foo')


class B:
    def __init__(self):
        self._a = A()

    def bar(self):
        print('B.bar')

    # Expose all of the methods defined on class A
    def __getattr__(self, name):
        return getattr(self._a, name)


b = B()
b.bar()  # Calls B.bar() (exists on B)
b.spam(42)  # Calls B.__getattr__('spam') and delegates to A.spam
b.foo()
print()


# A proxy class that wraps around another object, but
# exposes its public attributes
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

    # Delegate attribute deletion
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)


# wrap the class Proxy around another instance
class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)


# Create an instance
s = Spam(2)
# Create a proxy around it
p = Proxy(s)
# Access the proxy
print(p.x)     # Outputs 2
p.bar(3)       # Outputs "Spam.bar: 2 3"
p.x = 37       # Changes s.x to 37
print()


class ListLike:
    def __init__(self):
        self._items = []

    def __getattr__(self, name):
        return getattr(self._items, name)

    # Added special methods to support certain list operations
    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __delitem__(self, index):
        del self._items[index]


a = ListLike()
a.append(2)
a.insert(0, 1)
a.sort()
print(len(a))
print(a[0])
