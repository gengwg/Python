import threading
from contextlib import contextmanager
import time

_local = threading.local()

@contextmanager
def acquire(*locks):
    # locks = sorted(locks, key=lambda x: id(x))
    locks = sorted(locks, key=id)


    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation: {} -> {}'.format(acquired[-1], locks[0]))
    
    acquired.extend(locks)
    _local.acquired = acquired

    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


if __name__ == '__main__':

    x_lock = threading.Lock()
    y_lock = threading.Lock()

    def thread1():
        while True:
            with acquire(x_lock, y_lock):
                print('Thread 1 acquired x_lock and y_lock')
            time.sleep(2)
    
    def thread2():
        while True:
            with acquire(y_lock, x_lock):
                print('Thread 2 acquired y_lock and x_lock')
            time.sleep(10)

    t1 = threading.Thread(target=thread1)
    t1.daemon = True
    t1.start()


    t2 = threading.Thread(target=thread2)
    t2.daemon = True
    t2.start()