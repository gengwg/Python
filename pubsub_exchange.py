from collections import defaultdict
from contextlib import contextmanager

class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


# Classes are callable in Python (calling them creates instances)
# e.g. Exchange() calls Exchange.__init__()
# So we can use them as factory functions
# Here we use a dictionary to map names to Exchange instances
# This is a simple form of a service locator pattern
# Each exchange is a singleton
# We use defaultdict to create exchanges on demand
# defaultdict(Exchange) means: "When a key is missing, call Exchange() to create a new instance"
_exchanges = defaultdict(Exchange)

def get_exchange(name):
    return _exchanges[name]

class Task:
    def __init__(self, name):
        self.name = name

    def send(self, msg):
        # raise NotImplementedError
        print(f'Task {self.name} processed message: {msg}')
    
if __name__ == '__main__':
    task_a = Task('A')
    task_b = Task('B')

    exc = get_exchange('test')
    
    with exc.subscribe(task_a, task_b):
        exc.send('Hello, World!')
        exc.send('Goodbye, World!')
