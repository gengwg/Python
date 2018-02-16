import os
path = '/Users/gengwg/Data/data.csv'

# get the last component of path
print(os.path.basename(path))

# get the dir name
print(os.path.dirname(path))

# join path components together
print(os.path.join('tmp', 'data', os.path.basename(path)))

# expand user home dir
path = '~/Data/data.csv'
print(os.path.expanduser(path))

# split file extention
print(os.path.splitext(path))

