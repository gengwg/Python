"""
memory map a binary file into a mutable byte array
for random access to its contents and make inplace modifications.
"""
import os
import mmap

# OS independent mmap function
def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

# create a file filled with \x00.
size = 100000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

m = memory_map('data')
print(len(m))
print(m[0:10])
print(m[0], m[1])

# reasign a slice
m[0:11] = b'Hello World'
m.close()

# verify that changes were made
with open('data', 'rb') as f:
    print(f.read(11))

# mmap object can be used a context manager

with memory_map('data') as m:
    print(len(m))
    print(m[0:11])
    print(m[0:12])
print(m.closed)
