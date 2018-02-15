import os.path

# read data into mutable array
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        # print (f.readinto(buf))
        f.readinto(buf)
    return buf

with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('sample.bin')
print(buf)

buf[0:5] = b'Hallo'
print(buf)

with open('newsample.bin', 'wb') as f:
    f.write(buf)

def read_record():
    record_size = 32

    buf = bytearray(record_size)
    with open('somefile', 'rb') as f:
        while True:
            n = f.readinto(buf)
            if n < record_size:
                break
            # use the content of buf
