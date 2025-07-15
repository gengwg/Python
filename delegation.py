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

b = B()
b.bar()
b.spam(42)  # Delegates to A's spam method