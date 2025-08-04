from functools import wraps

class A:
    # decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator 1")
            return func(*args, **kwargs)
        return wrapper
    
    # decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator 2")
            return func(*args, **kwargs)
        return wrapper
    

a = A()

@a.decorator1
def func1():
    pass

@A.decorator2
def func2():
    pass

func1()
func2()