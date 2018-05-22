from collections import Iterable

# flatten a nested sequence into a single list of values.
# recursive generator function involving yield from
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

if __name__ == '__main__':
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    items = [
      [1,2],
      [3],
      [],
      [4,5,6],
      []
    ]
    for x in flatten(items):
        print(x)

    items = ['dave', 'wang', ['thomas', 'geng']]
    print(list(flatten(items)))
    for x in flatten(items):
        print(x)
