class Spam:
    def __init__(self, name):
        self.name = name

a = Spam("gengwg")
b = Spam("wangwg")

class NoInstances(type):
    def __call__(self, *args, **kwds):
        raise TypeError("Cannot create instances of this class")
    
class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print(f"Spam.grok({x})")

Spam.grok(42)
# s = Spam()  # This will raise TypeError

class Singleton(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__instance = None

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
        return self.__instance

class Spam(metaclass=Singleton):
    def __init__(self):
        print(f"Creating Spam instance")

s1 = Spam()
s2 = Spam()
print(s1 is s2)  # True, both variables point to the same instance
s3 = Spam()
print(s1 is s3)  # True, still the same instance


import weakref

class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._instances = weakref.WeakValueDictionary()

    def __call__(self, *args, **kwargs):
        if args in self._instances:
            return self._instances[args]
        else:
            instance = super().__call__(*args, **kwargs)
            self._instances[args] = instance
            return instance
        
class Spam(metaclass=Cached):
    def __init__(self, name):
        self.name = name
        print(f"Creating Spam instance with name: {self.name}")

a = Spam("gengwg")
b = Spam("wangwg")
c = Spam("gengwg")  # This will return the cached instance for "gengwg"
print(a is b)   # False, a and b are different instances
print(a is c)  # True, a and c are the same instance

