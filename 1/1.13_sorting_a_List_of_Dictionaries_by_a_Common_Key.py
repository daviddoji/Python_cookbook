#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 20:27:16 2017

@author: david
"""

from operator import itemgetter
from pprint import pprint

"""
Problem
-------
You have a list of dictionaries and you would like to sort the entries
according to one or more of the dictionary values.
"""

rows = [{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
        ]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))


print("Sorted by fname:")
pprint(rows_by_fname)

print("Sorted by uid:")
pprint(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print("Sorted by lname, fname:")
pprint(rows_by_lfname)

min_row = min(rows, key=itemgetter('uid'))
print("Row with min 'uid'")
pprint(min_row)

max_row = max(rows, key=itemgetter('uid'))
print("Row with max 'uid'")
pprint(max_row)
