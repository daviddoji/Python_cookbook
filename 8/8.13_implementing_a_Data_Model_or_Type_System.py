#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:39:43 2017

@author: david
"""

"""
You want to define various kinds of data structures, but want to enforce
constraints on the values that are allowed to be assigned to certain
attributes.
"""


# Base class. Uses a descriptor to set a value
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        self.__dict__.update(opts)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


# Descriptor for enforcing types
class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)


# Descriptor for enforcing values
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        self.size = opts['size']
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super().__set__(instance, value)


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


# Class decorator to apply constraints
def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls
    return decorate

# A metaclass that applies checking
class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        # Attach attribute names to the descriptors
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)

# Testing code
def test(s):
    print(s.name)
    s.shares = 75
    print(s.shares)
    try:
        s.shares = -10
    except ValueError as e:
        print(e)
    try:
        s.price = 'a lot'
    except TypeError as e:
        print(e)

    try:
        s.name = 'ABRACADABRA'
    except ValueError as e:
        print(e)


# Various Examples:
print("# --- Class with descriptors")


class Stock:
    # Specify constraints
    name = SizedString('name', size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('ACME', 50, 91.1)
test(s)

print("# --- Class with class decorator")


@check_attributes(name=SizedString(size=8),
                  shares=UnsignedInteger,
                  price=UnsignedFloat)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('ACME', 50, 91.1)
test(s)

print("# --- Class with metaclass")


class Stock(metaclass=checkedmeta):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('ACME', 50, 91.1)
test(s)


## Base class. Uses a descriptor to set a value
#class Descriptor:
#    def __init__(self, name=None, **opts):
#        self.name = name
#        self.__dict__.update(opts)
#
#    def __set__(self, instance, value):
#        instance.__dict__[self.name] = value
#
#
#def Typed(expected_type, cls=None):
#    if cls is None:
#        return lambda cls: Typed(expected_type, cls)
#
#    super_set = cls.__set__
#
#    def __set__(self, instance, value):
#        if not isinstance(value, expected_type):
#            raise TypeError('expected ' + str(expected_type))
#        super_set(self, instance, value)
#    cls.__set__ = __set__
#    return cls
#
#
#def Unsigned(cls):
#    super_set = cls.__set__
#
#    def __set__(self, instance, value):
#        if value < 0:
#            raise ValueError('Expected >= 0')
#        super_set(self, instance, value)
#    cls.__set__ = __set__
#    return cls
#
#
#def MaxSized(cls):
#    super_init = cls.__init__
#
#    def __init__(self, name=None, **opts):
#        if 'size' not in opts:
#            raise TypeError('missing size option')
#        self.size = opts['size']
#        super_init(self, name, **opts)
#    cls.__init__ = __init__
#
#    super_set = cls.__set__
#
#    def __set__(self, instance, value):
#        if len(value) >= self.size:
#            raise ValueError('size must be < ' + str(self.size))
#        super_set(self, instance, value)
#    cls.__set__ = __set__
#    return cls
#
#
#@Typed(int)
#class Integer(Descriptor):
#    pass
#
#
#@Unsigned
#class UnsignedInteger(Integer):
#    pass
#
#
#@Typed(float)
#class Float(Descriptor):
#    pass
#
#
#@Unsigned
#class UnsignedFloat(Float):
#    pass
#
#
#@Typed(str)
#class String(Descriptor):
#    pass
#
#
#@MaxSized
#class SizedString(String):
#    pass
