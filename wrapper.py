import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n: int):
    '''
    counts down
    '''
    while n > 0:
        n -= 1

countdown(10000)
countdown(100000)
countdown(1000000)
countdown(10000000)

print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)
print(countdown.__wrapped__)

from inspect import signature
print(signature(countdown))