"""
Diff Backlog vs Worker Pool

CLIENTS TRYING TO CONNECT:
Client A → Client B → Client C → Client D → Client E → Client F

SERVER:
            ┌─── BACKLOG QUEUE (listen(5)) ───┐
            │ Client B (waiting)              │
            │ Client C (waiting)              │
            │ Client D (waiting)              │
            │ Client E (waiting)              │
            │ Client F (waiting)              │
            └─────────────────────────────────┘
            ❌ Client G → REJECTED (backlog full!)

            ┌─── WORKER POOL (max_workers=4) ─┐
            │ Thread 1: Processing Client A   │
            │ Thread 2: Processing Client H   │
            │ Thread 3: Processing Client I   │
            │ Thread 4: Processing Client J   │
            └─────────────────────────────────┘
            │ Client K → Queued in thread pool│


    Connection Phase: sock.listen(5) controls how many connections can wait to be accepted

    Acceptance Phase: sock.accept() takes connections from the backlog queue

    Processing Phase: pool.submit() sends accepted connections to thread pool workers


    Backlog: Protects against connection floods - prevents the OS from being overwhelmed with too many pending connections

    Worker Pool: Limits resource usage - prevents your application from using too much CPU/memory by processing too many clients at once

"""

from socket import AF_INET, socket, SOCK_STREAM
from concurrent.futures import ThreadPoolExecutor

def echo_client(sock, client_addr):
    print('Got connection from', client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('Client closed connection')
    sock.close()

def echo_server(addr):
    # pool workers manages number of active connections
    pool = ThreadPoolExecutor(max_workers=2)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)  # backlog of connections manages waiting conections
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)

import urllib.request

def fetch_url(url):
    u = urllib.request.urlopen(url)
    data = u.read()
    return data


if __name__ == '__main__':

    # pool = ThreadPoolExecutor(max_workers=1)
    # pool = ThreadPoolExecutor(max_workers=3)
    # a = pool.submit(fetch_url, 'http://www.python.org')
    # b = pool.submit(fetch_url, 'http://www.python.org/about/')
    # c = pool.submit(fetch_url, 'http://www.python.org/robots.txt')

    # x = a.result()
    # y = b.result()
    # z = c.result()
    # print(z)

    # Use context manager for automatic cleanup
    with ThreadPoolExecutor(max_workers=3) as pool:
        a = pool.submit(fetch_url, 'http://www.python.org')
        b = pool.submit(fetch_url, 'http://www.python.org/about/')
        c = pool.submit(fetch_url, 'http://www.python.org/robots.txt')
        
        # Get all results (blocks until all complete)
        x, y, z = a.result(), b.result(), c.result()

    print(f'Got {len(x)} bytes from http://www.python.org')
    print(f'Got {len(y)} bytes from http://www.python.org/about/')
    print(f'Got {len(z)} bytes from http://www.python.org/robots.txt')

    # echo_server(('', 15000))

    # To test, run in another terminal:
    # $ telnet localhost 15000
    # Then type a few lines and see them echoed back.
    # Press Ctrl+] then type quit to exit

    # Or run the following:
    # $ echo "Hello Server" | nc localhost 15000
    # Or interactive:
    # $ nc localhost 15000
    # Type messages and see them echoed
