import types
from functools import wraps

class Profiled:
    def __init__(self, func):
        # Copies metadata (like __name__, __doc__, etc.) from func to the wrapper (self).
        # Sets self.__wrapped__ = func, storing the original function for later use.
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)
    
    # A bound method is a function attached to an instance, automatically receiving self.
    # Python creates bound methods using the descriptor protocol (__get__).
    # Decorators that work on methods must implement __get__ to preserve binding behavior.
    # Without __get__, decorated methods would fail when called on instances (since self wouldn’t be passed correctly).
    def __get__(self, instance, cls):
        if instance is None:
            return self
        return types.MethodType(self, instance)
    

@Profiled
def add(x, y):
    return x + y

class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)

print(add(2, 3))
print(add(4, 5))
print(add.ncalls)

s = Spam()
s.bar(1)
s.bar(2)
s.bar(3)
print(s.bar.ncalls)

# alternative formation of the decorator using closure and nonlocal variable
def profiled(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda: ncalls
    return wrapper

@profiled
def add2(x, y):
    return x + y

print(add2(2, 3))
print(add2(4, 5))
print(add2.ncalls())