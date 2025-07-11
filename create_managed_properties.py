# add type checking to getting or setting of an instance attribute.
# only works in py3
class Person:
    def __init__(self, first_name):
        # In Python, when you define a property using the `@property` decorator along with a setter (using `@<property_name>.setter`), 
        # assignments to that property (like `self.first_name = first_name`) will automatically call the setter method 
        # instead of directly setting the attribute.
        self.first_name = first_name 

    # getter function
    @property
    def first_name(self):
        return self._first_name

    # setter function
    @first_name.setter
    def first_name(self, val):
        if not isinstance(val, str):
            raise TypeError('Expected a string')
        self._first_name = val

    # deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError('Cannot delete attribute')

a = Person('Guido') # calls the setter
print(a.first_name) # calls the getter

a.first_name = 'Wei'    # calls the setter
print(a.first_name)

try:
    a.first_name = 43   # calls the setter
except TypeError as e:
    print(e)

try:
    b = Person(666)     # initialization also calls the setter
except TypeError as e:
    print(e)

try:
    del a.first_name  # calls the deleter
except AttributeError as e:
    print(e)


import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(4.0)
print(c.radius) # calls the radius attribute directly
print(c.area) # calls the area property. w/o @property, it would be a method call c.area().
print(c.perimeter) # calls the perimeter property

c.radius = 5.0 # changes the radius
print(c.area) # calls the area property again
print(c.perimeter)
