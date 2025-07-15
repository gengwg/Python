class A:
    def spam(self, x):
        print(f"A's spam method called with {x}")
        return x * 2
    
    def foo(self):
        pass

class B:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        print("B's spam method called")
        # Delegates to A's spam method
        return self._a.spam(x)
    
    def foo(self):
        return self._a.foo()
    
    def bar(self):
        pass

class C:
    def __init__(self):
        self._a = A()

    def bar(self):
        print("C's bar method called")

    def __getattribute__(self, name):
        # Custom attribute access to delegate to A's methods
        # This is a simplified delegation mechanism
        print(f"Accessing {name} in C")
        # If the attribute is one of A's methods, delegate to A
        if name in ('_a', 'bar', '__getattribute__'):
            return super().__getattribute__(name)
        # If the attribute is not found in C, delegate to A
        if hasattr(self._a, name):
            print(f"Delegating {name} to A")
        return getattr(self._a, name)
    
b = B()
b.bar()
b.spam(42)  # Delegates to A's spam method

c = C()
c.bar()  # Calls C's bar method
c.spam(42)  # Delegates to A's spam method
c.foo()  # Delegates to A's foo method


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        # Delegate attribute access to the wrapped object
        print(f"Proxy accessing {name}")
        return getattr(self._obj, name)
    
    def __setattr__(self, name, value):
        if name == '_obj':
            # Allow setting the wrapped object
            super().__setattr__(name, value)
        else:
            print(f"Proxy setting {name} to {value}")
            setattr(self._obj, name, value)

class RealObject:
    def __init__(self, x):
        self.x = x
        
    def bar(self):
        print("RealObject's bar method called")

s = RealObject(2)
p = Proxy(s)
p.bar()  # Delegates to RealObject's bar method
print(p.x)  # Accesses RealObject's x attribute through Proxy
p.x = 5  # Sets RealObject's x attribute through Proxy
print(s.x)  # Verifies that the value was set in RealObject


print(p.__dict__)  # Accesses Proxy's __dict__ attribute
print(s.__dict__)  # Accesses RealObject's __dict__ attribute
