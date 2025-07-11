from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None
        # print('Connection closed')

from functools import partial

conn = LazyConnection(('www.python.org', 80))

with conn as s:
    # conn.__enter__() executes: connection open
    
    # s is the socket object returned by conn.__enter__()
    # s.send() is a method of the socket object
    # It sends data to the socket.
    # The data is sent in bytes, so we use b'' to create a byte string
    # The HTTP request is sent in the format:
    # GET /index.html HTTP/1.0\r\n
    # Host: www.python.org\r\n
    # \r\n indicates the end of the HTTP headers
    # This is a simple HTTP request to get the index.html page from www.python.org
    # The HTTP version is 1.0, which is a simple version of HTTP
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')

    # s.recv() is a method of the socket object
    # It receives data from the socket.
    # The data is received in chunks of 8192 bytes until no more data is available
    # The partial function is used to create a callable that takes no arguments
    # and calls s.recv with 8192 as the argument
    # This allows us to use iter() to read all data until the socket is closed
    # iter(partial(s.recv, 8192), b'') creates an iterator that
    # repeatedly calls s.recv(8192) until it returns an empty byte string (b'')
    # This is a common pattern to read all data from a socket until it is closed
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    print(resp)
    # conn.__exit__() executes: connection closed
    
# The __exit__ method is called automatically when the with block is exited
# It closes the socket and sets self.sock to None
# This ensures that the connection is properly closed and cleaned up
# If an exception occurs within the with block, __exit__ will still be called
# This is the essence of context management in Python
# It ensures that resources are properly managed and cleaned up
# even in the presence of exceptions.