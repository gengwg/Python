import sys

CHUNKSIZE  = 8192

# common scenario involving i/o
def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)

# same code using iter()
def reader(s):
    # iter() accepts a zero-argement callable, and sentinel value as inputs
    # creates an iterator that repeated call the supplied callable
    # until it returns the value given as sentinel
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        process_data(chunk)


f = open('/etc/passwd')
for chunk in iter(lambda: f.read(10), ''):
#for chunk in iter(lambda: f.read(10), 'bus-proxy:'):
    n = sys.stdout.write(chunk)
    # print(chunk)
