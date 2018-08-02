# generalize initialization of data structures into a single __init__() function
# defined in a common base class
class Structure:
    # class variables that specifies expected fileds
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # set the arguments
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

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
    s2 = Stock('ACME', 50) # TypeError

