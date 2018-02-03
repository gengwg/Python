values = ['1', '2', '-3', '-', '4', 'n/a', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

# filter(function, iterable) is equivalent to
# [item for item in iterable if function(item)] if function is not None
# and [item for item in iterable if item] if function is None.
ivals = filter(is_int, values)

# print ivals
for i in ivals:
    print i
