import threading

def worker(n, sema):
    sema.acquire()
    print(f"Worker {n} acquired semaphore")

sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema))
    t.start()
    
sema.release()
sema.release()