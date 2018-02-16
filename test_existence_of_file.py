# test whether or not a file or directory exists

import os

# test existence of file or directory
print(os.path.exists('/etc/passwd'))
print(os.path.exists('/tmp/spam'))

# is regular file
print(os.path.isfile('/etc/passwd'))

# is dir
print(os.path.isdir('/etc/passwd'))

# is symbolic link
print(os.path.islink('/usr/bin/python3'))

# get the file linked to
print(os.path.realpath('/usr/bin/python3'))

# get metadata
print(os.path.getsize('/etc/passwd'))
print(os.path.getmtime('/etc/passwd'))
import time
print(time.ctime(os.path.getmtime('/etc/passwd')))

