# easy way to execute functions or methods running on remote machines.

from xmlrpc.server import SimpleXMLRPCServer

class KeyValueServer:
    _rpc_methods_ = ['get', 'set', 'delete', 'exists', 'keys']

    def __init__(self, address):
        self._data = {}
        self._serv = SimpleXMLRPCServer(address, allow_none=True)
        for name in self._rpc_methods_:
            self._serv.register_function(getattr(self, name))

    def get(self, name):
        return self._data[name]

    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        del self._data[name]

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data) # return all the keys as a list

    def serve_forever(self):
        self._serv.serve_forever()

if __name__ == '__main__':
    kvserv = KeyValueServer(('', 15000))
    kvserv.serve_forever()


# access the server remotely from a client

# >>> from xmlrpc.client import ServerProxy
# >>> s = ServerProxy('http://localhost:15000', allow_none=True)
# >>> s.set('foo', 'bar')
# >>> s.set('spam', [1,2,3])
# >>> s.keys()
# ['foo', 'spam']
# >>> s.get('foo')
# 'bar'
# >>> s.get('spam')
# [1, 2, 3]
# >>> s.delete('spam')
# >>> s.exists('spam')
# False

# no class

from xmlrpc.server import SimpleXMLRPCServer
def add(x, y):
    return x + y

serv = SimpleXMLRPCServer(('', 15000))
serv.register_function(add)
serv.serve_forever()

# >>> from xmlrpc.client import ServerProxy
# >>> s = ServerProxy('http://localhost:15000', allow_none=True)
# >>> s.add(1, 2)
# 3
