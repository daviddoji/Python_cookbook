#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 16:37:01 2018

@author: david
"""

from collections import defaultdict, OrderedDict

"""
You have a collection of generally useful methods that you would like to make
available for extending the functionality of other class definitions. However,
the classes where the methods might be added aren’t necessarily related to one
another via inheritance. Thus, you can’t just attach the methods to a common
base class.
"""


# Useless classes by themselves
class LoggedMappingMixin:
    '''
    Add logging to get/set/delete operations for debugging.
    '''
    __slots__ = ()

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)


class SetOnceMappingMixin:
    '''
    Only allow a key to be set once.
    '''
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class StringKeysMappingMixin:
    '''
    Restrict keys to strings only
    '''
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings')
        return super().__setitem__(key, value)


# Examples
print('# ---- LoggedDict Example')


# But if they are mixed with other mapping clases through multiple inheritance
class LoggedDict(LoggedMappingMixin, dict):
    pass


d = LoggedDict()
d['x'] = 23
print(d['x'])
del d['x']


print('\n# ---- SetOnceDefaultDict Example')


class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass


d = SetOnceDefaultDict(list)
d['x'].append(2)
d['y'].append(3)
d['x'].append(10)
try:
    d['x'] = 23
except KeyError as e:
    print(e)

print('\n# ---- StringOrderedDict Example')


class StringOrderedDict(StringKeysMappingMixin,
                        SetOnceMappingMixin,
                        OrderedDict):
    pass


d = StringOrderedDict()
d['x'] = 23
try:
    d[42] = 10
except TypeError as e:
    print(e)

try:
    d['x'] = 42
except KeyError as e:
    print(e)


# Here is one possible implementation of a mixin defining an __init__()
# and accepting a keyword argument:
class RestrictKeysMixin:
    def __init__(self, *args, _restrict_key_type, **kwargs):
        self.__restrict_key_type = _restrict_key_type
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if not isinstance(key, self.__restrict_key_type):
            raise TypeError('Keys must be ' + str(self.__restrict_key_type))
        super().__setitem__(key, value)


# Example
class RDict(RestrictKeysMixin, dict):
    pass


d = RDict(_restrict_key_type=str)
e = RDict([('name', 'Dave'), ('n', 37)], _restrict_key_type=str)
f = RDict(name='Dave', n=37, _restrict_key_type=str)
print()
print(f)
try:
    f[42] = 10
except TypeError as e:
    print(e)


# Class decorator alternative to mixins
def LoggedMapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, key):
        print('Getting %s' % key)
        return cls_getitem(self, key)

    def __setitem__(self, key, value):
        print('Setting %s = %r' % (key, value))
        return cls_setitem(self, key, value)

    def __delitem__(self, key):
        print('Deleting %s' % key)
        return cls_delitem(self, key)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls


# This function is applied as a decorator to a class definition
@LoggedMapping
class LoggedDict(dict):
    pass


d = LoggedDict()
d['x'] = 23
print()
print(d['x'])
del d['x']
