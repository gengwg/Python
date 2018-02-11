"""
process a huge directory of log files.

yield act as data producer
for loop act as data consumer
when stacked together each yield feeds a single item to the next state of the pieplie
that is consuming it with iteration.
"""

import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    '''
    find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)
        
def gen_opener(filenames):
    '''
    open a sequence of filenames one at a time producing a file object.
    the file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    '''
    chain a sequence of iterators together into a single sequence.
    '''
    for it in iterators:
        yield from it 

def gen_grep(pattern, lines):
    '''
    look for a regex pattern in a sequence of lines.
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

# stack the generator functions together to make a processing line.
# find all log lines that contain the word python. 
lognames = gen_find('access-log*', 'www')
# lognames = gen_find('*py', '.')       # Test
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines) # Case-insensitive while matching "python"
for line in pylines:
    print(line, end='')