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
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s

a = get_spam('foo')
b = get_spam('bar')
c = get_spam('foo')

print(a is b)
print(a is c)
