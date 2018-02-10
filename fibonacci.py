#!/usr/bin/env python

def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib = [0] * 200
def fibonacci2 (n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if fib[n] != 0:
        return fib[n]
    fib[n] = fibonacci2(n-1) + fibonacci2(n-2)
    return fib[n]

# print first 30 fibonacci numbers
a = []
for i in range(30):
    a.append(fibonacci2(i))
print a


# print first 10 fibonacci numbers
x = [1,1]
for i in xrange(10):
    x.append(x[-1] + x[-2])
print x

