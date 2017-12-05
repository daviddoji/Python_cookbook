#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 21:31:56 2017

@author: david
"""

"""
You want to invoke a method in a parent class in place of a method that has
been overridden in a subclass.
"""


# To call a method in a parent (or superclass), use the super() function
class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        super().spam()      # Call parent spam()


# Example
b = B()
b.spam()
print()


# the __init__() method makes sure that parents are properly initialized:
class A:
    def __init__(self):
        self.x = 0


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1


# Example
b = B()
print(b.x, b.y)
print()


# Another common use of super() is in code that overrides any of Python’s
# special methods
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)    # Call original __setattr__
        else:
            setattr(self._obj, name, value)


class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        print('A.spam')


a = A(42)
p = Proxy(a)
print(p.x)
print(p.spam())
p.x = 37
print('Should be 37:', p.x)
print('Should be 37:', a.x)
print()


# Tricky initialization problem involving multiple inheritance.
# Does NOT use super()
class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')


class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')


# Please observe double call of Base.__init__
c = C()
print()


# Tricky initialization problem involving multiple inheritance.
# Uses super()
class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(A, B):
    def __init__(self):
        super().__init__()     # Only one call to super() here
        print('C.__init__')


# Observe that each class initialized only once
c = C()
print()

# Python method resolution order (MRO)
print(C.__mro__)
