'''
read write binary array of uniform structures into python tuples
'''

from struct import Struct

def write_records(records, format, f):
    '''
    write a sequence of typles to a binary file of structures.
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))
    
def read_records(format, f):
    '''
    read file increamentally in chunks
    '''
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)

def unpack_records(format, data):
    '''
    read the file entirely into a byte string with a single read
    and convert it piece by piece
    '''
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))
    
if __name__ == '__main__':
    records = [ (1, 2.3, 4.5),
                (6, 7.8, 9.0),
                (12, 13.4, 56.7) ]    

    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)

    with open('data.b', 'rb') as f:
        for rec in read_records('<idd',f):
            print(rec)

    with open('data.b', 'rb') as f:
        data = f.read()

    for rec in unpack_records('<idd', data):
        print(rec)

    record_struct = Struct('<idd')
    print(record_struct.size)   # 20 = 4 + 8 + 8
    print(record_struct.pack(1, 2.0, 3.0))
    print(record_struct.unpack(b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@'))

    # read into named tuple
    from collections import namedtuple

    Record = namedtuple('Record', ['kind', 'x', 'y'])

    with open('data.b', 'rb') as f:
        records = [Record(*r) for r in read_records('<idd', f)]
    # print(records)
    for r in records:
        print(r.kind, r.x, r.y)

    # if work with large amount of binary data use numpy
    import numpy as np 
    with open('data.b', 'rb') as f:
        records = np.fromfile(f, dtype='<i,<d,<d')
        print(records)
        print(records[0])
        print(records[1])
    