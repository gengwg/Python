# function that accepts any number of arguments
# * argument for any number of positional arguments
# ** argument for any number of keyword arguments
def anyargs(*args, **kwargs):
    print(args)     # a tuple
    print(kwargs)   # a dict

# functions that only accept keyword arguments
def onlykwargs(maxsize, *, block):
    """ hello """
    pass

def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

def spam(a, b='sadfd'):
    print (a, b)

spam(3, [2,34])

if __name__ == '__main__':
    anyargs(3, 6, a=5, b=9, c=8, x='foo', y='bar')
    # (3, 6)
    # {'a': 5, 'b': 9, 'c': 8, 'x': 'foo', 'y': 'bar'}

    # onlykwargs(1024, True)    # TypeError
    print(onlykwargs(1024, block=True))

    print(minimum(1, 5, 2, -5))
    print(minimum(1, 5, 2, clip=0))


