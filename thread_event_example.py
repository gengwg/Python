from threading import Thread, Event 
import time 

def countdown(n, started_evt):
    print("countdown starting")
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)

started_evt = Event()
t = Thread(target=countdown, args=(10, started_evt))
t.start()

started_evt.wait()  # wait until thread has started
print("countdown is running")