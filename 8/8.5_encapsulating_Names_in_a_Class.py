#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 22:30:39 2017

@author: david
"""

"""
You want to encapsulate “private” data on instances of a class, but are
concerned about Python’s lack of access control.
"""


class A:
    def __init__(self):
        self._internal = 0  # An internal attribute
        self.public = 1     # A public attribute

    def public_method(self):
        '''
        A public method
        '''
#        ...

    def _internal_method(self):
        '''
        A public method
        '''
#        ...


class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        ...
        self.__private_method()
        ...


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1  # Does not override B.__private

    # Does not override B.__private_method()
    def __private_method(self):
        pass


# you may want to define a variable that clashes with the name of a
# reserved word
lambda_ = 2.0  # Trailing _ to avoid clash with lambda keyword
