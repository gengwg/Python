#!/usr/bin/env python3
# skip only first few items of an iterable.

from itertools import dropwhile

with open('mysql_db_connect_yaml.py') as f:
    # the result iterator discards the first items in the sequence
    # as long as the supplied function returns True
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

# if you know exact number of items to skip, use itertools.islice()
from itertools import islice

items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):   # skip [:3]
# for x in islice(items, 3):       # skip [3:]
    print(x)
