print 'spam.txt'.endswith('txt')
# True

url = 'http://www.xyz.com'
print url.startswith('http:')
# True

filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
import os

# must use tuple, not list
print [name for name in filenames if name.endswith(('.c', '.h'))]
# ['foo.c', 'spam.c', 'spam.h']

print any(name.endswith('.py') for name in filenames)
# True

print [name.endswith('.py') for name in filenames]
# [False, False, True, False, False]

