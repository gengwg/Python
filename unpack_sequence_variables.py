#!/usr/bin/env python3

# any sequence or iterable can be unpacked into separate variables using a simple assignment operation.
# the only requirement is that number of variables and strucutre match the sequence.

p = (4, 5)
x, y = p

print(p)
print("x: ", x, \
    "y: ", y)

name, shares, price, date = ['ACME', 50, 91.1, (2012, 12, 21)]
print(name, shares, price, date)

print("any iterable including strings, files, iterators, generators works:")
a, b, c, d, e = "Hello"
print(a, b, c, d, e)

print("use a throwaway variable to discard certain values:")
_, shares, price, _ = ['ACME', 50, 91.1, (2012, 12, 21)]
print(shares, price)


# extended unpacking is for iterables of unknown or arbitrary length
# only available in py3.

# a sequence of tagged tuple
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print(('foo', x, y))


def do_bar(s):
    print(('bar', s))

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)

    elif tag == 'bar':
        do_bar(*args)


# unpacking combined with string processing
line = 'targeting:x:1003:1003::/mnt/targeting:/bin/bash'
uname, *_, homedir, sh = line.split(':')
print (uname, homedir, sh)

record = ('ACME', 50, 91.1, (2012, 12, 21))
name, *_, (*_, year) = record
print (name, year)

# the start variable will always be a list, regardless of how many elements are unpacked, including none.
# thus any code uses it do not have to account for the possibility that it might not be list
# or perform any kind of additional type checking


