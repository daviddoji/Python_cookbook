#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 19:19:25 2017

@author: david
"""

import json
from collections import OrderedDict
from urllib.request import urlopen
from pprint import pprint

"""
Problem
-------
You want to read or write data encoded as JSON (JavaScript Object Notation).
"""

# Some JSON encoded text
s = '{"name": "ACME", "shares": 50, "price": 490.1}'

# turn a Python data structure into JSON
json_str = json.dumps(s)
print(json_str)
json_str_indented = json.dumps(s, indent=4)
print(json_str_indented)
json_str_sorted = json.dumps(s, sort_keys=True)
print(json_str_sorted)

# turn a JSON-encoded string into a data structure
data = json.loads(json_str)
print(data)

# If you are working with files instead of strings
# Writing JSON data
with open('data/data.json', 'w') as f:
    json.dump(data, f)
# Reading data back
with open('data/data.json', 'r') as f:
    data = json.load(f)


# Discrepancies between JSON and Python encoding
json.dumps(False)
d = {'a': True,
     'b': 'Hello',
     'c': None}
json.dumps(d)


## Decode from JSON using pprint
#u = urlopen('https://api.twitter.com/1.1/statuses/user_timeline.json')
#resp = json.loads(u.read().decode('utf-8'))
#pprint(resp)


# (a) Turning JSON into an OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)

print()


# (b) Using JSON to populate an instance
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


data = json.loads(s, object_hook=JSONObject)
print(data.name)
print(data.shares)
print(data.price)

print()


# (c) Encoding instances
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Instances are not normally serializable as JSON
def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


p = Point(3, 4)
s = json.dumps(p, default=serialize_instance)
print(s)

print()


# (d) Decoding instances
classes = {'Point': Point}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d


a = json.loads(s, object_hook=unserialize_object)
print(a)
print(a.x)
print(a.y)
