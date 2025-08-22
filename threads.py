import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        time.sleep(1)
        n -= 1
    print("Countdown finished!")

from threading import Thread
t = Thread(target=countdown, args=(10,), daemon=True)
print("Countdown started in a separate thread.")
t.start()

# Blocks the calling thread (main thread) until the target thread completes
# Can optionally take a timeout parameter: t.join(timeout=5) would wait max 5 seconds
t.join(timeout=8)
print("Main thread waited for countdown to finish.")

class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while n > 0 and self._running:
            print('T-minus', n)
            time.sleep(1)
            n -= 1
        if not self._running:
            print("Countdown aborted!")
        else:
            print("Countdown finished!")

c = CountdownTask()
t2 = Thread(target=c.run, args=(10,))
t2.start()
print("t2 started")
time.sleep(5)
c.terminate()
print("t2 terminate called")
t2.join()