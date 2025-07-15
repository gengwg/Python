from collections.abc import Iterable

class A(Iterable):
    def __init__(self):
        print("A initialized")
        self._li = [1, 2, 3]

    def __iter__(self):
        print("A.__iter__ called")
        return iter(self._li)

a = A()
for item in a:
    print(item)

