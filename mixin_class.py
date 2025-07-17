class LoggedMappingMixin:
    '''
    add loggingto get, set, and del methods
    '''
    __slots__ = () # Using __slots__ to prevent dynamic attribute creation

    def __getitem__(self, key):
        value = super().__getitem__(key)
        print(f"Getting item: {key} -> {value}")
        return value
    
    def __setitem__(self, key, value):
        print(f"Setting item: {key} -> {value}")
        super().__setitem__(key, value)

    def __delitem__(self, key):
        print(f"Deleting item: {key}")
        super().__delitem__(key)

        
class SetOnceMappingMixin:
    '''
    only allow setting a key once
    '''
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(f"Key '{key}' already set. Cannot overwrite.")
        print(f"Setting item: {key} -> {value}")
        super().__setitem__(key, value)

class StringKeysMappingMixin:
    '''
    only allow string keys
    '''
    __slots__ = ()
    
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError(f"Key must be a string, got {type(key).__name__}")
        print(f"Setting item: {key} -> {value}")
        super().__setitem__(key, value)

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise TypeError(f"Key must be a string, got {type(key).__name__}")
        return super().__getitem__(key)
    

if __name__ == "__main__":

    # Example usage of the mixins
    class LoggedDict(LoggedMappingMixin, dict):
        pass
    d = LoggedDict()
    d['x'] = 42
    print(d['x'])
    del d['x']

    from collections import defaultdict
    class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
        pass
    d2 = SetOnceDefaultDict(list)
    d2['x'].append(1)
    d2['y'].append(2)
    try:
        d2['x'] = 23  # This should raise an error
    except KeyError as e:
        print(e)

    from collections import OrderedDict
    class StringKeysOrderedDict(StringKeysMappingMixin, SetOnceMappingMixin, OrderedDict):
        pass
    d3 = StringKeysOrderedDict()
    d3['a'] = 1
    try:
        d3[1] = 2  # This should raise a TypeError
    except TypeError as e:
        print(e)
    try:
        d3['a'] = 3  # This should raise a KeyError
    except KeyError as e:
        print(e)

    def LoggedMapping(cls):
        '''
        Decorator to add logging to a mapping class
        '''
        cls_getitem = cls.__getitem__
        cls_setitem = cls.__setitem__
        cls_delitem = cls.__delitem__

        def __getitem__(self, key):
            value = cls_getitem(self, key)
            print(f"Getting item: {key} -> {value}")
            return cls_getitem(self, key)
        
        def __setitem__(self, key, value):
            print(f"Setting item: {key} -> {value}")
            cls_setitem(self, key, value)

        def __delitem__(self, key):
            print(f"Deleting item: {key}")
            cls_delitem(self, key)

        cls.__getitem__ = __getitem__
        cls.__setitem__ = __setitem__
        cls.__delitem__ = __delitem__

        return cls
    
    # Example usage of the decorator
    # You get the same functionality as LoggedMappingMixin
    # but multiple inheritance is no longer needed.
    @LoggedMapping
    class LoggedDict2(dict):
        pass

    d4 = LoggedDict2()
    d4['a'] = 1
    print(d4['a'])
    del d4['a']