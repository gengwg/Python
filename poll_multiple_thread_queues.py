import queue
import socket
import os

class PollableQueue(queue.Queue):
    def __init__(self):
        super().__init__()
        if os.name == 'posix':
            self._putsocket, self._getsocket = socket.socketpair()
        else:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('localhost', 0))
            server.listen(1)
            self._putsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._putsocket.connect(server.getsockname())
            self._getsocket, _ = server.accept()
            server.close()

    def fileno(self):
        # print(self._getsocket.fileno())
        return self._getsocket.fileno()
    
    def put(self, item):
        super().put(item)
        self._putsocket.send(b'x')

    def get(self):
        self._getsocket.recv(1)
        return super().get()
    

if __name__ == "__main__":
    import select
    import threading

    def consumer(queues):
        while True:
            readable, _, _ = select.select(queues, [], [])
            for q in readable:
                item = q.get()
                print(f"Got: {item}")
                print(f"queue file descriptor number: {q.fileno()}")

    q1 = PollableQueue()
    q2 = PollableQueue()
    q3 = PollableQueue()
    t = threading.Thread(target=consumer, args=([q1, q2, q3],))
    t.daemon = True
    t.start()

    q1.put("item from q1")
    q2.put("item from q2")
    q3.put("item from q3")
    q2.put("another item from q2")
    q1.put("another item from q1")

    t.join(1)
    