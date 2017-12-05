#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 22:40:33 2017

@author: david
"""

import math

"""
You want to add extra processing (e.g., type checking or validation) to the
getting or setting of an instance attribute.
"""


# Example of managed attributes via properties
class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


a = Person('Guido')
print(a.first_name)  # Calls the getter
a.first_name = 'Dave'
print(a.first_name)
try:
    a.first_name = 42  # Calls the setter
except TypeError as e:
    print(e)
#del a.first_name
# AttributeError: Can't delete attribute
print()


# Properties can also be defined for existing get and set methods
class Person2:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name

    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)


p = Person2('Guido')
print(p.get_first_name())
p.set_first_name('Larry')
print(p.get_first_name())
print()


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(4.0)
print(c.radius)
print(c.area)  # Notice lack of ()
print(c.perimeter)  # Notice lack of ()
