def countdown(n):
    while n > 0:
        print(f'T-minus {n}')
        yield
        n -= 1
    print('Blastoff!')

def countup(n):
    i = 0
    while i < n:
        print(f'Countup {i}')
        yield
        i += 1
    print('Done!')

from collections import deque

class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()
    
    def new_task(self, task):
        self._task_queue.append(task)

    def run(self):
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                pass

if __name__ == '__main__':
    sched = TaskScheduler()
    sched.new_task(countdown(10))
    sched.new_task(countup(5))
    sched.run()
    