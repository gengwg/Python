import signal
import resource
import os

def time_exceeded(signo, frame):
    print('Time is up!')
    raise SystemExit(1)

def set_max_runtime(seconds):
    # install the signal handler and set a resource limit
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)

def limit_memory(maxsize):
    '''
    restrict memory usage
    put a limit on total address space in use
    '''
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))

if __name__ == '__main__':
    set_max_runtime(10)
    limit_memory(5)
    while True:
        pass
    else:
        pass