# Python is dynamically typed, so type hints are not enforced at runtime
# but are meant for static analysis and code readability.

# 1. Basic types like `str`, `int`, `float`, etc. don't require importing from `typing`.
# 2. Complex types like `List`, `Tuple`, `Dict`, `Any`, `Union`, etc. 
# should be imported from `typing` when used as type hints.
    
# To indicate that a variable or function parameter can be optional, use Optional from typing:
from typing import Optional

def greet_optional(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, World!"
    else:
        return f"Hello, {name}!"

print(greet_optional())
print(greet_optional('Tom'))

# Example:
# $ py /tmp/test2.py
# Hello, World!
# Hello, Tom!
