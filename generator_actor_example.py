from collections import deque

class ActorScheduler:
    def __init__(self):
        self._actors = {}
        self._msg_queue = deque()

    def new_actor(self, name, actor):
        self._msg_queue.append((actor, None))  # Prime the actor/generator
        self._actors[name] = actor

    def send(self, name, msg):
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor, msg))

    def run(self):
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                actor.send(msg) # built-in generator method send()
            except StopIteration:
                pass

if __name__ == '__main__':
    def printer():
        while True:
            msg = yield
            print(f'Got: {msg}')

    def counter(sched):
        while True:
            n = yield
            if n == 0:
                break
            sched.send('printer', n)
            # No Stack Overflow Risk
            # Each "recursive step" is a separate message execution
            # No deep call stack → can handle very large numbers
            # The queue acts as the "stack" instead of the call stack
            sched.send('counter', n - 1)
    
    sched = ActorScheduler()
    sched.new_actor('printer', printer())
    sched.new_actor('counter', counter(sched))
    sched.send('counter', 10000)
    sched.run()

    def counter_recursive(n):
        if n == 0:
            return
        print(f'Recursive Counter Got: {n}')
        counter_recursive(n - 1)

    # This will cause a RecursionError for large n
    # counter_recursive(10000)  # Uncommenting this line will likely cause a stack overflow
    counter_recursive(10)  # Safe for small n