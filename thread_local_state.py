from socket import socket, AF_INET, SOCK_STREAM
import threading

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.local = threading.local()

    def __enter__(self):
        if hasattr(self.local, 'socket'):
            raise RuntimeError('Already connected')
        self.local.socket = socket(self.family, self.type)
        self.local.socket.connect(self.address)
        return self.local.socket
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.local.socket.close()
        del self.local.socket

from functools import partial

def test(conn):
    with conn as s:
        s.send(b'GET / HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
    print(f'Got {len(resp)} bytes')

if __name__ == '__main__':
    conn = LazyConnection(('www.python.org', 80))

    t1 = threading.Thread(target=test, args=(conn,))
    t2 = threading.Thread(target=test, args=(conn,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()