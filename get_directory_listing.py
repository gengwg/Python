# example of getting a directory listing

import os
names = os.listdir('.')
print(names)

import os.path

# get regular files
names = [name for name in os.listdir('.')
        if os.path.isfile(os.path.join('.', name))]
print(names)

# get all dirs
names = [name for name in os.listdir('.')
        if os.path.isdir(os.path.join('.', name))]
print(names)

# get py files using endswith() string method
pyfiles = [name for name in os.listdir('.')
        if name.endswith('.py')]
print(pyfiles)

# get py files using glob module
import glob
pyfiles = glob.glob('*.py')
print(pyfiles)

# get py files using fnmatch module
from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('.')
           if fnmatch(name, '*.py')]
print(pyfiles)

import os
import os.path
import glob

pyfiles = glob.glob('*.py')

# get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]

for name, size, mtime in name_sz_date:
    print(name, size, mtime)

# alternative: get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
