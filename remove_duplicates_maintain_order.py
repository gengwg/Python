# eliminate the duplicate values in a sequence, but preserver the order of the remaining items.
# note: set(a) cannot achieve this, because it doesn't preserve any order.

# sequence is hashable
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            # generator function works beyond list processing
            yield item
            seen.add(item)

# sequence can be unhashable
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            # generator function works beyond list processing
            yield item
            seen.add(val)

if __name__ == '__main__':
    a = [1,5,2,1,9,1,5,10]
    print list(dedupe(a))
    # [1, 5, 2, 9, 10]

    b = [{'x': 1, 'y':2},{'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
    print list(dedupe(b, key=lambda d: (d['x'], d['y'])))
    # [{'y': 2, 'x': 1}, {'y': 3, 'x': 1}, {'y': 4, 'x': 2}]
    print list(dedupe(b, key=lambda d: d['x']))
    # [{'y': 2, 'x': 1}, {'y': 4, 'x': 2}]
