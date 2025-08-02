from functools import wraps
import logging

def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

@logged(logging.ERROR)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example', 'example msg')
def spam():
    print("Spam!")

add(3, 4)

spam()