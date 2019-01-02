# rpcserver.py

# rpc is easy to implement by encoding function requests, arguments, and return values using pickle
# and passing the pickled byte strings between interpreters.

import pickle

class RPCHandler:
    def __init__(self):
        self._functions = {}

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                # Receive a message
                func_name, args, kwargs = pickle.loads(connection.recv())
                try:
                    r = self._functions[func_name](*args, *kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass


from multiprocessing.connection import Listener
from threading import Thread

def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()

# some remote functions
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

# register with a handler
handler = RPCHandler()
handler.register_function(add)
handler.register_function(sub)

# run the server
rpc_server(handler, ('localhost', 17000), authkey=b'peekaboo')


# rpcclient.py

# to access the server from a remote client, you need to create a corresponding RPC proxy class
# that forwards the requests.
import pickle

class RPCProxy:
    def __init__(self, connection):
        self._connection = connection

    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self._connection.send(pickle.dumps((name, args, kwargs)))
            result = pickle.loads(self._connection.recv())
            if isinstance(result, Exception):
                raise result
            return result
        return do_rpc

# to use the proxy you wrap it around a connection to the server.

>>> from multiprocessing.connection import Client
>>> from client import RPCProxy
>>> c = Client(('localhost', 17000), authkey=b'peekaboo')
>>> proxy = RPCProxy(c)
>>> proxy.add(2,3)
5
>>> proxy.sub(2,3)
-1
>>> proxy.sub([1,2],3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/gengwg/Nextcloud/github/Python/client.py", line 12, in do_rpc
    raise result
TypeError: unsupported operand type(s) for -: 'list' and 'int'

