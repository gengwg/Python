class Spam:
    def __init__(self, name):
        self.name = name

a = Spam('foo')
b = Spam('bar')
c = Spam('foo')

print(a is b)   # False
print(a is c)   # False

import weakref
_spam_cache = weakref.WeakValueDictionary()

# factory function
def get_spam(name):
    if name in _spam_cache:
        return _spam_cache[name]

    s = Spam(name)
    _spam_cache[name] = s
    return s

a = get_spam('foo')
b = get_spam('bar')
c = get_spam('foo')

print(a is b)  # False (different names)
print(a is c)  # True (same name, cached instance)

print(list(_spam_cache))    # ['foo', 'bar']
del a 
print(list(_spam_cache))    # ['foo', 'bar']
del c
print(list(_spam_cache))    # ['bar']
del b 
print(list(_spam_cache))    # []
