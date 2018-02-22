import time

class Timer:
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()
    
    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None
    
    # support context management protocol
    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, *args):
        self.stop()

    
if __name__ == '__main__':
    
    def countdown(n):
        while n > 0:
            n -= 1

    # explicit start/stop
    t = Timer()
    t.start()
    countdown(10000000)
    t.stop()
    print(t.elapsed)

    # as context manager
    with t:
        countdown(10000000)
    # must indent out. otherwise stop not called thus no new elapse added
    # since t has not call reset() method, time will be added
    print(t.elapsed)
        
    with Timer(time.process_time) as t2:
        countdown(10000000)
    print(t2.elapsed)
        