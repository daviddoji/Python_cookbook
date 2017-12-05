#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 21:47:47 2017

@author: david
"""

"""
Within a subclass, you want to extend the functionality of a property
defined in a parent class.
"""


# Example of managed attributes via properties
class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


class SubPerson2(Person):
    @Person.name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson2, SubPerson2).name.__set__(self, value)


class SubPerson3(Person):
#    @property
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name


s = SubPerson('Guido')
print(s.name)
s.name = 'Larry'
# s.name = 42
# TypeError: Expected a string
a = Person('Guido')
print(a.name)
a.name = 'Dave'
print(a.name)
try:
    a.name = 42
except TypeError as e:
    print(e)
print()


# Example of managed attributes via properties
# A descriptor
class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value


# A class with a descriptor
class Person:
    name = String('name')

    def __init__(self, name):
        self.name = name


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


a = Person('Guido')
print(a.name)
a.name = 'Dave'
print(a.name)
try:
    a.name = 42
except TypeError as e:
    print(e)
