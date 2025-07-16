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

from collections.abc import Sequence, Iterable
import bisect

class SortedItems(Sequence):
    def __init__(self, items=None):
        self._items = sorted(items) if items else []

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def add(self, item):
        bisect.insort(self._items, item)

if __name__ == "__main__":
    sorted_items = SortedItems([5, 3, 8])
    print("Initial items:", list(sorted_items))

    sorted_items.add(4)
    print("After adding 4:", list(sorted_items))

    sorted_items.add(1)
    print("After adding 1:", list(sorted_items))

    print("Item at index 2:", sorted_items[2])  # Should print the item at index 2
    print("Length of sorted items:", len(sorted_items))  # Should print the length of the sorted items
    print("All items:", list(sorted_items))  # Should print all items
    print("Is sorted_items an instance of collections.abc.Sequence?", isinstance(sorted_items, Sequence))  # Should print True
    print("Is sorted_items an instance of collections.abc.Iterable?", isinstance(sorted_items, Iterable))  # Should print True