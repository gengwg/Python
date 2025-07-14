# File: data_model_type_system.py
# This code implements a simple type system for managing properties in Python classes.
# It uses descriptors to enforce type checking, unsigned values, and maximum size constraints.
# The descriptors can be used to define properties with specific constraints, such as integer, float,
# string types, and more. The Stock class demonstrates how to use these descriptors to manage stock
# attributes like name, shares, and price with appropriate validations.
class Descriptor:
    def __init__(self, name, **opts):
        self.name = name

        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        print(f'Setting {self.name} to {value}')
        instance.__dict__[self.name] = value


# This function is a decorator that checks if the value is of the expected type.
def Typed(expected_type, cls=None):
    # If cls is None, it means we are using this as a decorator.
    # We return a function that takes a class and applies the Typed descriptor.
    if cls is None:
        return lambda cls: Typed(expected_type, cls)
    
    super_set = cls.__set__
    def __set__(self, instance, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}, got {type(value)}')
        super_set(self, instance, value)
    cls.__set__ = __set__
    return cls

# This function is a decorator that checks if the value is non-negative.
def Unsigned(cls):
    # This function is a decorator that modifies the __set__ method of the class
    # to raise a ValueError if the value is negative.
    super_set = cls.__set__
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Value must be non-negative')
        super_set(self, instance, value)
    cls.__set__ = __set__
    return cls

# This function is a decorator that sets a maximum size for the value.
# If the value exceeds this size, it raises a ValueError.
def MaxSized(cls):
    # This function is a decorator that modifies the __init__ and __set__ methods
    # of the class to enforce a maximum size for the value.
    super_init = cls.__init__ # Save the original __init__ method to call it later.
    # This allows us to add additional initialization logic without losing the original behavior.
    # The __init__ method is modified to accept a max_size parameter.
    # If max_size is not provided, it defaults to 100.
    # This allows the class to be initialized with a specific maximum size for its value.
    def __init__(self, name=None, **opts):
        if 'max_size' in opts:
            self.max_size = opts['max_size']
        else:
            self.max_size = 100
        super_init(self, name, **opts) # Call the original __init__ method with the modified parameters.
        # This ensures that the original initialization logic is preserved while adding the max_size functionality.
    cls.__init__ = __init__ # This replaces the original __init__ method with the modified one.
    
    # This modifies the __set__ method to enforce the maximum size constraint.
    # If the value exceeds the maximum size, it raises a ValueError.
    super_set = cls.__set__
    def __set__(self, instance, value):
        if len(value) > self.max_size:
            raise ValueError(f'Value exceeds maximum size of {self.max_size}')
        super_set(self, instance, value) # Call the original __set__ method with the modified value.
    # This replaces the original __set__ method with the modified one.
    cls.__set__ = __set__
    return cls


# The following classes define various data types using the descriptors.
@Typed(int)
class Integer(Descriptor):
    pass

# This class defines an unsigned integer type.
# It inherits from the Descriptor class and applies the Unsigned decorator.
@Unsigned
class UnsignedInteger(Integer):
    pass

# This class defines a float type.
# It inherits from the Descriptor class and applies the Typed decorator with float as the expected type.
@Typed(float)
class Float(Descriptor):
    pass

# This class defines an unsigned float type.
# It inherits from the Float class and applies the Unsigned decorator.
@Unsigned
class UnsignedFloat(Float):
    pass

@Typed(str)
class String(Descriptor):
    pass

@MaxSized
class SizedString(String):
    pass


class Stock:
    name = SizedString('name', max_size=50)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

if __name__ == "__main__":
    s = Stock('AAPL', 100, 150.0)
    print(f'Stock: {s.name}, Shares: {s.shares}, Price: {s.price}')
    
    try:
        s.name = 'A very long stock name that exceeds the maximum size limit'
    except ValueError as e:
        print(e)
    
    try:
        s.shares = -10
    except ValueError as e:
        print(e)
    
    try:
        s.price = -50.0
    except ValueError as e:
        print(e)
    
    try:
        s.shares = 'hundred'
    except TypeError as e:
        print(e)
