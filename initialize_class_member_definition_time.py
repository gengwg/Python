import operator

class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))

class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []
    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError(f"{cls.__name__} requires {len(cls._fields)} arguments")
        return super().__new__(cls, args)
    
class Stock(StructTuple):
    _fields = ['name', 'quantity', 'price']

class Point(StructTuple):
    _fields = ['x', 'y']

s = Stock("AAPL", 50, 150.0)
print(s)    # Output: AAPL
print(s.name)  # Output: AAPL
print(s[0])
s.name = "GOOGL"  # Raises AttributeError: can't set attribute