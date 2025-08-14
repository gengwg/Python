def typed_property(name, expected_type):
    storage_name = f"_{name}"

    @property
    def prop(self):
        return getattr(self, storage_name)
    
    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f"Expected {expected_type.__name__}, got {type(value).__name__}")
        setattr(self, storage_name, value)

    return prop

class Person:
    name = typed_property("name", str)
    age = typed_property("age", int)

    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    p = Person("Alice", 30)
    print(p.name)  # Output: Alice
    print(p.age)   # Output: 30

    try:
        p.age = "thirty"  # Raises TypeError
    except TypeError as e:
        print(e)  # Output: Expected int, got str

    try:
        p.name = 12345  # Raises TypeError
    except TypeError as e:
        print(e)  # Output: Expected str, got int
