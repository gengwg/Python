"""
to manually consume an iterable, use the next() function,
and write your code to catch the StopIteration exception.
"""

with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end='') # remove extra added new line
            #print(line)
    except StopIteration:
        pass

# instrct next() to return None as terminating value
with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

items = [1, 2, 3]
# TypeError: 'list' object is not an iterator
# print (next(items))
it = iter(items)    # invokes items.__iter__()
print(next(it))     # invokes items.__next__()
print(next(it))
