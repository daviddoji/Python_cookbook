#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 11:50:20 2017

@author: david
"""

from collections import OrderedDict
import json

"""
Problem
-------
You want to create a dictionary, and you also want to control the order of
items when iterating or serializing.
"""

# The size of an OrderedDict is more than twice as large as a normal
# dictionary due to the extra linked list that’s created to order the keys
# according to insertion order
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4


for key in d:
    print(key, d[key])

print(json.dumps(d))
