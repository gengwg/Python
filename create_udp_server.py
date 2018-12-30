from socketserver import BaseRequestHandler, UDPServer
import time

# this implements a time server. when client requests, it replies with current time.
class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        #Get message and client socket
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii') + ': ' + msg, self.client_address)

if __name__ == '__main__':
    serv = UDPServer(('', 20000), TimeHandler)
    serv.serve_forever()


# test server
from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
print(s.sendto(b'Hello', ('localhost', 20000)))
print(s.recvfrom(8192))

