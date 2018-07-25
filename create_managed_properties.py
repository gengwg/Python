# add type checking to getting or setting of an instance attribute.
# only works in py3
class Person:
    def __init__(self, first_name):
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

a = Person('Guido')
print(a.first_name) # calls the getter
a.first_name = 'abc'
print(a.first_name)
# a.first_name = 43   # calls the setter
# del a.first_name
# a = Person(43)

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
print(c.radius)
print(c.area)
print(c.perimeter)
