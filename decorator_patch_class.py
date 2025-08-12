def log_getattributes(cls):
    orig_getattribute = cls.__getattribute__

    def new_getattribute(self, name):
        print(f"Accessing attribute '{name}'")
        return orig_getattribute(self, name)
    
    cls.__getattribute__ = new_getattribute
    return cls

@log_getattributes
class A:
    def __init__(self, x):
        self.x = x

    def method(self):
        pass

if __name__ == "__main__":
    a = A(10) 
    a.x
    a.method()