#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 11:35:20 2017

@author: david
"""

from collections import defaultdict

"""
Problem
-------
You want to make a dictionary that maps keys to more than one value (a
so-called “multidict”).
"""

d = {'a': [1, 2, 3],
     'b': [4, 5],
     }

e = {'a': {1, 2, 3},
     'b': {4, 5},
     }

# list if you want to preserve the insertion order of the items.
d_list = defaultdict(list)
d_list['a'].append(1)
d_list['a'].append(2)
d_list['b'].append(4)


# set if you want to eliminate duplicates (and don’t care about the order).
d_set = defaultdict(set)
d_set['a'].add(1)
d_set['a'].add(2)
d_set['b'].add(4)


d0 = defaultdict(list)
for key, value in d:
    d0[key].append(value)
# Error!!!