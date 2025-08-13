from inspect import Signature, Parameter

parms = [
    Parameter(name='x', kind=Parameter.POSITIONAL_OR_KEYWORD),
    Parameter(name='y', kind=Parameter.POSITIONAL_OR_KEYWORD, default=42),
    Parameter(name='z', kind=Parameter.KEYWORD_ONLY, default=None),
]

sig = Signature(parameters=parms)
print(sig)

def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    print(bound_values)

func(1, 2, z=3)  # x=1, y=2, z=3
func(1, z=3)     # x=1, y=42, z=3
func(1)          # x=1, y=42, z=None
func(y=2, x=1)

# func(1, 2, 3)    # Raises TypeError: func() got an unexpected keyword argument '3'
# func(1,2,3,4)
# func(1, 2, x=3)
# func(y=2)

def make_sig(*names):
    parms = [Parameter(name=name, kind=Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(parameters=parms)

class Structure:
    __signature__ = make_sig()
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)

class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')
    
class Point(Structure):
    __signature__ = make_sig('x', 'y')

import inspect
print(inspect.signature(Stock))

s1 = Stock("AAPL", 50, 150.0)
print(s1.name)    # Output: AAPL
print(s1.shares)  # Output: 50
print(s1.price)   # Output: 150.0

# s2 = Stock(name="GOOGL", shares=30)
# s3 = Stock("GOOGL", 30, 2800.0, shares=30)  # Extra argument, should raise TypeError
