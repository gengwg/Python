#!/usr/bin/env python3

import os
import sys
import atexit
import signal

def daemonize(pidfile, *, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    if os.path.exists(pidfile):
        raise RuntimeError(f"Already running: {pidfile}")
    
    try:
        if os.fork() > 0:
            raise SystemExit(0)  # Parent exits
    except OSError as e:
        raise RuntimeError(f"Fork #1 failed: {e.errno} ({e.strerror})")
    
    os.chdir('/')
    os.umask(0)
    os.setsid()

    try:
        if os.fork() > 0:
            raise SystemExit(0)  # Parent exits
    except OSError as e:
        raise RuntimeError(f"Fork #2 failed: {e.errno} ({e.strerror})")
    
    sys.stdout.flush()
    sys.stderr.flush()

    with open(stdin, 'rb', 0) as f:
        os.dup2(f.fileno(), sys.stdin.fileno())
    with open(stdout, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stdout.fileno())
    with open(stderr, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stderr.fileno())

    with open(pidfile, 'w') as f:
        print(os.getpid(), file=f)

    atexit.register(lambda: os.remove(pidfile))

    def sigterm_handler(signo, frame):
        raise SystemExit(1)
    
    signal.signal(signal.SIGTERM, sigterm_handler)

def main():
    import time
    sys.stdout.write("Daemon started with pid {}\n".format(os.getpid()))
    while True:
        sys.stdout.write("Daemon is alive! {}\n".format(time.ctime()))
        time.sleep(10)

if __name__ == '__main__':
    PIDFILE = '/tmp/daemon.pid'

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} start|stop")
        raise SystemExit(1)
    
    if 'start' == sys.argv[1]:
        try:
            daemonize(PIDFILE, stdout='/tmp/daemon.log', stderr='/tmp/daemon.log')
        except RuntimeError as e:
            print(e, file=sys.stderr)
            raise SystemExit(1)
        main()
    elif 'stop' == sys.argv[1]:
        if os.path.exists(PIDFILE):
            with open(PIDFILE) as f:
                os.kill(int(f.read()), signal.SIGTERM)
        else:
            print(f"Not running: {PIDFILE}", file=sys.stderr)
            raise SystemExit(1)
    else:
        print(f"Unknown command: {sys.argv[1]}", file=sys.stderr)
        raise SystemExit(1)
    
    