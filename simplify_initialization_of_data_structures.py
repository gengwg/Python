# generalize initialization of data structures into a single __init__() function
# defined in a common base class
class Structure:
    # class variables that specifies expected fileds
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # using setattr() to set attributes **dynamically**
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

# handle keyword arguments
class Structure2:
    _fields = []
    def __init__(self, *args, **kwargs):
        if len(args) + len(kwargs) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # using setattr() to set attributes **dynamically**
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

        # handle keyword arguments
        for name in kwargs:
            if name not in self._fields:
                raise TypeError('Unexpected keyword argument: {}'.format(name))
            setattr(self, name, kwargs[name])

# example class definitions
if __name__ == '__main__':
    import math
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    class Point(Structure):
        _fields = ['x', 'y']

    class Circle(Structure):
        _fields = ['radius']
        def area(self):
            return math.pi * self.radius ** 2

    s = Stock('ACME', 50, 91.1)
    print(vars(s))
    p = Point(2, 3)
    print(vars(p))
    c = Circle(4.5)
    print(vars(c))
    print('area:', c.area())
    # s2 = Stock('ACME', 50) # TypeError


    class Stock2(Structure2):
        _fields = ['name', 'shares', 'price']

    # s3 = Stock('ACME', 50, 91.1, 100) # TypeError
    s4 = Stock2(name='ACME', shares=50, price=91.1) # works
    print(vars(s4))
    s5 = Stock2('ACME', 50, price=91.1) # works
    print(vars(s5))
