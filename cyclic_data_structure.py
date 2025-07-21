import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return f"Node({self.value!r})"

    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()
        # _parent() derererences the weakref to get the original object
        # self._parent      # This is the weakref object itself
        # self._parent()    # This dereferences the weakref to get the original object (or None)

        # return self._parent # strong ref test
    
    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)
        # self._parent = node # strong ref test

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


if __name__ == '__main__':
    root = Node('parent')
    c1 = Node('child')
    root.add_child(c1)
    print(c1.parent)
    del root
    print(c1.parent)