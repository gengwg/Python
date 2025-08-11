from functools import wraps, partial
import logging


def logged(func = None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)
    
    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper

# enables logging output
logging.basicConfig(level=logging.DEBUG)

@logged
def add(x, y):
    return x + y

@logged(level=logging.CRITICAL, name='example')
def spam():
    print("Spam!")

add(3, 4)
spam()

"""
## Key Components

(A) functools.wraps(func)

    Preserves the original function's metadata (__name__, __doc__, etc.) in the wrapper.

(B) functools.partial

    Helps handle the case where the decorator is called with arguments (@logged(...)).

    Returns a new function that "remembers" the provided arguments (level, name, message) and waits for func.
"""