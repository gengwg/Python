class Spam:
    def __init__(self, name):
        self.name = name

a = Spam('foo')
b = Spam('bar')
c = Spam('foo')

print(a is b)
print(a is c)

import weakref
_spam_cache = weakref.WeakValueDictionary()

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