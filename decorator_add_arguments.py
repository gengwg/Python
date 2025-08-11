from functools import wraps

def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


if __name__ == "__main__":
    @optional_debug
    def spam(a, b, c):
        print(a, b, c)

    spam(1,2,3)
    spam(1, 2, 3, debug=True)
